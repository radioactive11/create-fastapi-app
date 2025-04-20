from app.db.redis_client import redis_client
from loguru import logger 

def rate_limiter(refill_rate: int = 60, bucket_size: int = 3) -> bool: 
    bucket_capacity = redis_client.get("bucket_capacity")
    result = True

    if bucket_capacity:
        if int(bucket_capacity) <= 0:
            result = False
            logger.warning("Request was rate limited")
        else:
            redis_client.decr("bucket_capacity")
            logger.info("Request went through")
    else: 
        redis_client.setex("bucket_capacity", 60, bucket_size-1)
        logger.info("Bucket was refreshed")

    return result 

