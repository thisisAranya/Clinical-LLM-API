from fastapi import FastAPI, Request
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

# Load quantized model (example: Qwen/Qwen1.5-0.5B)
model_name = "Aranya31/gpt2-medqa-ft"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True)

class InferenceRequest(BaseModel):
    input: str

@app.post("/infer")
def infer(request: InferenceRequest):
    input_text = request.input
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, temperature=0.7)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": decoded}
