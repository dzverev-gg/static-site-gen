import unittest

from markdown_to_html import extract_title


class TestTitleExtract(unittest.TestCase):
    def test_extract_title(self):
        md = "# This is Header"
        self.assertEqual("This is Header", extract_title(md))

    def test_extract_title_from_long_file(self):
        md = """"
        we have an interesting test_extract_no_title
which includes a lot 

## second level title 

# This is Header

and some other text that we include
        """
        self.assertEqual("This is Header", extract_title(md))

    def test_extract_no_title(self):
        md = "## This is Header"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_no_title_from_a_big_file(self):
        md = """"
        This is the test 

## That will read this stuff 

and then return an exception 

> because none of this is an h1 Title"""
        with self.assertRaises(Exception):
            extract_title(md)
