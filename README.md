
## Install Redis-
https://askubuntu.com/questions/868848/how-to-install-redis-on-ubuntu-16-04

## How to launch celery workers-
celery -A file_processor.celery worker -l DEBUG -E
OR
celery -A file_processor.celery worker --loglevel INFO --concurrency=8

## How to run Celery Flower-
celery flower -A file_processor --address=127.0.0.1 --port=5555

