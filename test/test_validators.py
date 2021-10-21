import unittest
from archicad.validators import value_set, matches, min_length, max_length, multiple_of, minimum, maximum, \
    listitem_validator, min_items, max_items, unique_items

class TestStringValidators(unittest.TestCase):
    def test_matches(self):
        pattern = r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-((0[1-9])|([1-2][0-9])|(3[0-1]))$'
        test_matches = matches(pattern)
        self.assertTrue(test_matches('1982-01-01'))
        self.assertFalse(test_matches('22-12-2012'))

    def test_min_length(self):
        test_min_length = min_length(4)
        self.assertFalse(test_min_length("ONE"))
        self.assertFalse(test_min_length("TWO"))
        self.assertTrue(test_min_length("THREE"))
        self.assertTrue(test_min_length("FOUR"))

    def test_max_length(self):
        test_max_length = max_length(4)
        self.assertTrue(test_max_length("ONE"))
        self.assertTrue(test_max_length("TWO"))
        self.assertTrue(test_max_length("FOUR"))
        self.assertFalse(test_max_length("THREE"))

    def test_value_set(self):
        test_value_set = value_set(['ONE', 'THREE', 'FOUR'])
        self.assertTrue(test_value_set('ONE'))
        self.assertTrue(test_value_set('THREE'))
        self.assertTrue(test_value_set('FOUR'))
        self.assertFalse(test_value_set('TWO'))


class TestNumberValidators(unittest.TestCase):
    def test_multiple_of(self):
        test_int_multiple_of = multiple_of(2)
        self.assertTrue(test_int_multiple_of(4))
        self.assertTrue(test_int_multiple_of(2))
        self.assertFalse(test_int_multiple_of(3))
        self.assertFalse(test_int_multiple_of(1))
        self.assertTrue(test_int_multiple_of(0))

        test_float_multiple_of = multiple_of(2.5)
        self.assertTrue(test_float_multiple_of(2.5))
        self.assertTrue(test_float_multiple_of(10))
        self.assertFalse(test_float_multiple_of(10.1))
        self.assertFalse(test_float_multiple_of(9.9))
        self.assertFalse(test_float_multiple_of(2.6))
        self.assertFalse(test_float_multiple_of(2.4))
        self.assertTrue(test_float_multiple_of(0.0))

    def test_minimum(self):
        test_int_minimum = minimum(5, False)
        self.assertTrue(test_int_minimum(5))
        self.assertFalse(test_int_minimum(-5))
        self.assertFalse(test_int_minimum(0))
        self.assertFalse(test_int_minimum(4))
        self.assertTrue(test_int_minimum(6))
        self.assertTrue(test_int_minimum(1000))

        test_int_exclusive_minimum = minimum(5, True)
        self.assertFalse(test_int_exclusive_minimum(5))
        self.assertFalse(test_int_exclusive_minimum(-5))
        self.assertFalse(test_int_exclusive_minimum(0))
        self.assertFalse(test_int_exclusive_minimum(4))
        self.assertTrue(test_int_exclusive_minimum(6))
        self.assertTrue(test_int_exclusive_minimum(1000))
        
        test_float_minimum = minimum(5.5, False)
        self.assertTrue(test_float_minimum(5.5))
        self.assertFalse(test_float_minimum(-5.5))
        self.assertFalse(test_float_minimum(0))
        self.assertFalse(test_float_minimum(4))
        self.assertFalse(test_float_minimum(5.4))
        self.assertFalse(test_float_minimum(4.5))
        self.assertTrue(test_float_minimum(5.6))
        self.assertTrue(test_float_minimum(6.6))
        self.assertTrue(test_float_minimum(6))

        test_exclusive_minimum = minimum(5.5, True)
        self.assertFalse(test_exclusive_minimum(5.5))
        self.assertFalse(test_exclusive_minimum(-5.5))
        self.assertFalse(test_exclusive_minimum(0))
        self.assertFalse(test_exclusive_minimum(4))
        self.assertFalse(test_exclusive_minimum(5.4))
        self.assertFalse(test_exclusive_minimum(5.499999))
        self.assertFalse(test_exclusive_minimum(4.5))
        self.assertTrue(test_exclusive_minimum(5.5000001))
        self.assertTrue(test_exclusive_minimum(5.6))
        self.assertTrue(test_exclusive_minimum(6.6))
        self.assertTrue(test_exclusive_minimum(6))

    def test_maximum(self):
        test_int_maximum = maximum(5, False)
        self.assertTrue(test_int_maximum(5))
        self.assertTrue(test_int_maximum(-5))
        self.assertTrue(test_int_maximum(0))
        self.assertTrue(test_int_maximum(4))
        self.assertFalse(test_int_maximum(6))
        self.assertFalse(test_int_maximum(1000))

        test_int_exclusive_maximum = maximum(5, True)
        self.assertFalse(test_int_exclusive_maximum(5))
        self.assertTrue(test_int_exclusive_maximum(-5))
        self.assertTrue(test_int_exclusive_maximum(0))
        self.assertTrue(test_int_exclusive_maximum(4))
        self.assertFalse(test_int_exclusive_maximum(6))
        self.assertFalse(test_int_exclusive_maximum(1000))
        
        test_float_maximum = maximum(5.5, False)
        self.assertTrue(test_float_maximum(5.5))
        self.assertTrue(test_float_maximum(-5.5))
        self.assertTrue(test_float_maximum(0))
        self.assertTrue(test_float_maximum(4))
        self.assertTrue(test_float_maximum(5.4))
        self.assertTrue(test_float_maximum(4.5))
        self.assertFalse(test_float_maximum(5.6))
        self.assertFalse(test_float_maximum(6.6))
        self.assertFalse(test_float_maximum(6))

        test_exclusive_maximum = maximum(5.5, True)
        self.assertFalse(test_exclusive_maximum(5.5))
        self.assertTrue(test_exclusive_maximum(-5.5))
        self.assertTrue(test_exclusive_maximum(0))
        self.assertTrue(test_exclusive_maximum(4))
        self.assertTrue(test_exclusive_maximum(5.4))
        self.assertTrue(test_exclusive_maximum(5.499999))
        self.assertTrue(test_exclusive_maximum(4.5))
        self.assertFalse(test_exclusive_maximum(5.5000001))
        self.assertFalse(test_exclusive_maximum(5.6))
        self.assertFalse(test_exclusive_maximum(6.6))
        self.assertFalse(test_exclusive_maximum(6))
    
    def test_value_set(self):
        test_value_set = value_set([4, 5.5, .5, 3.])
        self.assertTrue(test_value_set(4))
        self.assertTrue(test_value_set(3))
        self.assertTrue(test_value_set(3.))
        self.assertTrue(test_value_set(4.))
        self.assertTrue(test_value_set(5.5))
        self.assertTrue(test_value_set(.5))
        self.assertTrue(test_value_set(0.5))
        self.assertFalse(test_value_set(5.4))
        self.assertFalse(test_value_set(5.6))
        self.assertFalse(test_value_set(3.01))
        self.assertFalse(test_value_set(2.99))
        self.assertFalse(test_value_set(4.0001))
        self.assertFalse(test_value_set(3.99))
        self.assertFalse(test_value_set(.51))
        self.assertFalse(test_value_set(.49))
        self.assertFalse(test_value_set(6))
        self.assertFalse(test_value_set(1))
        self.assertFalse(test_value_set(0))


class TestListValidators(unittest.TestCase):
    def test_min_items(self):
        test_min_items = min_items(3)
        self.assertTrue(test_min_items([1,2,3,4,5,6]))
        self.assertTrue(test_min_items(["1","2","3"]))
        self.assertTrue(test_min_items([1,2,3]))
        self.assertFalse(test_min_items([1,2]))
        self.assertFalse(test_min_items([1,]))
        self.assertFalse(test_min_items(["123456"]))
        self.assertFalse(test_min_items(["12"]))

    def test_max_items(self):
        test_max_items = max_items(3)
        self.assertFalse(test_max_items([1,2,3,4,5,6]))
        self.assertFalse(test_max_items(["1","2","3","4"]))
        self.assertTrue(test_max_items(["1","2","3"]))
        self.assertTrue(test_max_items([1,2,3]))
        self.assertTrue(test_max_items([1,2]))
        self.assertTrue(test_max_items([123456]))
        self.assertTrue(test_max_items(["123456"]))
        self.assertTrue(test_max_items(["12"]))


    def test_unique_items(self):
        test_unique_items = unique_items()
        self.assertTrue(test_unique_items([]))
        self.assertTrue(test_unique_items([1]))
        self.assertTrue(test_unique_items(["1"]))
        self.assertTrue(test_unique_items([1,2,3,4,5,6]))
        self.assertTrue(test_unique_items(["1","2","3","4","5","6"]))
        self.assertFalse(test_unique_items([1,2,2.,3,4,5,6]))
        self.assertFalse(test_unique_items(["1","212","3","4","212","5","6"]))
        self.assertFalse(test_unique_items([1,1,1,1]))

    def test_listitem_validator(self):
        test_listitem_validator = listitem_validator(multiple_of(2), minimum(4, False), maximum(16, True))
        self.assertTrue(test_listitem_validator([4,6,10]))
        self.assertTrue(test_listitem_validator([4,6,6,10,14]))
        self.assertFalse(test_listitem_validator([2,4,6]))
        self.assertFalse(test_listitem_validator([2,4,16]))
        self.assertFalse(test_listitem_validator([2,3,6,11]))

