# 🎬 Sentiment Analysis using NLP & Machine Learning

A complete end-to-end NLP pipeline that classifies movie reviews as **Positive** or **Negative** using advanced text preprocessing, feature engineering, and multiple machine learning models.

---

## 🚀 Project Overview

This project demonstrates how raw text data can be transformed into meaningful insights using Natural Language Processing (NLP) and Machine Learning.

The pipeline includes:

* Text preprocessing
* Feature extraction (BoW & TF-IDF)
* Model training (Logistic Regression, Naive Bayes, Decision Tree)
* Performance evaluation and comparison

---

## 🎯 Objective

To build a robust sentiment analysis system that:

* Cleans and preprocesses real-world text data
* Converts text into numerical features
* Trains multiple ML models
* Compares their performance using evaluation metrics

---

## 🧩 Dataset

* **Source**: IMDb Movie Reviews Dataset (Kaggle)
* **Size**: 50,000 reviews
* **Classes**:

  * Positive
  * Negative

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas
* NLTK
* Scikit-learn

---

## 🔄 Pipeline Workflow

```text
Raw Text
   ↓
Preprocessing
   ↓
Feature Engineering (BoW / TF-IDF)
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Evaluation
   ↓
Comparison & Insights
```

---

## 🧠 NLP Preprocessing

The following preprocessing steps were applied:

* Lowercasing
* URL removal
* Punctuation removal
* Tokenization (NLTK)
* Stopword removal (with exceptions like "no", "not")
* Lemmatization

---

## 🔧 Core Function

### `preprocess_text(text)`

Transforms raw text into cleaned and normalized form suitable for ML models.

---

## 📊 Feature Engineering

### 🔹 Bag of Words (BoW)

* Converts text into frequency-based vectors
* Simple but ignores word importance

### 🔹 TF-IDF (Used for final model)

* Assigns weights based on word importance
* Reduces impact of common words
* Improves model performance

---

## 🤖 Models Implemented

* Logistic Regression
* Naive Bayes (MultinomialNB)
* Decision Tree

---

## 📈 Model Evaluation

Evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

---

## 🏆 Results

* **Best Model**: Logistic Regression
* **Best Feature Method**: TF-IDF

### 🔍 Why Logistic Regression performed best:

* Handles high-dimensional sparse data effectively
* Captures relationships between features
* Provides better generalization

---

## ⚖️ Model Comparison

| Model               | Strength          | Weakness                           |
| ------------------- | ----------------- | ---------------------------------- |
| Naive Bayes         | Fast, efficient   | Assumes word independence          |
| Logistic Regression | Accurate, robust  | Slightly slower                    |
| Decision Tree       | Easy to interpret | Overfitting, poor with sparse data |

---

## 🔮 Predicting New Reviews

You can test the model on custom input:

```python
def sentiment_analizer(text):
    clean_text = preprocess_text(text)
    vector = tfidf.transform([clean_text])
    prediction = model.predict(vector)
    print("Review : ", text)
    print("Sentiment : ",prediction)
```

### Example:

```python
sentiment_analizer("This movie was amazing!")
# Output: positive

sentiment_analizer("Worst movie ever")
# Output: negative
```

---

## ⚠️ Important Insight

The same preprocessing pipeline must be applied during both training and prediction. Any mismatch in data processing can lead to incorrect predictions.

---

## 🧠 Key Learnings

* Importance of text preprocessing in NLP
* Difference between BoW and TF-IDF
* Model comparison and evaluation
* Handling high-dimensional text data
* Building end-to-end ML pipelines

---

## 📌 How to Run

1. Clone the repository
2. Install required libraries
3. Open the notebook
4. Run all cells sequentially

---

## 📁 Project Structure

```text
├── sentiment_analysis.ipynb
├── README.md
```

---

## 👨‍💻 Author

**Prem Palkar**
B.Tech CSE (AI & ML) Student
Aspiring AI Engineer 🚀

---

## ⭐ Acknowledgment

This project was developed as part of a Data Science Internship assignment focused on building real-world NLP pipelines and machine learning models.
