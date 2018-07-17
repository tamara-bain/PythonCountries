#!/usr/local/bin/python3

import unittest

from countries import COUNTRY_TUPLES, Country, get_country_for_code

class CountriesTestCase(unittest.TestCase):

    def test_country_tuples(self):
        self.assertNotEqual(len(COUNTRY_TUPLES), 0)
        self.assertEqual(len(COUNTRY_TUPLES[0]), 2)
        self.assertEqual(len(COUNTRY_TUPLES[0][0]), 2)
        self.assertGreater(len(COUNTRY_TUPLES[0][1]), 2)
        self.assertIsInstance(COUNTRY_TUPLES[0][0], str)
        self.assertIsInstance(COUNTRY_TUPLES[0][1], str)

    def test_country_object(self):
        country = Country('CA', 'Canada')
        self.assertEqual(country.code, 'CA')
        self.assertEqual(country.name, 'Canada')

    def test_get_country_for_code(self):
        country = get_country_for_code('CA')
        self.assertEqual('Canada', country.name)

    def test_get_country_for_invalid_code(self):
        country = get_country_for_code('BLAH')
        self.assertIsNone(country, None)



