from fpdf import FPDF
from PIL import Image

def images_to_pdf(image_paths, output_pdf):
    pdf = FPDF()
    for image_path in image_paths:
        cover = Image.open(image_path)
        width, height = cover.size
        pdf.add_page()
        pdf.image(image_path, 0, 0, 210, 0)  # fits A4 width
    pdf.output(output_pdf, "F")
    return output_pdf
