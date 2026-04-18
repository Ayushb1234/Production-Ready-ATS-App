import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form

from app.services.resume_parser import parse_resume
from app.services.scan_pipeline import run_ai_scan

router = APIRouter(prefix="/scan-ai", tags=["AI Scan"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def scan_ai(
    file: UploadFile = File(...),
    jd_text: str = Form(...)
):
    path = f"{UPLOAD_DIR}/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = parse_resume(path)

    result = run_ai_scan(
        resume_text=resume_text,
        jd_text=jd_text
    )

    return result