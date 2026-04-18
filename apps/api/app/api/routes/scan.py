import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form

from app.services.resume_parser import parse_resume
from app.services.ats_engine import calculate_score

router = APIRouter(prefix="/scan", tags=["Scan"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def scan_resume(
    file: UploadFile = File(...),
    jd_text: str = Form(...)
):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = parse_resume(file_path)

    result = calculate_score(resume_text, jd_text)

    return result