from django.db import connections
from django.db.utils import OperationalError
import redis
from decouple import config


def check_db():
    try:
        connections["default"].cursor()
        return True
    except OperationalError:
        return False


def check_redis():
    try:
        r = redis.Redis.from_url(config("CELERY_BROKER_URL"))
        r.ping()
        return True
    except Exception:
        return False
