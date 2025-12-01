"""
MongoDB connection helper with retry logic and error handling.
"""
import logging
import asyncio
from typing import Optional, Any
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError, NetworkTimeout

logger = logging.getLogger('discord.bot.mongo_helper')


class MongoConnectionManager:
    """Manages MongoDB connections with automatic retry and error handling."""
    
    def __init__(self, client: Optional[AsyncIOMotorClient], db_name: str):
        self.client = client
        self.db_name = db_name
        self.db: Optional[AsyncIOMotorDatabase] = None
        self.connected = False
        
        if self.client:
            self.db = self.client[db_name]
    
    async def execute_with_retry(
        self, 
        operation, 
        max_retries: int = 3, 
        retry_delay: float = 1.0,
        fallback_value: Any = None
    ):
        """
        Execute a MongoDB operation with automatic retry on connection failures.
        
        Args:
            operation: Async function to execute
            max_retries: Maximum number of retry attempts
            retry_delay: Delay between retries in seconds
            fallback_value: Value to return if all retries fail
            
        Returns:
            Result of the operation or fallback_value on failure
        """
        if not self.client or not self.db:
            logger.warning("MongoDB not configured, returning fallback value")
            return fallback_value
        
        last_error = None
        for attempt in range(max_retries):
            try:
                result = await operation()
                if attempt > 0:
                    logger.info(f"MongoDB operation succeeded after {attempt + 1} attempts")
                return result
            except (ConnectionFailure, ServerSelectionTimeoutError, NetworkTimeout) as e:
                last_error = e
                if attempt < max_retries - 1:
                    wait_time = retry_delay * (2 ** attempt)  # Exponential backoff
                    logger.warning(
                        f"MongoDB connection error (attempt {attempt + 1}/{max_retries}): {e}. "
                        f"Retrying in {wait_time}s..."
                    )
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(
                        f"MongoDB operation failed after {max_retries} attempts: {e}. "
                        f"Returning fallback value."
                    )
            except Exception as e:
                # Non-connection errors should not be retried
                logger.error(f"MongoDB operation error (non-retryable): {e}")
                last_error = e
                break
        
        return fallback_value
    
    async def ping(self) -> bool:
        """Check if MongoDB connection is alive."""
        async def _ping():
            await self.client.admin.command('ping')
            return True
        
        try:
            result = await self.execute_with_retry(_ping, max_retries=1, fallback_value=False)
            self.connected = result
            return result
        except Exception:
            self.connected = False
            return False
    
    def is_connected(self) -> bool:
        """Check if MongoDB client exists (doesn't verify actual connection)."""
        return self.client is not None and self.db is not None


def suppress_pymongo_logs():
    """Suppress verbose pymongo background task error logs."""
    pymongo_logger = logging.getLogger('pymongo')
    pymongo_logger.setLevel(logging.CRITICAL)
    
    # Also suppress motor logs
    motor_logger = logging.getLogger('motor')
    motor_logger.setLevel(logging.WARNING)
