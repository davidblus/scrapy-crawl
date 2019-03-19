
celery -A celery_tasks control shutdown
celery -A celery_tasks worker -D -l info -f logs/celery/worker.log -B
