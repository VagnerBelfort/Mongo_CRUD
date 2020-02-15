import os
import re
import base64
import subprocess
from typing import Union, AnyStr, List

from core.exceptions.mypdf import MyPDFFileError


def npage(file_path: str) -> int:
    try:
        cmd_output = subprocess.check_output(['pdfinfo', file_path])
    except subprocess.CalledProcessError:
        raise MyPDFFileError
    pages = re.findall(r'Pages:\s+(\d+)', cmd_output.decode('utf-8'))[0]
    return int(pages)


def totext(file_path: str) -> Union[int, str]:
    file_directory = os.path.dirname(file_path)
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))

    try:
        subprocess.check_output(['pdftotext', '-raw', file_path])
    except subprocess.CalledProcessError:
        raise MyPDFFileError

    text_file = f'{os.path.join(file_directory, file_name)}.txt'
    with open(text_file, 'r') as output_file:
        text = ''.join(output_file.readlines())
    os.remove(text_file)

    return text


def toimage(file_path: str, image_type: AnyStr = '-jpeg') -> Union[int, List]:
    pages = npage(file_path)

    images = []
    for page in range(1, pages + 1):
        try:
            cmd_output = subprocess.check_output(['pdftoppm', image_type, '-f', str(page), '-l', str(page), file_path])
        except subprocess.CalledProcessError:
            raise MyPDFFileError

        image = base64.b64encode(cmd_output)
        image = image.decode('utf-8')
        images.append(image)

    return images
