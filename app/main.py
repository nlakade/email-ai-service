from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.prompts import classify_email_prompt, rewrite_email_prompt
from app.utils import get_llm_response
import logging
import os
from typing import Optional

app = FastAPI(
    title="Smart Email AI",
    description="Gen-AI powered email classification and rewriting service",
    version="1.0",
    docs_url="/docs",
    redoc_url=None
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmailRequest(BaseModel):
    email_content: str

class RewriteRequest(EmailRequest):
    tone: str
    length: Optional[str] = None  

class ClassificationResponse(BaseModel):
    category: str
    confidence: Optional[float] = None  

class RewriteResponse(BaseModel):
    rewritten_email: str
    tone_used: str

@app.post("/classify_email", response_model=ClassificationResponse)
async def classify_email(request: EmailRequest):
    try:
        logger.info(f"Classifying email: {request.email_content[:50]}...")
        prompt = classify_email_prompt(request.email_content)
        category = await get_llm_response(prompt)
        return {"category": category.strip()}
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Classification failed")
        raise HTTPException(
            status_code=500,
            detail=f"Classification failed: {str(e)}"
        )

@app.post("/rewrite_email", response_model=RewriteResponse)
async def rewrite_email(request: RewriteRequest):
    try:
        logger.info(f"Rewriting email in {request.tone} tone")
        prompt = rewrite_email_prompt(request.email_content, request.tone)
        rewritten = await get_llm_response(prompt)
        return {
            "rewritten_email": rewritten.strip(),
            "tone_used": request.tone
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Rewrite failed")
        raise HTTPException(
            status_code=500,
            detail=f"Rewriting failed: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {
        "status": "active",
        "model": os.getenv("LLM_MODEL", "gpt-3.5-turbo"),
        "environment": os.getenv("ENVIRONMENT", "development")
    }