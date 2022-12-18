from django.db.models import Max
from django.test import Client, TestCase
from django.test import SimpleTestCase
from fileoperations.views import encrypt, index, build, api_file
from fileoperations.models import File, FileBuilder


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_encrypt(self):
        response = self.client.get("/encrypt")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "encrypt.html")

    def test_unreachable_page(self):
        response = self.client.get("/unreachable/")
        self.assertEqual(response.status_code, 404)

    def test_build(self):
        response = self.client.get("/build")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "build.html")

    def test_api_valid_file(self):
        fielbuilder = FileBuilder.objects.create(input_file="input_file.json", output_file="output_file.json", file_type="json", is_zipped=False, is_encrypted=True, key_file="key_file.txt")
        response = self.client.get(f"/api/file/{fielbuilder.id}")
        self.assertEqual(response.status_code, 200)
