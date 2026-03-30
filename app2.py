import requests
from io import BytesIO
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def create_file(client, file_path):
    if file_path.startswith("http://") or file_path.startswith("https://"):
        # Download the file content from the URL
        response = requests.get(file_path)
        file_content = BytesIO(response.content)
        file_name = file_path.split("/")[-1]
        file_tuple = (file_name, file_content)
        result = client.files.create(
            file=file_tuple,
            purpose="assistants"
        )
    else:
        # Handle local file path
        with open(file_path, "rb") as file_content:
            result = client.files.create(
                file=file_content,
                purpose="assistants"
            )
    print(result.id)
    return result.id

# Replace with your own file path or URL
file_id = create_file(client, "https://www.partner4work.org/uploads/attachment-a-2023-handbook-revised-11-2023.pdf")

vector_store = client.vector_stores.create(
    name="knowledge_base"
)
print(vector_store.id)

result = client.vector_stores.files.create(
    vector_store_id=vector_store.id,
    file_id=file_id
)
print(result)

result = client.vector_stores.files.list(
    vector_store_id=vector_store.id
)
print(result)
