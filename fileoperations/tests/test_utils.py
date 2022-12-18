from django.test import SimpleTestCase
from fileoperations.utils import calculate_math_expressions, TxtFile, JSONFile, XMLFile

class TestUtils(SimpleTestCase):

    def test_simple_math_expression(self):
        self.assertEqual(calculate_math_expressions("1+1"), "2 ")

    def test_compex_math_expression(self):
        self.assertEqual(calculate_math_expressions("2*5-3+1"), "8 ")

    def test_expression_with_random_characters(self):
        self.assertEqual(calculate_math_expressions(" hi 2*5-3+1 my name is 12/3 Jack 2*3-17"), " hi 8  my name is 4.0  Jack -11  ")

    def test_expression_with_random_invalid_math_operators(self):
        self.assertEqual(calculate_math_expressions("some te*xt 2*2+3 good job 13/7 goodb/ye "), "some te*xt 7  good job 1.8571428571428572  goodb/ye ")

    def test_txt_reading_and_writing(self):
        txt = TxtFile("fileoperations/tests/test.txt", "fileoperations/tests/test.txt")
        txt.write("Hello World")
        self.assertEqual(txt.read(), "Hello World")

    def test_json_reading_and_writing(self):
        json = JSONFile("fileoperations/tests/test.json", "fileoperations/tests/test.json")
        json.write("{\'Hello\': \'World\'}")
        self.assertEqual(json.read(), "{\'Hello\': \'World\'}")

    def test_xml_reading_and_writing(self):
        xml = XMLFile("fileoperations/tests/test.xml", "fileoperations/tests/test.xml")
        xml.write("<Hello>World</Hello>")
        self.assertEqual(xml.read(), "<Hello>World</Hello>")



