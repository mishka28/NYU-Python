# ake sure to delete db before running the tests if possible

import unittest
from mock import patch as patch
import blog
import sys
import os

from flask import (Flask, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)


class TestEntry(unittest.TestCase):
    def setUp(self):
        self.entry = blog.Entry()

    def testdb(self):
        path = '../blog.db'
        assert os.path.exists(path) is True

if __name__ == '__main__':
    unittest.main()
