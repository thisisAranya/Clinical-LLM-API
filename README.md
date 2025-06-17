# 🏥 Dockerized LLM API for Clinical Text Processing

A lightweight, production-ready REST API that wraps a fine-tuned transformer model for generating medical reports and answering clinical questions. Built for deployment in healthcare environments with resource constraints.

## 🚀 Features

- FastAPI-based REST interface for model inference
- Fine-tuned on clinical QA and report-generation datasets
- Optimized using 4-bit quantization (bitsandbytes)
- Containerized with Docker for portability and deployment
- ROUGE/BLEU metrics for output evaluation

## 🧠 Model Details

- Base Model: Qwen 1.5 / LLaMA2 (4-bit quantized)
- Fine-Tuning: Clinical question-answer pairs and SOAP note generation (MIMIC-lite or synthetic)

## 🧪 Example API Usage

```bash
curl -X POST http://localhost:8000/infer \
    -H "Content-Type: application/json" \
    -d '{"input": "A 45-year-old male with hypertension presents with chest pain..."}'
