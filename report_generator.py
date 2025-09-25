
import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

# Load templates from a 'templates' folder
TEMPLATE_FOLDER = os.path.join(os.path.dirname(__file__), "templates")
WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
def generate_html_report(data, filename="report.html"):
    env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
    template = env.get_template("report_template.html")
    html_content = template.render(data)
    
    output_path = os.path.join("reports", filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return output_path

def generate_pdf_report(data, filename="report.pdf"):
    html_file = generate_html_report(data, filename="temp.html")
    pdf_path = os.path.join("reports", filename)
    pdfkit.from_file(html_file, pdf_path , configuration=config)
    os.remove(html_file)  # Remove temp HTML
    return pdf_path