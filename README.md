# Text Summarizer

## Overview

The Text Summarizer is a Python application that provides a simple interface for summarizing text documents or input using natural language processing techniques. It leverages a text summarization model to generate concise summaries from large blocks of text, enhancing readability and efficiency in information retrieval.

## Features

- **Input Options:** Accepts text input via a textbox or PDF file upload.
- **Summarization Techniques:** Utilizes advanced algorithms to condense text while preserving key information.
- **Downloadable Summary:** Provides the option to download the generated summary as a text file or PDF.
- **Integration with Gradio:** Offers a user-friendly interface powered by Gradio for easy interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kirai-Kevin/textsum.git
   cd textsum

Install dependencies:

pip install -r requirements.txt
Ensure necessary NLTK data is downloaded:

python -m nltk.downloader stopwords punkt
Usage
Run the application:

python main.py
Access the application through the provided URL or open in your browser.

Paste text into the textbox or upload a PDF file.

Click on "Summarize" to generate a summary.
