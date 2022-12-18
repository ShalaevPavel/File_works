from django.test import SimpleTestCase
from django.urls import reverse, resolve
from fileoperations.views import index, api_file


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')

        self.assertEquals(resolve(url).func, index)

    def test_n_times_string_is_resolved(self):
        url = reverse("api_file", args=[1])

        self.assertEquals(resolve(url).func, api_file)
