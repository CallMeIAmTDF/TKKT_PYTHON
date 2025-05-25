from fastapi import APIRouter, Depends
from models.request import FilterRequest
from services.filter_service import WordFilterService, URLFilterService
from repositories.file_repo import FileURLRepository, FileWordRepository

router = APIRouter()

# Khởi tạo repository và service
url_repo = FileURLRepository()
url_service = URLFilterService(url_repo)

word_repo = FileWordRepository()
word_service = WordFilterService(word_repo)


@router.post("/filter")
def filter_content(request: FilterRequest):
    censored_text, has_sensitive_content = word_service.censor_text(request.content)

    return {"filtered_content": censored_text, "has_sensitive_content": has_sensitive_content}


@router.get("/badUrlDetection")
def bad_url_detection(request: FilterRequest):
    isBad = url_service.contains_sensitive_url(request.content)
    return {"hasBadUrl": isBad}


@router.get("/")
def index():
    return {"message": "Hello World"}
