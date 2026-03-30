from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-5.1",
    input="How many days time off do I get in my first year?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": ["vs_69cab10bacc88191a58cea3d634cc9fa"]
    }]
)
print(response.output_text)


    