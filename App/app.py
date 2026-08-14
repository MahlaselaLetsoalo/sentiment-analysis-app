# Import libraries
import streamlit as st

# Import predictor
from predictor import predict_sentiment

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)

# Title
st.title("💬 Sentiment Analysis System")

st.write(
    "Enter a piece of text and the machine learning model "
    "will classify it as positive or negative."
)

# Example text
example = st.selectbox(
    "Try an example",
    [
        "Select an example...",
        "Machine learning is amazing.",
        "This is the worst pizza ever.",
        "The service was excellent and the staff were friendly.",
        "I absolutely love my new car, it's so comfortable."
    ]
)

# Text input
text = st.text_area(
    "Enter your text",
    value="" if example == "Select an example..." else example,
    height=150,
    placeholder="Example: I absolutely love machine learning"
)

# Analyze button
if st.button("🔍 Analyze Sentiment", use_container_width=True):

    if not text.strip():

        st.warning("Please enter some text before analyzing.")

    else:

        sentiment, confidence = predict_sentiment(text)

        st.divider()

        st.subheader("Prediction")

        # Display sentiment
        if sentiment == "Positive":

            st.success(f"😊 {sentiment}")

        else:

            st.error(f"😞 {sentiment}")

        # Display confidence
        st.write(
            f"**Confidence:** {confidence:.2%}"
        )

        # Confidence progress bar
        st.progress(confidence)

st.divider()

# About section
st.subheader("About the Model")

st.write(
    "This application uses a Logistic Regression classifier "
    "trained on the Sentiment140 dataset to classify the sentiment "
    "of text into positive and negative. Text is converted into "
    "into numerical features using TF-IDF before classification."
)

st.caption(
    "Machine Learning • Natural Language Processing • "
    "TF-IDF • Logistic Regression"
)