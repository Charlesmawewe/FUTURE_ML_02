import streamlit as st
import pickle
import os

# Load Models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "ticket_type_model.pkl")
priority_path = os.path.join(BASE_DIR, "models", "priority_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
priority_model = pickle.load(open(priority_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# Page Config

st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎫",
    layout="centered"
)

# Header

st.title("Support Ticket Classifier & Priority Predictor")

st.markdown("""
This NLP-powered system automatically classifies customer support tickets
and predicts their priority level to help support teams respond faster.
""")

st.divider()

# Examples

st.subheader("Example Tickets")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Billing Example"):
        st.session_state.ticket = "I was charged twice for my subscription."

with col2:
    if st.button("Technical Example"):
        st.session_state.ticket = "The application crashes every time I log in."

with col3:
    if st.button("Cancellation Example"):
        st.session_state.ticket = "I would like to cancel my subscription immediately."

# Input

ticket = st.text_area(
    "Customer Ticket",
    value=st.session_state.get("ticket", ""),
    height=150
)

# Prediction

if st.button("Predict"):

    if ticket.strip():

        vec = vectorizer.transform([ticket])

        category = model.predict(vec)[0]
        priority = priority_model.predict(vec)[0]

        st.divider()

        st.subheader("Prediction Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Ticket Category",
                value=category
            )

        with col2:
            st.metric(
                label="Priority Level",
                value=priority
            )

        # Color-coded priority
        if priority.lower() == "critical":
            st.error("🔴 Critical Priority")
        elif priority.lower() == "high":
            st.warning("🟠 High Priority")
        elif priority.lower() == "medium":
            st.info("🟡 Medium Priority")
        else:
            st.success("🟢 Low Priority")

        # Confidence Scores
        st.subheader("Model Confidence")

        category_conf = model.predict_proba(vec).max() * 100
        priority_conf = priority_model.predict_proba(vec).max() * 100

        st.write(f"Category Confidence: **{category_conf:.2f}%**")
        st.write(f"Priority Confidence: **{priority_conf:.2f}%**")

    else:
        st.warning("Please enter a customer support ticket.")