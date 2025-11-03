from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY, MODEL_NAME

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
  groq_api_key = GROQ_API_KEY,
  model_name = MODEL_NAME,
  temperature = 0.3
)

itinerary_prompt = ChatPromptTemplate([
  ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on user's interests {interests}. Provide the itinerary in bulleted format"),
  ("human", "Create an itinerary for my day trip")
])

def generate_itinerary(city: str, interests: list[str]) -> str:
  response = llm.invoke(
    itinerary_prompt.format_messages(city=city, interests = ','.join(interests))
  )

  return response.content