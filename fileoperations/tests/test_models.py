from django.db.models import Max
from django.test import Client, TestCase
from django.test import SimpleTestCase
from fileoperations.models import File, FileBuilder


class TestModels(TestCase):

    def setUp(self):
        self.file_builder = FileBuilder.objects.create(input_file="input_file.json", output_file="output_file.json",
                                                       file_type="json", is_zipped=False, is_encrypted=True,
                                                       key_file="key_file.txt")

    def test_serialize(self):
        self.assertEqual(self.file_builder.serialize(), {
            "input_file": "input_file.json",
            "output_file": "output_file.json",
            "file_type": "json",
            "is_zipped": False,
            "is_encrypted": True,
            "key_file": "key_file.txt"
        })

    def test_file_builder_str(self):
        self.assertEqual(str(self.file_builder), "input_file.json to output_file.json")
