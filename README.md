# 🧠 Twitter Sentiment Analysis App

A machine learning project that classifies tweets into **Positive, Negative, Neutral, and Irrelevant** sentiments using **TF-IDF and Logistic Regression**.

---

## 📌 Project Overview

This project performs sentiment analysis on Twitter data using classical NLP techniques. It includes:

* Data collection from Kaggle
* Text preprocessing and cleaning
* Feature extraction using TF-IDF
* Model training using Logistic Regression
* Evaluation with classification metrics
* Model saving and report generation

---

## 📂 Dataset

Dataset used: **Twitter Entity Sentiment Analysis**

* Source: Kaggle (via `kagglehub`)
* Training samples: **74,681**
* Test samples: **999**
* Classes:

  * Positive
  * Negative
  * Neutral
  * Irrelevant

---

## ⚙️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Regex (Text Cleaning)
* ReportLab (PDF generation)
* Pickle (Model saving)

---

## 🔄 Workflow

### 1. Data Collection

* Dataset downloaded using `kagglehub`
* Extracted ZIP files automatically

### 2. Data Preprocessing

* Lowercasing text
* Removing URLs, mentions, special characters
* Removing extra spaces

### 3. Feature Engineering

* TF-IDF Vectorization
* N-grams: (1,2)
* Max features: 5000

### 4. Model Training

* Algorithm: Logistic Regression
* Parameters:

  * `max_iter=1000`
  * `class_weight="balanced"`

### 5. Evaluation

* Accuracy Score
* Precision, Recall, F1-score

---

## 📊 Model Performance

* **Accuracy:** 80.28%

### Classification Report:

| Class      | Precision | Recall | F1-score |
| ---------- | --------- | ------ | -------- |
| Irrelevant | 0.73      | 0.82   | 0.77     |
| Negative   | 0.81      | 0.82   | 0.81     |
| Neutral    | 0.82      | 0.75   | 0.79     |
| Positive   | 0.83      | 0.83   | 0.83     |

---

## 💾 Model Saving

The trained model and vectorizer are saved using pickle:

* `model.pkl`
* `vectorizer.pkl`

---

## 📄 PDF Report Generation

* Automatically generates report using ReportLab
* Saves file with sequential naming:

sentiment_report_1.pdf
sentiment_report_2.pdf
...

---

## 📸 Screenshot

Add your screenshot here:

```md
![Prediction Output](prediction_result.png)
```

---

## 🚀 How to Run

### 1. Clone Repository

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2. Install Dependencies

```bash
pip install pandas scikit-learn kagglehub reportlab
```

### 3. Run Notebook / Script

```bash
python app.py
```

---

## 📁 Project Structure

```
sentiment-analysis-app/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── notebook.ipynb
│── prediction_result.png
│── sentiment_report_1.pdf
│── README.md
│── .gitignore
```

---

## 🔮 Future Improvements

* Deploy using Streamlit / Hugging Face
* Add deep learning models (LSTM, BERT)
* Improve preprocessing (stemming, lemmatization)
* Add real-time tweet prediction

---

## 👨‍💻 Author

**Mohd Fauzan**
M.Tech Data Science | JNU

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
