

How to launch celery workers:
celery -A file_processor.celery worker -l DEBUG -E
celery -A file_processor.celery worker --loglevel INFO --concurrency=8

How to run Celery Flower:
celery flower -A file_processor --address=127.0.0.1 --port=5555

