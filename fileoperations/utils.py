import re
import json
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from pathlib import Path

from cryptography import fernet
from cryptography.fernet import Fernet


class FileInterface:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def write(self, text):
        pass

    def read(self):
        pass


def calculate_math_expressions(strq: str) -> str:
    math_expressions_only = re.sub(r'((?:[^\d+\-*/]+)|(?<!\d)[+\-*/]|[+\-*/](?!\d))', ' ', strq)
    marked_string = re.sub(r'[0-9]+([\+\-\*\/][0-9])*', '__to_replace_back__ ', strq)
    arr = math_expressions_only.split()
    evaluated_values = []
    for element in arr:
        evaluated_values.append(eval(element))

    for i in range(len(evaluated_values)):
        str_tmp = marked_string.replace('__to_replace_back__', str(evaluated_values[i]), 1)
        marked_string = str_tmp
    marked_string = marked_string.replace('__to_replace_back__', '')
    return marked_string


class TxtFile(FileInterface):

    def write(self, text: str):
        with open(self.output_file, "w") as f:
            f.write(text)

    def read(self) -> str:
        with open(self.input_file, "r") as f:
            text = f.read()
        return text


class JSONFile(FileInterface):

    def write(self, text: str):
        with open(self.output_file, "w") as f:
            f.write(text)

    def read(self) -> str:
        with open(self.input_file, "r") as f:
            text = f.read()
            return text


class XMLFile(FileInterface):

    def write(self, text: str):
        with open(self.output_file, "w") as f:
            f.write(text)

    def read(self) -> str:
        with open(self.input_file, "r") as f:
            text = f.read()
        return text


class DecryptFile:
    @staticmethod
    def decrypt(input_file: str, key_file: str):
        with open(key_file, "rb") as f:
            key = f.read()
        fernet = Fernet(key)

        with open(input_file, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(input_file, 'wb') as dec_file:
            dec_file.write(decrypted)


class ZipperFile:
    @staticmethod
    def unzip_in_same_dir(input_file: str) -> str:
        with ZipFile(input_file, 'r') as f:
            path = Path(input_file)

            f.extractall(path.parent.absolute())
        tmp = input_file[:len(input_file) - 4]
        return tmp


class Builder:
    def __init__(self, input_file, output_file, file_type, is_encrypted, is_zipped, key_file=None):
        self.input_file = input_file
        self.output_file = output_file
        self.file_type = file_type
        self.is_encrypted = is_encrypted
        self.is_zipped = is_zipped
        self.key_file = key_file

    def build(self):
        if self.is_zipped:
            self.input_file = ZipperFile.unzip_in_same_dir(self.input_file)
            print(self.input_file)

        if self.is_encrypted:
            DecryptFile.decrypt(self.input_file, self.key_file)

        if self.file_type == "txt":
            return TxtFile(self.input_file, self.output_file)
        elif self.file_type == "json":
            return JSONFile(self.input_file, self.output_file)
        elif self.file_type == "xml":
            return XMLFile(self.input_file, self.output_file)
        else:
            raise Exception("Invalid file type")

# cl = Builder("input.txt.zip", "output.txt", "txt", True, True, "key.txt")
# a = cl.build()
# a.write(calculate_math_expressions(a.read()))

# if __name__ == "__main__":
    # cl = Builder("../files/input.txt.zip", "../files/output.txt", "txt", True, True, "../files/key.txt")
    # a = cl.build()
    # a.write(calculate_math_expressions(a.read())) works!!
    #cl = Builder("input.txt.zip", "output.txt", "txt", True, True, "key.txt")