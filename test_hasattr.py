import unittest
from hasattr import new_hasattr


class HasAttrTestCase(unittest.TestCase):
    def test_on_exist_field(self):
        class C(object):
            y = 1
        self.assertTrue(new_hasattr(C(), "y"))

    def test_on_exist_none_field(self):
        class C(object):
            y = None
        self.assertTrue(new_hasattr(C(), "y"))

    def test_on_no_exist_field(self):
        class C(object):
            pass
        self.assertFalse(new_hasattr(C(), "y"))

    def test_on_simple_property(self):
        class C(object):
            @property
            def y(self):
                return 1
        self.assertTrue(new_hasattr(C(), "y"))

    def test_on_property_which_raise_exception_but_not_attribute_error(self):
        class C(object):
            @property
            def y(self):
                return 0 / 0
        self.assertTrue(new_hasattr(C(), "y"))

    def test_on_property_which_raise_attribute_error(self):
        class C(object):
            @property
            def y(self):
                return self.non_existing_field
        self.assertTrue(new_hasattr(C(), "y"))
