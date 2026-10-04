import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

# Page configuration
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="centered"
)

# Title
st.title("🎯 AI Interview Coach")
st.write("Practice interviews and get AI-powered feedback.")

# Job role
job_role = st.selectbox(
    "Select your job role",
    [
        "Data Analyst",
        "Python Developer",
        "AI/ML Fresher",
        "Software Developer",
        "Business Analyst",
        "frontend developer",
        "backend developer"
        "software engineer"
    ]
)

# Interview question
question = st.text_area(
    "Interview Question",
    "Tell me about yourself."
)

# User answer
answer = st.text_area(
    "Your Answer",
    height=200,
    placeholder="Type your interview answer here..."
)

# Button
if st.button("Evaluate My Answer"):

    if answer.strip() == "":
        st.warning("Please enter your answer first.")

    else:

        prompt = f"""
You are an expert interview coach.

The candidate is applying for the role of {job_role}.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Give the response in this format:

Overall Score: X/10

Communication: X/10

Relevance: X/10

Confidence: X/10

Strengths:
- Point 1
- Point 2
- Point 3

Weaknesses:
- Point 1
- Point 2
- Point 3

Improved Answer:
Give a better version of the candidate's answer.

Tips:
- Tip 1
- Tip 2
- Tip 3
"""

        with st.spinner("AI is analyzing your answer..."):

            response = model.generate_content(prompt)

        st.subheader("📊 AI Feedback")

        st.write(response.text)