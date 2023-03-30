from PyPDF2 import PdfReader

class Reader:
    def __init__(self, pdf):
        self.reader = PdfReader(pdf)
        self.page = self.reader.pages[0]
        self.text = self.page.extract_text()

    def read(self):
        return self.text
