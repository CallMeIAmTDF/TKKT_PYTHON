from abc import ABC, abstractmethod
from typing import List


class IWordRepository(ABC):
    """Interface lấy danh sách từ nhạy cảm"""

    @abstractmethod
    def get_sensitive_words(self) -> List[str]:
        pass


class IURLRepository(ABC):
    """Interface lấy danh sách URL nhạy cảm"""

    @abstractmethod
    def get_sensitive_urls(self) -> List[str]:
        pass
