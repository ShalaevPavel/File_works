import os
import pathlib
import unittest

from selenium import webdriver





driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get('http://127.0.0.1:8000/')
        self.assertEqual(driver.title, "Home - File works")

    def test_encrypt_button(self):
        driver.get('http://127.0.0.1:8000/')
        button = driver.find_element("id", "encrypt_button")
        button.click()
        self.assertIsNotNone(driver.find_element("id","to_insert"))

    def test_hide(self):
        driver.get('http://127.0.0.1:8000/')
        button = driver.find_element("id", "encrypt_button")
        button.click()
        hide = driver.find_element("id", "hide_button")
        hide.click()
        self.assertEqual(driver.find_element("id", "to_insert").text, "")

    def test_multiple_increase(self):
        driver.get('http://127.0.0.1:8000/')

        self.assertIsNotNone(driver.find_element("id", "page-top"))



if __name__ == "__main__":
    unittest.main()