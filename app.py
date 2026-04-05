import streamlit as st
import pickle
import re

# -----------------------------
# Load saved model & vectorizer
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -----------------------------
# Text cleaning function
# -----------------------------
def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -----------------------------
# UI
# -----------------------------
st.title("Twitter Sentiment Analysis")
st.write("Enter a tweet and get sentiment prediction")

user_input = st.text_area("Enter Tweet")

if st.button("Predict"):
    if user_input.strip() != "":
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        # Map back to label
        label_map = {
            1: "Positive 😊",
            0: "Neutral 😐",
            -1: "Negative 😡"
        }

        st.success(f"Prediction: {label_map.get(prediction, prediction)}")
    else:
        st.warning("Please enter some text")