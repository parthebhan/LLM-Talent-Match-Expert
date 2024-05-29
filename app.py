import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf

# Configure the API key
api_key = st.secrets["auth_token"]
genai.configure(api_key=api_key)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Gemini Pro Response
def gemini_response(input):
  model = genai.GenerativeModel("gemini-1.5-pro-latest")
  response=model.generate_content(input)
  return response.text

# Extrating Text from PDF
def input_pdf_text(resume):
  reader=pdf.PdfReader(resume)
  text=""
  for page in reader:
    page=reader.pages[pages]
    text += str(page.extract_text())
  return text

# prompt template

prompt = """
Hey AI, assume the role of a seasoned and adept ATS (Application Tracking System) specialized in software engineering, data science, data analysis, and big data engineering.
Your mission is to meticulously assess a resume in comparison to a provided job description. The job market is fiercely competitive, and your objective is to provide unparalleled assistance in enhancing resumes.
Assign a percentage match based on the job description criteria and pinpoint missing keywords with utmost accuracy.

Evaluation Instructions:

    1. Thoroughly evaluate the resume against the provided job description.
    2. Assign a percentage match based on the degree of alignment with the job description.
    3. Precisely identify missing keywords, meticulously considering the job's specific requirements.
    4. Offer expert guidance for refining the resume to bolster its competitiveness in the job market.

resume:{text}
description:{jd}

I want the response in string having the structure in seperate line
{{"Talent Match":"%",
"Missing skills:[]",
"Profile Summary":""
}}

"""

# Inializing Streatlit app

st.header("Talent Match Expert")
st.write("")
st.write("Created by: Parthebhan pari")
st.write("")
st.text("checking resume and job description compatibility")
jd=st.text_area("paste the Job Description here..")
resume=st.file_uploader("Upload your resume",type= "pdf",help="Upload PDF file only")

submit = st.button("Submit")

if submit:
  if resume is not None:
    resume_content = resume.read()  # Read the content of the uploaded file
    text = input_pdf_text(resume_content)  # Pass the content to input_pdf_text function
    response = gemini_response(prompt)
    st.write(response)