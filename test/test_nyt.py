import unittest
from NYTPythonWrapper.nyt import NoKeyException, NYTSearch


class TestNYTSearch(unittest.TestCase):

    def test_no_key(self):
        with self.assertRaises(NoKeyException) as context:
            NYTSearch()


if __name__ == '__main__':
    unittest.main()
