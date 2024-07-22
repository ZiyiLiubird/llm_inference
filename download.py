# Load model directly
import os
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM

access_token = os.getenv('hf_token')
print(access_token)

save_path = "/data/p3/ziyiliu/llm/models/qwen/1_5B_instruct_awq"
if not os.path.exists(save_path):
    os.makedirs(save_path)

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-1.5B-Instruct-AWQ")
tokenizer.save_pretrained(save_directory=save_path)

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-1.5B-Instruct-AWQ")
model.save_pretrained(save_path)
