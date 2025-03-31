from repositories.base import IWordRepository, IURLRepository


class FileWordRepository(IWordRepository):
    """Repository lấy từ nhạy cảm từ file"""

    def __init__(self, word_file: str = "./assets/sensitive_words.txt"):
        self.word_file = word_file

    def get_sensitive_words(self):
        """Đọc danh sách từ nhạy cảm từ file"""
        with open(self.word_file, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]


class FileURLRepository(IURLRepository):
    """Repository lấy URL nhạy cảm từ file"""

    def __init__(self, url_file: str = "sensitive_urls.txt"):
        self.url_file = url_file

    def get_sensitive_urls(self):
        """Đọc danh sách URL nhạy cảm từ file"""
        with open(self.url_file, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]