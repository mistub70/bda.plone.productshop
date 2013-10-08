import unittest2 as unittest
from bda.plone.productshop.tests import (
    ProductShop_INTEGRATION_TESTING,
    set_browserlayer,
)


class TestProductShop(unittest.TestCase):
    layer = ProductShop_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        set_browserlayer(self.request)

    def test_foo(self):
        self.assertEquals(1, 1)
