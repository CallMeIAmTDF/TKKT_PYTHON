class PromptTemplates:
    SUMARY_PROMPT = """
    Hãy tóm tắt bài blog sau đây. Không cần giữ lại các định dạng đặc biệt như in đậm, in nghiêng, chú thích hay hình ảnh.. Nếu có lỗi trong quá trình tóm tắt, hãy trả về JSON với thông tin lỗi.
    ### **Định dạng JSON yêu cầu:**
    ```json
    {
      "summary": "Tóm tắt bài blog (nếu thành công, giữ nguyên định dạng đặc biệt)",
    }
    
    ### **📌 Ví dụ kết quả JSON mong muốn**
    **Khi thành công:**
    ```json
    {
      "summary": "Đây là một bài blog về **AI và tương lai**. Trong bài viết, tác giả nhấn mạnh rằng *AI sẽ thay đổi thế giới*...",
    }
    
    **Khi có lỗi:**
    ```json
    {
      "summary": "",
    }
    
    Nội dung gốc: <<DATA_IAMTDF_1992003_HAHAHHAHAH>>
    """

    @classmethod
    def get_prompt(cls, prompt_name: str) -> str:
        return getattr(cls, prompt_name, cls.BASIC_NLP)