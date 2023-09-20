def get_parser(*args, **kwargs):
    from .parsers import TextractParser

    return TextractParser(*args, **kwargs)


def textract_consumer_declaration(sender, **kwargs):
    return {
        "parser": get_parser,
        "weight": 1,
        "mime_types": {
            "image/jpeg": ".jpg",
        },
    }
