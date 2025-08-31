from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from pydantic import Field , BaseModel
from typing import Optional , Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from os import getenv

load_dotenv()


# Model
model = ChatOpenAI(
    api_key=getenv("OPENROUTER_API_KEY"),
    base_url=getenv("OPENROUTER_BASE_URL"),
    model="openai/gpt-oss-120b",
)


prompt = PromptTemplate(
    template="""Your task is to suggest small, personalized eco-friendly actions based on the content of the given article. These actions should be easy to implement and directly related to the themes and issues discussed in the article.

The structure for each recommendation should be as follows:
```
{
  "action": "The eco-friendly action recommendation here",
  "description": "A brief description of why this action is important and how it relates to the article's content"
}
```

The article is provided below:
{article}

Guidelines:
1. Provide specific and personalized steps that individuals can take to reduce their environmental impact.
2. Ensure each action is clearly formulated and directly related to the themes and issues discussed in the article.
3. Include a brief description explaining the significance of each action and how it connects to the article.
4. Present the recommendations in a structured format using the schema provided above.

Please generate the eco-friendly action recommendations following the structure and guidelines above.""",
    input_variables=["article"],
    partial_variables={""}
)