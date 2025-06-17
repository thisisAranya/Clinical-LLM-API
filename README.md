# 🏥 Clinical LLM API – Dockerized REST Service for Medical Text Generation

This project is a lightweight, production-ready REST API that wraps a quantized, fine-tuned language model for clinical tasks such as medical report generation or question answering. Designed for healthcare applications where deployment efficiency and interpretability are critical.

## 🚀 Features

- 🔬 Fine-tuned transformer model for medical QA or report generation
- 🚀 FastAPI server for quick and scalable inference
- 📦 Dockerized for portability and deployment
- 🧠 4-bit quantization using `bitsandbytes` for efficient model execution
- 📊 ROUGE/BLEU-based evaluation support (optional)

## 🧠 Model Overview

- Base Model: Qwen1.5-0.5B (can be swapped with your fine-tuned model)
- Quantization: 4-bit with `bitsandbytes`
- Task: Converts clinical input (e.g. patient history) into reports or answers medical queries

## 💡 Example Input

```json
{
  "input": "A 65-year-old diabetic patient complains of chest tightness and shortness of breath..."
}
```

## 📤 Example Output

```json
{
  "response": "The patient is experiencing symptoms that may indicate angina. Recommend ECG and blood tests..."
}
```

## 🧪 Quickstart

### 1. Clone and Build

```bash
docker build -t clinical-llm .
```

### 2. Run the API

```bash
docker run -p 8000:8000 clinical-llm
```

### 3. Test Locally

```bash
curl -X POST http://localhost:8000/infer     -H "Content-Type: application/json"     -d '{"input": "A 45-year-old male with hypertension presents with chest pain..."}'
```

## 🧰 Tech Stack

- `Python`, `FastAPI`, `Transformers`, `bitsandbytes`, `Docker`

## 📂 Project Structure

```
clinical_llm_api/
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

## ✍️ Author

**Aranya Saha**  
📧 aranyasaha932@gmail.com  
🌐 [GitHub](https://github.com/aranyasaha) (add your repo link here if public)

---

_This project is built for demonstrating real-world, lightweight deployment of medical LLMs. Perfect for healthcare startups, clinical research, or AI interviews._ 🩺
