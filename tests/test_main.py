from flask import url_for

import unittest

from UgniusR import app


class ViewsEndpointsOK(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.url = '/coursework'

    def tearDown(self):
        pass

    # TESTS

    def test_load_coursework(self):
        with app.app_context():
            r = self.app.get('/coursework')
            self.assertEqual(r.status_code, 200)
