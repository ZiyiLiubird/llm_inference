# Load model directly
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from prompt import prompt

print(prompt)
device = "cuda"

# model_path = "/data/p3/ziyiliu/checkpoints/Qwen/Qwen2-1.5B-Instruct"
model_path = "/data/p3/ziyiliu/checkpoints/microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, torch_dtype="auto", device_map="auto")
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)

model = model.cuda()

messages = [
    {"role": "system", "content": ""},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)

generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print('-'* 20)
print(response)