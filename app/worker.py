import datetime

from sqlalchemy.sql.functions import current_date
from app.queue import redis_client
from app.db import SessionLocal
from app.models import Build
from uuid import UUID
from datetime import datetime, timezone

while True:
    queue_name, build_id = redis_client.brpop("build_queue")

    db = SessionLocal()
    try:
        build = db.get(Build, UUID(build_id))
        build.status = "Running"
        db.commit()
        build.started_at = datetime.now(timezone.utc)

        print(build.repo)
    finally:
        db.close()