import os
import pytest
from chatgpt import ChatGPTBOT


class TestChatGPTBot:
    @classmethod
    def setup_class(cls):
        cls.api_key = os.environ.get("API_KEY")
        cls.chatbot = ChatGPTBOT(cls.api_key)
        cls.chatbot.initialize_gpt3()

    def test_create_prompt(self):
        self.chatbot.create_prompt("Tell me a joke")
        assert len(self.chatbot.prompts) == 1

    def test_get_response(self):
        self.chatbot.create_prompt("Tell me a fact")
        response = self.chatbot.get_response(0)
        assert response is not None

    def test_get_response_invalid_index(self):
        response = self.chatbot.get_response(-1)
        assert response == "Invalid prompt index"

    def test_update_prompt(self):
        self.chatbot.create_prompt("What's the weather today?")
        result = self.chatbot.update_prompt(
            0, "What is Data Science")
        assert result == "Prompt updated successfully"
        assert self.chatbot.prompts[0] == "What is Data Science"

    def test_update_prompt_invalid_index(self):
        result = self.chatbot.update_prompt(-1, "New prompt")
        assert result == "Invalid prompt index"


if __name__ == '__main__':
    pytest.main()
