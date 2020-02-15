import base64
import binascii
import tempfile

from core.exceptions.temb64 import BrokenBase64


class TemporaryBase64:

    def __init__(self, directory: str):
        self.directory = directory
        self.file = tempfile.NamedTemporaryFile(dir=directory)
        self.file_path = self.file.name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write_string(self, b64: str) -> None:
        try:
            b64 = base64.b64decode(b64)
        except binascii.Error:
            raise BrokenBase64
        self.file.write(b64)
