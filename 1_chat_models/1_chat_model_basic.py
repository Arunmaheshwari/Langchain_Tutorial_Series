# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

# from dotenv import load_dotenv
from langchain_together import ChatTogether
# import os

# # Load environment variables from .env
# load_dotenv()

# # Get the API key from the environment variable
# api_key = os.getenv('TOGATHER_API_KEY')

# # Check if the API key is loaded correctly 
# if not api_key:
#     raise ValueError("API key not found. Please check your .env file.")

# # Initialize the ChatTogether model with the API key
# model = ChatTogether(api_key=api_key, model="meta-llama/Llama-3-70b-chat-hf")

# # Invoke the model with a message
# result = model.invoke("What is 81 divided by 9?")
# print("Full result:")
# print(result)
# print("Content only:")
# print(result.content)



from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

api_key = os.getenv('TOGATHER_API_KEY')

# Check if the API key is loaded correctly
if not api_key:
    raise ValueError("API key not found. Please check your .env file.")
else:
    print("API key loaded")


# Initialize the ChatTogether model with the API key
model = ChatTogether(api_key=api_key, model="meta-llama/Llama-3-70b-chat-hf")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)



