from fastapi import APIRouter, Depends
from core.config import settings
from services.ai_service import AIService
from models.request import FilterRequest
from core.prompts import PromptTemplates

router = APIRouter()

service = AIService(settings.GEMINI_KEY)

@router.post("/summary")
async def summary(request: FilterRequest):
    result = service.process_input(user_input=request.content, prompt_template=PromptTemplates.SUMARY_PROMPT)
    return result
