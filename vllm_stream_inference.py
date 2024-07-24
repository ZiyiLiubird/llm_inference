from openai import OpenAI

from prompt1 import new_prompt

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.106.4.16:62027/v1"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

chat_completion = client.chat.completions.create(
    messages=[{
        "role": "system",
        "content": ""
    }, {
        "role": "user",
        "content": "给出老舍的散文《骆驼祥子》段落，不少于3千字"
    }],
    model=model,
    stream=True
)

print("Chat completion results:")
for response in chat_completion:
    print(response.choices[0].delta.content, end="")
print("")
