import streamlit as st
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "ticket_type_model.pkl")
priority_path = os.path.join(BASE_DIR, "models", "priority_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
priority_model = pickle.load(open(priority_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

st.title("Support Ticket Classifier & Priority Predictor")

st.write(
    "Enter a customer support ticket below and the model will predict "
    "the ticket category and priority level."
)

ticket = st.text_area(
    "Customer Ticket",
    placeholder="Example: I was charged twice for my subscription and need a refund."
)

if st.button("Predict"):

    if ticket.strip():

        vec = vectorizer.transform([ticket])

        category = model.predict(vec)[0]
        priority = priority_model.predict(vec)[0]

        st.subheader("Prediction Results")

        st.write(f"**Ticket Category:** {category}")
        st.write(f"**Priority Level:** {priority}")

    else:
        st.warning("Please enter a ticket description.")