# 🧠 BERT Fine-Tuning for Sentiment Analysis — IMDB Movie Reviews

Fine-tuning a pre-trained BERT model on the IMDB Movie Reviews dataset for binary sentiment classification (Positive / Negative). This project explores three different fine-tuning strategies and compares their performance.

---

## 📌 Project Overview

This project demonstrates how to fine-tune `bert-base-uncased` using Hugging Face Transformers and PyTorch on a real-world NLP task — sentiment analysis on 50,000 IMDB movie reviews.

The goal was not just to achieve high accuracy, but to deeply understand:
- How BERT processes and understands language
- How different fine-tuning strategies affect performance
- How smart selective fine-tuning can match full fine-tuning with far fewer parameters

---

## 📂 Dataset

- **Source:** [IMDB Dataset of 50K Movie Reviews — Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- **Size:** 50,000 reviews (25,000 Positive / 25,000 Negative)
- **Split:** 80% Train | 10% Validation | 10% Test

---

## 🛠️ Tools & Technologies

- Python
- PyTorch
- Hugging Face Transformers
- Scikit-learn
- Pandas & NumPy
- Matplotlib & Seaborn
- Jupyter Notebook / VS Code

---

## 🔄 Pipeline

```
Raw CSV Data
     ↓
Text Cleaning (HTML tags, numbers, lowercase)
     ↓
Label Encoding (positive → 1, negative → 0)
     ↓
Train / Validation / Test Split (80/10/10)
     ↓
BERT Tokenization (bert-base-uncased, max_length=256)
     ↓
PyTorch Dataset & DataLoader (batch_size=16)
     ↓
Model Training & Fine-tuning
     ↓
Evaluation & Comparison
     ↓
Real-time Sentiment Prediction
```

---

## 🧪 Experiments

Three different fine-tuning strategies were implemented and compared:

| Experiment | Strategy | Trainable Parameters |
|------------|----------|----------------------|
| Experiment 1 | Full Fine-tuning (all layers) | 109,483,778 |
| Experiment 2 | Frozen BERT (only classifier) | 1,538 |
| Experiment 3 | Last 2 Layers + Classifier | 14,177,282 |

---

## 📊 Results

| Metric | Exp 1 — Full | Exp 2 — Frozen | Exp 3 — Last 2 Layers |
|--------|-------------|----------------|----------------------|
| Accuracy | 0.9172 | 0.6916 | **0.9192** |
| Precision | 0.8843 | 0.6405 | **0.9021** |
| Recall | 0.9600 | 0.8736 | **0.9404** |
| F1 Score | 0.9206 | 0.7391 | **0.9209** |

---

## 💡 Key Insight

> Experiment 3 trained only **14 million parameters** instead of 109 million — that's **87% fewer parameters** — and still outperformed full fine-tuning!

BERT already has deep language understanding from pre-training on 3.3 billion words. The lower layers capture fundamental language patterns (grammar, syntax) that don't need to change for sentiment analysis. Only the higher-level, task-specific layers need gentle nudging.

**Smart fine-tuning > Brute force fine-tuning.**

---

## 🚀 Real-time Prediction

The notebook includes a `predict_sentiment()` function that takes any raw review text and returns the sentiment:

```python
review = "This movie was absolutely brilliant! I loved every second of it."
result = predict_sentiment(review, model_exp3, tokenizer, device)
print(result)  # Positive 😊
```

---

## 📁 Repository Structure

```
├── BERT_Sentiment_Analysis_IMDB.ipynb   # Main notebook
├── README.md                             # Project documentation
```

---

## ⚙️ How to Run

1. Clone this repository:
```bash
git clone https://github.com/Prem-7171/BERT-Sentiment-Analysis-IMDB.git
```

2. Install required libraries:
```bash
pip install transformers torch scikit-learn pandas numpy matplotlib seaborn datasets
```

3. Download the IMDB dataset from Kaggle and place it in the project folder.

4. Open and run `BERT_Sentiment_Analysis_IMDB.ipynb` top to bottom.

---

## 📈 Training Details

- **Model:** bert-base-uncased
- **Optimizer:** AdamW
- **Learning Rate:** 2e-5
- **Epochs:** 3
- **Batch Size:** 16
- **Max Token Length:** 256

---

## 🙋‍♂️ Author

**Prem Palkar**
- B.Tech CSE (AI & ML) | Aspiring AI Researcher
- [LinkedIn](https://www.linkedin.com/in/prem-palkar-7a6b23297/)
- [GitHub](https://github.com/Prem-7171)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
