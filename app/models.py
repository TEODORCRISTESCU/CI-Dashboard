from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PostgresSQLUUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Build(Base):
    __tablename__ = "builds"

    id: Mapped[UUID] = mapped_column (
        PostgresSQLUUID(as_uuid=True),
        primary_key = True,
        default=uuid4
    )

    repo : Mapped[str] = mapped_column(String(255))

    branch: Mapped[str] = mapped_column(String(255))

    commit_sha: Mapped[str] = mapped_column(String(64))

    status: Mapped[str] = mapped_column(String(50), default = "Queued")

    retry_count: Mapped[int] = mapped_column(Integer, default = 0)

    exit_code: Mapped[int | None] = mapped_column(Integer, nullable = True)

    log: Mapped[str | None] = mapped_column(Text, nullable = True)

    created_at : Mapped[datetime] = mapped_column(DateTime(timezone = True), server_default = func.now())

    started_at: Mapped[datetime | None] = mapped_column( DateTime(timezone=True), nullable=True)
    
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)