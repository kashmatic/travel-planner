from langchain_core.messages import HumanMessage, AIMessage

from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
  def __init__(self):
    ## To store all user messages and Ai messages
    self.messages = []
    self.city = ""
    self.interests = []
    self.itinerary = ""

    logger.info("Initialized TravelPlanner")
  
  def set_city(self, city: str):
    try:
      self.city = city
      self.messages.append(HumanMessage(content=city))
      logger.info("City set successfully")
    except Exception as e:
      logger.error(f"while setting city: {e}")
      raise CustomException(f"Failed to set city: {city}")
  
  def set_interests(self, interests_str: str):
    try:
      self.interests = [i.strip() for i in interests_str.split(",")]
      self.messages.append(HumanMessage(content=interests_str))
      logger.info("Interests set successfully")
    except Exception as e:
      logger.error(f"while setting interests: {e}")
      raise CustomException(f"Failed to set interests: {e}")
  
  def create_itinerary(self):
    try:
      logger.info(f"Generating itinerary for {self.city} with interests {self.interests}")
      itinerary = generate_itinerary(self.city, self.interests)
      self.itinerary = itinerary
      self.messages.append(AIMessage(content=self.itinerary))
      logger.info("Itinerary generated successfully")
      return self.itinerary
    except Exception as e:
      logger.error(f"while generating itinerary: {e}")
      raise CustomException(f"Failed to set interests: {e}")
    