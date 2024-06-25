from actions import SummarizeTextAction
from utils import extract_text_from_pdf
from flow import Flow
import gradio as gr
from io import BytesIO
from reportlab.pdfgen import canvas
from flask import Flask, send_file

app = Flask(__name__)

async def summarize_input(input_text, input_pdf):
    try:
        if input_pdf:
            text = await extract_text_from_pdf(input_pdf.name)
        else:
            text = input_text

        summary = await flow.execute_action('summarize_text', text)
        
        # Generate PDF and save to a BytesIO buffer
        pdf_bytes = generate_pdf(summary)
        
        return summary, pdf_bytes
    except Exception as e:
        return f"Error: {str(e)}", None

def generate_pdf(summary):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, "Summarized Text:")
    pdf.drawString(100, 730, summary)
    pdf.save()
    buffer.seek(0)
    return buffer

# Initialize flow and add actions
flow = Flow()
flow.add_action('summarize_text', SummarizeTextAction())

# Gradio interface function
def gr_interface(input_text, input_pdf):
    summary, pdf_bytes = asyncio.run(summarize_input(input_text, input_pdf))
    return summary

# Route for downloading PDF
@app.route('/download-pdf')
def download_pdf():
    _, pdf_bytes = asyncio.run(summarize_input("", None))
    return send_file(pdf_bytes, as_attachment=True, attachment_filename="summary.pdf")

# Gradio interface setup
iface = gr.Interface(
    fn=gr_interface,
    inputs=[
        gr.Textbox(lines=10, placeholder="Paste text here..."),
        gr.File(label="Upload PDF")
    ],
    outputs="text",
    title="Text Summarizer",
    description="Upload a PDF file or paste text to get a summary. Download the summary as a PDF <a href='/download-pdf' target='_blank'>here</a>."
)

# Launch the interface
iface.launch(inbrowser=True, share=True, debug=True)
