from django.test import SimpleTestCase
from fileoperations.forms import FileForm, FileBuilderForm


class TestForms(SimpleTestCase):

    def test_file_builder_form_valid(self):
        form = FileBuilderForm(data={
            "input_file": "a.txt",
            "output_file": "b.txt",
            "file_type": "txt",
            "is_zipped": False,
            "is_encrypted": False,
            "key_file": "c.txt"
        })
        self.assertTrue(form.is_valid())

    def test_no_data_in_builder_form(self):
        form = FileBuilderForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)



    def test_file_form_valid(self):
        form = FileForm(data={
            "input_file": "a.txt",
            "output_file": "b.txt",
        })
        self.assertFalse(form.is_valid())

    def test_no_data_in_file_form(self):
        form = FileForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
