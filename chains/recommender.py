from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from pydantic import Field , BaseModel
from typing import Optional , Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from os import getenv
from utils.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL_NAME


load_dotenv()


# Model
model = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    model=MODEL_NAME,
)

class EcoAction(BaseModel):
    step: str = Field(description="The eco-friendly action step")
    category: Literal["energy", "waste", "transport", "water", "general"] = Field(
        description="Category of the action"
    )
    impact: Optional[str] = Field(
        description="The potential positive impact (short and simple)"
    )

class EcoPlan(BaseModel):
    actions: list[EcoAction]
    
schemify = PydanticOutputParser(pydantic_object=EcoPlan)
    
prompt = PromptTemplate(
    template="""Your task is to suggest small, personalized eco-friendly actions based on the content of the given article. These actions should be easy to implement and directly related to the themes and issues discussed in the article.

The structure for each recommendation should be as follows:
```

  "action": "The eco-friendly action recommendation here",
  "description": "A brief description of why this action is important and how it relates to the article's content"

```

The article is provided below:
{article}

Guidelines:
1. Provide specific and personalized steps that individuals can take to reduce their environmental impact.
2. Ensure each action is clearly formulated and directly related to the themes and issues discussed in the article.
3. Include a brief description explaining the significance of each action and how it connects to the article.
4. Present the recommendations in a structured format using the schema provided above.

Please generate the eco-friendly action recommendations following the structure and guidelines above.
\n {format_instructions}""",
    input_variables=["article"],
    partial_variables={"format_instructions":schemify.get_format_instructions()}
)

recommender_chain = prompt | model | schemify

def recommender(article:str) -> str:
    try:
        return recommender_chain.invoke({"article":article})
    except Exception as e:
        return {"error": str(e)}   
        
        
if __name__ == "__main__":
    sample_text = "A rainbow is formed by refraction, reflection, and dispersion of sunlight in water droplets..."
    print(recommender(sample_text))