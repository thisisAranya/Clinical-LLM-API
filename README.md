# Clinical LLM API: Fine-Tuning & Deployment for Medical QA

This project demonstrates the end-to-end process of fine-tuning a lightweight language model for clinical question answering and deploying it as a REST API.

## Features

- Fine-tuned Qwen1.5-0.5B model on clinical QA data using LoRA (PEFT) with 4-bit quantization
- Lightweight FastAPI backend serving model inference
- Dockerized for easy deployment and portability

## Project Structure

```
clinical-llm-api/
├── Notebook/train.py             # LoRA fine-tuning script
├── Notebook/clinical_qa.jsonl    # Sample clinical QA training data
├── app/main.py                   # FastAPI inference API
├── Dockerfile                    # Docker container setup
├── requirements.txt
└── README.md
```

## Usage

1. **Fine-tune model:**
   ```bash
   python training/train.py
   ```

2. **Build and run API container:**
   ```bash
   docker build -t clinical-llm .
   docker run -p 8000:8000 clinical-llm
   ```

3. **Send inference requests:**
   ```bash
   curl -X POST http://localhost:8000/infer \
     -H "Content-Type: application/json" \
     -d '{"input": "Patient with itchy red rash on cheeks"}'
   ```

## Tech Stack

- **Python** - Core programming language
- **Hugging Face Transformers** - Model training and inference
- **PEFT (LoRA)** - Parameter-efficient fine-tuning
- **FastAPI** - Web API framework
- **Docker** - Containerization
- **bitsandbytes** - 4-bit quantization

## Contact

Built by **Aranya Saha**  
Email: aranyasaha932@gmail.com
