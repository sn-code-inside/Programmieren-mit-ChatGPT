import openai
from apikey import *

def main():
	openai.api_key = openai_key

	conversation = [{"role": "system", 
		"content": "You are a helpful assistant."}]

	while True:
		user_input = input("Enter your prompt (or 'quit' to exit): ")

		if user_input.lower() == 'quit':
			break
		
		conversation.append({"role": "user", "content": user_input})

		try:
			response = openai.chat.completions.create(
				model="gpt-4o",
				messages=conversation,
				temperature=0.7
			)

			gpt4o_response = response.choices[0].message.content.strip()

			print(f"GPT-4o: {gpt4o_response}\n")

			conversation.append({"role": "assistant", 
				"content": gpt4o_response})

		except Exception as e:
			print(f"An error occurred: {e}")

if __name__ == "__main__":
	main()
