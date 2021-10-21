"""Unittests for ACBaseType and inherited classes
"""

import unittest
from enum import Enum
from uuid import UUID
from typing import List, Optional
from archicad.acbasetype import _ACBaseType
from archicad import validators as V


VIEWMAP = 'ViewMap'
PROJECTMAP = 'ProjectMap'
LAYOUTBOOK = 'LayoutBook'
PUBLISHERSET = 'PublisherSets'



EXAMPLE_DICT = {'name': 'First Level',
                'type': LAYOUTBOOK,
                'example': {
                    'name': 'Second Level',
                    'type': LAYOUTBOOK,
                    'example': {
                        'name': 'Third Level',
                        'type': PROJECTMAP,
                        'example': {
                            'name': 'Ékezetek támogatása 😍',
                            'type': 'ProjectMap'
                        }
                    }
                }}

class TestACBaseType(unittest.TestCase):
    def test_base_instantiation(self):
        with self.assertRaises(TypeError):
            _ACBaseType({})

    def test_base_classinfo(self):
        self.assertIsNotNone(_ACBaseType.get_classinfo())
        self.assertEqual(len(_ACBaseType.get_classinfo().fields), 0)


class TestACTypes(unittest.TestCase):
    def setUp(self):
        class Example1(_ACBaseType):
            pass


        class Example2(_ACBaseType):
            __slots__ = ('type', 'name', 'example')

            def __init__(self, type, name, example=None):
                self.type: str = type
                self.name: str = name
                self.example: Optional[Example2] = example

        Example2.get_classinfo().add_field('type', str, V.value_set(['ViewMap', 'ProjectMap', 'LayoutBook', 'PublisherSets']))
        Example2.get_classinfo().add_field('name', str)
        Example2.get_classinfo().add_field('example', Optional[Example2])


        class Example3(_ACBaseType):
            __slots__ = ('name', 'guid', 'numbers', 'strings')

            def __init__(self, name, guid, numbers, strings):
                self.name: str = name
                self.guid: UUID = guid
                self.numbers: List[int] = numbers
                self.strings: List[Optional[List[str]]] = strings

        Example3.get_classinfo().add_field('name', str)
        Example3.get_classinfo().add_field('guid', UUID)
        Example3.get_classinfo().add_field('numbers', List[int], V.min_length(2), V.max_length(6))
        Example3.get_classinfo().add_field('strings', List[Optional[List[str]]])


        class Example4(_ACBaseType):
            __slots__ = ('items')

            def __init__(self, items):
                self.items: List[Example2] = items

        Example4.get_classinfo().add_field('items', List[Example2])
        self.Example1 = Example1
        self.Example2 = Example2
        self.Example3 = Example3
        self.Example4 = Example4
        self.ex1 = Example1()
        self.ex2 = Example2(type=PUBLISHERSET, name="The Publisher Set")
        self.ex3 = Example3('Sample Name', '260D42E3-AA2E-4DAD-BFFA-F2B5021501CC', [5, 6, 7], [])

    def test_inherited_instantiation(self):
        self.assertIsInstance(self.ex1, _ACBaseType)
        self.assertIsInstance(self.ex2, _ACBaseType)
        self.assertIsInstance(self.ex1, self.Example1)
        self.assertIsInstance(self.ex2, self.Example2)
        self.assertNotIsInstance(self.ex1, self.Example2)
        self.assertNotIsInstance(self.ex2, self.Example1)
        self.assertIs(type(self.ex1), self.Example1)
        self.assertIs(type(self.ex2), self.Example2)
        self.assertIsNot(type(self.ex1), _ACBaseType)
        self.assertIsNot(type(self.ex2), _ACBaseType)

    def test_classinfo(self):
        self.assertIsNotNone(self.Example1.get_classinfo())
        self.assertEqual(len(self.Example1.get_classinfo().fields), 0)
        self.assertIsNotNone(self.Example2.get_classinfo())
        self.assertEqual(len(self.Example2.get_classinfo().fields), 3)
        self.assertEqual(len(self.Example2.get_classinfo().value_validators), 1)
        self.assertIsNot(self.ex3.get_classinfo(), self.ex2.get_classinfo())

    def test_fields(self):
        self.assertIs(self.Example2.get_classinfo().fields['type'], str)
        self.assertIs(self.ex2.get_classinfo().fields['name'], str)
        self.assertIs(self.Example2.get_classinfo().fields['example'], Optional[self.Example2])
        self.assertIsNot(self.Example2.get_classinfo().fields['example'], _ACBaseType)

        with self.assertRaises(KeyError):
            self.assertIs(self.Example2.get_classinfo().fields['nothing'], str)
        with self.assertRaises(KeyError):
            self.ex1.new_attribute = 15
        with self.assertRaises(TypeError):
            self.Example2("Sample Name")

    def test_invalid_simple_attributes(self):
        self.assertIsNone(self.ex2.example)
        with self.assertRaises(TypeError):
            self.ex2.name = 5
        with self.assertRaises(TypeError):
            self.ex2.name = {'key': 'value'}
        with self.assertRaises(TypeError):
            self.ex2.type = 5
        with self.assertRaises(ValueError):
            self.ex2.type = 'Invalid'
        with self.assertRaises(ValueError):
            self.ex3.guid = '260D42E3-AA2E-4DAD-BFFA'
        with self.assertRaises(TypeError):
            self.ex3.guid = 25
        with self.assertRaises(TypeError):
            self.ex3.guid = None

    def test_valid_simple_attributes(self):
        self.ex2.name = 'Test Case'
        self.assertEqual(self.ex2.name, 'Test Case')
        self.ex2.type = 'ViewMap'
        self.assertEqual(self.ex2.type, VIEWMAP)
        self.ex3.guid = '260D42E3-AA2E-4DAD-BFFA-F2B5021501CC'
        self.assertEqual(self.ex3.guid, UUID('260D42E3-AA2E-4DAD-BFFA-F2B5021501CC'))


    def test_complex_attributes(self):
        with self.assertRaises(TypeError):
            self.ex2.example = 5
        with self.assertRaises(TypeError):
            self.ex2.example = {'example': True}
        with self.assertRaises(TypeError):
            self.ex2.example = self.Example1()
        with self.assertRaises(AttributeError):
            self.ex2.example.type

        self.ex2.example = {'name': 'Example Name', 'type': LAYOUTBOOK}
        self.assertIsNotNone(self.ex2.example)
        self.assertIsNone(self.ex2.example.example)
        self.assertEqual(self.ex2.example.name, 'Example Name')

        self.ex2.example = self.Example2(name='First', type=PROJECTMAP, example={'name': 'Second', 'type': LAYOUTBOOK})
        self.assertEqual(self.ex2.example.example.name, 'Second')
        self.assertEqual(self.ex2.example.type, PROJECTMAP)
        self.assertEqual(self.ex2.example.example.type, LAYOUTBOOK)

    def test_serialization(self):
        self.ex2.example = EXAMPLE_DICT
        self.assertEqual(self.ex2.example.example.example.name, 'Third Level')
        self.assertEqual(self.ex2.example.example.example.example.name, 'Ékezetek támogatása 😍')
        self.assertEqual(self.ex2.example.example.example.example.type, PROJECTMAP)

        result_dict = self.ex2.to_dict()
        self.assertEqual(len(result_dict), 3)
        self.assertDictEqual(result_dict['example'], EXAMPLE_DICT)
    
    def test_deserialization(self):
        myEx2 = self.Example2(**EXAMPLE_DICT)
        self.assertEqual(myEx2.name, 'First Level')
        self.assertEqual(myEx2.example.example.example.type, PROJECTMAP)
    
    def test_failed_deserialization(self):
        with self.assertRaises(TypeError):
            self.Example2(**{'name': 'Only Name'})
        with self.assertRaises(TypeError):
            self.Example2(**{'type': PROJECTMAP})
        with self.assertRaises(TypeError):
            self.Example2(**{'name': 15, 'type': PROJECTMAP})
        with self.assertRaises(TypeError):
            self.Example2(**{'name': 'Name', 'type': {'a': 1}})
        with self.assertRaises(TypeError):
            self.Example2(**{'name': 'Name', 'type': PROJECTMAP, 'invalid': 15})
        with self.assertRaises(TypeError):
            self.Example2(**{'name': 'Name', 'type': PROJECTMAP, 'example': {'name': 'Name2'}})
        with self.assertRaises(TypeError):
            self.Example2(**{'name': 'Name', 'type': PROJECTMAP, 'example': {'name': 'Name', 'type': 'Invalid'}})
        with self.assertRaises(ValueError):
            self.Example2(**{'name': 'Name', 'type': 'Invalid'})

    def test_nested_lists(self):
        self.ex3 = self.Example3(guid='260D42E3-AA2E-4DAD-BFFA-F2B5021501CC',
                            numbers=[2, 4, 6, 8.4],
                            strings=[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                            name='Name')
        self.assertEqual(len(self.ex3.numbers), 4)
        self.assertEqual(len(self.ex3.strings), 3)
        self.assertListEqual(self.ex3.strings[1], ['d', 'e', 'f'])
        self.assertDictEqual(self.ex3.to_dict(), {'name': 'Name',
                                                  'guid': '260D42E3-AA2E-4DAD-BFFA-F2B5021501CC',
                                                  'numbers': [2, 4, 6, 8],
                                                  'strings': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]})

    def test_list_items(self):
        ex4 = self.Example4([self.ex2])
        self.assertEqual(len(ex4.items), 1)

    def test_number_initialization(self):
        class ExampleNumbers(_ACBaseType):
            __slots__ = ('guid', 'width', 'height', 'amount')

            def __init__(self, guid, width, height, amount):
                self.guid: UUID = guid
                self.width: float = width
                self.height: float = height
                self.amount: int = amount

        ExampleNumbers.get_classinfo().add_field('guid', UUID)
        ExampleNumbers.get_classinfo().add_field('width', float)
        ExampleNumbers.get_classinfo().add_field('height', float)
        ExampleNumbers.get_classinfo().add_field('amount', int, V.minimum(1, False))

        e1 = ExampleNumbers('260D42E3-AA2E-4DAD-BFFA-F2B5021501CC', 1.0, 2.5, 3)
        self.assertIsInstance(e1.width, float)
        self.assertIsInstance(e1.height, float)
        self.assertIsInstance(e1.amount, int)
        
        e2 = ExampleNumbers('260D42E3-AA2E-4DAD-BFFA-F2B5021501CC', 1, 2.5, 3)
        self.assertIsInstance(e2.width, float)
        self.assertIsInstance(e2.height, float)
        self.assertIsInstance(e2.amount, int)
        
        with self.assertRaises(TypeError):
            e3 = ExampleNumbers('260D42E3-AA2E-4DAD-BFFA-F2B5021501CC', 1.0, 2.5, 3.5)