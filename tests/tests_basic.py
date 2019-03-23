import os
from .context import whatsapp
dir_path = os.path.dirname(os.path.realpath(__file__))
test = os.path.join(dir_path, "resources/chat.txt")

def test_instance():
    instance = whatsapp.WhatsApp(test)
    assert instance.file == "Hello"

def test_parse():
    instance = whatsapp.WhatsApp(test)
    instance.parse_file()
    assert instance.file == "Hello"