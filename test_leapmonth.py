import sys
from io import StringIO
from unittest import TestCase
import calendar

import ast
from restrictions import check_import

import leapmonth


class TestMain(TestCase):
    def setUp(self):
       self.stdout = sys.stdout
       self.io = StringIO()
       sys.stdout = self.io

    def tearDown(self):
        sys.stdout = self.stdout
        pass

    def test_restrictions(self):
        import_set = ('sys')
        with open('leapmonth.py') as f:
            tree = ast.parse(f.read())
        check_import(tree, import_set)

    def test_main(self):
        test_years = [2000, 2001, 2002, 2003, 2004, 2100]
        test_monthes = [i for i in range(1, 13)]
        for year in test_years:
            for month in test_monthes:
                self.io.seek(0)
                sys.argv = ['command', str(year), str(month)]
                leapmonth.main()
                expected = 'Month of ' + str(month) + '/' + str(year) + ' has ' + str(calendar.monthrange(year, month)[1]) + ' days.'
                actual = self.io.getvalue().strip()
                with self.subTest((year, month)):
                        self.assertEqual(actual, expected)
