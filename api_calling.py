from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import io,os




# loading the environment variable

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# initializing a client

client = genai.Client(api_key = my_api_key)

# note generator
def note_generator(images):

    prompt ="""Summarize the picture in note format at max 100 words in plain bengali ,make sure to add necessary markdown to differentiate different section"""


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )

    return response.text


# audio generator

def audio_transcription(text):
    speech = gTTS(text , lang='bn',slow =False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer