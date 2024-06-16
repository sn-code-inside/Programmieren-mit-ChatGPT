import openai
from apikey import *

openai.api_key = openai_key

speech_file_path = "C:/temp/voice.mp3"

response = openai.audio.speech.create(
	model="tts-1",
	voice="alloy",
	response_format="mp3",
	speed=1.0,
	input="General artificial intelligence (AGI) refers to a type \
			of artificial intelligence that possesses the ability to \
			understand, learn, and apply knowledge across a wide range \
			of tasks and domains, similar to the capabilities of a human."
)

response.write_to_file(speech_file_path)