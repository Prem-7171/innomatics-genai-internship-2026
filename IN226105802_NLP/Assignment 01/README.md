# 🧠 NLP Preprocessing Engine (Advanced)

A robust and modular Natural Language Processing (NLP) preprocessing pipeline built as part of a Data Science Internship assignment.

This project focuses on transforming messy real-world text into clean, structured, and meaningful data suitable for machine learning models.

---

## 🚀 Features

* ✅ Lowercase normalization
* ✅ Removal of numbers and extra spaces
* ✅ Handling repeated characters (e.g., *"soooo" → "soo"*)
* ✅ Removal of URLs and email patterns
* ✅ Punctuation cleaning
* ✅ Intelligent short token filtering

  * Removes words with length ≤ 2
  * Preserves meaningful words like **"no"** and **"not"**
* ✅ Tokenization
* ✅ Token-level analytics
* ✅ Frequency analysis using `collections.Counter`
* ✅ Full pipeline for batch processing
* ✅ Edge case handling (empty text, emojis, numbers-only input)

---

## 🧩 Project Structure

```
├── NLP_Preprocessing.ipynb
├── README.md
```

---

## ⚙️ Technologies Used

* Python 🐍
* Regular Expressions (`re`)
* Collections (`Counter`)
* Jupyter Notebook

---

## 🔧 Core Function

### `preprocess_text(text)`

Cleans and normalizes a single text input.

### Steps performed:

1. Convert text to lowercase
2. Remove numbers
3. Normalize repeated characters
4. Remove URLs and email patterns
5. Remove punctuation
6. Remove extra spaces
7. Tokenize text
8. Remove short tokens (with exceptions)
9. Reconstruct cleaned sentence

---

## 🔄 Full Pipeline

### `full_pipeline(text_list)`

Processes a list of text inputs and returns structured output.

```python
{
  "tokens": [...],
  "clean_sentences": [...]
}
```

---

## 🧪 Sample Input

```python
[
"Get 100% FREE access now!!!",
"I absolutely looooved this product 😍😍",
"Worst service ever... 0/10",
"Call me at 9876543210",
"This is THE best course!!!",
"Visit https://openai.com now!",
"Nooooo this is baaad!!!",
"OK OK OK I got it",
"Win $$$ now!!! Limited offer!!!",
"I am not happy with this"
]
```

---

## 📊 Sample Output

```
Original: I absolutely looooved this product 😍😍  
Tokens: ['absolutely', 'looved', 'this', 'product']  
Cleaned: absolutely looved this product  

Original: OK OK OK I got it  
Tokens: ['got']  
Cleaned: got  
```

---

## 📈 Token Analytics

For each sentence:

* Total tokens
* Unique tokens
* Average token length

---

## 🔍 Frequency Analysis

* Top 10 most frequent words
* Top 5 least frequent words

Implemented using:

```python
from collections import Counter
```

---

## ⚠️ Edge Case Handling

The pipeline safely handles:

* Empty strings
* Only emojis
* Only numbers

---

## 🧠 Key Learnings

* Importance of text normalization in NLP
* Handling noisy real-world data
* Designing modular and reusable pipelines
* Balancing cleaning with meaning preservation
* Using Python efficiently for text processing

---

## 📌 How to Run

1. Clone the repository
2. Open the notebook in Jupyter/VS Code
3. Run all cells sequentially

---

## 🎯 Future Improvements

* Stopword customization
* Stemming & Lemmatization integration
* N-gram analysis
* Vectorization (TF-IDF, Word2Vec)
* Integration with ML models

---

## 👨‍💻 Author

**Prem Palkar**
B.Tech CSE (AI & ML) Student
Aspiring AI Engineer 🚀

---

## ⭐ Acknowledgment

This project was developed as part of an internship assignment focused on building real-world NLP preprocessing pipelines.
