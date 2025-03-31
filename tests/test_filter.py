from services.filter_service import WordFilterService, URLFilterService
from repositories.file_repo import FileURLRepository, FileWordRepository


def test_filter_content():
    repository = FileWordRepository()
    service = WordFilterService(repository)

    text = "Tham gia casino và tài xỉu ngay!"
    expected = "Tham gia **** và ***** ngay!"

    assert service.censor_text(text) == expected
