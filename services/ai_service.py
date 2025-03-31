from typing import Dict

from core.ai_singleton import AISingleton


class AIService:
    def __init__(self, api_key: str):
        self.ai = AISingleton(api_key)

    def process_input(self, user_input: str, prompt_template: str = "<<DATA_IAMTDF_1992003_HAHAHHAHAH>>") -> Dict:
        """
            Hàm process_input sử dụng Gemini để tạo nội dung dựa trên input.
            :param user_input: Chuỗi đầu vào từ người dùng
            :param prompt_template: Template prompt, mặc định có placeholder <<DATA_IAMTDF_1992003_HAHAHHAHAH>>
            :return: Dict chứa kết quả JSON hoặc dict rỗng nếu lỗi
        """
        return self.ai.predict(user_input, prompt_template)
