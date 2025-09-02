from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from pydantic import Field , BaseModel
from typing import Optional , Literal
from langchain_openai import ChatOpenAI
from os import getenv
from utils.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL_NAME


# Load environment variables
load_dotenv()

# Define schema
class QuizItem(BaseModel):
    question: str = Field(description="The question text here")
    answer: str = Field(description="The correct answer here")
    difficulty: Literal["easy", "medium", "hard"] = Field(description="Difficulty level of the question")

class Quiz(BaseModel):
    quiz: list[QuizItem]
    
schemify = PydanticOutputParser(pydantic_object=Quiz)
# Prompt
prompt = PromptTemplate(
    template="""Your task is to create an awareness quiz related to the given article, 
with questions that gradually increase in difficulty. Each question should be directly related to the content.

The structure for each question and answer pair should be:

{{
  "question": "The question text here",
  "answer": "The correct answer here",
  "difficulty": "easy | medium | hard"
}}

Article:
{article}

Guidelines:
* Start with easy questions and gradually increase the difficulty.
* Ensure each question is clearly formulated and relevant to the article.
* Provide the correct answer for each question.
* Use the schema below for structured output.

{format_instructions}""",
    input_variables=["article"],
    partial_variables={"format_instructions": schemify.get_format_instructions()},
)

# Model
model = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    model=MODEL_NAME,
)

# Chain
quiz_chain = prompt | model | schemify


# Wrapper function
def generate_quiz(article: str):
    """
    Generate a structured quiz (question, answer, difficulty)
    based on the given article.
    """
    try:
        return quiz_chain.invoke({"article": article})
    except Exception as e:
        return {"error": str(e)}


# Local test
if __name__ == "__main__":
    sample_text = "A rainbow is formed by refraction, reflection, and dispersion of sunlight in water droplets..."
    print(generate_quiz(sample_text))