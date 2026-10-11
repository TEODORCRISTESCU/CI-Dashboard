import os
import redis

REDIS_URL = os.environ["REDIS_URL"]

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses =True)