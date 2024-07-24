from openai import OpenAI

from prompt1 import prompt, new_prompt

openai_api_key = "EMPTY"

# openai_api_base = "http://0.0.0.0:62027/v1"
openai_api_base = "http://10.106.4.16:62027/v1"
qwen_plus_base = "http://10.106.4.16:8004/v1"


client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

pt = "给出老舍的散文《骆驼祥子》段落，不少于3千字"

print('-'*20)
print(pt)
print('-'*20)

model_name = "/data1/ziyiliu/checkpoints/Qwen/Qwen2-1.5B-Instruct"
qwen_plus_model = "/data2/llms/Qwen1.5-72B-Chat-GPTQ-Int4"
# completion = client.completions.create(model=model_name,
#                                       prompt=prompt,
#                                       max_tokens=300)

# print(completion.choices[0].text)
chat_completion = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": pt
    }],
    model=model_name,
)

print("Chat completion results:")
print(chat_completion.choices[0].message.content)