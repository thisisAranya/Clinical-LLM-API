# Simple MedQA-GPT: GPT Tailored for Medical Q&A

This project demonstrates the end-to-end workflow of fine-tuning a lightweight GPT-2 model for clinical question answering and deploying it as a REST API.

## ✨ Features

- Fine-tunes a **GPT-2** model on custom clinical QA data  
- Uses Hugging Face `Trainer` within a Jupyter Notebook  
- FastAPI backend for real-time inference  
- Dockerized setup for easy deployment

---

## 📁 Project Structure

```
simple-medqa-gpt/
├── Notebook/
│   ├── medqa_train.ipynb       # Jupyter notebook for fine-tuning GPT-2
│   └── med_qa.jsonl            # Training data in JSONL format
├── main.py                     # FastAPI inference API
├── Dockerfile                  # Docker container configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Usage

### 1. Prepare your dataset

Ensure your training file (`med_qa.jsonl`) follows this format (one JSON object per line):

```json
{"instruction": "Describe symptoms of eczema", "output": "Itchy, inflamed skin, often red and dry."}
```

### 2. Fine-tune the model

Open the Jupyter notebook:

```bash
jupyter notebook Notebook/medqa_train.ipynb
```

Run all cells to train and save the fine-tuned GPT-2 model.

### 3. Build and run the API server

```bash
docker build -t simple-medqa-gpt .
docker run -p 8000:8000 simple-medqa-gpt
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
- **Docker** – Containerization and deployment  
- **PyTorch** – Deep learning framework under the hood  
- **Jupyter Notebook** – Interactive development for training

---

## 📬 Contact

Built with ❤️ by **Aranya Saha**  
📧 aranyasaha932@gmail.com
