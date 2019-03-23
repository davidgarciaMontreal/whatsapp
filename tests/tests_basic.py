from .context import whatsapp



def test_instance():
    instance = whatsapp.WhatsApp()
    assert instance.file == "Hello"
