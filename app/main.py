from sre_parse import BRANCH
from fastapi import FastAPI, Depends
from app.schema import BuildCreate, BuildSummary
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Build
from sqlalchemy import select
from app.queue import redis_client
app = FastAPI()

@app.get("/health")
def check():
    return {"status" : "ok"}

@app.post("/builds")
def build(build_request: BuildCreate, db: Session = Depends(get_db)):

    new_build = Build(
        repo = build_request.repo,
        branch = build_request.branch,
        commit_sha = build_request.commit_sha
    )
    
    db.add(new_build)
    db.commit()
    db.refresh(new_build)
    
    redis_client.lpush("build_queue", str(new_build.id))

    return str(new_build.id)

@app.get("/builds", response_model = list[BuildSummary])
def get_build(db : Session = Depends(get_db)):
    statement = select(Build).order_by(Build.created_at.desc())

    res = db.scalars(statement).all()

    return res
