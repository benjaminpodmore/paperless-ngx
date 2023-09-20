import os

from django.conf import settings
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from documents.parsers import DocumentParser

class TextractParser(DocumentParser):
    def parse(self, document_path, mime_type, file_name=None):
        # This method does not return anything. Rather, you should assign
        # whatever you got from the document to the following fields:

        # The content of the document.
        self.text = "content"

    def get_thumbnail(self, document_path, mime_type, file_name=None):
        temp_dir = self.tempdir
        out_path = os.path.join(os.getcwd(), "Johnrogershousemay2020.webp")
        return out_path 