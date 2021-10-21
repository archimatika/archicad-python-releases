import unittest
import os
import json
from typing import Dict, Any

from schemaparser import SchemaParser
from converter import SchemaConverter, Class, Command, ClassType, Attribute


class TestConverterForClasses(unittest.TestCase):
    def test_class_with_primitives(self):
        REQUIRED_FILES = ['APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        PUBLISHERSETID_CLASS: Class = converter.classes[converter.classes.index('PublisherSetId')]
        self.assertEqual(PUBLISHERSETID_CLASS.name, 'PublisherSetId')
        self.assertEqual(PUBLISHERSETID_CLASS.description, 'The identifier of a publisher set.')
        self.assertEqual(PUBLISHERSETID_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(PUBLISHERSETID_CLASS.title)
        self.assertIsNone(PUBLISHERSETID_CLASS.default)
        self.assertEqual(PUBLISHERSETID_CLASS.additional_properties, False)
        self.assertTrue(PUBLISHERSETID_CLASS.attributes)

        FIRST_ATTRIBUTE = PUBLISHERSETID_CLASS.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE.name, 'name')
        self.assertEqual(FIRST_ATTRIBUTE.description, 'The name of the publisher set.')
        self.assertEqual(FIRST_ATTRIBUTE.type, 'str')
        self.assertEqual(FIRST_ATTRIBUTE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE.min_length)
        self.assertIsNone(FIRST_ATTRIBUTE.max_length)
        self.assertIsNone(FIRST_ATTRIBUTE.pattern)
        self.assertIsNone(FIRST_ATTRIBUTE.values)
        
        SECOND_ATTRIBUTE = PUBLISHERSETID_CLASS.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE.description, 'The type of the navigator item tree.')
        self.assertEqual(SECOND_ATTRIBUTE.type, 'str')
        self.assertEqual(SECOND_ATTRIBUTE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE.min_length)
        self.assertIsNone(SECOND_ATTRIBUTE.max_length)
        self.assertIsNone(SECOND_ATTRIBUTE.pattern)
        self.assertTrue(SECOND_ATTRIBUTE.values)
        self.assertEqual(len(SECOND_ATTRIBUTE.values), 1)
        self.assertIn('PublisherSets', SECOND_ATTRIBUTE.values)


    def test_class_with_array(self):
        REQUIRED_FILES = ['APITypes.json', 'APIPropertyTypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        USERDEFINEDPROPERTYUSERID_CLASS: Class = converter.classes[converter.classes.index('UserDefinedPropertyUserId')]
        self.assertEqual(USERDEFINEDPROPERTYUSERID_CLASS.name, 'UserDefinedPropertyUserId')
        self.assertEqual(USERDEFINEDPROPERTYUSERID_CLASS.description, 'The unique identifier of a User-Defined Property, identified by its name.')
        self.assertEqual(USERDEFINEDPROPERTYUSERID_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(USERDEFINEDPROPERTYUSERID_CLASS.title)
        self.assertIsNone(USERDEFINEDPROPERTYUSERID_CLASS.default)
        self.assertEqual(USERDEFINEDPROPERTYUSERID_CLASS.additional_properties, False)
        self.assertTrue(USERDEFINEDPROPERTYUSERID_CLASS.attributes)

        FIRST_ATTRIBUTE = USERDEFINEDPROPERTYUSERID_CLASS.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE.name, 'localizedName')
        self.assertEqual(FIRST_ATTRIBUTE.description, 'A two-element list of the localized name parts. The first element is the name of the group the property belongs to, and the second element is the actual name of the property.')
        self.assertEqual(FIRST_ATTRIBUTE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE.required, True)
        self.assertEqual(FIRST_ATTRIBUTE.min_items, 2)
        self.assertEqual(FIRST_ATTRIBUTE.max_items, 2)
        self.assertIsNone(FIRST_ATTRIBUTE.unique_items)
        self.assertEqual(FIRST_ATTRIBUTE.itemtype.name, 'ListItem')
        self.assertEqual(FIRST_ATTRIBUTE.itemtype.type, 'str')
        self.assertIsNone(FIRST_ATTRIBUTE.itemtype.description)
        self.assertEqual(FIRST_ATTRIBUTE.itemtype.required, False)
        self.assertIsNone(FIRST_ATTRIBUTE.itemtype.min_length)
        self.assertIsNone(FIRST_ATTRIBUTE.itemtype.max_length)
        self.assertIsNone(FIRST_ATTRIBUTE.itemtype.pattern)
        self.assertIsNone(FIRST_ATTRIBUTE.itemtype.values)

        SECOND_ATTRIBUTE = USERDEFINEDPROPERTYUSERID_CLASS.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE.name, 'type')
        self.assertIsNone(SECOND_ATTRIBUTE.description)
        self.assertEqual(SECOND_ATTRIBUTE.type, 'str')
        self.assertEqual(SECOND_ATTRIBUTE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE.min_length)
        self.assertIsNone(SECOND_ATTRIBUTE.max_length)
        self.assertIsNone(SECOND_ATTRIBUTE.pattern)
        self.assertTrue(SECOND_ATTRIBUTE.values)
        self.assertEqual(len(SECOND_ATTRIBUTE.values), 1)
        self.assertIn('UserDefined', SECOND_ATTRIBUTE.values)


    def test_class_with_object(self):
        REQUIRED_FILES = ['APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        ELEMENTIDARRAYITEM_CLASS = converter.classes[converter.classes.index('ElementIdArrayItem')]
        self.assertEqual(ELEMENTIDARRAYITEM_CLASS.name, 'ElementIdArrayItem')
        self.assertFalse(ELEMENTIDARRAYITEM_CLASS.description)
        self.assertEqual(ELEMENTIDARRAYITEM_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(ELEMENTIDARRAYITEM_CLASS.title)
        self.assertIsNone(ELEMENTIDARRAYITEM_CLASS.default)
        self.assertEqual(ELEMENTIDARRAYITEM_CLASS.additional_properties, False)
        ELEMENTID_CLASS = converter.classes[converter.classes.index(ELEMENTIDARRAYITEM_CLASS.attributes[0].type)]
        self.assertEqual(ELEMENTID_CLASS.name, 'ElementId')
        self.assertEqual(ELEMENTID_CLASS.description, 'The identifier of an element.')
        self.assertEqual(ELEMENTID_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(ELEMENTID_CLASS.title)
        self.assertIsNone(ELEMENTID_CLASS.default)
        self.assertEqual(ELEMENTID_CLASS.additional_properties, False)
        self.assertEqual(ELEMENTID_CLASS.attributes[0].name, 'guid')
        self.assertEqual(ELEMENTID_CLASS.attributes[0].type, 'UUID')
        self.assertEqual(ELEMENTID_CLASS.attributes[0].description, 'A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.')
        self.assertEqual(ELEMENTID_CLASS.attributes[0].pattern, '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')

    def test_class_with_or_error(self):
        REQUIRED_FILES = ['APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        BOUNDINGBOX2DORERROR_CLASS = converter.classes[converter.classes.index('BoundingBox2DOrError')]
        self.assertEqual(BOUNDINGBOX2DORERROR_CLASS.name, 'BoundingBox2DOrError')
        self.assertEqual(BOUNDINGBOX2DORERROR_CLASS.description, 'A 2D bounding box or an error.')
        self.assertEqual(BOUNDINGBOX2DORERROR_CLASS.class_type, ClassType.ONEOF)
        self.assertIsNone(BOUNDINGBOX2DORERROR_CLASS.title)
        self.assertIsNone(BOUNDINGBOX2DORERROR_CLASS.default)
        self.assertIsNone(BOUNDINGBOX2DORERROR_CLASS.additional_properties)

        FIRST_TYPE: Class = converter.classes[converter.classes.index(BOUNDINGBOX2DORERROR_CLASS.of_type_class_names[0])]
        self.assertEqual(FIRST_TYPE.name, 'BoundingBox2DWrapper')
        self.assertFalse(FIRST_TYPE.description)
        self.assertEqual(FIRST_TYPE.class_type, ClassType.NORMAL)
        self.assertEqual(FIRST_TYPE.title, 'boundingBox2D')
        self.assertIsNone(FIRST_TYPE.default)
        self.assertEqual(FIRST_TYPE.additional_properties, False)
        self.assertTrue(FIRST_TYPE.attributes)
        self.assertTrue(len(FIRST_TYPE.attributes) == 1)
        self.assertEqual(FIRST_TYPE.attributes[0].name, 'boundingBox2D')
        FIRST_ATTRIBUTE: Attribute = BOUNDINGBOX2DORERROR_CLASS.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE.name, 'boundingBox2D')
        self.assertEqual(FIRST_ATTRIBUTE.type, 'BoundingBox2D')
        self.assertEqual(FIRST_ATTRIBUTE.description, 'The 2D bounding box of an element.')
        self.assertFalse(FIRST_ATTRIBUTE.required)
        self.assertIsNone(FIRST_ATTRIBUTE.title)
        self.assertIsNone(FIRST_ATTRIBUTE.default)

        SECOND_TYPE: Class = converter.classes[converter.classes.index(BOUNDINGBOX2DORERROR_CLASS.of_type_class_names[1])]
        self.assertEqual(SECOND_TYPE.name, 'ErrorItem')
        self.assertFalse(SECOND_TYPE.description)
        self.assertEqual(SECOND_TYPE.class_type, ClassType.NORMAL)
        self.assertIsNone(SECOND_TYPE.title)
        self.assertIsNone(SECOND_TYPE.default)
        self.assertEqual(SECOND_TYPE.additional_properties, False)
        self.assertTrue(SECOND_TYPE.attributes)
        self.assertTrue(len(SECOND_TYPE.attributes) == 1)
        self.assertEqual(SECOND_TYPE.attributes[0].name, 'error')
        SECOND_ATTRIBUTE: Attribute = BOUNDINGBOX2DORERROR_CLASS.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE.name, 'error')
        self.assertEqual(SECOND_ATTRIBUTE.type, 'Error')
        self.assertEqual(SECOND_ATTRIBUTE.description, 'The details of an error.')
        self.assertFalse(SECOND_ATTRIBUTE.required)
        self.assertIsNone(SECOND_ATTRIBUTE.title)
        self.assertIsNone(SECOND_ATTRIBUTE.default)

    def test_class_with_one_of(self):
        REQUIRED_FILES = ['APITypes.json', 'APIPropertyTypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)
        PROPERTY_VALUE = converter.classes[converter.classes.index('PropertyValue')]
        self.assertEqual(PROPERTY_VALUE.name, 'PropertyValue')
        self.assertEqual(PROPERTY_VALUE.description, 'A normal, userUndefined, notAvailable or notEvaluated property value.')
        self.assertEqual(PROPERTY_VALUE.class_type, ClassType.ONEOF)
        self.assertIsNone(PROPERTY_VALUE.title)
        self.assertIsNone(PROPERTY_VALUE.default)
        self.assertIsNone(PROPERTY_VALUE.additional_properties)
        self.assertEqual(len(PROPERTY_VALUE.of_type_class_names), 3)
        self.assertEqual(PROPERTY_VALUE.of_type_class_names[0], 'NormalOrUserUndefinedPropertyValue')
        self.assertEqual(PROPERTY_VALUE.of_type_class_names[1], 'NotAvailablePropertyValue')
        self.assertEqual(PROPERTY_VALUE.of_type_class_names[2], 'NotEvaluatedPropertyValue')
        self.assertTrue(PROPERTY_VALUE.attributes)
        self.assertTrue(len(PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_PROPERTY_VALUE: Attribute = PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_PROPERTY_VALUE.name, 'type')
        self.assertEqual(FIRST_ATTRIBUTE_OF_PROPERTY_VALUE.type, 'str')
        self.assertEqual(FIRST_ATTRIBUTE_OF_PROPERTY_VALUE.description, 'None')
        self.assertEqual(FIRST_ATTRIBUTE_OF_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_PROPERTY_VALUE: Attribute = PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_PROPERTY_VALUE.name, 'status')
        self.assertEqual(SECOND_ATTRIBUTE_OF_PROPERTY_VALUE.type, 'str')
        self.assertEqual(SECOND_ATTRIBUTE_OF_PROPERTY_VALUE.description, 'None')
        self.assertEqual(SECOND_ATTRIBUTE_OF_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_PROPERTY_VALUE.default)
        THIRD_ATTRIBUTE_OF_PROPERTY_VALUE: Attribute = PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_PROPERTY_VALUE.name, 'value')
        self.assertEqual(THIRD_ATTRIBUTE_OF_PROPERTY_VALUE.type, 'float;int;str;bool;List[float];List[int];List[str];List[bool];EnumValueId;List[EnumValueIdWrapper]')
        self.assertEqual(THIRD_ATTRIBUTE_OF_PROPERTY_VALUE.description, 'None; The identifier of a property enumeration value.; A list of enumeration identifiers.')
        self.assertEqual(THIRD_ATTRIBUTE_OF_PROPERTY_VALUE.required, False)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_PROPERTY_VALUE.default)

        FIRST_TYPE: Class = converter.classes[converter.classes.index(PROPERTY_VALUE.of_type_class_names[0])]
        self.assertEqual(FIRST_TYPE.name, 'NormalOrUserUndefinedPropertyValue')
        self.assertEqual(FIRST_TYPE.description, 'A normal or a userUndefined property value.')
        self.assertEqual(FIRST_TYPE.class_type, ClassType.ONEOF)
        self.assertIsNone(FIRST_TYPE.title)
        self.assertIsNone(FIRST_TYPE.default)
        self.assertIsNone(FIRST_TYPE.additional_properties)
        self.assertEqual(len(FIRST_TYPE.of_type_class_names), 19)
        self.assertEqual(FIRST_TYPE.of_type_class_names[0], 'NormalNumberPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[1], 'NormalIntegerPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[2], 'NormalStringPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[3], 'NormalBooleanPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[4], 'NormalLengthPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[5], 'NormalAreaPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[6], 'NormalVolumePropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[7], 'NormalAnglePropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[8], 'NormalNumberListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[9], 'NormalIntegerListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[10], 'NormalStringListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[11], 'NormalBooleanListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[12], 'NormalLengthListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[13], 'NormalAreaListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[14], 'NormalVolumeListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[15], 'NormalAngleListPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[16], 'NormalSingleEnumPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[17], 'NormalMultiEnumPropertyValue')
        self.assertEqual(FIRST_TYPE.of_type_class_names[18], 'UserUndefinedPropertyValue')
        self.assertTrue(FIRST_TYPE.attributes)
        self.assertTrue(len(FIRST_TYPE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_FIRST_TYPE: Attribute = FIRST_TYPE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_FIRST_TYPE.name, 'type')
        self.assertEqual(FIRST_ATTRIBUTE_OF_FIRST_TYPE.type, 'str')
        self.assertEqual(FIRST_ATTRIBUTE_OF_FIRST_TYPE.description, 'None')
        self.assertEqual(FIRST_ATTRIBUTE_OF_FIRST_TYPE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_FIRST_TYPE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_FIRST_TYPE.default)
        SECOND_ATTRIBUTE_OF_FIRST_TYPE: Attribute = FIRST_TYPE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_FIRST_TYPE.name, 'status')
        self.assertEqual(SECOND_ATTRIBUTE_OF_FIRST_TYPE.type, 'str')
        self.assertEqual(SECOND_ATTRIBUTE_OF_FIRST_TYPE.description, 'None')
        self.assertEqual(SECOND_ATTRIBUTE_OF_FIRST_TYPE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_FIRST_TYPE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_FIRST_TYPE.default)
        THIRD_ATTRIBUTE_OF_FIRST_TYPE: Attribute = FIRST_TYPE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_FIRST_TYPE.name, 'value')
        self.assertEqual(THIRD_ATTRIBUTE_OF_FIRST_TYPE.type, 'float;int;str;bool;List[float];List[int];List[str];List[bool];EnumValueId;List[EnumValueIdWrapper]')
        self.assertEqual(THIRD_ATTRIBUTE_OF_FIRST_TYPE.description, 'None; The identifier of a property enumeration value.; A list of enumeration identifiers.')
        self.assertEqual(THIRD_ATTRIBUTE_OF_FIRST_TYPE.required, False)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_FIRST_TYPE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_FIRST_TYPE.default)
        
        NORMAL_NUMBER_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[0])]
        self.assertEqual(NORMAL_NUMBER_PROPERTY_VALUE.name, 'NormalNumberPropertyValue')
        self.assertEqual(NORMAL_NUMBER_PROPERTY_VALUE.description, 'A number property value containing a valid numeric value.')
        self.assertEqual(NORMAL_NUMBER_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_NUMBER_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_NUMBER_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_NUMBER_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_NUMBER_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_NUMBER_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_NUMBER_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE: Attribute = NORMAL_NUMBER_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.type, 'float')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE: Attribute = NORMAL_NUMBER_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.values, ['number'])
        THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE: Attribute = NORMAL_NUMBER_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_INTEGER_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[1])]
        self.assertEqual(NORMAL_INTEGER_PROPERTY_VALUE.name, 'NormalIntegerPropertyValue')
        self.assertEqual(NORMAL_INTEGER_PROPERTY_VALUE.description, 'An integer property value containing a valid integer number.')
        self.assertEqual(NORMAL_INTEGER_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_INTEGER_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_INTEGER_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_INTEGER_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_INTEGER_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_INTEGER_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_INTEGER_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE: Attribute = NORMAL_INTEGER_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.type, 'int')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE: Attribute = NORMAL_INTEGER_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.values, ['integer'])
        THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE: Attribute = NORMAL_INTEGER_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_STRING_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[2])]
        self.assertEqual(NORMAL_STRING_PROPERTY_VALUE.name, 'NormalStringPropertyValue')
        self.assertEqual(NORMAL_STRING_PROPERTY_VALUE.description, 'A string property value containing a valid string.')
        self.assertEqual(NORMAL_STRING_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_STRING_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_STRING_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_STRING_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_STRING_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_STRING_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_STRING_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE: Attribute = NORMAL_STRING_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE: Attribute = NORMAL_STRING_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.values, ['string'])
        THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE: Attribute = NORMAL_STRING_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_BOOLEAN_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[3])]
        self.assertEqual(NORMAL_BOOLEAN_PROPERTY_VALUE.name, 'NormalBooleanPropertyValue')
        self.assertEqual(NORMAL_BOOLEAN_PROPERTY_VALUE.description, 'A boolean property value containing a valid boolean value.')
        self.assertEqual(NORMAL_BOOLEAN_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_BOOLEAN_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_BOOLEAN_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_BOOLEAN_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_BOOLEAN_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_BOOLEAN_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_BOOLEAN_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE: Attribute = NORMAL_BOOLEAN_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.type, 'bool')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE: Attribute = NORMAL_BOOLEAN_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.values, ['boolean'])
        THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE: Attribute = NORMAL_BOOLEAN_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_LENGTH_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[4])]
        self.assertEqual(NORMAL_LENGTH_PROPERTY_VALUE.name, 'NormalLengthPropertyValue')
        self.assertEqual(NORMAL_LENGTH_PROPERTY_VALUE.description, 'A length property value containing a real length value. The value is measured in SI (meters).')
        self.assertEqual(NORMAL_LENGTH_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_LENGTH_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_LENGTH_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_LENGTH_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_LENGTH_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_LENGTH_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_LENGTH_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE: Attribute = NORMAL_LENGTH_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.type, 'float')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE: Attribute = NORMAL_LENGTH_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.values, ['length'])
        THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE: Attribute = NORMAL_LENGTH_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_AREA_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[5])]
        self.assertEqual(NORMAL_AREA_PROPERTY_VALUE.name, 'NormalAreaPropertyValue')
        self.assertEqual(NORMAL_AREA_PROPERTY_VALUE.description, 'An area property value containing a real area. The value is measured in SI (square meters).')
        self.assertEqual(NORMAL_AREA_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_AREA_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_AREA_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_AREA_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_AREA_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_AREA_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_AREA_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE: Attribute = NORMAL_AREA_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.type, 'float')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE: Attribute = NORMAL_AREA_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.values, ['area'])
        THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE: Attribute = NORMAL_AREA_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_VOLUME_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[6])]
        self.assertEqual(NORMAL_VOLUME_PROPERTY_VALUE.name, 'NormalVolumePropertyValue')
        self.assertEqual(NORMAL_VOLUME_PROPERTY_VALUE.description, 'A volume property value containing a real volume. The value is measured in SI (cubic meters).')
        self.assertEqual(NORMAL_VOLUME_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_VOLUME_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_VOLUME_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_VOLUME_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_VOLUME_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_VOLUME_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_VOLUME_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE: Attribute = NORMAL_VOLUME_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.type, 'float')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE: Attribute = NORMAL_VOLUME_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.values, ['volume'])
        THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE: Attribute = NORMAL_VOLUME_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_ANGLE_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[7])]
        self.assertEqual(NORMAL_ANGLE_PROPERTY_VALUE.name, 'NormalAnglePropertyValue')
        self.assertEqual(NORMAL_ANGLE_PROPERTY_VALUE.description, 'An angle property value containing a real angle. The value is measured in SI (radians).')
        self.assertEqual(NORMAL_ANGLE_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_ANGLE_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_ANGLE_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_ANGLE_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_ANGLE_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_ANGLE_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_ANGLE_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE: Attribute = NORMAL_ANGLE_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.type, 'float')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE: Attribute = NORMAL_ANGLE_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.values, ['angle'])
        THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE: Attribute = NORMAL_ANGLE_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_NUMBER_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[8])]
        self.assertEqual(NORMAL_NUMBER_LIST_PROPERTY_VALUE.name, 'NormalNumberListPropertyValue')
        self.assertEqual(NORMAL_NUMBER_LIST_PROPERTY_VALUE.description, 'A number list property value containing numbers in an array.')
        self.assertEqual(NORMAL_NUMBER_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_NUMBER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_NUMBER_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_NUMBER_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_NUMBER_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_NUMBER_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_NUMBER_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE: Attribute = NORMAL_NUMBER_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.itemtype.type, 'float')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE: Attribute = NORMAL_NUMBER_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.values, ['numberList'])
        THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE: Attribute = NORMAL_NUMBER_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_NUMBER_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_INTEGER_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[9])]
        self.assertEqual(NORMAL_INTEGER_LIST_PROPERTY_VALUE.name, 'NormalIntegerListPropertyValue')
        self.assertEqual(NORMAL_INTEGER_LIST_PROPERTY_VALUE.description, 'An integer list property value containing integers in an array.')
        self.assertEqual(NORMAL_INTEGER_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_INTEGER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_INTEGER_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_INTEGER_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_INTEGER_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_INTEGER_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_INTEGER_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE: Attribute = NORMAL_INTEGER_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.itemtype.type, 'int')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE: Attribute = NORMAL_INTEGER_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.values, ['integerList'])
        THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE: Attribute = NORMAL_INTEGER_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_INTEGER_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_STRING_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[10])]
        self.assertEqual(NORMAL_STRING_LIST_PROPERTY_VALUE.name, 'NormalStringListPropertyValue')
        self.assertEqual(NORMAL_STRING_LIST_PROPERTY_VALUE.description, 'A string list property value containing strings in an array.')
        self.assertEqual(NORMAL_STRING_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_STRING_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_STRING_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_STRING_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_STRING_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_STRING_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_STRING_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE: Attribute = NORMAL_STRING_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.itemtype.type, 'str')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE: Attribute = NORMAL_STRING_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.values, ['stringList'])
        THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE: Attribute = NORMAL_STRING_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_STRING_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_BOOLEAN_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[11])]
        self.assertEqual(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.name, 'NormalBooleanListPropertyValue')
        self.assertEqual(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.description, 'A boolean list property value containing boolean values in an array.')
        self.assertEqual(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE: Attribute = NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.itemtype.type, 'bool')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE: Attribute = NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.values, ['booleanList'])
        THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE: Attribute = NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_BOOLEAN_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_LENGTH_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[12])]
        self.assertEqual(NORMAL_LENGTH_LIST_PROPERTY_VALUE.name, 'NormalLengthListPropertyValue')
        self.assertEqual(NORMAL_LENGTH_LIST_PROPERTY_VALUE.description, 'A length list property value containing length values in an array. The values are measured in SI (meters).')
        self.assertEqual(NORMAL_LENGTH_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_LENGTH_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_LENGTH_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_LENGTH_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_LENGTH_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_LENGTH_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_LENGTH_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE: Attribute = NORMAL_LENGTH_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.itemtype.type, 'float')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE: Attribute = NORMAL_LENGTH_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.values, ['lengthList'])
        THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE: Attribute = NORMAL_LENGTH_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_LENGTH_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_AREA_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[13])]
        self.assertEqual(NORMAL_AREA_LIST_PROPERTY_VALUE.name, 'NormalAreaListPropertyValue')
        self.assertEqual(NORMAL_AREA_LIST_PROPERTY_VALUE.description, 'An area list property value containing areas in an array. The values are measured in SI (square meters).')
        self.assertEqual(NORMAL_AREA_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_AREA_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_AREA_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_AREA_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_AREA_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_AREA_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_AREA_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE: Attribute = NORMAL_AREA_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.itemtype.type, 'float')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE: Attribute = NORMAL_AREA_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.values, ['areaList'])
        THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE: Attribute = NORMAL_AREA_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_AREA_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_VOLUME_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[14])]
        self.assertEqual(NORMAL_VOLUME_LIST_PROPERTY_VALUE.name, 'NormalVolumeListPropertyValue')
        self.assertEqual(NORMAL_VOLUME_LIST_PROPERTY_VALUE.description, 'A volume list property value containing volumes in an array. The values are measured in SI (cubic meters).')
        self.assertEqual(NORMAL_VOLUME_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_VOLUME_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_VOLUME_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_VOLUME_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_VOLUME_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_VOLUME_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_VOLUME_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE: Attribute = NORMAL_VOLUME_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.itemtype.type, 'float')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE: Attribute = NORMAL_VOLUME_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.values, ['volumeList'])
        THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE: Attribute = NORMAL_VOLUME_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_VOLUME_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_ANGLE_LIST_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[15])]
        self.assertEqual(NORMAL_ANGLE_LIST_PROPERTY_VALUE.name, 'NormalAngleListPropertyValue')
        self.assertEqual(NORMAL_ANGLE_LIST_PROPERTY_VALUE.description, 'An angle list property value containing angles in an array. The values are measured in SI (radians).')
        self.assertEqual(NORMAL_ANGLE_LIST_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_ANGLE_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_ANGLE_LIST_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_ANGLE_LIST_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_ANGLE_LIST_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_ANGLE_LIST_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_ANGLE_LIST_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE: Attribute = NORMAL_ANGLE_LIST_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.itemtype.type, 'float')
        self.assertFalse(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE: Attribute = NORMAL_ANGLE_LIST_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.values, ['angleList'])
        THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE: Attribute = NORMAL_ANGLE_LIST_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_ANGLE_LIST_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_SINGLE_ENUM_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[16])]
        self.assertEqual(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.name, 'NormalSingleEnumPropertyValue')
        self.assertEqual(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.description, 'A single enumeration property value containing the ID of the selected enum value.')
        self.assertEqual(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_SINGLE_ENUM_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE: Attribute = NORMAL_SINGLE_ENUM_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.type, 'EnumValueId')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.description, 'The identifier of a property enumeration value.')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE: Attribute = NORMAL_SINGLE_ENUM_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.values, ['singleEnum'])
        THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE: Attribute = NORMAL_SINGLE_ENUM_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_SINGLE_ENUM_PROPERTY_VALUE.values, ['normal'])
        
        NORMAL_MULTI_ENUM_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[17])]
        self.assertEqual(NORMAL_MULTI_ENUM_PROPERTY_VALUE.name, 'NormalMultiEnumPropertyValue')
        self.assertEqual(NORMAL_MULTI_ENUM_PROPERTY_VALUE.description, 'A multiple choice enumeration property value containing the IDs of the selected enum values in an array.')
        self.assertEqual(NORMAL_MULTI_ENUM_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(NORMAL_MULTI_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(NORMAL_MULTI_ENUM_PROPERTY_VALUE.default)
        self.assertEqual(NORMAL_MULTI_ENUM_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(NORMAL_MULTI_ENUM_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(NORMAL_MULTI_ENUM_PROPERTY_VALUE.attributes)
        self.assertTrue(len(NORMAL_MULTI_ENUM_PROPERTY_VALUE.attributes) == 3)
        FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE: Attribute = NORMAL_MULTI_ENUM_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.name, 'value')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.type, 'List')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.itemtype, 'EnumValueIdWrapper')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.description, 'A list of enumeration identifiers.')
        self.assertEqual(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.default)
        SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE: Attribute = NORMAL_MULTI_ENUM_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.name, 'type')
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.values, ['multiEnum'])
        THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE: Attribute = NORMAL_MULTI_ENUM_PROPERTY_VALUE.attributes[2]
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.name, 'status')
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.description)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.required, True)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.title)
        self.assertIsNone(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.default)
        self.assertEqual(THIRD_ATTRIBUTE_OF_NORMAL_MULTI_ENUM_PROPERTY_VALUE.values, ['normal'])
        
        USER_UNDEFINED_PROPERTY_VALUE: Class = converter.classes[converter.classes.index(FIRST_TYPE.of_type_class_names[18])]
        self.assertEqual(USER_UNDEFINED_PROPERTY_VALUE.name, 'UserUndefinedPropertyValue')
        self.assertEqual(USER_UNDEFINED_PROPERTY_VALUE.description, 'A userUndefined value means that there is no actual number/string/etc. value, but the user deliberately set an Undefined value: this is a valid value, too.')
        self.assertEqual(USER_UNDEFINED_PROPERTY_VALUE.class_type, ClassType.NORMAL)
        self.assertIsNone(USER_UNDEFINED_PROPERTY_VALUE.title)
        self.assertIsNone(USER_UNDEFINED_PROPERTY_VALUE.default)
        self.assertEqual(USER_UNDEFINED_PROPERTY_VALUE.additional_properties, False)
        self.assertFalse(USER_UNDEFINED_PROPERTY_VALUE.of_type_class_names)
        self.assertTrue(USER_UNDEFINED_PROPERTY_VALUE.attributes)
        self.assertTrue(len(USER_UNDEFINED_PROPERTY_VALUE.attributes) == 2)
        FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE: Attribute = USER_UNDEFINED_PROPERTY_VALUE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.name, 'type')
        self.assertEqual(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.default)
        self.assertEqual(FIRST_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.values, ['number', 'integer', 'string', 'boolean', 'length', 'area', 'volume', 'angle', 'numberList', 'integerList', 'stringList', 'booleanList', 'lengthList', 'areaList', 'volumeList', 'angleList', 'singleEnum', 'multiEnum'])
        SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE: Attribute = USER_UNDEFINED_PROPERTY_VALUE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.name, 'status')
        self.assertEqual(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_USER_UNDEFINED_PROPERTY_VALUE.values, ['userUndefined'])

        SECOND_TYPE: Class = converter.classes[converter.classes.index(PROPERTY_VALUE.of_type_class_names[1])]
        self.assertEqual(SECOND_TYPE.name, 'NotAvailablePropertyValue')
        self.assertEqual(SECOND_TYPE.description, 'A notAvailable value means that the property is not available for the property owner (and therefore it has no property value for it).')
        self.assertEqual(SECOND_TYPE.class_type, ClassType.NORMAL)
        self.assertIsNone(SECOND_TYPE.title)
        self.assertIsNone(SECOND_TYPE.default)
        self.assertEqual(SECOND_TYPE.additional_properties, False)
        self.assertFalse(SECOND_TYPE.of_type_class_names)
        self.assertTrue(SECOND_TYPE.attributes)
        self.assertTrue(len(SECOND_TYPE.attributes) == 2)
        FIRST_ATTRIBUTE_OF_SECOND_TYPE: Attribute = SECOND_TYPE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_SECOND_TYPE.name, 'type')
        self.assertEqual(FIRST_ATTRIBUTE_OF_SECOND_TYPE.type, 'str')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_SECOND_TYPE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_SECOND_TYPE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_SECOND_TYPE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_SECOND_TYPE.default)
        self.assertEqual(FIRST_ATTRIBUTE_OF_SECOND_TYPE.values, ['number', 'integer', 'string', 'boolean', 'length', 'area', 'volume', 'angle', 'numberList', 'integerList', 'stringList', 'booleanList', 'lengthList', 'areaList', 'volumeList', 'angleList', 'singleEnum', 'multiEnum'])
        SECOND_ATTRIBUTE_OF_SECOND_TYPE: Attribute = SECOND_TYPE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_SECOND_TYPE.name, 'status')
        self.assertEqual(SECOND_ATTRIBUTE_OF_SECOND_TYPE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_SECOND_TYPE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_SECOND_TYPE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_SECOND_TYPE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_SECOND_TYPE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_SECOND_TYPE.values, ['notAvailable'])

        THIRD_TYPE: Class = converter.classes[converter.classes.index(PROPERTY_VALUE.of_type_class_names[2])]
        self.assertEqual(THIRD_TYPE.name, 'NotEvaluatedPropertyValue')
        self.assertEqual(THIRD_TYPE.description, 'A notEvaluated value means that the property could not be evaluated for the property owner for some reason.')
        self.assertEqual(THIRD_TYPE.class_type, ClassType.NORMAL)
        self.assertIsNone(THIRD_TYPE.title)
        self.assertIsNone(THIRD_TYPE.default)
        self.assertEqual(THIRD_TYPE.additional_properties, False)
        self.assertFalse(THIRD_TYPE.of_type_class_names)
        self.assertTrue(THIRD_TYPE.attributes)
        self.assertTrue(len(THIRD_TYPE.attributes) == 2)
        FIRST_ATTRIBUTE_OF_THIRD_TYPE: Attribute = THIRD_TYPE.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE_OF_THIRD_TYPE.name, 'type')
        self.assertEqual(FIRST_ATTRIBUTE_OF_THIRD_TYPE.type, 'str')
        self.assertIsNone(FIRST_ATTRIBUTE_OF_THIRD_TYPE.description)
        self.assertEqual(FIRST_ATTRIBUTE_OF_THIRD_TYPE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_THIRD_TYPE.title)
        self.assertIsNone(FIRST_ATTRIBUTE_OF_THIRD_TYPE.default)
        self.assertEqual(FIRST_ATTRIBUTE_OF_THIRD_TYPE.values, ['number', 'integer', 'string', 'boolean', 'length', 'area', 'volume', 'angle', 'numberList', 'integerList', 'stringList', 'booleanList', 'lengthList', 'areaList', 'volumeList', 'angleList', 'singleEnum', 'multiEnum'])
        SECOND_ATTRIBUTE_OF_THIRD_TYPE: Attribute = THIRD_TYPE.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE_OF_THIRD_TYPE.name, 'status')
        self.assertEqual(SECOND_ATTRIBUTE_OF_THIRD_TYPE.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE_OF_THIRD_TYPE.description)
        self.assertEqual(SECOND_ATTRIBUTE_OF_THIRD_TYPE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_THIRD_TYPE.title)
        self.assertIsNone(SECOND_ATTRIBUTE_OF_THIRD_TYPE.default)
        self.assertEqual(SECOND_ATTRIBUTE_OF_THIRD_TYPE.values, ['notEvaluated'])

        
class TestConverterForCommands(unittest.TestCase):
    def test_getter_command(self):
        REQUIRED_FILES = ['API.GetProductInfo.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertFalse(converter.classes)
        self.assertTrue(converter.commands)

        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'GetProductInfo')
        self.assertEqual(COMMAND.description, 'Accesses the version information from the running ARCHICAD.')
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)

        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'GetProductInfo_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertEqual(COMMAND_PARAMETERS.additional_properties, False)
        self.assertFalse(COMMAND_PARAMETERS.attributes)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'GetProductInfo_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)

        FIRST_RESPONSE_PARAMETER: Attribute = RESPONSE_PARAMETERS.attributes[0]
        self.assertEqual(FIRST_RESPONSE_PARAMETER.name, 'version')
        self.assertEqual(FIRST_RESPONSE_PARAMETER.description, 'The version of the running ARCHICAD.')
        self.assertEqual(FIRST_RESPONSE_PARAMETER.type, 'int')
        self.assertEqual(FIRST_RESPONSE_PARAMETER.required, True)

        SECOND_RESPONSE_PARAMETER: Attribute = RESPONSE_PARAMETERS.attributes[1]
        self.assertEqual(SECOND_RESPONSE_PARAMETER.name, 'buildNumber')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.description, 'The build number of the running ARCHICAD.')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.type, 'int')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.required, True)

        SECOND_RESPONSE_PARAMETER: Attribute = RESPONSE_PARAMETERS.attributes[2]
        self.assertEqual(SECOND_RESPONSE_PARAMETER.name, 'languageCode')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.description, 'The language code of the running ARCHICAD.')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.type, 'str')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.required, True)

    def test_setter_command(self):
        REQUIRED_FILES = ['API.SetLayoutSettings.json', 'APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)

        self.assertTrue(converter.classes)
        self.assertTrue(converter.commands)

        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'SetLayoutSettings')
        self.assertEqual(COMMAND.description, 'Sets the parameters (settings) of the given layout.')
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)
        
        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'SetLayoutSettings_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertEqual(COMMAND_PARAMETERS.additional_properties, False)

        FIRST_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[0]
        self.assertEqual(FIRST_COMMAND_PARAMETER.name, 'layoutParameters')
        self.assertEqual(FIRST_COMMAND_PARAMETER.description, 'The parameters of the layout.')
        self.assertTrue(FIRST_COMMAND_PARAMETER.type in converter.classes)
        self.assertEqual(FIRST_COMMAND_PARAMETER.type, 'LayoutParameters')
        self.assertEqual(FIRST_COMMAND_PARAMETER.required, True)
        self.assertIsNone(FIRST_COMMAND_PARAMETER.title)
        self.assertIsNone(FIRST_COMMAND_PARAMETER.default)

        SECOND_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[1]
        self.assertEqual(SECOND_COMMAND_PARAMETER.name, 'layoutNavigatorItemId')
        self.assertEqual(SECOND_COMMAND_PARAMETER.description, 'The identifier of a navigator item.')
        self.assertTrue(SECOND_COMMAND_PARAMETER.type in converter.classes)
        self.assertEqual(SECOND_COMMAND_PARAMETER.type, 'NavigatorItemId')
        self.assertEqual(SECOND_COMMAND_PARAMETER.required, True)
        self.assertIsNone(SECOND_COMMAND_PARAMETER.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER.default)

        FIRST_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(FIRST_COMMAND_PARAMETER.type)]
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.name, 'LayoutParameters')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.description, 'The parameters of the layout.')
        self.assertEqual(len(FIRST_COMMAND_PARAMETER_CLASS.attributes), 16)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].name, 'leftMargin')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].type, 'float')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].description, 'The layout margin from the left side of the paper.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].name, 'customLayoutNumber')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].type, 'str')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].description, 'The custom ID.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].name, 'layoutPageNumber')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].type, 'int')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].description, 'The page number of layout when this layout contains multi-page drawings.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].name, 'hasIssuedRevision')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].type, 'bool')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].description, 'Defines whether one or more issued document revisions have already been created for the layout or not.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(FIRST_COMMAND_PARAMETER_CLASS.title)
        self.assertIsNone(FIRST_COMMAND_PARAMETER_CLASS.default)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.additional_properties, False)

        SECOND_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(SECOND_COMMAND_PARAMETER.type)]
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.name, 'NavigatorItemId')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.description, 'The identifier of a navigator item.')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.class_type, ClassType.NORMAL)
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.additional_properties, False)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS.default)

        SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR: Attribute = SECOND_COMMAND_PARAMETER_CLASS.attributes[0]
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.name, 'guid')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.type, 'UUID')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.description, 'A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.pattern, '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.required, True)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.default)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.min_length)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.max_length)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.values)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'SetLayoutSettings_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)

    def test_complex_command(self):
        REQUIRED_FILES = ['API.GetElementsByType.json', 'APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)

        self.assertTrue(converter.classes)
        self.assertTrue(converter.commands)
        
        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'GetElementsByType')
        self.assertEqual(COMMAND.description, "Returns the identifier of every element of the given type on the plan.")
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)

        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'GetElementsByType_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertEqual(COMMAND_PARAMETERS.additional_properties, False)
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].name, 'elementType')
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].description, 'The type of an element.')
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].type, 'str')
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].required, True)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].title)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].default)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].min_length)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].max_length)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].pattern)
        self.assertIsNotNone(COMMAND_PARAMETERS.attributes[0].values)
        self.assertEqual(len(COMMAND_PARAMETERS.attributes[0].values), 18)
        self.assertIn('Lamp', COMMAND_PARAMETERS.attributes[0].values)
        self.assertIn('Morph', COMMAND_PARAMETERS.attributes[0].values)
        self.assertIn('Wall', COMMAND_PARAMETERS.attributes[0].values)
        self.assertIn('Opening', COMMAND_PARAMETERS.attributes[0].values)
        self.assertNotIn('NotStair', COMMAND_PARAMETERS.attributes[0].values)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'GetElementsByType_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].name, 'elements')
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].description, 'A list of elements.')
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].type, 'List')
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].required, True)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].title)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].default)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].min_items)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].max_items)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].unique_items)
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].itemtype, 'ElementIdArrayItem')
        self.assertIn(RESPONSE_PARAMETERS.attributes[0].itemtype, converter.classes)
        
        RESPONSE_PARAMETER_ITEMTYPE = converter.classes[converter.classes.index(RESPONSE_PARAMETERS.attributes[0].itemtype)]
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE.name, 'ElementIdArrayItem')
        self.assertFalse(RESPONSE_PARAMETER_ITEMTYPE.description)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE.title)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE.default)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE.additional_properties, False)
        RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS = converter.classes[converter.classes.index(RESPONSE_PARAMETER_ITEMTYPE.attributes[0].type)]
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.name, 'ElementId')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.description, 'The identifier of an element.')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.title)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.default)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.additional_properties, False)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].name, 'guid')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].type, 'UUID')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].description, 'A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].pattern, '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
        
    def test_one_of_command(self):
        REQUIRED_FILES = ['API.RenameNavigatorItem.json', 'APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.realpath(__file__))
        schema_folder = os.path.join(script_path, 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)

        self.assertTrue(converter.classes)
        self.assertTrue(converter.commands)
        
        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'RenameNavigatorItem')
        self.assertEqual(COMMAND.description, "Renames an existing navigator item by specifying either the name or the ID, or both.")
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)

        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'RenameNavigatorItem_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.ONEOF)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertIsNone(COMMAND_PARAMETERS.additional_properties)
        
        FIRST_COMMAND_PARAMETER_ATTRIBUTE: Attribute = COMMAND_PARAMETERS.attributes[0]
        self.assertEqual(FIRST_COMMAND_PARAMETER_ATTRIBUTE.name, 'navigatorItemId')
        self.assertEqual(FIRST_COMMAND_PARAMETER_ATTRIBUTE.description, 'The identifier of a navigator item.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_ATTRIBUTE.type, 'NavigatorItemId')
        self.assertEqual(FIRST_COMMAND_PARAMETER_ATTRIBUTE.required, True)
        self.assertIsNone(FIRST_COMMAND_PARAMETER_ATTRIBUTE.title)
        self.assertIsNone(FIRST_COMMAND_PARAMETER_ATTRIBUTE.default)
        
        SECOND_COMMAND_PARAMETER_ATTRIBUTE: Attribute = COMMAND_PARAMETERS.attributes[1]
        self.assertEqual(SECOND_COMMAND_PARAMETER_ATTRIBUTE.name, 'newName')
        self.assertEqual(SECOND_COMMAND_PARAMETER_ATTRIBUTE.description, 'New name of the navigator item.')
        self.assertEqual(SECOND_COMMAND_PARAMETER_ATTRIBUTE.type, 'str')
        self.assertEqual(SECOND_COMMAND_PARAMETER_ATTRIBUTE.required, False)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_ATTRIBUTE.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_ATTRIBUTE.default)

        THIRD_COMMAND_PARAMETER_ATTRIBUTE: Attribute = COMMAND_PARAMETERS.attributes[2]
        self.assertEqual(THIRD_COMMAND_PARAMETER_ATTRIBUTE.name, 'newId')
        self.assertEqual(THIRD_COMMAND_PARAMETER_ATTRIBUTE.description, 'New ID of the navigator item.')
        self.assertEqual(THIRD_COMMAND_PARAMETER_ATTRIBUTE.type, 'str')
        self.assertEqual(THIRD_COMMAND_PARAMETER_ATTRIBUTE.required, False)
        self.assertIsNone(THIRD_COMMAND_PARAMETER_ATTRIBUTE.title)
        self.assertIsNone(THIRD_COMMAND_PARAMETER_ATTRIBUTE.default)

        FIRST_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(COMMAND_PARAMETERS.of_type_class_names[0])]
        FIRST_PARAMETER_OF_FIRST_CLASS: Attribute = FIRST_COMMAND_PARAMETER_CLASS.attributes[0]
        self.assertEqual(FIRST_PARAMETER_OF_FIRST_CLASS.name, 'navigatorItemId')
        self.assertEqual(FIRST_PARAMETER_OF_FIRST_CLASS.description, 'The identifier of a navigator item.')
        self.assertEqual(FIRST_PARAMETER_OF_FIRST_CLASS.type, 'NavigatorItemId')
        self.assertEqual(FIRST_PARAMETER_OF_FIRST_CLASS.required, True)
        self.assertIsNone(FIRST_PARAMETER_OF_FIRST_CLASS.title)
        self.assertIsNone(FIRST_PARAMETER_OF_FIRST_CLASS.default)
        SECOND_PARAMETER_OF_FIRST_CLASS: Attribute = FIRST_COMMAND_PARAMETER_CLASS.attributes[1]
        self.assertEqual(SECOND_PARAMETER_OF_FIRST_CLASS.name, 'newName')
        self.assertEqual(SECOND_PARAMETER_OF_FIRST_CLASS.description, 'New name of the navigator item.')
        self.assertEqual(SECOND_PARAMETER_OF_FIRST_CLASS.type, 'str')
        self.assertEqual(SECOND_PARAMETER_OF_FIRST_CLASS.required, True)
        self.assertIsNone(SECOND_PARAMETER_OF_FIRST_CLASS.title)
        self.assertIsNone(SECOND_PARAMETER_OF_FIRST_CLASS.default)

        SECOND_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(COMMAND_PARAMETERS.of_type_class_names[1])]
        FIRST_PARAMETER_OF_SECOND_CLASS: Attribute = SECOND_COMMAND_PARAMETER_CLASS.attributes[0]
        self.assertEqual(FIRST_PARAMETER_OF_SECOND_CLASS.name, 'navigatorItemId')
        self.assertEqual(FIRST_PARAMETER_OF_SECOND_CLASS.description, 'The identifier of a navigator item.')
        self.assertEqual(FIRST_PARAMETER_OF_SECOND_CLASS.type, 'NavigatorItemId')
        self.assertEqual(FIRST_PARAMETER_OF_SECOND_CLASS.required, True)
        self.assertIsNone(FIRST_PARAMETER_OF_SECOND_CLASS.title)
        self.assertIsNone(FIRST_PARAMETER_OF_SECOND_CLASS.default)
        SECOND_PARAMETER_OF_SECOND_CLASS: Attribute = SECOND_COMMAND_PARAMETER_CLASS.attributes[1]
        self.assertEqual(SECOND_PARAMETER_OF_SECOND_CLASS.name, 'newId')
        self.assertEqual(SECOND_PARAMETER_OF_SECOND_CLASS.description, 'New ID of the navigator item.')
        self.assertEqual(SECOND_PARAMETER_OF_SECOND_CLASS.type, 'str')
        self.assertEqual(SECOND_PARAMETER_OF_SECOND_CLASS.required, True)
        self.assertIsNone(SECOND_PARAMETER_OF_SECOND_CLASS.title)
        self.assertIsNone(SECOND_PARAMETER_OF_SECOND_CLASS.default)
        
        THIRD_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(COMMAND_PARAMETERS.of_type_class_names[2])]
        FIRST_PARAMETER_OF_THIRD_CLASS: Attribute = THIRD_COMMAND_PARAMETER_CLASS.attributes[0]
        self.assertEqual(FIRST_PARAMETER_OF_THIRD_CLASS.name, 'navigatorItemId')
        self.assertEqual(FIRST_PARAMETER_OF_THIRD_CLASS.description, 'The identifier of a navigator item.')
        self.assertEqual(FIRST_PARAMETER_OF_THIRD_CLASS.type, 'NavigatorItemId')
        self.assertEqual(FIRST_PARAMETER_OF_THIRD_CLASS.required, True)
        self.assertIsNone(FIRST_PARAMETER_OF_THIRD_CLASS.title)
        self.assertIsNone(FIRST_PARAMETER_OF_THIRD_CLASS.default)
        SECOND_PARAMETER_OF_THIRD_CLASS: Attribute = THIRD_COMMAND_PARAMETER_CLASS.attributes[1]
        self.assertEqual(SECOND_PARAMETER_OF_THIRD_CLASS.name, 'newName')
        self.assertEqual(SECOND_PARAMETER_OF_THIRD_CLASS.description, 'New name of the navigator item.')
        self.assertEqual(SECOND_PARAMETER_OF_THIRD_CLASS.type, 'str')
        self.assertEqual(SECOND_PARAMETER_OF_THIRD_CLASS.required, True)
        self.assertIsNone(SECOND_PARAMETER_OF_THIRD_CLASS.title)
        self.assertIsNone(SECOND_PARAMETER_OF_THIRD_CLASS.default)
        THIRD_PARAMETER_OF_THIRD_CLASS: Attribute = THIRD_COMMAND_PARAMETER_CLASS.attributes[2]
        self.assertEqual(THIRD_PARAMETER_OF_THIRD_CLASS.name, 'newId')
        self.assertEqual(THIRD_PARAMETER_OF_THIRD_CLASS.description, 'New ID of the navigator item.')
        self.assertEqual(THIRD_PARAMETER_OF_THIRD_CLASS.type, 'str')
        self.assertEqual(THIRD_PARAMETER_OF_THIRD_CLASS.required, True)
        self.assertIsNone(THIRD_PARAMETER_OF_THIRD_CLASS.title)
        self.assertIsNone(THIRD_PARAMETER_OF_THIRD_CLASS.default)
        
        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'RenameNavigatorItem_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)
        self.assertFalse(RESPONSE_PARAMETERS.attributes)

