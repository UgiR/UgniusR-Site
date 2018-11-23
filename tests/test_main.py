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



    def test_projects(self):
        r = self.app.get('/projects')
        self.assertEqual(r.status_code, 200)

    def test_library(self):
        r = self.app.get('/library')
        self.assertEqual(r.status_code, 200)

    def test_coursework(self):
        r = self.app.get('/coursework')
        self.assertEqual(r.status_code, 200)

    def test_experience(self):
        r = self.app.get('/experience')
        self.assertEqual(r.status_code, 200)

unittest.main()
