# Simple MedQA-GPT: GPT tailored for medical Q&A

This project demonstrates the end-to-end workflow of fine-tuning a lightweight GPT-2 model for clinical question answering and deploying it as a REST API.

## ✨ Features

- Fine-tunes a **GPT-2** model on custom clinical QA data  
- Uses Hugging Face `Trainer` for simple supervised learning  
- FastAPI backend serves real-time inference  
- Dockerized setup for easy deployment

---

## 📁 Project Structure

```
clinical-llm-api/
├── Notebook/
│   ├── train.py                 # GPT-2 fine-tuning script (supervised)
│   ├── medqa_train.jsonl       # Training data in JSONL format
│   └── medqa_val.jsonl         # Validation data in JSONL format
├── app/
│   └── main.py                 # FastAPI inference API
├── Dockerfile                  # Docker container configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Usage

### 1. Prepare your dataset

Make sure your training/validation files are in the following format (one JSON object per line):

```json
{"instruction": "Describe symptoms of eczema", "output": "Itchy, inflamed skin, often red and dry."}
```

### 2. Fine-tune the model

```bash
python Notebook/train.py
```

This script uses Hugging Face’s `Trainer` to fine-tune GPT-2. Adjust batch size, epochs, or max token length in the script as needed.

### 3. Build and run the API server

```bash
docker build -t clinical-llm .
docker run -p 8000:8000 clinical-llm
```

### 4. Query the API

```bash
curl -X POST http://localhost:8000/infer \
  -H "Content-Type: application/json" \
  -d '{"input": "Patient has a persistent rash and fever"}'
```

---

## 🧠 Tech Stack

- **Python** – Core development language  
- **Hugging Face Transformers** – Model training and inference  
- **FastAPI** – High-performance API backend  
- **Docker** – Deployment and containerization  
- **PyTorch** – Deep learning framework under the hood

---

## 📬 Contact

Built with ❤️ by **Aranya Saha**  
📧 aranyasaha932@gmail.com
