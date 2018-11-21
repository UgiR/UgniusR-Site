import unittest

from UgniusR import app


class CourseworkPage(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        print(app.blueprints)

    def tearDown(self):
        pass

    # TESTS

    def test_courses(self):
        r = self.app.get('/api/public/courses')
        self.assertEqual(r.status_code, 200)


#unittest.main()
