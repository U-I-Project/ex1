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

    def test_main_happy(self):
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
    def test_main_unhappy(self):
        self.io.seek(0)
        sys.argv = ['command']
        leapmonth.main()
        usage = self.io.getvalue().strip()
        test_patterns =[
            {'in':['command', '-2000', '1'], 'expected':usage},
            {'in':['command'], 'expected':usage},
            {'in':['command', '2000', '13'], 'expected':usage},
            {'in': ['command', 'test', 'test2'], 'expected': usage},
        ]
        for pattern in test_patterns:
            with self.subTest(pattern['in']):
                self.io.seek(0)
                sys.argv = pattern['in']
                leapmonth.main()
                actual = self.io.getvalue().strip()
                with self.subTest(pattern['in']):
                    self.assertEqual(actual, pattern['expected'])
