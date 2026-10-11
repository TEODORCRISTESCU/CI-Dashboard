# CI-Dashboard

## Current Progress

The project foundation and first end-to-end build submission flow are complete.

- Docker Compose environment with FastAPI, PostgreSQL, and Redis services.
- PostgreSQL-backed `Build` model managed through Alembic migrations.
- `POST /builds` endpoint accepts a repository, branch, and commit SHA, persists the build with a `Queued` status, and enqueues its ID in Redis.
- `GET /builds` returns builds ordered by newest first.
- A background worker blocks on the Redis queue, retrieves each build from PostgreSQL, and transitions it from `Queued` to `Running`.
- Built a separate Docker runner image (`ci-runner:dev`) containing `pytest`.
- Verified that a repository can be mounted read-only into the runner and tested in isolation with `pytest -q`.

### Architecture so far

1. Client submits a build to the FastAPI API.
2. The API stores the build in PostgreSQL.
3. The API pushes the build ID to a Redis queue.
4. A worker removes the ID from the queue, loads the build record, and marks it as running.
5. The next milestone is for the worker to start the isolated runner container, capture the test output and exit code, and persist a final `Passed` or `Failed` status.

### Next Steps

- Allow the worker to control Docker and start `ci-runner` containers.
- Run `pytest -q` for each queued build.
- Store test logs, exit codes, completion time, and final status in PostgreSQL.
- Add a build-detail endpoint and a simple dashboard UI.
- Add retries, timeout handling, and failure recovery.
