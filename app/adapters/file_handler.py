from xhtml2pdf import pisa 
import jinja2
import pathlib

from ..usecases.i_file_handler import IFileHandler

class FileHandler(IFileHandler):
    def __init__(self):
        self.object_generated_path = pathlib.Path(__file__).parent.resolve() / ".." / "generated"
        self.templates_path = pathlib.Path(__file__).parent.resolve() / ".." / "templates/"
        self.template_loader = jinja2.FileSystemLoader(searchpath=f"{self.templates_path}")
        self.template_file = "qoute.html"
    
    def write(self, content: str, path: str) -> None:
        with open(path, 'w') as file:
            file.write(content)
    
    def read(self, path: str) -> None:
        with open(path, 'r') as file:
            file.read(path)
            
    def convertHtmlToPdf(self, body, filename):
        templateEnv = jinja2.Environment(loader=self.template_loader)
        template = templateEnv.get_template(self.template_file)
        source_html = template.render(json_data=body)
        file = open(f"{self.object_generated_path}/{filename}", "w+b")
        pisaStatus = pisa.CreatePDF(src=source_html, dest=file)
        file.close()
        print(pisaStatus.err, type(pisaStatus.err))
        # return pisaStatus.err
           

    