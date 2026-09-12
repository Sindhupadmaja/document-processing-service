# Worker progression
The API currently uses an in-process worker simulation so the project runs with one command. The next learning step is to replace that section with Celery + Redis, add retry/backoff, idempotency, and dead-letter handling.
