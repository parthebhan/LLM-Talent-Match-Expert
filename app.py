import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import json

# Configure the API key
api_key = st.secrets["auth_token"]
genai.configure(api_key=api_key)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in string having the structure in each line

  "Talent Match":" %",

  "MissingKeywords":[ ]",

  "Profile Summary":" ",

  
"""


# Inializing Streatlit app

st.header("Talent Match Expert")
st.write("")
st.write("Created by: Parthebhan pari")
st.write("")
st.text("checking resume and job description compatibility")
jd=st.text_area("paste the Job Description here..")
uploaded_file=st.file_uploader("Upload your resume",type= "pdf",help="Upload PDF file only")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=gemini_repsonse(prompt)
        st.write("Talent Expert's response")
        st.subheader(response)





