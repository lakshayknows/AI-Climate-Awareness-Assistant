from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.prompts import load_prompt
from langchain_openai import ChatOpenAI
from os import getenv
from utils.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL_NAME

load_dotenv()


model = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    model=MODEL_NAME,
)

prompt = load_prompt('templates/template1.json')


stringify = StrOutputParser()

summarizer = prompt | model | stringify
 
def summarize_text(article: str) -> str:
    try:
        return summarizer.invoke({"article": article})
    except Exception as e:
        return f"Error during summarization: {str(e)}"
    

if __name__ == "__main__":
    sample_text = "A rainbow is formed by refraction, reflection, and dispersion of sunlight in water droplets..."
    print(summarize_text(sample_text))