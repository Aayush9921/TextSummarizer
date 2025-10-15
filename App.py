from transformers import pipeline
import streamlit as st

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.title("📝⚡ Text Summarization App")
st.write("Enter your text below in 500 words and get a concise summary using AI.")

input_text=st.text_area("Enter Text Here",height=200)

if st.button("Generate Summary"):
    if input_text.strip()=="":
        st.warning("Please write something!")
    else:   
        summary = summarizer(
            input_text
            #max_length=80,   # maximum length of summary
            #min_length=30,   # minimum length
            #do_sample=False  # deterministic output
        )
        
        
        st.subheader("✨ Summary")
        st.write(summary[0]['summary_text'])