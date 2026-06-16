import streamlit as st
import pickle
import os

# Page Config

st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎫",
    layout="wide"
)

# Load Models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "ticket_type_model.pkl")
priority_path = os.path.join(BASE_DIR, "models", "priority_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
priority_model = pickle.load(open(priority_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))


# Header

st.title(" Support Ticket Classification & Prioritization System")

st.markdown("""
This NLP-powered system automatically classifies customer support tickets
and predicts their priority level to help support teams respond faster and
manage support operations more efficiently.
""")

st.divider()


# Example Tickets

st.subheader("Quick Examples")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(" Billing Issue"):
        st.session_state.ticket = (
            "I was charged twice for my subscription and need a refund."
        )

with col2:
    if st.button(" Technical Issue"):
        st.session_state.ticket = (
            "The application crashes every time I try to log in."
        )

with col3:
    if st.button(" Cancellation Request"):
        st.session_state.ticket = (
            "I would like to cancel my subscription immediately."
        )

st.divider()


# Two-Column Dashboard Layout

left_col, right_col = st.columns([2, 1])


# Left Side - Ticket Input

with left_col:

    st.subheader("Customer Support Ticket")

    ticket = st.text_area(
        "Enter Ticket",
        value=st.session_state.get("ticket", ""),
        height=350,
        label_visibility="collapsed",
        placeholder="Enter customer ticket here..."
    )

    predict = st.button(" Predict")


# Right Side - Results

with right_col:

    st.subheader("Prediction Results")

    if predict:

        if ticket.strip():

            vec = vectorizer.transform([ticket])

            category = model.predict(vec)[0]
            priority = priority_model.predict(vec)[0]

            st.metric(
                label="Ticket Category",
                value=category
            )

            st.metric(
                label="Priority Level",
                value=priority
            )

            # Priority Badge
            if priority.lower() == "critical":
                st.error("🔴 Critical Priority")

            elif priority.lower() == "high":
                st.warning("🟠 High Priority")

            elif priority.lower() == "medium":
                st.info("🟡 Medium Priority")

            else:
                st.success("🟢 Low Priority")

            st.divider()

            # Confidence Scores
            st.subheader("Model Confidence")

            category_conf = model.predict_proba(vec).max() * 100
            priority_conf = priority_model.predict_proba(vec).max() * 100

            st.write(
                f"**Category Confidence:** {category_conf:.2f}%"
            )

            st.write(
                f"**Priority Confidence:** {priority_conf:.2f}%"
            )

        else:
            st.warning("Please enter a support ticket.")