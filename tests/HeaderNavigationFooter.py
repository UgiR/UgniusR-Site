import unittest
import urllib.request

from UgniusR import app


class HeaderNavigationFooter(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    # TESTs


