from dotenv import load_dotenv
import os

load_dotenv()

LLM_API_KEY=os.getenv('LLM_API_KEY', None)
VOYAGE_API_KEY=os.getenv('VOYAGE_API_KEY', None)
MONGODB_URI=os.getenv('MONGODB_URI', None)