from django.apps import AppConfig

from paperless_textract.signals import textract_consumer_declaration


class PaperlessTextractConfig(AppConfig):
    name = "paperless_textract"

    def ready(self):
        from documents.signals import document_consumer_declaration

        document_consumer_declaration.connect(textract_consumer_declaration)

        AppConfig.ready(self)
