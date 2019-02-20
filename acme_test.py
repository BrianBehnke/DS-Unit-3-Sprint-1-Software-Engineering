#!/usr/bin/env python

import unittest
from acme import Product, BoxingGlove
import acme_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_new_product_weight(self):
        """Test new product weight being 15."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 15)

    def test_default_product_flammability(self):
        """Test default product weight being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_product_stealability(self):
        """Test product stealability"""
        prod = Product('Test Product', price=8, weight=20)
        self.assertEqual(prod.stealability(), "Not so stealable...")

    def test_product_explode(self):
        """Test product explodity"""
        prod = Product('Test Product', weight=100, flammability=800000)
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    """Test Acme Reporting Functions"""
    def test_default_num_products(self):
        """Test default number of items is 30 in report"""
        x = acme_report.generate_products()
        self.assertEqual(len(x), 30)

    def test_legal_names(self):
        """Test for legal names"""
        prods = acme_report.generate_products()
        adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        for i in range(len(prods)):
            p_name = prods[i].name
            split_list = p_name.split()
            self.assertIn(split_list[0], adjectives)
            self.assertIn(split_list[1], nouns)

if __name__ == '__main__':
    unittest.main()
