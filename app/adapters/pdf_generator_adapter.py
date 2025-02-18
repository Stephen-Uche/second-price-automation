from xhtml2pdf import pisa 
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "invoice.html"
template = templateEnv.get_template(TEMPLATE_FILE)

from ..usecases.i_file_handler import IFileHandler


class PdfGeneratorAdapter(IFileHandler):
    def __init__(self, pdf_generator):
        self.pdf_generator = pdf_generator
        
    def write(self, content: str, path: str) -> None:
        with open(path, 'w') as file:
            file.write(content)
            
    def read(self, path: str) -> None:
        with open(path, 'r') as file:
            file.read(path)           

