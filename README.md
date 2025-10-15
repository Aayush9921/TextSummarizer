# 📝⚡ Text Summarization App

This is a simple web application built with **Streamlit** and **Hugging Face Transformers** that allows users to summarize text using AI. The app uses the `facebook/bart-large-cnn` model for generating concise summaries of the input text.

---

## Features

- Enter text (up to ~500 words) and generate a summarized version.
- Easy-to-use web interface.
- Powered by state-of-the-art Transformer model for high-quality summarization.

---

## Requirements

- Python 3.8 or above
- Streamlit
- Transformers
- PyTorch (required by Transformers)

The required packages are listed in `requirements.txt`.

---
## Project Structure

TextSummarizer/
├── App.py           # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md        # Project documentation

---

## Installation

1. **Clone the repository** (or download the files):

```bash
git clone https://github.com/Aayush9921/TextSummarizer.git
cd TextSummarizer

2. **Install dependencies:**

pip install -r requirements.txt

3. **Run the Streamlit app:**

streamlit run App.py

