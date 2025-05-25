import json

from core.singleton_meta import SingletonMeta
import google.generativeai as genai


class AISingleton(metaclass=SingletonMeta):
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

        print("AI Singleton Gemini")

    def predict(self, user_input: str, prompt_template: str = "<<DATA_IAMTDF_1992003_HAHAHHAHAH>>"):
        """
            Hàm predict sử dụng Gemini để tạo nội dung dựa trên input.
            :param user_input: Chuỗi đầu vào từ người dùng
            :param prompt_template: Template prompt, mặc định có placeholder <<DATA_IAMTDF_1992003_HAHAHHAHAH>>
            :return: Dict chứa kết quả JSON hoặc dict rỗng nếu lỗi
        """
        try:
            full_prompt = prompt_template.replace("<<DATA_IAMTDF_1992003_HAHAHHAHAH>>", user_input)
            response = self.model.generate_content(full_prompt)
            response_text = response.text.strip().replace("```json", "").replace("```", "").strip()
            return json.loads(response_text)["summary"]
        except json.JSONDecodeError as e:
            print(f"Lỗi giải mã JSON: {e}")
            return {}
        except Exception as e:
            print(f"Lỗi khi gọi Gemini API: {e}")
            return {}
