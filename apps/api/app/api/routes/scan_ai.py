import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.resume_parser import parse_resume
from app.services.scan_pipeline import run_ai_scan
from sqlalchemy import text
router = APIRouter(prefix="/scan-ai", tags=["AI Scan"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Temporary mock current user
# Replace later with JWT auth current user dependency
class TempUser:
    id = 1
    plan = "free"


@router.post("/")
async def scan_ai(
    file: UploadFile = File(...),
    jd_text: str = Form(...),
    db: Session = Depends(get_db)
):
    user = TempUser()

    # Check scan count
    count = db.execute(
        """
        select count(*) from scan_history
        where user_id=:u
        """,
        {"u": user.id}
    ).scalar()

    if user.plan == "free" and count >= 2:
        raise HTTPException(
            status_code=403,
            detail="Free scan limit reached. Upgrade to Pro."
        )

    # Save uploaded file
    path = f"{UPLOAD_DIR}/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = parse_resume(path)

    # Run ATS scan
    result = run_ai_scan(
        resume_text=resume_text,
        jd_text=jd_text,
        db=db
    )

    # Save scan history
    job_title = "Unknown Role"

    if "job_title" in result:
        job_title = result["job_title"]

    db.execute(
        """
        insert into scan_history (user_id, score, job_title)
        values (:u, :s, :j)
        """,
        {
            "u": user.id,
            "s": result["score"],
            "j": job_title
        }
    )

    db.commit()

    return result