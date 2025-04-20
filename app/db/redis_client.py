from redis import Redis
from app.config.config import REDIS_URI

redis_client = Redis.from_url(url=REDIS_URI)