import os
from pyElevenlabs import pyElevenlabs
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)

t = pyElevenlabs(api_key)
data = t.speak("21m00Tcm4TlvDq8ikWAM",
               "This is a realy long text to test the api.")

with open("test.wav", "wb") as f:
    f.write(data)

# play audio file
os.system("test.wav")
