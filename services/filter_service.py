import re
from typing import Tuple
from urllib.parse import urlparse

from repositories.base import IURLRepository, IWordRepository


class WordFilterService:
    """Xử lý lọc từ nhạy cảm"""

    def __init__(self, repository: IWordRepository):
        self.repository = repository

    def censor_text(self, content: str) -> tuple[str, bool]:
        """Thay thế từ nhạy cảm bằng **"""
        sensitive_words = self.repository.get_sensitive_words()
        has_sensitive = False

        def change_word(word):
            words = word.split(" ")
            res = ""
            for w in words:
                res = res + (
                    w[0] + '*' * (len(w) - 2) + w[-1] if len(w) > 2 else w[0] + "*" if len(w) == 2 else w) + " "
            return res.strip()

        def censor_word(match):
            nonlocal has_sensitive
            has_sensitive = True
            word = match.group()
            return change_word(word)

        pattern = r"\b(" + "|".join(map(re.escape, sensitive_words)) + r")\b"
        censored_content = re.sub(pattern, censor_word, content, flags=re.IGNORECASE)

        return censored_content, has_sensitive


class URLFilterService:
    """Xử lý kiểm tra URL nhạy cảm"""

    def __init__(self, url_repo: IURLRepository):
        self.url_repo = url_repo

    def contains_sensitive_url(self, content: str) -> bool:
        """Kiểm tra nội dung có chứa URL nhạy cảm không"""
        sensitive_urls = self.url_repo.get_sensitive_urls()
        extracted_urls = re.findall(r'https?://[^\s]+', content)

        for url in extracted_urls:
            domain = urlparse(url).netloc
            if any(sensitive_url in domain for sensitive_url in sensitive_urls):
                return True

        return False
