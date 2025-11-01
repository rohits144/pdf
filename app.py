import streamlit as st
from fpdf import FPDF
from PIL import Image
import tempfile
import os

st.title("🖼️ Images to PDF Converter")

uploaded_files = st.file_uploader("Upload images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    if st.button("Convert to PDF"):
        pdf = FPDF()
        temp_dir = tempfile.mkdtemp()

        for file in uploaded_files:
            image_path = os.path.join(temp_dir, file.name)
            with open(image_path, "wb") as f:
                f.write(file.getbuffer())
            cover = Image.open(image_path)
            pdf.add_page()
            pdf.image(image_path, 0, 0, 210, 0)

        output_pdf = os.path.join(temp_dir, "output.pdf")
        pdf.output(output_pdf, "F")

        with open(output_pdf, "rb") as f:
            st.download_button("📥 Download PDF", f, file_name="converted.pdf")
