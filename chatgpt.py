import openai


class ChatGPTBOT:
    def __init__(self, api_key):
        self.api_key = api_key
        self.prompts = []

    def initialize_gpt3(self):
        openai.api_key = self.api_key

    def create_prompt(self, prompt):
        self.prompts.append(prompt)

    def get_response(self, prompt_index):
        if 0 <= prompt_index < len(self.prompts):
            prompt = self.prompts[prompt_index]
            try:
                response = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    prompt=prompt,
                    max_tokens=50
                )
                return response.choices[0].text.strip()
            except Exception as e:
                return str(e).strip()
        else:
            return "Invalid prompt index"

    def update_prompt(self, prompt_index, new_prompt):
        if 0 <= prompt_index < len(self.prompts):
            self.prompts[prompt_index] = new_prompt
            return "Prompt updated successfully"
        else:
            return "Invalid prompt index"
