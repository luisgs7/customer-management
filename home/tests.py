from django.test import TestCase


class TestApp(TestCase):

    def test_one(self):
        self.assertEqual(2, 1+1)

    def test_two(self):
        self.assertEqual(2, 1+1)