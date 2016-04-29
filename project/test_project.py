import unittest

from project import (
    is_leap_year,
)

class TestLeapYear(unittest.TestCase):
    def test_year_2000(self):
        self.assertTrue( is_leap_year(2000) )

