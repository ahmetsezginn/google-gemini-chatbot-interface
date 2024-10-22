import os
import google.generativeai as genai
class Model:
    def __init__(self):
        self.api_key=""# your api key here or you can set it as environment variable os.getenv('GENAI_API_KEY')
        self.generation_config={}
        self.model=None
        self.chat_section=None
        self.genai=None
        
    def upload_to_gemini(self,path, mime_type=None):
        """Uploads the given file to Gemini.

        See https://ai.google.dev/gemini-api/docs/prompting_with_media
        """
        file = self.genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file
    def init_chat(self):
        genai.configure(api_key=self.api_key)
        self.genai = genai  # Assign the configured module to self.genai

        self.generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-002",
        generation_config=self.generation_config,
        )
    def chat_section_funcition(self):
                
        # TODO Make these files available on the local file system
        # You may need to update the file paths
        files = [
            #this part is for uploading files for chat session
        ]

        self.chat_session = self.model.start_chat(
        history=[
            #your chat history
        ]
        )
if __name__ == "__main__":
    model=Model()
    model.init_chat()
    model.chat_section_funcition()
    response = model.chat_session.send_message("Thank you")
    print(response.text)
