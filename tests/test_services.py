import unittest
from unittest.mock import MagicMock

from repositories.base import IWordRepository, IURLRepository
from services.filter_service import WordFilterService, URLFilterService


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.word_repo = MagicMock(spec=IWordRepository)
        self.url_repo = MagicMock(spec=IURLRepository)
        self.word_service = WordFilterService(self.word_repo)
        self.url_service = URLFilterService(self.url_repo)

    def test_censor_text_no_sensitive_words(self):
        self.word_repo.get_sensitive_words.return_value = ["bad", "worst"]
        content = "This is a good text"
        censored_content, has_sensitive = self.word_service.censor_text(content)
        self.assertEqual(censored_content, content)
        self.assertFalse(has_sensitive)
        self.word_repo.get_sensitive_words.assert_called_once()

    def test_censor_text_with_sensitive_words(self):
        # Arrange
        self.word_repo.get_sensitive_words.return_value = ["bad", "worst"]
        content = "This is a bad worst text"
        # Act
        censored_content, has_sensitive = self.word_service.censor_text(content)
        # Assert
        self.assertEqual(censored_content, "This is a b*d w***t text")
        self.assertTrue(has_sensitive)
        self.word_repo.get_sensitive_words.assert_called_once()

    def test_censor_text_case_insensitive(self):
        # Arrange
        self.word_repo.get_sensitive_words.return_value = ["bad"]
        content = "This is BAD text"
        # Act
        censored_content, has_sensitive = self.word_service.censor_text(content)
        # Assert
        self.assertEqual(censored_content, "This is B*D text")
        self.assertTrue(has_sensitive)
        self.word_repo.get_sensitive_words.assert_called_once()

    def test_censor_text_short_words(self):
        # Arrange
        self.word_repo.get_sensitive_words.return_value = ["is", "a"]
        content = "This is a test"
        # Act
        censored_content, has_sensitive = self.word_service.censor_text(content)
        # Assert
        self.assertEqual(censored_content, "This i* a test")
        self.assertTrue(has_sensitive)
        self.word_repo.get_sensitive_words.assert_called_once()

    def test_censor_text_empty_content(self):
        self.word_repo.get_sensitive_words.return_value = ["bad"]
        content = ""

        censored_content, has_sensitive = self.word_service.censor_text(content)
        # Assert
        self.assertEqual(censored_content, "")
        self.assertFalse(has_sensitive)
        self.word_repo.get_sensitive_words.assert_called_once()


if __name__ == '__main__':
    unittest.main()
