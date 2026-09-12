# Architecture
Client -> FastAPI upload -> validation -> job record -> worker -> extractor -> structured result -> status endpoint.

Production extension: FastAPI -> Redis queue -> Celery workers -> object storage -> PostgreSQL, with retries, idempotency keys, metrics, tracing, and malware scanning.
