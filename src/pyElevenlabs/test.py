from pyElevenlabs import pyElevenlabs
from dotenv import load_dotenv

load_dotenv()

api_key = ""

t = pyElevenlabs(api_key)
data = t.speak("Hello World!")
