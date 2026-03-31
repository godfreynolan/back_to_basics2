from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.responses.create(
    model="ft:gpt-4.1-2025-04-14:riis-llc::DPH9Yk7N",
    input="What security measures are in place to protect my account?"
)

print(response.output_text)





