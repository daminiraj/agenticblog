from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import httpx

custom_client = httpx.Client(verify=False)
class OpenAiLLM():
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            os.environ["OPENAI_API_KEY"] =self.openai_api_key= os.getenv("OPENAI_API_KEY")
            llm= ChatOpenAI(api_key=self.openai_api_key,model="gpt-4-0613",http_client=httpx.Client(verify=False))
            return llm
        except Exception as e:
            raise ValueError(f"Error occurred with exception:{e}")
