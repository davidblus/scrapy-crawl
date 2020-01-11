celery -A celery_tasks control shutdown
rm celerybeat-schedule.db
celery -A celery_tasks worker -D -l info -f logs/celery/worker.log -B
