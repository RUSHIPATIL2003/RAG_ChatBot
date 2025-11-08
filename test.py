from groq import Groq

client = Groq(api_key="your_API_key")
print(client.models.list())  