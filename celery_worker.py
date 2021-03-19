from __future__ import absolute_import
from celery import Celery
from celery.utils.log import get_task_logger

celery = Celery('tasks', broker='redis://localhost:6379/0')


@celery.task
def update_lru_cache():
    logger = get_task_logger(__name__)
    celery.config_from_object('main')
    from main import lru_cache
    logger.info(f"lru_cache {lru_cache.cache}")


