"""GRAPHISOFT
"""
from uuid import UUID
from typing import Union, Optional, List

from archicad.acbasetype import _ACBaseType, _ACUnionType, _ConstructUnion
from archicad.validators import value_set, matches, min_length, max_length, multiple_of, minimum, maximum, listitem_validator, min_items, max_items, unique_items


class ClassificationSystemId(_ACBaseType):
    """ The identifier of a classification system.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

ClassificationSystemId.get_classinfo().add_field('guid', UUID)


class ClassificationSystemIdArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.

    """
    __slots__ = ("classificationSystemId", )

    def __init__(self, classificationSystemId: ClassificationSystemId):
        self.classificationSystemId: ClassificationSystemId = classificationSystemId

ClassificationSystemIdArrayItem.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)


class ClassificationItemId(_ACBaseType):
    """ The identifier of a classification item.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

ClassificationItemId.get_classinfo().add_field('guid', UUID)


class ClassificationItemIdArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        classificationItemId (:obj:`ClassificationItemId`): The identifier of a classification item.

    """
    __slots__ = ("classificationItemId", )

    def __init__(self, classificationItemId: ClassificationItemId):
        self.classificationItemId: ClassificationItemId = classificationItemId

ClassificationItemIdArrayItem.get_classinfo().add_field('classificationItemId', ClassificationItemId)


class ClassificationId(_ACBaseType):
    """ The element classification identifier.

    Attributes:
        classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.
        classificationItemId (:obj:`ClassificationItemId`, optional): The identifier of a classification item.

    """
    __slots__ = ("classificationSystemId", "classificationItemId", )

    def __init__(self, classificationSystemId: ClassificationSystemId, classificationItemId: Optional[ClassificationItemId] = None):
        self.classificationSystemId: ClassificationSystemId = classificationSystemId
        self.classificationItemId: Optional[ClassificationItemId] = classificationItemId

ClassificationId.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)
ClassificationId.get_classinfo().add_field('classificationItemId', Optional[ClassificationItemId])


class ClassificationItemDetails(_ACBaseType):
    """ Details of a classification item.

    Attributes:
        id (:obj:`str`): The user specified unique identifier of the classification item.
        name (:obj:`str`): The display name of the classification item.
        description (:obj:`str`): The description of the classification item.

    """
    __slots__ = ("id", "name", "description", )

    def __init__(self, id: str, name: str, description: str):
        self.id: str = id
        self.name: str = name
        self.description: str = description

ClassificationItemDetails.get_classinfo().add_field('id', str)
ClassificationItemDetails.get_classinfo().add_field('name', str)
ClassificationItemDetails.get_classinfo().add_field('description', str)


class ClassificationSystem(_ACBaseType):
    """ Details of a classification system.

    Attributes:
        classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.
        name (:obj:`str`): The display name of the classification system.
        description (:obj:`str`): The description of the classification system.
        source (:obj:`str`): The source of the classification system (e.g. URL to a classification system standard).
        version (:obj:`str`): The version string of the classification system.
        date (:obj:`str`): A date in its string representation as defined in ISO 8601: YYYY-MM-DD.

    """
    __slots__ = ("classificationSystemId", "name", "description", "source", "version", "date", )

    def __init__(self, classificationSystemId: ClassificationSystemId, name: str, description: str, source: str, version: str, date: str):
        self.classificationSystemId: ClassificationSystemId = classificationSystemId
        self.name: str = name
        self.description: str = description
        self.source: str = source
        self.version: str = version
        self.date: str = date

ClassificationSystem.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)
ClassificationSystem.get_classinfo().add_field('name', str)
ClassificationSystem.get_classinfo().add_field('description', str)
ClassificationSystem.get_classinfo().add_field('source', str)
ClassificationSystem.get_classinfo().add_field('version', str)
ClassificationSystem.get_classinfo().add_field('date', str, matches(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"))


class UserDefinedPropertyUserId(_ACBaseType):
    """ An object which uniquely identifies a User-Defined Property by its name in human-readable form.

    Attributes:
        localizedName (:obj:`list` of :obj:`str`): List of the localized name parts: first element is the Group Name, second element is the Property Name of the Property.
        type (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("localizedName", "type", )

    def __init__(self, localizedName: List[str], type: str = "UserDefined"):
        self.localizedName: List[str] = localizedName
        self.type: str = type

UserDefinedPropertyUserId.get_classinfo().add_field('localizedName', List[str], min_items(2), max_items(2))
UserDefinedPropertyUserId.get_classinfo().add_field('type', str, value_set(['UserDefined']))


class BuiltInPropertyUserId(_ACBaseType):
    """ An object which uniquely identifies a Built-In Property by its name in a human-readable form.

    Attributes:
        nonLocalizedName (:obj:`str`): Non-localized name of the Built-In Property.
        type (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("nonLocalizedName", "type", )

    def __init__(self, nonLocalizedName: str, type: str = "BuiltIn"):
        self.nonLocalizedName: str = nonLocalizedName
        self.type: str = type

BuiltInPropertyUserId.get_classinfo().add_field('nonLocalizedName', str)
BuiltInPropertyUserId.get_classinfo().add_field('type', str, value_set(['BuiltIn']))


class PropertyUserId(_ACUnionType):
    """ An object which uniquely identifies a Property by its name in human-readable form. May represent a User-Defined or a Built-In Property.

    Attributes:
        type (:obj:`str`): None
        localizedName (:obj:`list` of :obj:`str`, optional): List of the localized name parts: first element is the Group Name, second element is the Property Name of the Property.
        nonLocalizedName (:obj:`str`, optional): Non-localized name of the Built-In Property.

    """
    __slots__ = ("type", "localizedName", "nonLocalizedName", )

    constructor  = _ConstructUnion(Union[UserDefinedPropertyUserId, BuiltInPropertyUserId])

    def __new__(cls, type: str, localizedName: Optional[List[str]] = None, nonLocalizedName: Optional[str] = None):
        return cls.constructor(type=type, localizedName=localizedName, nonLocalizedName=nonLocalizedName)

    def __init__(self, type: str, localizedName: Optional[List[str]] = None, nonLocalizedName: Optional[str] = None):
        self.type: str = type
        self.localizedName: Optional[List[str]] = localizedName
        self.nonLocalizedName: Optional[str] = nonLocalizedName


class PropertyId(_ACBaseType):
    """ The identifier of a property.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

PropertyId.get_classinfo().add_field('guid', UUID)


class PropertyIdArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        propertyId (:obj:`PropertyId`): The identifier of a property.

    """
    __slots__ = ("propertyId", )

    def __init__(self, propertyId: PropertyId):
        self.propertyId: PropertyId = propertyId

PropertyIdArrayItem.get_classinfo().add_field('propertyId', PropertyId)


class PropertyGroup(_ACBaseType):
    """ A property group.

    Attributes:
        name (:obj:`str`): The property group name.

    """
    __slots__ = ("name", )

    def __init__(self, name: str):
        self.name: str = name

PropertyGroup.get_classinfo().add_field('name', str)


class NormalNumberPropertyValue(_ACBaseType):
    """ A number property value containing a valid numeric value.

    Attributes:
        value (:obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: float, type: str = "number", status: str = "normal"):
        self.value: float = value
        self.type: str = type
        self.status: str = status

NormalNumberPropertyValue.get_classinfo().add_field('value', float)
NormalNumberPropertyValue.get_classinfo().add_field('type', str, value_set(['number']))
NormalNumberPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalIntegerPropertyValue(_ACBaseType):
    """ An integer property value containing a valid integer number.

    Attributes:
        value (:obj:`int`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: int, type: str = "integer", status: str = "normal"):
        self.value: int = value
        self.type: str = type
        self.status: str = status

NormalIntegerPropertyValue.get_classinfo().add_field('value', int)
NormalIntegerPropertyValue.get_classinfo().add_field('type', str, value_set(['integer']))
NormalIntegerPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalStringPropertyValue(_ACBaseType):
    """ A string property value containing a valid string.

    Attributes:
        value (:obj:`str`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: str, type: str = "string", status: str = "normal"):
        self.value: str = value
        self.type: str = type
        self.status: str = status

NormalStringPropertyValue.get_classinfo().add_field('value', str)
NormalStringPropertyValue.get_classinfo().add_field('type', str, value_set(['string']))
NormalStringPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalBooleanPropertyValue(_ACBaseType):
    """ A boolean property value containing a valid boolean value.

    Attributes:
        value (:obj:`bool`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: bool, type: str = "boolean", status: str = "normal"):
        self.value: bool = value
        self.type: str = type
        self.status: str = status

NormalBooleanPropertyValue.get_classinfo().add_field('value', bool)
NormalBooleanPropertyValue.get_classinfo().add_field('type', str, value_set(['boolean']))
NormalBooleanPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalLengthPropertyValue(_ACBaseType):
    """ A length property value containing a real length value. Value is measured in SI (meters).

    Attributes:
        value (:obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: float, type: str = "length", status: str = "normal"):
        self.value: float = value
        self.type: str = type
        self.status: str = status

NormalLengthPropertyValue.get_classinfo().add_field('value', float)
NormalLengthPropertyValue.get_classinfo().add_field('type', str, value_set(['length']))
NormalLengthPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalAreaPropertyValue(_ACBaseType):
    """ An area property value containing a real area. Value is measured in SI (square meters).

    Attributes:
        value (:obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: float, type: str = "area", status: str = "normal"):
        self.value: float = value
        self.type: str = type
        self.status: str = status

NormalAreaPropertyValue.get_classinfo().add_field('value', float)
NormalAreaPropertyValue.get_classinfo().add_field('type', str, value_set(['area']))
NormalAreaPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalVolumePropertyValue(_ACBaseType):
    """ A volume property value containing a real volume. Value is measured in SI (cubic meters).

    Attributes:
        value (:obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: float, type: str = "volume", status: str = "normal"):
        self.value: float = value
        self.type: str = type
        self.status: str = status

NormalVolumePropertyValue.get_classinfo().add_field('value', float)
NormalVolumePropertyValue.get_classinfo().add_field('type', str, value_set(['volume']))
NormalVolumePropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalAnglePropertyValue(_ACBaseType):
    """ An angle property value containing a real angle. Value is measured in SI (radians).

    Attributes:
        value (:obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: float, type: str = "angle", status: str = "normal"):
        self.value: float = value
        self.type: str = type
        self.status: str = status

NormalAnglePropertyValue.get_classinfo().add_field('value', float)
NormalAnglePropertyValue.get_classinfo().add_field('type', str, value_set(['angle']))
NormalAnglePropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalNumberListPropertyValue(_ACBaseType):
    """ A number list property value containing numbers in an array.

    Attributes:
        value (:obj:`list` of :obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[float], type: str = "numberList", status: str = "normal"):
        self.value: List[float] = value
        self.type: str = type
        self.status: str = status

NormalNumberListPropertyValue.get_classinfo().add_field('value', List[float])
NormalNumberListPropertyValue.get_classinfo().add_field('type', str, value_set(['numberList']))
NormalNumberListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalIntegerListPropertyValue(_ACBaseType):
    """ An integer list property value containing integers in an array.

    Attributes:
        value (:obj:`list` of :obj:`int`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[int], type: str = "integerList", status: str = "normal"):
        self.value: List[int] = value
        self.type: str = type
        self.status: str = status

NormalIntegerListPropertyValue.get_classinfo().add_field('value', List[int])
NormalIntegerListPropertyValue.get_classinfo().add_field('type', str, value_set(['integerList']))
NormalIntegerListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalStringListPropertyValue(_ACBaseType):
    """ A string list property value containing strings in an array.

    Attributes:
        value (:obj:`list` of :obj:`str`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[str], type: str = "stringList", status: str = "normal"):
        self.value: List[str] = value
        self.type: str = type
        self.status: str = status

NormalStringListPropertyValue.get_classinfo().add_field('value', List[str])
NormalStringListPropertyValue.get_classinfo().add_field('type', str, value_set(['stringList']))
NormalStringListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalBooleanListPropertyValue(_ACBaseType):
    """ A boolean list property value containing boolean values in an array.

    Attributes:
        value (:obj:`list` of :obj:`bool`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[bool], type: str = "booleanList", status: str = "normal"):
        self.value: List[bool] = value
        self.type: str = type
        self.status: str = status

NormalBooleanListPropertyValue.get_classinfo().add_field('value', List[bool])
NormalBooleanListPropertyValue.get_classinfo().add_field('type', str, value_set(['booleanList']))
NormalBooleanListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalLengthListPropertyValue(_ACBaseType):
    """ A length list property value containing length values in an array. Values are measured in SI (meters).

    Attributes:
        value (:obj:`list` of :obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[float], type: str = "lengthList", status: str = "normal"):
        self.value: List[float] = value
        self.type: str = type
        self.status: str = status

NormalLengthListPropertyValue.get_classinfo().add_field('value', List[float])
NormalLengthListPropertyValue.get_classinfo().add_field('type', str, value_set(['lengthList']))
NormalLengthListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalAreaListPropertyValue(_ACBaseType):
    """ A area list property value containing areas in an array. Values are measured in SI (square meters).

    Attributes:
        value (:obj:`list` of :obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[float], type: str = "areaList", status: str = "normal"):
        self.value: List[float] = value
        self.type: str = type
        self.status: str = status

NormalAreaListPropertyValue.get_classinfo().add_field('value', List[float])
NormalAreaListPropertyValue.get_classinfo().add_field('type', str, value_set(['areaList']))
NormalAreaListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalVolumeListPropertyValue(_ACBaseType):
    """ A volume list property value containing volumes in an array. Values are measured in SI (cubic meters).

    Attributes:
        value (:obj:`list` of :obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[float], type: str = "volumeList", status: str = "normal"):
        self.value: List[float] = value
        self.type: str = type
        self.status: str = status

NormalVolumeListPropertyValue.get_classinfo().add_field('value', List[float])
NormalVolumeListPropertyValue.get_classinfo().add_field('type', str, value_set(['volumeList']))
NormalVolumeListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalAngleListPropertyValue(_ACBaseType):
    """ A angle list property value containing angles in an array. Values are measured in SI (radians).

    Attributes:
        value (:obj:`list` of :obj:`float`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[float], type: str = "angleList", status: str = "normal"):
        self.value: List[float] = value
        self.type: str = type
        self.status: str = status

NormalAngleListPropertyValue.get_classinfo().add_field('value', List[float])
NormalAngleListPropertyValue.get_classinfo().add_field('type', str, value_set(['angleList']))
NormalAngleListPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class UserUndefinedPropertyValue(_ACBaseType):
    """ A userUndefined value means that there is no actual number/string/etc. value, but the user deliberately set an Undefined value: this is a valid value, too.

    Attributes:
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("type", "status", )

    def __init__(self, type: str, status: str = "userUndefined"):
        self.type: str = type
        self.status: str = status

UserUndefinedPropertyValue.get_classinfo().add_field('type', str, value_set(['number', 'integer', 'string', 'boolean', 'length', 'area', 'volume', 'angle', 'numberList', 'integerList', 'stringList', 'booleanList', 'lengthList', 'areaList', 'volumeList', 'angleList', 'singleEnum', 'multiEnum']))
UserUndefinedPropertyValue.get_classinfo().add_field('status', str, value_set(['userUndefined']))


class NotAvailablePropertyValue(_ACBaseType):
    """ A notAvailable value means that the property is not available for the property owner (and therefore it has no property value for it).

    Attributes:
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("type", "status", )

    def __init__(self, type: str, status: str = "notAvailable"):
        self.type: str = type
        self.status: str = status

NotAvailablePropertyValue.get_classinfo().add_field('type', str, value_set(['number', 'integer', 'string', 'boolean', 'length', 'area', 'volume', 'angle', 'numberList', 'integerList', 'stringList', 'booleanList', 'lengthList', 'areaList', 'volumeList', 'angleList', 'singleEnum', 'multiEnum']))
NotAvailablePropertyValue.get_classinfo().add_field('status', str, value_set(['notAvailable']))


class NotEvaluatedPropertyValue(_ACBaseType):
    """ A notEvaluated value means that the property could not be evaluated for the property owner for some reason.

    Attributes:
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("type", "status", )

    def __init__(self, type: str, status: str = "notEvaluated"):
        self.type: str = type
        self.status: str = status

NotEvaluatedPropertyValue.get_classinfo().add_field('type', str, value_set(['number', 'integer', 'string', 'boolean', 'length', 'area', 'volume', 'angle', 'numberList', 'integerList', 'stringList', 'booleanList', 'lengthList', 'areaList', 'volumeList', 'angleList', 'singleEnum', 'multiEnum']))
NotEvaluatedPropertyValue.get_classinfo().add_field('status', str, value_set(['notEvaluated']))


class DisplayValueEnumId(_ACBaseType):
    """ An enumeration value identifier using the displayed value.

    Attributes:
        displayValue (:obj:`str`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("displayValue", "type", )

    def __init__(self, displayValue: str, type: str = "displayValue"):
        self.displayValue: str = displayValue
        self.type: str = type

DisplayValueEnumId.get_classinfo().add_field('displayValue', str)
DisplayValueEnumId.get_classinfo().add_field('type', str, value_set(['displayValue']))


EnumValueId = DisplayValueEnumId
""" The identifier of a property enumeration value.
"""


class PossibleEnumValue(_ACBaseType):
    """ Description of an enumeration value.

    Attributes:
        enumValueId (:obj:`EnumValueId`): The identifier of a property enumeration value.
        displayValue (:obj:`str`): Displayed value of the enumeration.

    """
    __slots__ = ("enumValueId", "displayValue", )

    def __init__(self, enumValueId: EnumValueId, displayValue: str):
        self.enumValueId: EnumValueId = enumValueId
        self.displayValue: str = displayValue

PossibleEnumValue.get_classinfo().add_field('enumValueId', EnumValueId)
PossibleEnumValue.get_classinfo().add_field('displayValue', str)


class PossibleEnumValuesArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        enumValue (:obj:`PossibleEnumValue`): Description of an enumeration value.

    """
    __slots__ = ("enumValue", )

    def __init__(self, enumValue: PossibleEnumValue):
        self.enumValue: PossibleEnumValue = enumValue

PossibleEnumValuesArrayItem.get_classinfo().add_field('enumValue', PossibleEnumValue)


class Error(_ACBaseType):
    """ Error details.

    Attributes:
        code (:obj:`int`): The error code.
        message (:obj:`str`): The error message.

    """
    __slots__ = ("code", "message", )

    def __init__(self, code: int, message: str):
        self.code: int = code
        self.message: str = message

Error.get_classinfo().add_field('code', int)
Error.get_classinfo().add_field('message', str)


class ErrorItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        error (:obj:`Error`): Error details.

    """
    __slots__ = ("error", )

    def __init__(self, error: Error):
        self.error: Error = error

ErrorItem.get_classinfo().add_field('error', Error)


class SuccessfulExecutionResult(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        success (:obj:`bool`): EMPTY STRING

    """
    __slots__ = ("success", )

    def __init__(self, success: bool):
        self.success: bool = success

SuccessfulExecutionResult.get_classinfo().add_field('success', bool)


class FailedExecutionResult(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        success (:obj:`bool`): EMPTY STRING
        error (:obj:`Error`): Error details.

    """
    __slots__ = ("success", "error", )

    def __init__(self, success: bool, error: Error):
        self.success: bool = success
        self.error: Error = error

FailedExecutionResult.get_classinfo().add_field('success', bool)
FailedExecutionResult.get_classinfo().add_field('error', Error)


class ExecutionResult(_ACUnionType):
    """ The result of the execution for one case.

    Attributes:
        success (:obj:`bool`): None
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("success", "error", )

    constructor  = _ConstructUnion(Union[SuccessfulExecutionResult, FailedExecutionResult])

    def __new__(cls, success: bool, error: Optional[Error] = None):
        return cls.constructor(success=success, error=error)

    def __init__(self, success: bool, error: Optional[Error] = None):
        self.success: bool = success
        self.error: Optional[Error] = error


class ElementId(_ACBaseType):
    """ The identifier of an element.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

ElementId.get_classinfo().add_field('guid', UUID)


class ElementIdArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        elementId (:obj:`ElementId`): The identifier of an element.

    """
    __slots__ = ("elementId", )

    def __init__(self, elementId: ElementId):
        self.elementId: ElementId = elementId

ElementIdArrayItem.get_classinfo().add_field('elementId', ElementId)


class ElementsWrapper(_ACBaseType):
    """ List of elements.

    Attributes:
        elements (:obj:`list` of :obj:`ElementIdArrayItem`): List of the elements.

    """
    __slots__ = ("elements", )

    def __init__(self, elements: List[ElementIdArrayItem]):
        self.elements: List[ElementIdArrayItem] = elements

ElementsWrapper.get_classinfo().add_field('elements', List[ElementIdArrayItem])


class ElementsOrError(_ACUnionType):
    """ List of elements or error.

    Attributes:
        elements (:obj:`list` of :obj:`ElementIdArrayItem`, optional): List of the elements.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("elements", "error", )

    constructor  = _ConstructUnion(Union[ElementsWrapper, ErrorItem])

    def __new__(cls, elements: Optional[List[ElementIdArrayItem]] = None, error: Optional[Error] = None):
        return cls.constructor(elements=elements, error=error)

    def __init__(self, elements: Optional[List[ElementIdArrayItem]] = None, error: Optional[Error] = None):
        self.elements: Optional[List[ElementIdArrayItem]] = elements
        self.error: Optional[Error] = error


class NavigatorItemId(_ACBaseType):
    """ The identifier of a navigator item.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

NavigatorItemId.get_classinfo().add_field('guid', UUID)


class PublisherSetId(_ACBaseType):
    """ The identifier of a publisher set.

    Attributes:
        name (:obj:`str`): Name of the publisher set.
        type (:obj:`str`): Type of the navigator item tree.

    """
    __slots__ = ("name", "type", )

    def __init__(self, name: str, type: str = "PublisherSets"):
        self.name: str = name
        self.type: str = type

PublisherSetId.get_classinfo().add_field('name', str)
PublisherSetId.get_classinfo().add_field('type', str, value_set(['PublisherSets']))


class OtherNavigatorTreeId(_ACBaseType):
    """ The identifier of a navigator item tree.

    Attributes:
        type (:obj:`str`): Type of the navigator item tree.

    """
    __slots__ = ("type", )

    def __init__(self, type: str):
        self.type: str = type

OtherNavigatorTreeId.get_classinfo().add_field('type', str, value_set(['ProjectMap', 'ViewMap', 'MyViewMap', 'LayoutBook']))


class FolderParameters(_ACBaseType):
    """ The parameters of a folder.

    Attributes:
        name (:obj:`str`): The name of the folder to create.

    """
    __slots__ = ("name", )

    def __init__(self, name: str):
        self.name: str = name

FolderParameters.get_classinfo().add_field('name', str)


class NavigatorTreeId(_ACUnionType):
    """ The identifier of a navigator item tree.

    Attributes:
        type (:obj:`str`): Type of the navigator item tree.
        name (:obj:`str`, optional): Name of the publisher set.

    """
    __slots__ = ("type", "name", )

    constructor  = _ConstructUnion(Union[PublisherSetId, OtherNavigatorTreeId])

    def __new__(cls, type: str, name: Optional[str] = None):
        return cls.constructor(type=type, name=name)

    def __init__(self, type: str, name: Optional[str] = None):
        self.type: str = type
        self.name: Optional[str] = name


class BoundingBox2D(_ACBaseType):
    """ 2D bounding box of an element.

    Attributes:
        xMin (:obj:`float`): Minimum X value of bounding box.
        yMin (:obj:`float`): Minimum Y value of bounding box.
        xMax (:obj:`float`): Maximum X value of bounding box.
        yMax (:obj:`float`): Maximum Y value of bounding box.

    """
    __slots__ = ("xMin", "yMin", "xMax", "yMax", )

    def __init__(self, xMin: float, yMin: float, xMax: float, yMax: float):
        self.xMin: float = xMin
        self.yMin: float = yMin
        self.xMax: float = xMax
        self.yMax: float = yMax

BoundingBox2D.get_classinfo().add_field('xMin', float)
BoundingBox2D.get_classinfo().add_field('yMin', float)
BoundingBox2D.get_classinfo().add_field('xMax', float)
BoundingBox2D.get_classinfo().add_field('yMax', float)


class BoundingBox3D(_ACBaseType):
    """ 3D bounding box of an element.

    Attributes:
        xMin (:obj:`float`): Minimum X value of bounding box.
        yMin (:obj:`float`): Minimum Y value of bounding box.
        zMin (:obj:`float`): Minimum Z value of bounding box.
        xMax (:obj:`float`): Maximum X value of bounding box.
        yMax (:obj:`float`): Maximum Y value of bounding box.
        zMax (:obj:`float`): Maximum Z value of bounding box.

    """
    __slots__ = ("xMin", "yMin", "zMin", "xMax", "yMax", "zMax", )

    def __init__(self, xMin: float, yMin: float, zMin: float, xMax: float, yMax: float, zMax: float):
        self.xMin: float = xMin
        self.yMin: float = yMin
        self.zMin: float = zMin
        self.xMax: float = xMax
        self.yMax: float = yMax
        self.zMax: float = zMax

BoundingBox3D.get_classinfo().add_field('xMin', float)
BoundingBox3D.get_classinfo().add_field('yMin', float)
BoundingBox3D.get_classinfo().add_field('zMin', float)
BoundingBox3D.get_classinfo().add_field('xMax', float)
BoundingBox3D.get_classinfo().add_field('yMax', float)
BoundingBox3D.get_classinfo().add_field('zMax', float)


class Subset(_ACBaseType):
    """ Provides a way to assign IDs to the layouts contained in the subset.

    Attributes:
        name (:obj:`str`): Defines the name for the layout subset.
        includeToIDSequence (:obj:`bool`): Indicates whether this subset is included in or excluded from automatic ID assignment.
        customNumbering (:obj:`bool`): Defines whether the IDs are generated automatically or use a custom numbering.
        continueNumbering (:obj:`bool`): Continue using the ID assignment of upper levels. Layouts within this subset are going to be assigned IDs as if they were not within this subset, but part of the level above. In this case you are only using the Subset as a logical grouping which has no effect on IDs.
        useUpperPrefix (:obj:`bool`): Use the prefix and ID of upper levels. Layouts in this subset will be assigned IDs based on the previous layout in the layout book structure.
        addOwnPrefix (:obj:`bool`): Adds own prefix to the subset.
        customNumber (:obj:`str`): Specifies the custom subset ID.
        autoNumber (:obj:`str`): Specifies the automatic subset ID.
        numberingStyle (:obj:`str`): List of the supported numbering styles.
        startAt (:obj:`int`): Specifies a number from which the numbering starts.
        ownPrefix (:obj:`str`): Defines a custom prefix for the subset.

    """
    __slots__ = ("name", "includeToIDSequence", "customNumbering", "continueNumbering", "useUpperPrefix", "addOwnPrefix", "customNumber", "autoNumber", "numberingStyle", "startAt", "ownPrefix", )

    def __init__(self, name: str, includeToIDSequence: bool, customNumbering: bool, continueNumbering: bool, useUpperPrefix: bool, addOwnPrefix: bool, customNumber: str, autoNumber: str, numberingStyle: str, startAt: int, ownPrefix: str):
        self.name: str = name
        self.includeToIDSequence: bool = includeToIDSequence
        self.customNumbering: bool = customNumbering
        self.continueNumbering: bool = continueNumbering
        self.useUpperPrefix: bool = useUpperPrefix
        self.addOwnPrefix: bool = addOwnPrefix
        self.customNumber: str = customNumber
        self.autoNumber: str = autoNumber
        self.numberingStyle: str = numberingStyle
        self.startAt: int = startAt
        self.ownPrefix: str = ownPrefix

Subset.get_classinfo().add_field('name', str, min_length(1))
Subset.get_classinfo().add_field('includeToIDSequence', bool)
Subset.get_classinfo().add_field('customNumbering', bool)
Subset.get_classinfo().add_field('continueNumbering', bool)
Subset.get_classinfo().add_field('useUpperPrefix', bool)
Subset.get_classinfo().add_field('addOwnPrefix', bool)
Subset.get_classinfo().add_field('customNumber', str)
Subset.get_classinfo().add_field('autoNumber', str)
Subset.get_classinfo().add_field('numberingStyle', str, value_set(['Undefined', 'abc', 'ABC', '1', '01', '001', '0001', 'noID']))
Subset.get_classinfo().add_field('startAt', int)
Subset.get_classinfo().add_field('ownPrefix', str)


class LayoutParameters(_ACBaseType):
    """ The parameters of the layout.

    Attributes:
        horizontalSize (:obj:`float`): Horizontal size of the layout in millimeters.
        verticalSize (:obj:`float`): Vertical size of the layout in millimeters.
        leftMargin (:obj:`float`): Layout margin from the left side of the paper.
        topMargin (:obj:`float`): Layout margin from the top side of the paper.
        rightMargin (:obj:`float`): Layout margin from the right side of the paper.
        bottomMargin (:obj:`float`): Layout margin from the bottom side of the paper.
        customLayoutNumber (:obj:`str`): Specifies the custom ID.
        customLayoutNumbering (:obj:`bool`): Defines whether a unique ID is used for the current layout or not.
        doNotIncludeInNumbering (:obj:`bool`): Indicates whether this layout is included in or excluded from automatic ID assignment.
        displayMasterLayoutBelow (:obj:`bool`): Display the master layout above or below the layout.
        layoutPageNumber (:obj:`int`): Page number of layout when this layout contains multi-page drawings.
        actPageIndex (:obj:`int`): The actual index of layout inside the multi-page layout.
        currentRevisionId (:obj:`str`): ID of the current document revision of the layout.
        currentFinalRevisionId (:obj:`str`): ID with optional suffix of the current document revision of the layout.
        hasIssuedRevision (:obj:`bool`): One or more issued document revisions have already been created for the layout.
        hasActualRevision (:obj:`bool`): An open document revision exists for the layout.

    """
    __slots__ = ("horizontalSize", "verticalSize", "leftMargin", "topMargin", "rightMargin", "bottomMargin", "customLayoutNumber", "customLayoutNumbering", "doNotIncludeInNumbering", "displayMasterLayoutBelow", "layoutPageNumber", "actPageIndex", "currentRevisionId", "currentFinalRevisionId", "hasIssuedRevision", "hasActualRevision", )

    def __init__(self, horizontalSize: float, verticalSize: float, leftMargin: float, topMargin: float, rightMargin: float, bottomMargin: float, customLayoutNumber: str, customLayoutNumbering: bool, doNotIncludeInNumbering: bool, displayMasterLayoutBelow: bool, layoutPageNumber: int, actPageIndex: int, currentRevisionId: str, currentFinalRevisionId: str, hasIssuedRevision: bool, hasActualRevision: bool):
        self.horizontalSize: float = horizontalSize
        self.verticalSize: float = verticalSize
        self.leftMargin: float = leftMargin
        self.topMargin: float = topMargin
        self.rightMargin: float = rightMargin
        self.bottomMargin: float = bottomMargin
        self.customLayoutNumber: str = customLayoutNumber
        self.customLayoutNumbering: bool = customLayoutNumbering
        self.doNotIncludeInNumbering: bool = doNotIncludeInNumbering
        self.displayMasterLayoutBelow: bool = displayMasterLayoutBelow
        self.layoutPageNumber: int = layoutPageNumber
        self.actPageIndex: int = actPageIndex
        self.currentRevisionId: str = currentRevisionId
        self.currentFinalRevisionId: str = currentFinalRevisionId
        self.hasIssuedRevision: bool = hasIssuedRevision
        self.hasActualRevision: bool = hasActualRevision

LayoutParameters.get_classinfo().add_field('horizontalSize', float)
LayoutParameters.get_classinfo().add_field('verticalSize', float)
LayoutParameters.get_classinfo().add_field('leftMargin', float)
LayoutParameters.get_classinfo().add_field('topMargin', float)
LayoutParameters.get_classinfo().add_field('rightMargin', float)
LayoutParameters.get_classinfo().add_field('bottomMargin', float)
LayoutParameters.get_classinfo().add_field('customLayoutNumber', str)
LayoutParameters.get_classinfo().add_field('customLayoutNumbering', bool)
LayoutParameters.get_classinfo().add_field('doNotIncludeInNumbering', bool)
LayoutParameters.get_classinfo().add_field('displayMasterLayoutBelow', bool)
LayoutParameters.get_classinfo().add_field('layoutPageNumber', int)
LayoutParameters.get_classinfo().add_field('actPageIndex', int)
LayoutParameters.get_classinfo().add_field('currentRevisionId', str)
LayoutParameters.get_classinfo().add_field('currentFinalRevisionId', str)
LayoutParameters.get_classinfo().add_field('hasIssuedRevision', bool)
LayoutParameters.get_classinfo().add_field('hasActualRevision', bool)


class ClassificationIdWrapper(_ACBaseType):
    """ 

    Attributes:
        classificationId (:obj:`ClassificationId`): The element classification identifier.

    """
    __slots__ = ("classificationId", )

    def __init__(self, classificationId: ClassificationId):
        self.classificationId: ClassificationId = classificationId

ClassificationIdWrapper.get_classinfo().add_field('classificationId', ClassificationId)


class ClassificationItemDetailsWrapper(_ACBaseType):
    """ 

    Attributes:
        classificationItem (:obj:`ClassificationItemDetails`): Details of a classification item.

    """
    __slots__ = ("classificationItem", )

    def __init__(self, classificationItem: ClassificationItemDetails):
        self.classificationItem: ClassificationItemDetails = classificationItem

ClassificationItemDetailsWrapper.get_classinfo().add_field('classificationItem', ClassificationItemDetails)


class EnumValueIdWrapper(_ACBaseType):
    """ 

    Attributes:
        enumValueId (:obj:`EnumValueId`): The identifier of a property enumeration value.

    """
    __slots__ = ("enumValueId", )

    def __init__(self, enumValueId: EnumValueId):
        self.enumValueId: EnumValueId = enumValueId

EnumValueIdWrapper.get_classinfo().add_field('enumValueId', EnumValueId)


class NavigatorItemIdWrapper(_ACBaseType):
    """ 

    Attributes:
        navigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

    """
    __slots__ = ("navigatorItemId", )

    def __init__(self, navigatorItemId: NavigatorItemId):
        self.navigatorItemId: NavigatorItemId = navigatorItemId

NavigatorItemIdWrapper.get_classinfo().add_field('navigatorItemId', NavigatorItemId)


class BoundingBox2DWrapper(_ACBaseType):
    """ 

    Attributes:
        boundingBox2D (:obj:`BoundingBox2D`): 2D bounding box of an element.

    """
    __slots__ = ("boundingBox2D", )

    def __init__(self, boundingBox2D: BoundingBox2D):
        self.boundingBox2D: BoundingBox2D = boundingBox2D

BoundingBox2DWrapper.get_classinfo().add_field('boundingBox2D', BoundingBox2D)


class BoundingBox3DWrapper(_ACBaseType):
    """ 

    Attributes:
        boundingBox3D (:obj:`BoundingBox3D`): 3D bounding box of an element.

    """
    __slots__ = ("boundingBox3D", )

    def __init__(self, boundingBox3D: BoundingBox3D):
        self.boundingBox3D: BoundingBox3D = boundingBox3D

BoundingBox3DWrapper.get_classinfo().add_field('boundingBox3D', BoundingBox3D)


class ClassificationIdOrError(_ACUnionType):
    """ EMPTY STRING

    Attributes:
        classificationId (:obj:`ClassificationId`, optional): The element classification identifier.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("classificationId", "error", )

    constructor  = _ConstructUnion(Union[ClassificationIdWrapper, ErrorItem])

    def __new__(cls, classificationId: Optional[ClassificationId] = None, error: Optional[Error] = None):
        return cls.constructor(classificationId=classificationId, error=error)

    def __init__(self, classificationId: Optional[ClassificationId] = None, error: Optional[Error] = None):
        self.classificationId: Optional[ClassificationId] = classificationId
        self.error: Optional[Error] = error


class ElementClassification(_ACBaseType):
    """ Element classification.

    Attributes:
        elementId (:obj:`ElementId`): The identifier of an element.
        classificationId (:obj:`ClassificationId`): The element classification identifier.

    """
    __slots__ = ("elementId", "classificationId", )

    def __init__(self, elementId: ElementId, classificationId: ClassificationId):
        self.elementId: ElementId = elementId
        self.classificationId: ClassificationId = classificationId

ElementClassification.get_classinfo().add_field('elementId', ElementId)
ElementClassification.get_classinfo().add_field('classificationId', ClassificationId)


class ClassificationItemOrError(_ACUnionType):
    """ EMPTY STRING

    Attributes:
        classificationItem (:obj:`ClassificationItemDetails`, optional): Details of a classification item.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("classificationItem", "error", )

    constructor  = _ConstructUnion(Union[ClassificationItemDetailsWrapper, ErrorItem])

    def __new__(cls, classificationItem: Optional[ClassificationItemDetails] = None, error: Optional[Error] = None):
        return cls.constructor(classificationItem=classificationItem, error=error)

    def __init__(self, classificationItem: Optional[ClassificationItemDetails] = None, error: Optional[Error] = None):
        self.classificationItem: Optional[ClassificationItemDetails] = classificationItem
        self.error: Optional[Error] = error


class PropertyIdOrError(_ACUnionType):
    """ A property identifier or error.

    Attributes:
        propertyId (:obj:`PropertyId`, optional): The identifier of a property.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("propertyId", "error", )

    constructor  = _ConstructUnion(Union[PropertyIdArrayItem, ErrorItem])

    def __new__(cls, propertyId: Optional[PropertyId] = None, error: Optional[Error] = None):
        return cls.constructor(propertyId=propertyId, error=error)

    def __init__(self, propertyId: Optional[PropertyId] = None, error: Optional[Error] = None):
        self.propertyId: Optional[PropertyId] = propertyId
        self.error: Optional[Error] = error


class PropertyDefinition(_ACBaseType):
    """ A property definition.

    Attributes:
        group (:obj:`PropertyGroup`): A property group.
        name (:obj:`str`): The localized name of the property.
        description (:obj:`str`): The description of the property.
        possibleEnumValues (:obj:`list` of :obj:`PossibleEnumValuesArrayItem`, optional): List of enumeration values.

    """
    __slots__ = ("group", "name", "description", "possibleEnumValues", )

    def __init__(self, group: PropertyGroup, name: str, description: str, possibleEnumValues: Optional[List[PossibleEnumValuesArrayItem]] = None):
        self.group: PropertyGroup = group
        self.name: str = name
        self.description: str = description
        self.possibleEnumValues: Optional[List[PossibleEnumValuesArrayItem]] = possibleEnumValues

PropertyDefinition.get_classinfo().add_field('group', PropertyGroup)
PropertyDefinition.get_classinfo().add_field('name', str)
PropertyDefinition.get_classinfo().add_field('description', str)
PropertyDefinition.get_classinfo().add_field('possibleEnumValues', Optional[List[PossibleEnumValuesArrayItem]])


class NormalSingleEnumPropertyValue(_ACBaseType):
    """ A single enumeration property value containing the ID of the selected enum value.

    Attributes:
        value (:obj:`EnumValueId`): The identifier of a property enumeration value.
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: EnumValueId, type: str = "singleEnum", status: str = "normal"):
        self.value: EnumValueId = value
        self.type: str = type
        self.status: str = status

NormalSingleEnumPropertyValue.get_classinfo().add_field('value', EnumValueId)
NormalSingleEnumPropertyValue.get_classinfo().add_field('type', str, value_set(['singleEnum']))
NormalSingleEnumPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class NormalMultiEnumPropertyValue(_ACBaseType):
    """ A multiple choice enumeration property value containing the IDs of the selected enum values in an array.

    Attributes:
        value (:obj:`list` of :obj:`EnumValueIdWrapper`): List of enumeration identifiers.
        type (:obj:`str`): EMPTY STRING
        status (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("value", "type", "status", )

    def __init__(self, value: List[EnumValueIdWrapper], type: str = "multiEnum", status: str = "normal"):
        self.value: List[EnumValueIdWrapper] = value
        self.type: str = type
        self.status: str = status

NormalMultiEnumPropertyValue.get_classinfo().add_field('value', List[EnumValueIdWrapper])
NormalMultiEnumPropertyValue.get_classinfo().add_field('type', str, value_set(['multiEnum']))
NormalMultiEnumPropertyValue.get_classinfo().add_field('status', str, value_set(['normal']))


class BoundingBox2DOrError(_ACUnionType):
    """ A 2D bounding box or error.

    Attributes:
        boundingBox2D (:obj:`BoundingBox2D`, optional): 2D bounding box of an element.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("boundingBox2D", "error", )

    constructor  = _ConstructUnion(Union[BoundingBox2DWrapper, ErrorItem])

    def __new__(cls, boundingBox2D: Optional[BoundingBox2D] = None, error: Optional[Error] = None):
        return cls.constructor(boundingBox2D=boundingBox2D, error=error)

    def __init__(self, boundingBox2D: Optional[BoundingBox2D] = None, error: Optional[Error] = None):
        self.boundingBox2D: Optional[BoundingBox2D] = boundingBox2D
        self.error: Optional[Error] = error


class BoundingBox3DOrError(_ACUnionType):
    """ A 3D bounding box or error.

    Attributes:
        boundingBox3D (:obj:`BoundingBox3D`, optional): 3D bounding box of an element.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("boundingBox3D", "error", )

    constructor  = _ConstructUnion(Union[BoundingBox3DWrapper, ErrorItem])

    def __new__(cls, boundingBox3D: Optional[BoundingBox3D] = None, error: Optional[Error] = None):
        return cls.constructor(boundingBox3D=boundingBox3D, error=error)

    def __init__(self, boundingBox3D: Optional[BoundingBox3D] = None, error: Optional[Error] = None):
        self.boundingBox3D: Optional[BoundingBox3D] = boundingBox3D
        self.error: Optional[Error] = error


class ClassificationIdsOrErrorsWrapper(_ACBaseType):
    """ 

    Attributes:
        classificationIds (:obj:`list` of :obj:`ClassificationIdOrError`): The list of element classification identifiers or errors.

    """
    __slots__ = ("classificationIds", )

    def __init__(self, classificationIds: List[ClassificationIdOrError]):
        self.classificationIds: List[ClassificationIdOrError] = classificationIds

ClassificationIdsOrErrorsWrapper.get_classinfo().add_field('classificationIds', List[ClassificationIdOrError])


class PropertyDefinitionWrapper(_ACBaseType):
    """ 

    Attributes:
        propertyDefinition (:obj:`PropertyDefinition`): A property definition.

    """
    __slots__ = ("propertyDefinition", )

    def __init__(self, propertyDefinition: PropertyDefinition):
        self.propertyDefinition: PropertyDefinition = propertyDefinition

PropertyDefinitionWrapper.get_classinfo().add_field('propertyDefinition', PropertyDefinition)


class ElementClassificationOrError(_ACUnionType):
    """ Element classification identifiers or error.

    Attributes:
        classificationIds (:obj:`list` of :obj:`ClassificationIdOrError`, optional): The list of element classification identifiers or errors.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("classificationIds", "error", )

    constructor  = _ConstructUnion(Union[ClassificationIdsOrErrorsWrapper, ErrorItem])

    def __new__(cls, classificationIds: Optional[List[ClassificationIdOrError]] = None, error: Optional[Error] = None):
        return cls.constructor(classificationIds=classificationIds, error=error)

    def __init__(self, classificationIds: Optional[List[ClassificationIdOrError]] = None, error: Optional[Error] = None):
        self.classificationIds: Optional[List[ClassificationIdOrError]] = classificationIds
        self.error: Optional[Error] = error


class PropertyDefinitionOrError(_ACUnionType):
    """ A property definition or error.

    Attributes:
        propertyDefinition (:obj:`PropertyDefinition`, optional): A property definition.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("propertyDefinition", "error", )

    constructor  = _ConstructUnion(Union[PropertyDefinitionWrapper, ErrorItem])

    def __new__(cls, propertyDefinition: Optional[PropertyDefinition] = None, error: Optional[Error] = None):
        return cls.constructor(propertyDefinition=propertyDefinition, error=error)

    def __init__(self, propertyDefinition: Optional[PropertyDefinition] = None, error: Optional[Error] = None):
        self.propertyDefinition: Optional[PropertyDefinition] = propertyDefinition
        self.error: Optional[Error] = error


class ClassificationItemInTree_: pass
class ClassificationItemArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        classificationItem (:obj:`ClassificationItemInTree_`): Details of a classification item.

    """
    __slots__ = ("classificationItem", )

    def __init__(self, classificationItem: ClassificationItemInTree_):
        self.classificationItem: ClassificationItemInTree_ = classificationItem


class ClassificationItemInTree(_ACBaseType):
    """ Details of a classification item.

    Attributes:
        classificationItemId (:obj:`ClassificationItemId`): The identifier of a classification item.
        id (:obj:`str`): The user specified unique identifier of the classification item.
        name (:obj:`str`): The display name of the classification item.
        description (:obj:`str`): The description of the classification item.
        children (:obj:`list` of :obj:`ClassificationItemArrayItem`, optional): The list of classification items.

    """
    __slots__ = ("classificationItemId", "id", "name", "description", "children", )

    def __init__(self, classificationItemId: ClassificationItemId, id: str, name: str, description: str, children: Optional[List[ClassificationItemArrayItem]] = None):
        self.classificationItemId: ClassificationItemId = classificationItemId
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.children: Optional[List[ClassificationItemArrayItem]] = children

ClassificationItemInTree.get_classinfo().add_field('classificationItemId', ClassificationItemId)
ClassificationItemInTree.get_classinfo().add_field('id', str)
ClassificationItemInTree.get_classinfo().add_field('name', str)
ClassificationItemInTree.get_classinfo().add_field('description', str)
ClassificationItemInTree.get_classinfo().add_field('children', Optional[List[ClassificationItemArrayItem]])

ClassificationItemInTree_ = ClassificationItemInTree
ClassificationItemArrayItem.get_classinfo().add_field('classificationItem', ClassificationItemInTree)


class NormalOrUserUndefinedPropertyValue(_ACUnionType):
    """ A normal or a userUndefined property value.

    Attributes:
        type (:obj:`str`): None
        status (:obj:`str`): None
        value (:obj:`float`, :obj:`int`, :obj:`str`, :obj:`bool`, :obj:`list` of :obj:`float`, :obj:`list` of :obj:`int`, :obj:`list` of :obj:`str`, :obj:`list` of :obj:`bool`, :obj:`EnumValueId`, :obj:`list` of :obj:`EnumValueIdWrapper`): None; The identifier of a property enumeration value.; List of enumeration identifiers.

    """
    __slots__ = ("type", "status", "value", )

    constructor  = _ConstructUnion(Union[NormalNumberPropertyValue, NormalIntegerPropertyValue, NormalStringPropertyValue, NormalBooleanPropertyValue, NormalLengthPropertyValue, NormalAreaPropertyValue, NormalVolumePropertyValue, NormalAnglePropertyValue, NormalNumberListPropertyValue, NormalIntegerListPropertyValue, NormalStringListPropertyValue, NormalBooleanListPropertyValue, NormalLengthListPropertyValue, NormalAreaListPropertyValue, NormalVolumeListPropertyValue, NormalAngleListPropertyValue, NormalSingleEnumPropertyValue, NormalMultiEnumPropertyValue, UserUndefinedPropertyValue])

    def __new__(cls, type: str, status: str, value: Union[float, int, str, bool, List[float], List[int], List[str], List[bool], EnumValueId, List[EnumValueIdWrapper], None] = None):
        return cls.constructor(type=type, status=status, value=value)

    def __init__(self, type: str, status: str, value: Union[float, int, str, bool, List[float], List[int], List[str], List[bool], EnumValueId, List[EnumValueIdWrapper], None] = None):
        self.type: str = type
        self.status: str = status
        self.value: Union[float, int, str, bool, List[float], List[int], List[str], List[bool], EnumValueId, List[EnumValueIdWrapper], None] = value


class ElementPropertyValue(_ACBaseType):
    """ A property value with the identifier of the property and the owner element.

    Attributes:
        elementId (:obj:`ElementId`): The identifier of an element.
        propertyId (:obj:`PropertyId`): The identifier of a property.
        propertyValue (:obj:`NormalOrUserUndefinedPropertyValue`): A normal or a userUndefined property value.

    """
    __slots__ = ("elementId", "propertyId", "propertyValue", )

    def __init__(self, elementId: ElementId, propertyId: PropertyId, propertyValue: NormalOrUserUndefinedPropertyValue):
        self.elementId: ElementId = elementId
        self.propertyId: PropertyId = propertyId
        self.propertyValue: NormalOrUserUndefinedPropertyValue = propertyValue

ElementPropertyValue.get_classinfo().add_field('elementId', ElementId)
ElementPropertyValue.get_classinfo().add_field('propertyId', PropertyId)
ElementPropertyValue.get_classinfo().add_field('propertyValue', NormalOrUserUndefinedPropertyValue)


class PropertyValue(_ACUnionType):
    """ A normal, userUndefined, notAvailable or notEvaluated property value.

    Attributes:
        type (:obj:`str`): None
        status (:obj:`str`): None
        value (:obj:`float`, :obj:`int`, :obj:`str`, :obj:`bool`, :obj:`list` of :obj:`float`, :obj:`list` of :obj:`int`, :obj:`list` of :obj:`str`, :obj:`list` of :obj:`bool`, :obj:`EnumValueId`, :obj:`list` of :obj:`EnumValueIdWrapper`): None; The identifier of a property enumeration value.; List of enumeration identifiers.

    """
    __slots__ = ("type", "status", "value", )

    constructor  = _ConstructUnion(Union[NormalOrUserUndefinedPropertyValue, NotAvailablePropertyValue, NotEvaluatedPropertyValue])

    def __new__(cls, type: str, status: str, value: Union[float, int, str, bool, List[float], List[int], List[str], List[bool], EnumValueId, List[EnumValueIdWrapper], None] = None):
        return cls.constructor(type=type, status=status, value=value)

    def __init__(self, type: str, status: str, value: Union[float, int, str, bool, List[float], List[int], List[str], List[bool], EnumValueId, List[EnumValueIdWrapper], None] = None):
        self.type: str = type
        self.status: str = status
        self.value: Union[float, int, str, bool, List[float], List[int], List[str], List[bool], EnumValueId, List[EnumValueIdWrapper], None] = value


class PropertyValueWrapper(_ACBaseType):
    """ 

    Attributes:
        propertyValue (:obj:`PropertyValue`): A normal, userUndefined, notAvailable or notEvaluated property value.

    """
    __slots__ = ("propertyValue", )

    def __init__(self, propertyValue: PropertyValue):
        self.propertyValue: PropertyValue = propertyValue

PropertyValueWrapper.get_classinfo().add_field('propertyValue', PropertyValue)


class PropertyValueOrErrorItem(_ACUnionType):
    """ Contains a property value or an error for the property.

    Attributes:
        propertyValue (:obj:`PropertyValue`, optional): A normal, userUndefined, notAvailable or notEvaluated property value.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("propertyValue", "error", )

    constructor  = _ConstructUnion(Union[PropertyValueWrapper, ErrorItem])

    def __new__(cls, propertyValue: Optional[PropertyValue] = None, error: Optional[Error] = None):
        return cls.constructor(propertyValue=propertyValue, error=error)

    def __init__(self, propertyValue: Optional[PropertyValue] = None, error: Optional[Error] = None):
        self.propertyValue: Optional[PropertyValue] = propertyValue
        self.error: Optional[Error] = error


class PropertyValuesWrapper(_ACBaseType):
    """ 

    Attributes:
        propertyValues (:obj:`list` of :obj:`PropertyValueOrErrorItem`): List of property values.

    """
    __slots__ = ("propertyValues", )

    def __init__(self, propertyValues: List[PropertyValueOrErrorItem]):
        self.propertyValues: List[PropertyValueOrErrorItem] = propertyValues

PropertyValuesWrapper.get_classinfo().add_field('propertyValues', List[PropertyValueOrErrorItem])


class PropertyValuesOrError(_ACUnionType):
    """ Contains either a list of property values or an error.

    Attributes:
        propertyValues (:obj:`list` of :obj:`PropertyValueOrErrorItem`, optional): List of property values.
        error (:obj:`Error`, optional): Error details.

    """
    __slots__ = ("propertyValues", "error", )

    constructor  = _ConstructUnion(Union[PropertyValuesWrapper, ErrorItem])

    def __new__(cls, propertyValues: Optional[List[PropertyValueOrErrorItem]] = None, error: Optional[Error] = None):
        return cls.constructor(propertyValues=propertyValues, error=error)

    def __init__(self, propertyValues: Optional[List[PropertyValueOrErrorItem]] = None, error: Optional[Error] = None):
        self.propertyValues: Optional[List[PropertyValueOrErrorItem]] = propertyValues
        self.error: Optional[Error] = error


class NavigatorItem_: pass
class NavigatorItemArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        navigatorItem (:obj:`NavigatorItem_`): Details of a navigator item.

    """
    __slots__ = ("navigatorItem", )

    def __init__(self, navigatorItem: NavigatorItem_):
        self.navigatorItem: NavigatorItem_ = navigatorItem


class NavigatorItem(_ACBaseType):
    """ Details of a navigator item.

    Attributes:
        navigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
        prefix (:obj:`str`): Prefix of the name of the navigator item.
        name (:obj:`str`): Name of the navigator item.
        type (:obj:`str`): Possible types of a navigator item. Most of the names are self-explanatory, the only exception is 'UndefinedItem', which means that the type of this navigator item cannot be retrieved from ARCHICAD yet.
        sourceNavigatorItemId (:obj:`NavigatorItemId`, optional): The identifier of a navigator item.
        children (:obj:`list` of :obj:`NavigatorItemArrayItem`, optional): List of navigator items.

    """
    __slots__ = ("navigatorItemId", "prefix", "name", "type", "sourceNavigatorItemId", "children", )

    def __init__(self, navigatorItemId: NavigatorItemId, prefix: str, name: str, type: str, sourceNavigatorItemId: Optional[NavigatorItemId] = None, children: Optional[List[NavigatorItemArrayItem]] = None):
        self.navigatorItemId: NavigatorItemId = navigatorItemId
        self.prefix: str = prefix
        self.name: str = name
        self.type: str = type
        self.sourceNavigatorItemId: Optional[NavigatorItemId] = sourceNavigatorItemId
        self.children: Optional[List[NavigatorItemArrayItem]] = children

NavigatorItem.get_classinfo().add_field('navigatorItemId', NavigatorItemId)
NavigatorItem.get_classinfo().add_field('prefix', str)
NavigatorItem.get_classinfo().add_field('name', str)
NavigatorItem.get_classinfo().add_field('type', str, value_set(['UndefinedItem', 'ProjectMapRootItem', 'StoryItem', 'SectionItem', 'ElevationItem', 'InteriorElevationItem', 'WorksheetItem', 'DetailItem', 'DocumentFrom3DItem', 'Perspective3DItem', 'Axonometry3DItem', 'CameraSetItem', 'CameraItem', 'ScheduleItem', 'ProjectIndexItem', 'TextListItem', 'GraphicListItem', 'InfoItem', 'HelpItem', 'FolderItem', 'LayoutBookRootItem', 'SubsetItem', 'LayoutItem', 'DrawingItem', 'MasterFolderItem', 'MasterLayoutItem']))
NavigatorItem.get_classinfo().add_field('sourceNavigatorItemId', Optional[NavigatorItemId])
NavigatorItem.get_classinfo().add_field('children', Optional[List[NavigatorItemArrayItem]])

NavigatorItem_ = NavigatorItem
NavigatorItemArrayItem.get_classinfo().add_field('navigatorItem', NavigatorItem)


class NavigatorTree(_ACBaseType):
    """ A tree of navigator items.

    Attributes:
        rootItem (:obj:`NavigatorItem`): Details of a navigator item.

    """
    __slots__ = ("rootItem", )

    def __init__(self, rootItem: NavigatorItem):
        self.rootItem: NavigatorItem = rootItem

NavigatorTree.get_classinfo().add_field('rootItem', NavigatorItem)


class Types:
    """ 
    """
    ClassificationSystemId=ClassificationSystemId
    ClassificationSystemIdArrayItem=ClassificationSystemIdArrayItem
    ClassificationItemId=ClassificationItemId
    ClassificationItemIdArrayItem=ClassificationItemIdArrayItem
    ClassificationId=ClassificationId
    ClassificationItemDetails=ClassificationItemDetails
    ClassificationSystem=ClassificationSystem
    UserDefinedPropertyUserId=UserDefinedPropertyUserId
    BuiltInPropertyUserId=BuiltInPropertyUserId
    PropertyUserId=PropertyUserId
    PropertyId=PropertyId
    PropertyIdArrayItem=PropertyIdArrayItem
    PropertyGroup=PropertyGroup
    NormalNumberPropertyValue=NormalNumberPropertyValue
    NormalIntegerPropertyValue=NormalIntegerPropertyValue
    NormalStringPropertyValue=NormalStringPropertyValue
    NormalBooleanPropertyValue=NormalBooleanPropertyValue
    NormalLengthPropertyValue=NormalLengthPropertyValue
    NormalAreaPropertyValue=NormalAreaPropertyValue
    NormalVolumePropertyValue=NormalVolumePropertyValue
    NormalAnglePropertyValue=NormalAnglePropertyValue
    NormalNumberListPropertyValue=NormalNumberListPropertyValue
    NormalIntegerListPropertyValue=NormalIntegerListPropertyValue
    NormalStringListPropertyValue=NormalStringListPropertyValue
    NormalBooleanListPropertyValue=NormalBooleanListPropertyValue
    NormalLengthListPropertyValue=NormalLengthListPropertyValue
    NormalAreaListPropertyValue=NormalAreaListPropertyValue
    NormalVolumeListPropertyValue=NormalVolumeListPropertyValue
    NormalAngleListPropertyValue=NormalAngleListPropertyValue
    UserUndefinedPropertyValue=UserUndefinedPropertyValue
    NotAvailablePropertyValue=NotAvailablePropertyValue
    NotEvaluatedPropertyValue=NotEvaluatedPropertyValue
    DisplayValueEnumId=DisplayValueEnumId
    EnumValueId=EnumValueId
    PossibleEnumValue=PossibleEnumValue
    PossibleEnumValuesArrayItem=PossibleEnumValuesArrayItem
    Error=Error
    ErrorItem=ErrorItem
    SuccessfulExecutionResult=SuccessfulExecutionResult
    FailedExecutionResult=FailedExecutionResult
    ExecutionResult=ExecutionResult
    ElementId=ElementId
    ElementIdArrayItem=ElementIdArrayItem
    ElementsWrapper=ElementsWrapper
    ElementsOrError=ElementsOrError
    NavigatorItemId=NavigatorItemId
    PublisherSetId=PublisherSetId
    OtherNavigatorTreeId=OtherNavigatorTreeId
    FolderParameters=FolderParameters
    NavigatorTreeId=NavigatorTreeId
    BoundingBox2D=BoundingBox2D
    BoundingBox3D=BoundingBox3D
    Subset=Subset
    LayoutParameters=LayoutParameters
    ClassificationIdWrapper=ClassificationIdWrapper
    ClassificationItemDetailsWrapper=ClassificationItemDetailsWrapper
    EnumValueIdWrapper=EnumValueIdWrapper
    NavigatorItemIdWrapper=NavigatorItemIdWrapper
    BoundingBox2DWrapper=BoundingBox2DWrapper
    BoundingBox3DWrapper=BoundingBox3DWrapper
    ClassificationIdOrError=ClassificationIdOrError
    ElementClassification=ElementClassification
    ClassificationItemOrError=ClassificationItemOrError
    PropertyIdOrError=PropertyIdOrError
    PropertyDefinition=PropertyDefinition
    NormalSingleEnumPropertyValue=NormalSingleEnumPropertyValue
    NormalMultiEnumPropertyValue=NormalMultiEnumPropertyValue
    BoundingBox2DOrError=BoundingBox2DOrError
    BoundingBox3DOrError=BoundingBox3DOrError
    ClassificationIdsOrErrorsWrapper=ClassificationIdsOrErrorsWrapper
    PropertyDefinitionWrapper=PropertyDefinitionWrapper
    ElementClassificationOrError=ElementClassificationOrError
    PropertyDefinitionOrError=PropertyDefinitionOrError
    ClassificationItemArrayItem=ClassificationItemArrayItem
    ClassificationItemInTree=ClassificationItemInTree
    NormalOrUserUndefinedPropertyValue=NormalOrUserUndefinedPropertyValue
    ElementPropertyValue=ElementPropertyValue
    PropertyValue=PropertyValue
    PropertyValueWrapper=PropertyValueWrapper
    PropertyValueOrErrorItem=PropertyValueOrErrorItem
    PropertyValuesWrapper=PropertyValuesWrapper
    PropertyValuesOrError=PropertyValuesOrError
    NavigatorItemArrayItem=NavigatorItemArrayItem
    NavigatorItem=NavigatorItem
    NavigatorTree=NavigatorTree

