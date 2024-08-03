import streamlit
import google.generativeai as genai
import os
import streamlit as st
import PyPDF2  as pdf
from dotenv import load_dotenv
load_dotenv()

google_api = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api)


def get_response(prompt):
    model = genai.GenerativeModel(
        
        "gemini-pro"
    )
    response = model.generate_content(prompt)
    
    import json
    return json.loads(response.text.strip())

def inport_pdf_text(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

prompt = """
    Big Data Engineer ATS Assistant: Evaluate Resume and Job Description for Optimal Match
As a seasoned Big Data Engineer, your task is to scrutinize the resume based on the provided job description, considering the highly competitive job market. Provide expert assistance to enhance the resume, assigning a percentage match score based on the 3D framework (Demand, Delivered, and Differentiation). Identify missing keywords with high accuracy.
Input:
Resume:{text}
Job Description: {jd}
Response:
{{"Match Percentage": "30", "Missing Keywords": ["Data Lake", "Spark", "NoSQL"], "Profile Summary": "Highly skilled Big Data Engineer with 5+ years of experience in Hadoop, Java, and Python.
 Proven track record of delivering scalable data solutions. Enhance resume by highlighting expertise in Data Lake, 
Spark, and NoSQL to increase match percentage."}}
"""

st.title("ATS")
st.text("Improve the Resume ATS")

jd = st.text_input("Paste the Job Description")
upload_file = st.file_uploader("upload your resume",type = "pdf",help = "upload the pdf")
submit = st.button("submit")

try: 
    if submit and upload_file:
        file = upload_file
        text = inport_pdf_text(file)
        response = get_response(prompt.format(text=text, jd=jd))
        st.json(response)

        st.subheader("Resume Analysis")
        st.write(text)

except Exception as e:
    st.error("An error occurred: " + str(e))