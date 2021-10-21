import unittest
from schemaparser import SchemaParser

class TestPrimitiveTypes(unittest.TestCase):
    def test_basic_bool_schema(self):
        DO_NOT_INCLUDE = "doNotInclude"
        DO_NOT_INCLUDE_DESCRIPTION = "Include flag of the layout subset."

        schema = {
            "definitions": {
                DO_NOT_INCLUDE: {
                    "type": "boolean",
                    "description": DO_NOT_INCLUDE_DESCRIPTION
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(DO_NOT_INCLUDE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].type, 'boolean')
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].description, DO_NOT_INCLUDE_DESCRIPTION)

        self.assertIsNone(parser.primitive_type_schemas[DO_NOT_INCLUDE].title)
        self.assertIsNone(parser.primitive_type_schemas[DO_NOT_INCLUDE].default)
        self.assertIsNone(parser.primitive_type_schemas[DO_NOT_INCLUDE].examples)

    def test_full_bool_schema(self):
        DO_NOT_INCLUDE = "doNotInclude"
        DO_NOT_INCLUDE_DESCRIPTION = "Include flag of the layout subset."

        schema = {
            "definitions": {
                DO_NOT_INCLUDE: {
                    "title": "Title example",
                    "type": "boolean",
                    "description": DO_NOT_INCLUDE_DESCRIPTION,
                    "default": False,
                    "examples": [
                        True,
                        False
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(DO_NOT_INCLUDE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].type, 'boolean')
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].description, DO_NOT_INCLUDE_DESCRIPTION)
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].title, 'Title example')
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].default, False)
        self.assertEqual(parser.primitive_type_schemas[DO_NOT_INCLUDE].examples, [True, False])
        

    def test_basic_string_schema(self):
        MESSAGE = "message"
        MESSAGE_DESCRIPTION= "The error message."

        schema = {
            "definitions": {
                MESSAGE: {
                    "type": "string",
                    "description": MESSAGE_DESCRIPTION
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(MESSAGE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[MESSAGE].type, 'string')
        self.assertEqual(parser.primitive_type_schemas[MESSAGE].description, MESSAGE_DESCRIPTION)

        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].min_length)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].max_length)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].pattern)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].values)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].title)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].default)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].examples)

    def test_full_string_schema(self):
        MESSAGE = "message"
        MESSAGE_DESCRIPTION = "The error message."
        MESSAGE_PATTERN = "^[0-9A-Za-z ]+\\.$"

        schema = {
            "definitions": {
                MESSAGE: {
                    "type": "string",
                    "description": MESSAGE_DESCRIPTION,
                    "minLength": 2,
                    "maxLength": 3,
                    "pattern": MESSAGE_PATTERN,
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(MESSAGE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[MESSAGE].type, 'string')
        self.assertEqual(parser.primitive_type_schemas[MESSAGE].description, MESSAGE_DESCRIPTION)

        self.assertEqual(parser.primitive_type_schemas[MESSAGE].min_length, 2)
        self.assertEqual(parser.primitive_type_schemas[MESSAGE].max_length, 3)
        self.assertEqual(parser.primitive_type_schemas[MESSAGE].pattern, MESSAGE_PATTERN )

        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].values)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].title)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].default)
        self.assertIsNone(parser.primitive_type_schemas[MESSAGE].examples)

    def test_basic_integer_schema(self):
        CODE = "code"
        CODE_DESCRIPTION = "The error code."

        schema = {
            "definitions": {
                CODE: {
                    "type": "integer",
                    "description": CODE_DESCRIPTION
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(CODE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[CODE].type, 'integer')
        self.assertEqual(parser.primitive_type_schemas[CODE].description, CODE_DESCRIPTION)

        self.assertIsNone(parser.primitive_type_schemas[CODE].multiple_of)
        self.assertIsNone(parser.primitive_type_schemas[CODE].minimum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].exclusive_minimum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].maximum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].exclusive_maximum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].values)
        self.assertIsNone(parser.primitive_type_schemas[CODE].title)
        self.assertIsNone(parser.primitive_type_schemas[CODE].default)
        self.assertIsNone(parser.primitive_type_schemas[CODE].examples)

    def test_full_integer_schema(self):
        CODE = "code"
        CODE_DESCRIPTION = "The error code."

        schema = {
            "definitions": {
                CODE: {
                    "type": "integer",
                    "description": CODE_DESCRIPTION,
                    "multipleOf": 2,
                    "minimum": 0,
                    "exclusiveMinimum": True,
                    "maximum": 10,
                    "exclusiveMaximum": False
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(CODE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[CODE].type, 'integer')
        self.assertEqual(parser.primitive_type_schemas[CODE].description, CODE_DESCRIPTION)

        self.assertEqual(parser.primitive_type_schemas[CODE].multiple_of, 2)
        self.assertEqual(parser.primitive_type_schemas[CODE].minimum, 0)
        self.assertEqual(parser.primitive_type_schemas[CODE].exclusive_minimum, True)
        self.assertEqual(parser.primitive_type_schemas[CODE].maximum, 10)
        self.assertEqual(parser.primitive_type_schemas[CODE].exclusive_maximum, False)

        self.assertIsNone(parser.primitive_type_schemas[CODE].values)
        self.assertIsNone(parser.primitive_type_schemas[CODE].title)
        self.assertIsNone(parser.primitive_type_schemas[CODE].default)
        self.assertIsNone(parser.primitive_type_schemas[CODE].examples)
    
    def test_basic_number_schema(self):
        CODE = "code"
        CODE_DESCRIPTION = "The error code."

        schema = {
            "definitions": {
                CODE: {
                    "type": "number",
                    "description": CODE_DESCRIPTION
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(CODE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[CODE].type, 'number')
        self.assertEqual(parser.primitive_type_schemas[CODE].description, CODE_DESCRIPTION)
        
        self.assertIsNone(parser.primitive_type_schemas[CODE].multiple_of)
        self.assertIsNone(parser.primitive_type_schemas[CODE].minimum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].exclusive_minimum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].maximum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].exclusive_maximum)
        self.assertIsNone(parser.primitive_type_schemas[CODE].values)
        self.assertIsNone(parser.primitive_type_schemas[CODE].title)
        self.assertIsNone(parser.primitive_type_schemas[CODE].default)
        self.assertIsNone(parser.primitive_type_schemas[CODE].examples)

    def test_full_number_schema(self):
        CODE = "code"
        CODE_DESCRIPTION = "The error code."

        schema = {
            "definitions": {
                CODE: {
                    "type": "number",
                    "description": CODE_DESCRIPTION,
                    "multipleOf": 20.0,
                    "minimum": -20,
                    "exclusiveMinimum": False,
                    "maximum": 220.00,
                    "exclusiveMaximum": True
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(CODE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[CODE].type, 'number')
        self.assertEqual(parser.primitive_type_schemas[CODE].description, CODE_DESCRIPTION)
        
        self.assertEqual(parser.primitive_type_schemas[CODE].multiple_of, 20)
        self.assertEqual(parser.primitive_type_schemas[CODE].minimum, -20)
        self.assertEqual(parser.primitive_type_schemas[CODE].exclusive_minimum, False)
        self.assertEqual(parser.primitive_type_schemas[CODE].maximum, 220.0)
        self.assertEqual(parser.primitive_type_schemas[CODE].exclusive_maximum, True)

        self.assertIsNone(parser.primitive_type_schemas[CODE].values)
        self.assertIsNone(parser.primitive_type_schemas[CODE].title)
        self.assertIsNone(parser.primitive_type_schemas[CODE].default)
        self.assertIsNone(parser.primitive_type_schemas[CODE].examples)

    def test_guid(self):
        GUID = "guid"
        GUID_DESCRIPTION = "A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122."
        GUID_PATTERN = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"

        schema = {
            "definitions": {
                GUID: {
                    "type": "string",
                    "description": GUID_DESCRIPTION,
                    "format": "uuid",
                    "pattern": GUID_PATTERN
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(GUID, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[GUID].type, 'UUID')
        self.assertEqual(parser.primitive_type_schemas[GUID].description, GUID_DESCRIPTION)
        self.assertEqual(parser.primitive_type_schemas[GUID].pattern, GUID_PATTERN)

        self.assertIsNone(parser.primitive_type_schemas[GUID].min_length)
        self.assertIsNone(parser.primitive_type_schemas[GUID].max_length)
        self.assertIsNone(parser.primitive_type_schemas[GUID].values)
        self.assertIsNone(parser.primitive_type_schemas[GUID].title)
        self.assertIsNone(parser.primitive_type_schemas[GUID].default)
        self.assertIsNone(parser.primitive_type_schemas[GUID].examples)

    def test_string_enum(self):
        ELEMENT_TYPE = "elementType"
        ELEMENT_TYPE_DESCRIPTION = "The type of the element."

        schema = {
            "definitions": {
                ELEMENT_TYPE: {
                    "type": "string",
                    "description": ELEMENT_TYPE_DESCRIPTION,
                    "enum": [
                        "Wall",
                        "Window",
                        "Object",
                        "Beam"
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)
        
        self.assertIn(ELEMENT_TYPE, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[ELEMENT_TYPE].description, ELEMENT_TYPE_DESCRIPTION)

        self.assertEqual(4, len(parser.primitive_type_schemas[ELEMENT_TYPE].values))
        self.assertIn('Wall', parser.primitive_type_schemas[ELEMENT_TYPE].values)
        self.assertIn('Window', parser.primitive_type_schemas[ELEMENT_TYPE].values)
        self.assertIn('Object', parser.primitive_type_schemas[ELEMENT_TYPE].values)
        self.assertNotIn('Door', parser.primitive_type_schemas[ELEMENT_TYPE].values)
        self.assertFalse('Beam' not in parser.primitive_type_schemas[ELEMENT_TYPE].values)
        
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE].min_length)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE].max_length)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE].pattern)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE].title)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE].default)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE].examples)

    def test_integer_enum(self):
        ELEMENT_TYPE_ID = "elementTypeId"
        ELEMENT_TYPE_ID_DESCRIPTION = "The id of the element type."

        schema = {
            "definitions": {
                ELEMENT_TYPE_ID: {
                    "type": "integer",
                    "description": ELEMENT_TYPE_ID_DESCRIPTION,
                    "enum": [
                        1,
                        3,
                        4,
                        5,
                        8
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)
        
        self.assertIn(ELEMENT_TYPE_ID, parser.primitive_type_schemas)
        
        self.assertEqual(parser.primitive_type_schemas[ELEMENT_TYPE_ID].type, 'integer')
        self.assertEqual(parser.primitive_type_schemas[ELEMENT_TYPE_ID].description, ELEMENT_TYPE_ID_DESCRIPTION)

        self.assertEqual(5, len(parser.primitive_type_schemas[ELEMENT_TYPE_ID].values))
        self.assertIn(1, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertIn(4, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertIn(5, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertNotIn(2, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertNotIn(7, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertFalse(8 not in parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)

        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].multiple_of)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].minimum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].exclusive_minimum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].maximum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].exclusive_maximum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].title)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].default)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].examples)

    def test_number_enum(self):
        ELEMENT_TYPE_ID = "elementTypeId"
        ELEMENT_TYPE_ID_DESCRIPTION = "The id of the element type."

        schema = {
            "definitions": {
                ELEMENT_TYPE_ID: {
                    "type": "number",
                    "description": ELEMENT_TYPE_ID_DESCRIPTION,
                    "enum": [
                        1,
                        3.0,
                        8.2222
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)
        
        self.assertIn(ELEMENT_TYPE_ID, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[ELEMENT_TYPE_ID].description, ELEMENT_TYPE_ID_DESCRIPTION)

        self.assertEqual(3, len(parser.primitive_type_schemas[ELEMENT_TYPE_ID].values))
        self.assertIn(1, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertIn(1.0, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertIn(3, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertIn(3.0, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertNotIn(8, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertNotIn(2, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertNotIn(4.123, parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)
        self.assertFalse(8.2222 not in parser.primitive_type_schemas[ELEMENT_TYPE_ID].values)

        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].multiple_of)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].minimum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].exclusive_minimum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].maximum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].exclusive_maximum)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].title)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].default)
        self.assertIsNone(parser.primitive_type_schemas[ELEMENT_TYPE_ID].examples)


class TestObjects(unittest.TestCase):
    def test_object(self):
        ERROR = "error"
        ERROR_DESCRIPTION = "Error details."

        schema = {
            "definitions": {
                ERROR: {
                    "title": "Object title.",
                    "type": "object",
                    "description": ERROR_DESCRIPTION,
                    "properties": {
                        "code": {
                            "type": "integer",
                            "description": "The error code."
                        },
                        "message": {
                            "type": "string",
                            "description": "The error message."
                        }
                    },
                    "examples": [
                        {"code": 10, "message": "First test message"},
                        {"code": 15, "message": "Second est message"}
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)
        
        self.assertIn(ERROR, parser.object_schemas)
        self.assertEqual(parser.object_schemas[ERROR].description, ERROR_DESCRIPTION)
        self.assertEqual(parser.object_schemas[ERROR].title, 'Object title.')
        self.assertEqual(2, len(parser.object_schemas[ERROR].fields))
        self.assertIn('code', parser.object_schemas[ERROR].fields)
        self.assertIn('message', parser.object_schemas[ERROR].fields)

        CODE_REF_NAME = parser.object_schemas[ERROR].fields[0].type_reference
        self.assertIn(CODE_REF_NAME, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[CODE_REF_NAME].type, 'integer')
        self.assertEqual(parser.primitive_type_schemas[CODE_REF_NAME].description, 'The error code.')

        MESSAGE_REF_NAME = parser.object_schemas[ERROR].fields[1].type_reference
        self.assertIn(MESSAGE_REF_NAME, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[MESSAGE_REF_NAME].type, 'string')
        self.assertEqual(parser.primitive_type_schemas[MESSAGE_REF_NAME].description, 'The error message.')

        self.assertEqual(parser.object_schemas[ERROR].examples, 
                        [
                            {"code": 10, "message": "First test message"},
                            {"code": 15, "message": "Second est message"}
                        ])

        self.assertIsNone(parser.object_schemas[ERROR].required)
        self.assertIsNone(parser.object_schemas[ERROR].one_of_type_refs)
        self.assertIsNone(parser.object_schemas[ERROR].any_of_type_refs)
        self.assertIsNone(parser.object_schemas[ERROR].all_of_type_refs)
        self.assertIsNone(parser.object_schemas[ERROR].default)

    def test_object_with_required(self):
        EXECUTION_RESULT = "executionResult"
        EXECUTION_RESULT_DESCRIPTION = "The result of the execution."

        schema = {
            "definitions": {
                EXECUTION_RESULT: {
                    "type": "object",
                    "description": EXECUTION_RESULT_DESCRIPTION,
                    "properties": {
                        "success": {
                            "type": "boolean",
                            "description": "Success"
                        },
                        "error": {
                            "$ref": "#/definitions/error"
                        }
                    },
                    "required": [
                        "success"
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(EXECUTION_RESULT, parser.object_schemas)
        self.assertEqual(parser.object_schemas[EXECUTION_RESULT].description, EXECUTION_RESULT_DESCRIPTION)
        self.assertEqual(2, len(parser.object_schemas[EXECUTION_RESULT].fields))
        self.assertEqual(1, len(parser.object_schemas[EXECUTION_RESULT].required))
        self.assertIn('success', parser.object_schemas[EXECUTION_RESULT].fields)
        self.assertIn('error', parser.object_schemas[EXECUTION_RESULT].fields)
        self.assertIn('success', parser.object_schemas[EXECUTION_RESULT].required)

        SUCCESS_REF_NAME = parser.object_schemas[EXECUTION_RESULT].fields[0].type_reference
        self.assertIn(SUCCESS_REF_NAME, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[SUCCESS_REF_NAME].type, 'boolean')
        self.assertEqual(parser.primitive_type_schemas[SUCCESS_REF_NAME].description, 'Success')

        self.assertEqual(parser.object_schemas[EXECUTION_RESULT].fields[1].type_reference, 'error')

        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].one_of_type_refs)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].any_of_type_refs)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].all_of_type_refs)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].title)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].default)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].examples)


    def test_object_with_array(self):
        EXECUTION_RESULT = "executionResult"
        EXECUTION_RESULT_DESCRIPTION = "The result of the execution."

        schema = {
            "definitions": {
                EXECUTION_RESULT: {
                    "type": "object",
                    "description": EXECUTION_RESULT_DESCRIPTION,
                    "properties": {
                        "elements": {
                            "type": "array",
                            "description": "List of the elements.",
                            "items": {
                                "$ref": "#/definitions/elementId"
                            }
                        }
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)
        
        self.assertIn(EXECUTION_RESULT, parser.object_schemas)
        self.assertEqual(parser.object_schemas[EXECUTION_RESULT].description, EXECUTION_RESULT_DESCRIPTION)
        self.assertEqual(1, len(parser.object_schemas[EXECUTION_RESULT].fields))
        self.assertEqual(None, parser.object_schemas[EXECUTION_RESULT].required)
        self.assertIn('elements', parser.object_schemas[EXECUTION_RESULT].fields)

        ELEMENTS_REF_NAME = parser.object_schemas[EXECUTION_RESULT].fields[0].type_reference
        self.assertIn(ELEMENTS_REF_NAME, parser.list_schemas)
        self.assertEqual(parser.list_schemas[ELEMENTS_REF_NAME].description, "List of the elements.")
        self.assertEqual(parser.list_schemas[ELEMENTS_REF_NAME].itemtype, "elementId")

        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].required)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].one_of_type_refs)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].any_of_type_refs)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].all_of_type_refs)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].title)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].default)
        self.assertIsNone(parser.object_schemas[EXECUTION_RESULT].examples)

    def test_object_with_one_of(self):
        NAVIGATOR_TREE_ID = "NavigatorTreeId"
        NAVIGATOR_TREE_ID_DESCRIPTION = "The identifier of a navigator item tree."
        BOUNDING_BOX_2D_OR_ERROR = "BoundingBox2DOrError"
        BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION = "A 2D bounding box or error."
        
        schema = {
            "definitions": {
                NAVIGATOR_TREE_ID: {
                    "type": "object",
                    "description": NAVIGATOR_TREE_ID_DESCRIPTION,
                    "oneOf": [
                        {
                            "$ref": "#/definitions/PublisherSetId"
                        },
                        {
                            "$ref": "#/definitions/OtherNavigatorTreeId"
                        }
                    ]
                },
                BOUNDING_BOX_2D_OR_ERROR: {
                    "type": "object",
                    "description": BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION,
                    "oneOf": [
                        {
                            "properties": {
                                "boundingBox2D": {
                                    "$ref": "#/definitions/BoundingBox2D"
                                }
                            },
                            "required": [ "boundingBox2D" ]
                        },
                        {
                            "properties": {
                                "error": {
                                    "$ref": "#/definitions/Error"
                                }
                            },
                            "required": [ "error" ]
                        }
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(NAVIGATOR_TREE_ID, parser.object_schemas)
        self.assertIn(BOUNDING_BOX_2D_OR_ERROR, parser.object_schemas)

        self.assertEqual(parser.object_schemas[NAVIGATOR_TREE_ID].description, NAVIGATOR_TREE_ID_DESCRIPTION)
        self.assertEqual(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].description, BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].fields)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].fields)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].required)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].required)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].any_of_type_refs)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].all_of_type_refs)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs)
        
        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].title)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].title)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].default)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].default)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].examples)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].examples)


        self.assertIsNotNone(parser.object_schemas[NAVIGATOR_TREE_ID].one_of_type_refs)
        self.assertEqual(len(parser.object_schemas[NAVIGATOR_TREE_ID].one_of_type_refs), 2)
        self.assertEqual(['PublisherSetId', 'OtherNavigatorTreeId'], parser.object_schemas[NAVIGATOR_TREE_ID].one_of_type_refs)
        
        self.assertIsNotNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs)
        self.assertEqual(len(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs), 2)
        self.assertIn(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs[0], parser.object_schemas)
        self.assertIn(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs[1], parser.object_schemas)
        FIRST_OBJECT_TYPE = parser.object_schemas[parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs[0]]
        self.assertEqual(len(FIRST_OBJECT_TYPE.fields), 1)
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].name, 'boundingBox2D')
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].type_reference, 'BoundingBox2D')
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].type_reference, 'BoundingBox2D')
        self.assertEqual(len(FIRST_OBJECT_TYPE.required), 1)
        self.assertEqual(FIRST_OBJECT_TYPE.required[0], 'boundingBox2D')

        SECOND_OBJECT_TYPE = parser.object_schemas[parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs[1]]
        self.assertEqual(SECOND_OBJECT_TYPE.fields[0].name, 'error')
        self.assertEqual(SECOND_OBJECT_TYPE.fields[0].type_reference, 'Error')
        self.assertEqual(len(SECOND_OBJECT_TYPE.required), 1)
        self.assertEqual(SECOND_OBJECT_TYPE.required[0], 'error')


    def test_object_with_any_of(self):
        NAVIGATOR_TREE_ID = "NavigatorTreeId"
        NAVIGATOR_TREE_ID_DESCRIPTION = "The identifier of a navigator item tree."
        BOUNDING_BOX_2D_OR_ERROR = "BoundingBox2DOrError"
        BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION = "A 2D bounding box or error."

        schema = {
            "definitions": {
                NAVIGATOR_TREE_ID: {
                    "type": "object",
                    "description": NAVIGATOR_TREE_ID_DESCRIPTION,
                    "anyOf": [
                        {
                            "$ref": "#/definitions/PublisherSetId"
                        },
                        {
                            "$ref": "#/definitions/OtherNavigatorTreeId"
                        }
                    ]
                },
                BOUNDING_BOX_2D_OR_ERROR: {
                    "type": "object",
                    "description": BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION,
                    "anyOf": [
                        {
                            "properties": {
                                "boundingBox2D": {
                                    "$ref": "#/definitions/BoundingBox2D"
                                }
                            },
                            "required": [ "boundingBox2D" ]
                        },
                        {
                            "properties": {
                                "error": {
                                    "$ref": "#/definitions/Error"
                                }
                            },
                            "required": [ "error" ]
                        }
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(NAVIGATOR_TREE_ID, parser.object_schemas)
        self.assertIn(BOUNDING_BOX_2D_OR_ERROR, parser.object_schemas)

        self.assertEqual(parser.object_schemas[NAVIGATOR_TREE_ID].description, NAVIGATOR_TREE_ID_DESCRIPTION)
        self.assertEqual(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].description, BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].fields)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].fields)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].required)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].required)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].one_of_type_refs)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].all_of_type_refs)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs)
        
        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].title)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].title)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].default)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].default)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].examples)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].examples)
        
        self.assertIsNotNone(parser.object_schemas[NAVIGATOR_TREE_ID].any_of_type_refs)
        self.assertEqual(len(parser.object_schemas[NAVIGATOR_TREE_ID].any_of_type_refs), 2)
        self.assertEqual(['PublisherSetId', 'OtherNavigatorTreeId'], parser.object_schemas[NAVIGATOR_TREE_ID].any_of_type_refs)
        
        self.assertIsNotNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs)
        self.assertEqual(len(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs), 2)
        self.assertIn(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs[0], parser.object_schemas)
        self.assertIn(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs[1], parser.object_schemas)
        FIRST_OBJECT_TYPE = parser.object_schemas[parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs[0]]
        self.assertEqual(len(FIRST_OBJECT_TYPE.fields), 1)
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].name, 'boundingBox2D')
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].type_reference, 'BoundingBox2D')
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].type_reference, 'BoundingBox2D')
        self.assertEqual(len(FIRST_OBJECT_TYPE.required), 1)
        self.assertEqual(FIRST_OBJECT_TYPE.required[0], 'boundingBox2D')

        SECOND_OBJECT_TYPE = parser.object_schemas[parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs[1]]
        self.assertEqual(SECOND_OBJECT_TYPE.fields[0].name, 'error')
        self.assertEqual(SECOND_OBJECT_TYPE.fields[0].type_reference, 'Error')
        self.assertEqual(len(SECOND_OBJECT_TYPE.required), 1)
        self.assertEqual(SECOND_OBJECT_TYPE.required[0], 'error')
    
    def test_object_with_all_of(self):
        NAVIGATOR_TREE_ID = "NavigatorTreeId"
        NAVIGATOR_TREE_ID_DESCRIPTION = "The identifier of a navigator item tree."
        BOUNDING_BOX_2D_OR_ERROR = "BoundingBox2DOrError"
        BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION = "A 2D bounding box or error."

        schema = {
            "definitions": {
                NAVIGATOR_TREE_ID: {
                    "type": "object",
                    "description": NAVIGATOR_TREE_ID_DESCRIPTION,
                    "allOf": [
                        {
                            "$ref": "#/definitions/PublisherSetId"
                        },
                        {
                            "$ref": "#/definitions/OtherNavigatorTreeId"
                        }
                    ]
                },
                BOUNDING_BOX_2D_OR_ERROR: {
                    "type": "object",
                    "description": BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION,
                    "allOf": [
                        {
                            "properties": {
                                "boundingBox2D": {
                                    "$ref": "#/definitions/BoundingBox2D"
                                }
                            },
                            "required": [ "boundingBox2D" ]
                        },
                        {
                            "properties": {
                                "error": {
                                    "$ref": "#/definitions/Error"
                                }
                            },
                            "required": [ "error" ]
                        }
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(NAVIGATOR_TREE_ID, parser.object_schemas)
        self.assertIn(BOUNDING_BOX_2D_OR_ERROR, parser.object_schemas)

        self.assertEqual(parser.object_schemas[NAVIGATOR_TREE_ID].description, NAVIGATOR_TREE_ID_DESCRIPTION)
        self.assertEqual(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].description, BOUNDING_BOX_2D_OR_ERROR_DESCRIPTION)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].fields)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].fields)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].required)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].required)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].one_of_type_refs)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].one_of_type_refs)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].any_of_type_refs)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].any_of_type_refs)
        
        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].title)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].title)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].default)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].default)

        self.assertIsNone(parser.object_schemas[NAVIGATOR_TREE_ID].examples)
        self.assertIsNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].examples)
        
        self.assertIsNotNone(parser.object_schemas[NAVIGATOR_TREE_ID].all_of_type_refs)
        self.assertEqual(len(parser.object_schemas[NAVIGATOR_TREE_ID].all_of_type_refs), 2)
        self.assertEqual(['PublisherSetId', 'OtherNavigatorTreeId'], parser.object_schemas[NAVIGATOR_TREE_ID].all_of_type_refs)
        
        self.assertIsNotNone(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs)
        self.assertEqual(len(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs), 2)
        self.assertIn(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs[0], parser.object_schemas)
        self.assertIn(parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs[1], parser.object_schemas)
        FIRST_OBJECT_TYPE = parser.object_schemas[parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs[0]]
        self.assertEqual(len(FIRST_OBJECT_TYPE.fields), 1)
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].name, 'boundingBox2D')
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].type_reference, 'BoundingBox2D')
        self.assertEqual(FIRST_OBJECT_TYPE.fields[0].type_reference, 'BoundingBox2D')
        self.assertEqual(len(FIRST_OBJECT_TYPE.required), 1)
        self.assertEqual(FIRST_OBJECT_TYPE.required[0], 'boundingBox2D')

        SECOND_OBJECT_TYPE = parser.object_schemas[parser.object_schemas[BOUNDING_BOX_2D_OR_ERROR].all_of_type_refs[1]]
        self.assertEqual(SECOND_OBJECT_TYPE.fields[0].name, 'error')
        self.assertEqual(SECOND_OBJECT_TYPE.fields[0].type_reference, 'Error')
        self.assertEqual(len(SECOND_OBJECT_TYPE.required), 1)
        self.assertEqual(SECOND_OBJECT_TYPE.required[0], 'error')
    

class TestArrays(unittest.TestCase):
    def test_bool_array(self):
        BOOL_ARRAY = "boolArray"
        BOOL_ARRAY_DESCRIPTION = 'An array of booleans.'

        schema = {
            "definitions": {
                BOOL_ARRAY: {
                    "title": "Test bool array title.",
                    "type": "array",
                    "description": BOOL_ARRAY_DESCRIPTION,
                    "items": {
                        "type": "boolean",
                    },
                    "examples": [
                        [True, True, False],
                        [False, False, False]
                    ]
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(BOOL_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[BOOL_ARRAY].description, BOOL_ARRAY_DESCRIPTION)
        self.assertEqual(parser.list_schemas[BOOL_ARRAY].title, 'Test bool array title.')
        self.assertEqual(parser.list_schemas[BOOL_ARRAY].examples, 
                        [
                            [True, True, False],
                            [False, False, False]
                        ])
        self.assertIsNone(parser.list_schemas[BOOL_ARRAY].default)
        
        BOOL_REF_NAME = parser.list_schemas[BOOL_ARRAY].itemtype
        self.assertEqual(parser.primitive_type_schemas[BOOL_REF_NAME].type, 'boolean')

    def test_number_array(self):
        NUMBER_ARRAY = "numberArray"

        schema = {
            "definitions": {
                NUMBER_ARRAY: {
                    "type": "array",
                    "items": {
                        "type": "number",
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(NUMBER_ARRAY, parser.list_schemas)
        self.assertFalse(parser.list_schemas[NUMBER_ARRAY].description)
        self.assertIsNone(parser.list_schemas[NUMBER_ARRAY].title)
        self.assertIsNone(parser.list_schemas[NUMBER_ARRAY].default)
        self.assertIsNone(parser.list_schemas[NUMBER_ARRAY].examples)
        
        INTEGER_REF_NAME = parser.list_schemas[NUMBER_ARRAY].itemtype
        self.assertEqual(parser.primitive_type_schemas[INTEGER_REF_NAME].type, 'number')
        
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].maximum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].exclusive_maximum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].minimum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].exclusive_minimum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].values)

    def test_int_array(self):
        INTEGER_ARRAY = "integerArray"
        INTEGER_ARRAY_DESCRIPTION = "An array of integers."
        INTEGER_ARRAY_ITEMS_DESCRIPTION = "An integer of the array."

        schema = {
            "definitions": {
                INTEGER_ARRAY: {
                    "type": "array",
                    "description": INTEGER_ARRAY_DESCRIPTION,
                    "items": {
                        "type": "integer",
                        "description": INTEGER_ARRAY_ITEMS_DESCRIPTION
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(INTEGER_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[INTEGER_ARRAY].description, INTEGER_ARRAY_DESCRIPTION)
        self.assertIsNone(parser.list_schemas[INTEGER_ARRAY].title)
        self.assertIsNone(parser.list_schemas[INTEGER_ARRAY].default)
        self.assertIsNone(parser.list_schemas[INTEGER_ARRAY].examples)
        
        INTEGER_REF_NAME = parser.list_schemas[INTEGER_ARRAY].itemtype
        self.assertEqual(parser.primitive_type_schemas[INTEGER_REF_NAME].type, 'integer')
        self.assertEqual(parser.primitive_type_schemas[INTEGER_REF_NAME].description, INTEGER_ARRAY_ITEMS_DESCRIPTION)
        
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].maximum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].exclusive_maximum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].minimum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].exclusive_minimum)
        self.assertIsNone(parser.primitive_type_schemas[INTEGER_REF_NAME].values)

    def test_guid_array(self):
        GUID = "guid"
        GUID_PATTERN = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
        GUID_DESCRIPTION = "A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122."
        GUID_ARRAY = "guidArray"
        GUID_ARRAY_DESCRIPTION = "An array of guids."

        schema = {
            "definitions": {
                GUID: {
                    "type": "string",
                    "description": GUID_DESCRIPTION,
                    "format": "uuid",
                    "pattern": GUID_PATTERN
                },
                GUID_ARRAY: {
                    "type": "array",
                    "description": GUID_ARRAY_DESCRIPTION,
                    "items": {
                        "$ref": "#/definitions/guid"
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(GUID_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[GUID_ARRAY].description, GUID_ARRAY_DESCRIPTION)
        self.assertIsNone(parser.list_schemas[GUID_ARRAY].title)
        self.assertIsNone(parser.list_schemas[GUID_ARRAY].default)
        self.assertIsNone(parser.list_schemas[GUID_ARRAY].examples)
        
        self.assertEqual(parser.list_schemas[GUID_ARRAY].itemtype, GUID)
        GUID_REF_NAME = parser.list_schemas[GUID_ARRAY].itemtype
        self.assertEqual(parser.primitive_type_schemas[GUID_REF_NAME].type, 'UUID')
        self.assertEqual(parser.primitive_type_schemas[GUID_REF_NAME].description, GUID_DESCRIPTION)

        self.assertIsNotNone(parser.primitive_type_schemas[GUID_REF_NAME].pattern)
        self.assertEqual(parser.primitive_type_schemas[GUID_REF_NAME].pattern, GUID_PATTERN)

        self.assertIsNone(parser.primitive_type_schemas[GUID_REF_NAME].min_length)
        self.assertIsNone(parser.primitive_type_schemas[GUID_REF_NAME].max_length)
        self.assertIsNone(parser.primitive_type_schemas[GUID_REF_NAME].values)

    def test_string_array(self):
        STRING_ARRAY = "stringArray"
        STRING_ARRAY_DESCRIPTION = "An array of strings."
        STRING_ARRAY_ITEMS_DESCRIPTION = "A string of the array."

        schema = {
            "definitions": {
                STRING_ARRAY: {
                    "type": "array",
                    "description": STRING_ARRAY_DESCRIPTION,
                    "items": {
                        "type": "string",
                        "description": STRING_ARRAY_ITEMS_DESCRIPTION
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(STRING_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[STRING_ARRAY].description, STRING_ARRAY_DESCRIPTION)
        self.assertIsNone(parser.list_schemas[STRING_ARRAY].title)
        self.assertIsNone(parser.list_schemas[STRING_ARRAY].default)
        self.assertIsNone(parser.list_schemas[STRING_ARRAY].examples)
        
        STR_REF_NAME = parser.list_schemas[STRING_ARRAY].itemtype
        self.assertEqual(parser.primitive_type_schemas[STR_REF_NAME].type, 'string')
        self.assertEqual(parser.primitive_type_schemas[STR_REF_NAME].description, STRING_ARRAY_ITEMS_DESCRIPTION)
    
    def test_predefined_object_array(self):
        ERROR = "error"
        ERROR_DESCRIPTION = "Error details."
        OBJECT_ARRAY = "objectArray"
        OBJECT_ARRAY_DESCRIPTION = "An array of errors."

        schema = {
            "definitions": {
                ERROR: {
                    "type": "object",
                    "description": ERROR_DESCRIPTION,
                    "properties": {
                        "code": {
                            "type": "integer",
                            "description": "The error code."
                        },
                        "message": {
                            "type": "string",
                            "description": "The error message."
                        }
                    },
                    "required": [
                        "code",
                        "message"
                    ]
                },
                OBJECT_ARRAY: {
                    "type": "array",
                    "description": OBJECT_ARRAY_DESCRIPTION,
                    "items": {
                        "$ref": "#/definitions/error"
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(OBJECT_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[OBJECT_ARRAY].description, OBJECT_ARRAY_DESCRIPTION)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].title)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].default)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].examples)
        
        self.assertIn(ERROR, parser.object_schemas)
        self.assertEqual(parser.object_schemas[ERROR].description, ERROR_DESCRIPTION)
        self.assertEqual(2, len(parser.object_schemas[ERROR].fields))
        self.assertEqual(2, len(parser.object_schemas[ERROR].required))
        self.assertIn('code', parser.object_schemas[ERROR].fields)
        self.assertIn('message', parser.object_schemas[ERROR].fields)
        self.assertIn('code', parser.object_schemas[ERROR].required)
        self.assertIn('message', parser.object_schemas[ERROR].required)

        CODE_REF_NAME = parser.object_schemas[ERROR].fields[0].type_reference
        self.assertIn(CODE_REF_NAME, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[CODE_REF_NAME].type, 'integer')
        self.assertEqual(parser.primitive_type_schemas[CODE_REF_NAME].description, 'The error code.')

        MESSAGE_REF_NAME = parser.object_schemas[ERROR].fields[1].type_reference
        self.assertIn(MESSAGE_REF_NAME, parser.primitive_type_schemas)
        self.assertEqual(parser.primitive_type_schemas[MESSAGE_REF_NAME].type, 'string')
        self.assertEqual(parser.primitive_type_schemas[MESSAGE_REF_NAME].description, 'The error message.')
        
    def test_undefined_object_array(self):
        OBJECT_ARRAY = "objectArray"
        OBJECT_ARRAY_DESCRIPTION = "An array of undefined objects."

        schema = {
            "definitions": {
                OBJECT_ARRAY: {
                    "type": "array",
                    "description": OBJECT_ARRAY_DESCRIPTION,
                    "items": {
                        "type": "object",
                        "properties": {
                            "navigatorItemId": {
                                "$ref": "#/definitions/NavigatorItemId"
                            }
                        },
                        "required": [
                            "navigatorItemId"
                        ]
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)
        
        self.assertIn(OBJECT_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[OBJECT_ARRAY].description, OBJECT_ARRAY_DESCRIPTION)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].title)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].default)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].examples)

        ITEM_TYPE_REF: str = parser.list_schemas[OBJECT_ARRAY].itemtype
        self.assertRegex(ITEM_TYPE_REF, '^Object_[0-9a-fA-F]{8}_[0-9a-fA-F]{4}_[0-9a-fA-F]{4}_[0-9a-fA-F]{4}_[0-9a-fA-F]{12}$')
        self.assertEqual(len(parser.object_schemas[ITEM_TYPE_REF].fields), 1)
        self.assertEqual(parser.object_schemas[ITEM_TYPE_REF].fields[0].name, 'navigatorItemId')
        self.assertEqual(parser.object_schemas[ITEM_TYPE_REF].fields[0].type_reference, 'NavigatorItemId')
        self.assertEqual(len(parser.object_schemas[ITEM_TYPE_REF].required), 1)
        self.assertIn('navigatorItemId', parser.object_schemas[ITEM_TYPE_REF].required)

        self.assertEqual(parser.object_schemas[ITEM_TYPE_REF].description, '')
        self.assertIsNone(parser.object_schemas[ITEM_TYPE_REF].one_of_type_refs)
        self.assertIsNone(parser.object_schemas[ITEM_TYPE_REF].any_of_type_refs)
        self.assertIsNone(parser.object_schemas[ITEM_TYPE_REF].all_of_type_refs)

        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].min_items)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].max_items)
        self.assertIsNone(parser.list_schemas[OBJECT_ARRAY].unique_items)

    def test_full_array_schema(self):
        GUID_ARRAY = "guidArray"
        GUID_ARRAY_DESCRIPTION = "An array of guids."

        schema = {
            "definitions": {
                GUID_ARRAY: {
                    "title": "Test title.",
                    "type": "array",
                    "description": GUID_ARRAY_DESCRIPTION,
                    "items": {
                        "$ref": "#/definitions/guid"
                    },
                    "minItems": 5,
                    "maxItems": 10,
                    "uniqueItems": True
                }
            }
        }
        parser = SchemaParser()
        parser.parse_types(schema)

        self.assertIn(GUID_ARRAY, parser.list_schemas)
        self.assertEqual(parser.list_schemas[GUID_ARRAY].description, GUID_ARRAY_DESCRIPTION)
        self.assertEqual(parser.list_schemas[GUID_ARRAY].itemtype, 'guid')
        self.assertEqual(parser.list_schemas[GUID_ARRAY].title, 'Test title.')
        self.assertIsNone(parser.list_schemas[GUID_ARRAY].examples)
        self.assertIsNone(parser.list_schemas[GUID_ARRAY].default)

        self.assertEqual(parser.list_schemas[GUID_ARRAY].min_items, 5)
        self.assertEqual(parser.list_schemas[GUID_ARRAY].max_items, 10)
        self.assertEqual(parser.list_schemas[GUID_ARRAY].unique_items, True)

class TestCommands(unittest.TestCase):
    def test_command(self):
        COMMAND_NAME = "CreateViewMapFolder"
        COMMAND_DESCRIPTION = "Create a view folder item at a given position in the navigator tree."

        schema= {
            "$schema": "http://json-schema.org/draft-04/schema",
            "description": COMMAND_DESCRIPTION,
            "definitions": {
                "command_parameters": {
                    "type": "object",
                    "properties": {
                        "folderParameters": {
                            "$ref": "APITypes.json#/definitions/FolderParameters"
                        },
                        "parentFolder": {
                            "$ref": "APITypes.json#/definitions/NavigatorItemId"
                        },
                        "previousSiblingFolder": {
                            "$ref": "APITypes.json#/definitions/NavigatorItemId"
                        }
                    },
                    "required": [
                        "folderParameters"
                    ]
                },
                "response_parameters": {
                    "type": "object",
                    "properties": {
                    }
                },
                "examples": {
                    "command_example": {
                        "command": "API.CreateFolderInViewTree",
                        "parameters": {
                            "folderParameters": {
                                "folderName": "Test Folder"
                            },
                            "parentFolder": {
                                "guid": "8A3BBC57-86D6-407E-8B3C-3A862E32DF3A"
                            },
                            "previousSiblingFolder": {
                                "guid": "00000000-4315-4F9E-84F5-275194D29226"
                            }
                        }
                    },
                    "response_example": {
                        "succeeded": True,
                        "result": {
                            "createdFolderId": {
                                "guid": "EDB6197B-0754-4741-8BA6-712865FD0F76"
                            }
                        },
                        "executionDuration": 0.242254153
                    }
                }
            }
        }
        parser = SchemaParser()
        parser.parse_command(COMMAND_NAME, schema)

        self.assertIn(COMMAND_NAME, parser.command_schemas)
        COMMAND = parser.command_schemas[COMMAND_NAME]

        self.assertEqual(COMMAND.description, COMMAND_DESCRIPTION)
        self.assertIn(COMMAND.parameters_schema_name, parser.object_schemas)
        self.assertEqual(COMMAND.parameters_schema_name, f'{COMMAND_NAME}_parameters')
        self.assertIn(COMMAND.response_schema_name, parser.object_schemas)
        self.assertEqual(COMMAND.response_schema_name, f'{COMMAND_NAME}_response')

        PARAMETER_OBJECT = parser.object_schemas[COMMAND.parameters_schema_name]
        self.assertEqual(len(PARAMETER_OBJECT.fields), 3)
        self.assertEqual(PARAMETER_OBJECT.fields[0].name, 'folderParameters')
        self.assertEqual(PARAMETER_OBJECT.fields[0].type_reference, 'FolderParameters')

        self.assertEqual(PARAMETER_OBJECT.fields[1].name, 'parentFolder')
        self.assertEqual(PARAMETER_OBJECT.fields[1].type_reference, 'NavigatorItemId')

        self.assertEqual(PARAMETER_OBJECT.fields[2].name, 'previousSiblingFolder')
        self.assertEqual(PARAMETER_OBJECT.fields[2].type_reference, 'NavigatorItemId')

        self.assertIn('folderParameters', PARAMETER_OBJECT.required)

        self.assertEqual(PARAMETER_OBJECT.description, '')
        self.assertIsNone(PARAMETER_OBJECT.one_of_type_refs)
        self.assertIsNone(PARAMETER_OBJECT.any_of_type_refs)
        self.assertIsNone(PARAMETER_OBJECT.all_of_type_refs)

        RESPONSE_OBJECT = parser.object_schemas[COMMAND.response_schema_name]
        self.assertEqual(RESPONSE_OBJECT.description, '')
        self.assertIsNone(RESPONSE_OBJECT.fields)
        self.assertIsNone(RESPONSE_OBJECT.required)
        self.assertIsNone(RESPONSE_OBJECT.one_of_type_refs)
        self.assertIsNone(RESPONSE_OBJECT.any_of_type_refs)
        self.assertIsNone(RESPONSE_OBJECT.all_of_type_refs)
        
        self.assertEqual(COMMAND.examples,
                        {
                            "command_example": {
                                "command": "API.CreateFolderInViewTree",
                                "parameters": {
                                    "folderParameters": {
                                        "folderName": "Test Folder"
                                    },
                                    "parentFolder": {
                                        "guid": "8A3BBC57-86D6-407E-8B3C-3A862E32DF3A"
                                    },
                                    "previousSiblingFolder": {
                                        "guid": "00000000-4315-4F9E-84F5-275194D29226"
                                    }
                                }
                            },
                            "response_example": {
                                "succeeded": True,
                                "result": {
                                    "createdFolderId": {
                                        "guid": "EDB6197B-0754-4741-8BA6-712865FD0F76"
                                    }
                                },
                                "executionDuration": 0.242254153
                            }
                        })

