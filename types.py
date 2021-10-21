"""GRAPHISOFT
"""
from uuid import UUID
from typing import Union, Optional, List

from archicad.acbasetype import _ACBaseType, _ACUnionType, _ConstructUnion
from archicad.validators import value_set, matches, min_length, max_length, multiple_of, minimum, maximum, listitem_validator, min_items, max_items, unique_items


class AddOnCommandId(_ACBaseType):
    """ The identifier of an Add-On command.

    Attributes:
        commandNamespace (:obj:`str`): The namespace of the Add-On command.
        commandName (:obj:`str`): The name of the Add-On command.

    """
    __slots__ = ("commandNamespace", "commandName", )

    def __init__(self, commandNamespace: str, commandName: str):
        self.commandNamespace: str = commandNamespace
        self.commandName: str = commandName

AddOnCommandId.get_classinfo().add_field('commandNamespace', str, min_length(1))
AddOnCommandId.get_classinfo().add_field('commandName', str, min_length(1))


class AddOnCommandIdArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        addOnCommandId (:obj:`AddOnCommandId`): The identifier of an Add-On command.

    """
    __slots__ = ("addOnCommandId", )

    def __init__(self, addOnCommandId: AddOnCommandId):
        self.addOnCommandId: AddOnCommandId = addOnCommandId

AddOnCommandIdArrayItem.get_classinfo().add_field('addOnCommandId', AddOnCommandId)


class AddOnCommandParameters(_ACBaseType):
    """ The input parameters of an Add-On command.

    """
    def __init__(self):
        pass


class AddOnCommandResponse(_ACBaseType):
    """ The response returned by an Add-On command.

    """
    def __init__(self):
        pass


class AttributeId(_ACBaseType):
    """ The identifier of an attribute.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

AttributeId.get_classinfo().add_field('guid', UUID)


class AttributeIdWrapperItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.

    """
    __slots__ = ("attributeId", )

    def __init__(self, attributeId: AttributeId):
        self.attributeId: AttributeId = attributeId

AttributeIdWrapperItem.get_classinfo().add_field('attributeId', AttributeId)


class AttributeHeader(_ACBaseType):
    """ The header object of an attribute.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.

    """
    __slots__ = ("attributeId", "name", )

    def __init__(self, attributeId: AttributeId, name: str):
        self.attributeId: AttributeId = attributeId
        self.name: str = name

AttributeHeader.get_classinfo().add_field('attributeId', AttributeId)
AttributeHeader.get_classinfo().add_field('name', str)


class LayerAttribute(_ACBaseType):
    """ A layer attribute

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        intersectionGroupNr (:obj:`int`): The intersection group number
        isLocked (:obj:`bool`): Defines whether the layer is locked or not.
        isHidden (:obj:`bool`): Defines whether the layer is hidden or not.
        isWireframe (:obj:`bool`): Defines whether the elements placed on this layer are visible as wireframes or a solid model.

    """
    __slots__ = ("attributeId", "name", "intersectionGroupNr", "isLocked", "isHidden", "isWireframe", )

    def __init__(self, attributeId: AttributeId, name: str, intersectionGroupNr: int, isLocked: bool, isHidden: bool, isWireframe: bool):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.intersectionGroupNr: int = intersectionGroupNr
        self.isLocked: bool = isLocked
        self.isHidden: bool = isHidden
        self.isWireframe: bool = isWireframe

LayerAttribute.get_classinfo().add_field('attributeId', AttributeId)
LayerAttribute.get_classinfo().add_field('name', str)
LayerAttribute.get_classinfo().add_field('intersectionGroupNr', int)
LayerAttribute.get_classinfo().add_field('isLocked', bool)
LayerAttribute.get_classinfo().add_field('isHidden', bool)
LayerAttribute.get_classinfo().add_field('isWireframe', bool)


class FillAttribute(_ACBaseType):
    """ A fill attribute.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        subType (:obj:`str`): The filling type of a fill attribute.
        pattern (:obj:`int`): The pattern of the fill attribute, stored in a 64 bit unsigned integer, and represented as an 8x8 matrix. Each byte in the value is a row, and the bits are the columns of the matrix.
        appearanceType (:obj:`str`): The appearance type of a line or fill attribute.

    """
    __slots__ = ("attributeId", "name", "subType", "pattern", "appearanceType", )

    def __init__(self, attributeId: AttributeId, name: str, subType: str, pattern: int, appearanceType: str):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.subType: str = subType
        self.pattern: int = pattern
        self.appearanceType: str = appearanceType

FillAttribute.get_classinfo().add_field('attributeId', AttributeId)
FillAttribute.get_classinfo().add_field('name', str)
FillAttribute.get_classinfo().add_field('subType', str, value_set(['Vector', 'Symbol', 'Solid', 'Empty', 'LinearGradient', 'RadialGradient', 'Image']))
FillAttribute.get_classinfo().add_field('pattern', int)
FillAttribute.get_classinfo().add_field('appearanceType', str, value_set(['ScaleWithPlan', 'ScaleIndependent']))


class ProfileModifier(_ACBaseType):
    """ A profile modifier parameter.

    Attributes:
        name (:obj:`str`): The name of the modifier.
        value (:obj:`float`): The value of the modifier.

    """
    __slots__ = ("name", "value", )

    def __init__(self, name: str, value: float):
        self.name: str = name
        self.value: float = value

ProfileModifier.get_classinfo().add_field('name', str)
ProfileModifier.get_classinfo().add_field('value', float)


class ProfileModifierListItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        profileModifier (:obj:`ProfileModifier`): A profile modifier parameter.

    """
    __slots__ = ("profileModifier", )

    def __init__(self, profileModifier: ProfileModifier):
        self.profileModifier: ProfileModifier = profileModifier

ProfileModifierListItem.get_classinfo().add_field('profileModifier', ProfileModifier)


class ProfileAttribute(_ACBaseType):
    """ A profile attribute.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        useWith (:obj:`list` of :obj:`str`): A list of element types.
        width (:obj:`float`): The default width (horizontal size) of the profile.
        height (:obj:`float`): The default height (vertical size) of the profile.
        minimumWidth (:obj:`float`): The minimum width (horizontal size) of the profile.
        minimumHeight (:obj:`float`): The minimum height (vertical size) of the profile.
        widthStretchable (:obj:`bool`): Defines whether the profile's width can be increased beyond its default value or not.
        heightStretchable (:obj:`bool`): Defines whether the profile's height can be increased beyond its default value or not.
        hasCoreSkin (:obj:`bool`): Defines whether the profile has a core skin or not.
        profileModifiers (:obj:`list` of :obj:`ProfileModifierListItem`): A list of profile modifiers.

    """
    __slots__ = ("attributeId", "name", "useWith", "width", "height", "minimumWidth", "minimumHeight", "widthStretchable", "heightStretchable", "hasCoreSkin", "profileModifiers", )

    def __init__(self, attributeId: AttributeId, name: str, useWith: List[str], width: float, height: float, minimumWidth: float, minimumHeight: float, widthStretchable: bool, heightStretchable: bool, hasCoreSkin: bool, profileModifiers: List[ProfileModifierListItem]):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.useWith: List[str] = useWith
        self.width: float = width
        self.height: float = height
        self.minimumWidth: float = minimumWidth
        self.minimumHeight: float = minimumHeight
        self.widthStretchable: bool = widthStretchable
        self.heightStretchable: bool = heightStretchable
        self.hasCoreSkin: bool = hasCoreSkin
        self.profileModifiers: List[ProfileModifierListItem] = profileModifiers

ProfileAttribute.get_classinfo().add_field('attributeId', AttributeId)
ProfileAttribute.get_classinfo().add_field('name', str)
ProfileAttribute.get_classinfo().add_field('useWith', List[str], listitem_validator(value_set(['Wall', 'Column', 'Beam', 'Window', 'Door', 'Object', 'Lamp', 'Slab', 'Roof', 'Mesh', 'Zone', 'CurtainWall', 'Shell', 'Skylight', 'Morph', 'Stair', 'Railing', 'Opening'])))
ProfileAttribute.get_classinfo().add_field('width', float)
ProfileAttribute.get_classinfo().add_field('height', float)
ProfileAttribute.get_classinfo().add_field('minimumWidth', float)
ProfileAttribute.get_classinfo().add_field('minimumHeight', float)
ProfileAttribute.get_classinfo().add_field('widthStretchable', bool)
ProfileAttribute.get_classinfo().add_field('heightStretchable', bool)
ProfileAttribute.get_classinfo().add_field('hasCoreSkin', bool)
ProfileAttribute.get_classinfo().add_field('profileModifiers', List[ProfileModifierListItem])


class Texture(_ACBaseType):
    """ A texture

    Attributes:
        name (:obj:`str`): The name of the texture.

    """
    __slots__ = ("name", )

    def __init__(self, name: str):
        self.name: str = name

Texture.get_classinfo().add_field('name', str)


class DashItem(_ACBaseType):
    """ A dash item.

    Attributes:
        dash (:obj:`float`): The length of the dash.
        gap (:obj:`float`): The length of the gap.

    """
    __slots__ = ("dash", "gap", )

    def __init__(self, dash: float, gap: float):
        self.dash: float = dash
        self.gap: float = gap

DashItem.get_classinfo().add_field('dash', float)
DashItem.get_classinfo().add_field('gap', float)


class LayerCombinationAttribute(_ACBaseType):
    """ A layer combination attribute

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        layerAttributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

    """
    __slots__ = ("attributeId", "name", "layerAttributeIds", )

    def __init__(self, attributeId: AttributeId, name: str, layerAttributeIds: List[AttributeIdWrapperItem]):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.layerAttributeIds: List[AttributeIdWrapperItem] = layerAttributeIds

LayerCombinationAttribute.get_classinfo().add_field('attributeId', AttributeId)
LayerCombinationAttribute.get_classinfo().add_field('name', str)
LayerCombinationAttribute.get_classinfo().add_field('layerAttributeIds', List[AttributeIdWrapperItem])


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
    """ The details of a classification item.

    Attributes:
        id (:obj:`str`): The unique identifier of the classification item as specified by the user.
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
    """ The details of a classification system.

    Attributes:
        classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.
        name (:obj:`str`): The display name of the classification system.
        description (:obj:`str`): The description of the classification system.
        source (:obj:`str`): The source of the classification system (e.g. URL to a classification system standard).
        version (:obj:`str`): The version of the classification system.
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


class Point2D(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        x (:obj:`float`): X coordinate of 2D point
        y (:obj:`float`): Y coordinate of 2D point

    """
    __slots__ = ("x", "y", )

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

Point2D.get_classinfo().add_field('x', float)
Point2D.get_classinfo().add_field('y', float)


class UserDefinedPropertyUserId(_ACBaseType):
    """ The unique identifier of a User-Defined Property, identified by its name.

    Attributes:
        localizedName (:obj:`list` of :obj:`str`): A two-element list of the localized name parts. The first element is the name of the group the property belongs to, and the second element is the actual name of the property.
        type (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("localizedName", "type", )

    def __init__(self, localizedName: List[str], type: str = "UserDefined"):
        self.localizedName: List[str] = localizedName
        self.type: str = type

UserDefinedPropertyUserId.get_classinfo().add_field('localizedName', List[str], min_items(2), max_items(2))
UserDefinedPropertyUserId.get_classinfo().add_field('type', str, value_set(['UserDefined']))


class BuiltInPropertyUserId(_ACBaseType):
    """ The unique identifier of a Built-In Property, identified by its name.

    Attributes:
        nonLocalizedName (:obj:`str`): The non-localized name of the Built-In Property.
        type (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("nonLocalizedName", "type", )

    def __init__(self, nonLocalizedName: str, type: str = "BuiltIn"):
        self.nonLocalizedName: str = nonLocalizedName
        self.type: str = type

BuiltInPropertyUserId.get_classinfo().add_field('nonLocalizedName', str)
BuiltInPropertyUserId.get_classinfo().add_field('type', str, value_set(['BuiltIn']))


class PropertyUserId(_ACUnionType):
    """ The unique identifier of a Property, identified by its name. May represent a User-Defined or a Built-In Property.

    Attributes:
        type (:obj:`str`): None
        localizedName (:obj:`list` of :obj:`str`, optional): A two-element list of the localized name parts. The first element is the name of the group the property belongs to, and the second element is the actual name of the property.
        nonLocalizedName (:obj:`str`, optional): The non-localized name of the Built-In Property.

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
    """ A length property value containing a real length value. The value is measured in SI (meters).

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
    """ An area property value containing a real area. The value is measured in SI (square meters).

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
    """ A volume property value containing a real volume. The value is measured in SI (cubic meters).

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
    """ An angle property value containing a real angle. The value is measured in SI (radians).

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
    """ A length list property value containing length values in an array. The values are measured in SI (meters).

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
    """ An area list property value containing areas in an array. The values are measured in SI (square meters).

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
    """ A volume list property value containing volumes in an array. The values are measured in SI (cubic meters).

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
    """ An angle list property value containing angles in an array. The values are measured in SI (radians).

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


class NonLocalizedValueEnumId(_ACBaseType):
    """ An enumeration value identifier using the nonlocalized value.

    Attributes:
        nonLocalizedValue (:obj:`str`): EMPTY STRING
        type (:obj:`str`): EMPTY STRING

    """
    __slots__ = ("nonLocalizedValue", "type", )

    def __init__(self, nonLocalizedValue: str, type: str = "nonLocalizedValue"):
        self.nonLocalizedValue: str = nonLocalizedValue
        self.type: str = type

NonLocalizedValueEnumId.get_classinfo().add_field('nonLocalizedValue', str)
NonLocalizedValueEnumId.get_classinfo().add_field('type', str, value_set(['nonLocalizedValue']))


class EnumValueId(_ACUnionType):
    """ The identifier of a property enumeration value.

    Attributes:
        type (:obj:`str`): None
        displayValue (:obj:`str`, optional): EMPTY STRING
        nonLocalizedValue (:obj:`str`, optional): EMPTY STRING

    """
    __slots__ = ("type", "displayValue", "nonLocalizedValue", )

    constructor  = _ConstructUnion(Union[DisplayValueEnumId, NonLocalizedValueEnumId])

    def __new__(cls, type: str, displayValue: Optional[str] = None, nonLocalizedValue: Optional[str] = None):
        return cls.constructor(type=type, displayValue=displayValue, nonLocalizedValue=nonLocalizedValue)

    def __init__(self, type: str, displayValue: Optional[str] = None, nonLocalizedValue: Optional[str] = None):
        self.type: str = type
        self.displayValue: Optional[str] = displayValue
        self.nonLocalizedValue: Optional[str] = nonLocalizedValue


class PossibleEnumValue(_ACBaseType):
    """ The description of an enumeration value.

    Attributes:
        enumValueId (:obj:`EnumValueId`): The identifier of a property enumeration value.
        displayValue (:obj:`str`): Displayed value of the enumeration.
        nonLocalizedValue (:obj:`str`, optional): Nonlocalized value of the enumeration if there is one.

    """
    __slots__ = ("enumValueId", "displayValue", "nonLocalizedValue", )

    def __init__(self, enumValueId: EnumValueId, displayValue: str, nonLocalizedValue: Optional[str] = None):
        self.enumValueId: EnumValueId = enumValueId
        self.displayValue: str = displayValue
        self.nonLocalizedValue: Optional[str] = nonLocalizedValue

PossibleEnumValue.get_classinfo().add_field('enumValueId', EnumValueId)
PossibleEnumValue.get_classinfo().add_field('displayValue', str)
PossibleEnumValue.get_classinfo().add_field('nonLocalizedValue', Optional[str])


class PossibleEnumValuesArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        enumValue (:obj:`PossibleEnumValue`): The description of an enumeration value.

    """
    __slots__ = ("enumValue", )

    def __init__(self, enumValue: PossibleEnumValue):
        self.enumValue: PossibleEnumValue = enumValue

PossibleEnumValuesArrayItem.get_classinfo().add_field('enumValue', PossibleEnumValue)


class Error(_ACBaseType):
    """ The details of an error.

    Attributes:
        code (:obj:`int`): The code of the error.
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
        error (:obj:`Error`): The details of an error.

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
        error (:obj:`Error`): The details of an error.

    """
    __slots__ = ("success", "error", )

    def __init__(self, success: bool, error: Error):
        self.success: bool = success
        self.error: Error = error

FailedExecutionResult.get_classinfo().add_field('success', bool)
FailedExecutionResult.get_classinfo().add_field('error', Error)


class ExecutionResult(_ACUnionType):
    """ The result of the execution.

    Attributes:
        success (:obj:`bool`): None
        error (:obj:`Error`, optional): The details of an error.

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
    """ A wrapper for a list of elements.

    Attributes:
        elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.

    """
    __slots__ = ("elements", )

    def __init__(self, elements: List[ElementIdArrayItem]):
        self.elements: List[ElementIdArrayItem] = elements

ElementsWrapper.get_classinfo().add_field('elements', List[ElementIdArrayItem])


class ElementsOrError(_ACUnionType):
    """ A list of elements or an error.

    Attributes:
        elements (:obj:`list` of :obj:`ElementIdArrayItem`, optional): A list of elements.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("elements", "error", )

    constructor  = _ConstructUnion(Union[ElementsWrapper, ErrorItem])

    def __new__(cls, elements: Optional[List[ElementIdArrayItem]] = None, error: Optional[Error] = None):
        return cls.constructor(elements=elements, error=error)

    def __init__(self, elements: Optional[List[ElementIdArrayItem]] = None, error: Optional[Error] = None):
        self.elements: Optional[List[ElementIdArrayItem]] = elements
        self.error: Optional[Error] = error


class Image(_ACBaseType):
    """ An image encoded as a Base64 string.

    Attributes:
        content (:obj:`str`): The image content as a string .

    """
    __slots__ = ("content", )

    def __init__(self, content: str):
        self.content: str = content

Image.get_classinfo().add_field('content', str)


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
        name (:obj:`str`): The name of the publisher set.
        type (:obj:`str`): The type of the navigator item tree.

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
        type (:obj:`str`): The type of the navigator item tree.

    """
    __slots__ = ("type", )

    def __init__(self, type: str):
        self.type: str = type

OtherNavigatorTreeId.get_classinfo().add_field('type', str, value_set(['ProjectMap', 'ViewMap', 'MyViewMap', 'LayoutBook']))


class FolderParameters(_ACBaseType):
    """ The parameters of a folder.

    Attributes:
        name (:obj:`str`): The name of the folder.

    """
    __slots__ = ("name", )

    def __init__(self, name: str):
        self.name: str = name

FolderParameters.get_classinfo().add_field('name', str)


class NavigatorTreeId(_ACUnionType):
    """ The identifier of a navigator item tree.

    Attributes:
        type (:obj:`str`): The type of the navigator item tree.
        name (:obj:`str`, optional): The name of the publisher set.

    """
    __slots__ = ("type", "name", )

    constructor  = _ConstructUnion(Union[PublisherSetId, OtherNavigatorTreeId])

    def __new__(cls, type: str, name: Optional[str] = None):
        return cls.constructor(type=type, name=name)

    def __init__(self, type: str, name: Optional[str] = None):
        self.type: str = type
        self.name: Optional[str] = name


class BoundingBox2D(_ACBaseType):
    """ The 2D bounding box of an element.

    Attributes:
        xMin (:obj:`float`): The minimum X value of the bounding box.
        yMin (:obj:`float`): The minimum Y value of the bounding box.
        xMax (:obj:`float`): The maximum X value of the bounding box.
        yMax (:obj:`float`): The maximum Y value of the bounding box.

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
    """ A 3D bounding box of an element.

    Attributes:
        xMin (:obj:`float`): The minimum X value of the bounding box.
        yMin (:obj:`float`): The minimum Y value of the bounding box.
        zMin (:obj:`float`): The minimum Z value of the bounding box.
        xMax (:obj:`float`): The maximum X value of the bounding box.
        yMax (:obj:`float`): The maximum Y value of the bounding box.
        zMax (:obj:`float`): The maximum Z value of the bounding box.

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


class RGBColor(_ACBaseType):
    """ A color model represented via its red, green and blue components.

    Attributes:
        red (:obj:`float`): The red component of the color model.
        green (:obj:`float`): The green component of the color model.
        blue (:obj:`float`): The blue component of the color model.

    """
    __slots__ = ("red", "green", "blue", )

    def __init__(self, red: float, green: float, blue: float):
        self.red: float = red
        self.green: float = green
        self.blue: float = blue

RGBColor.get_classinfo().add_field('red', float, maximum(1, False))
RGBColor.get_classinfo().add_field('green', float, maximum(1, False))
RGBColor.get_classinfo().add_field('blue', float, maximum(1, False))


class Subset(_ACBaseType):
    """ A set of options used to assign IDs to the layouts contained in the subset.

    Attributes:
        name (:obj:`str`): The name for the layout subset.
        includeToIDSequence (:obj:`bool`): Defines whether this subset is included in automatic ID assignment or not.
        customNumbering (:obj:`bool`): Defines whether the IDs are generated automatically or a custom numbering is used.
        continueNumbering (:obj:`bool`): Defines whether to continue using the ID assignment of the upper levels or not. If 'true', layouts within this subset are going to be assigned IDs as if they were not within this subset, but part of the level above. In this case you only use the Subset as a logical grouping which has no effect on IDs.
        useUpperPrefix (:obj:`bool`): Defines whether to use the prefix and ID of the upper levels or not. If 'true', layouts in this subset will be assigned IDs based on the previous layout in the layout book structure.
        addOwnPrefix (:obj:`bool`): Defines whether to add own prefix to the subset or not.
        customNumber (:obj:`str`): The custom subset ID.
        autoNumber (:obj:`str`): The automatic subset ID.
        numberingStyle (:obj:`str`): A supported numbering style.
        startAt (:obj:`int`): The starting value of the numbering.
        ownPrefix (:obj:`str`): The custom prefix for the subset.

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
        horizontalSize (:obj:`float`): The horizontal size of the layout in millimeters.
        verticalSize (:obj:`float`): The vertical size of the layout in millimeters.
        leftMargin (:obj:`float`): The layout margin from the left side of the paper.
        topMargin (:obj:`float`): The layout margin from the top side of the paper.
        rightMargin (:obj:`float`): The layout margin from the right side of the paper.
        bottomMargin (:obj:`float`): The layout margin from the bottom side of the paper.
        customLayoutNumber (:obj:`str`): The custom ID.
        customLayoutNumbering (:obj:`bool`): Defines whether a unique ID is used for the current layout or not.
        doNotIncludeInNumbering (:obj:`bool`): Defines whether this layout is included in automatic ID assignment or not.
        displayMasterLayoutBelow (:obj:`bool`): Defines whether to display the master layout above or below the layout.
        layoutPageNumber (:obj:`int`): The page number of layout when this layout contains multi-page drawings.
        actPageIndex (:obj:`int`): The actual index of layout inside the multi-page layout.
        currentRevisionId (:obj:`str`): The ID of the current document revision of the layout.
        currentFinalRevisionId (:obj:`str`): The ID with optional suffix of the current document revision of the layout.
        hasIssuedRevision (:obj:`bool`): Defines whether one or more issued document revisions have already been created for the layout or not.
        hasActualRevision (:obj:`bool`): Defines whether an open document revision exists for the layout or not.

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


class ComponentId(_ACBaseType):
    """ The identifier of a component.

    Attributes:
        guid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

    """
    __slots__ = ("guid", )

    def __init__(self, guid: UUID):
        self.guid: UUID = guid

ComponentId.get_classinfo().add_field('guid', UUID)


class ElementComponentId(_ACBaseType):
    """ The identifier of an element's component.

    Attributes:
        elementId (:obj:`ElementId`): The identifier of an element.
        componentId (:obj:`ComponentId`): The identifier of a component.

    """
    __slots__ = ("elementId", "componentId", )

    def __init__(self, elementId: ElementId, componentId: ComponentId):
        self.elementId: ElementId = elementId
        self.componentId: ComponentId = componentId

ElementComponentId.get_classinfo().add_field('elementId', ElementId)
ElementComponentId.get_classinfo().add_field('componentId', ComponentId)


class ElementComponentIdArrayItem(_ACBaseType):
    """ An item of a component array.

    Attributes:
        elementComponentId (:obj:`ElementComponentId`): The identifier of an element's component.

    """
    __slots__ = ("elementComponentId", )

    def __init__(self, elementComponentId: ElementComponentId):
        self.elementComponentId: ElementComponentId = elementComponentId

ElementComponentIdArrayItem.get_classinfo().add_field('elementComponentId', ElementComponentId)


class ElementComponentsWrapper(_ACBaseType):
    """ List of components.

    Attributes:
        elementComponents (:obj:`list` of :obj:`ElementComponentIdArrayItem`): List of components of elements.

    """
    __slots__ = ("elementComponents", )

    def __init__(self, elementComponents: List[ElementComponentIdArrayItem]):
        self.elementComponents: List[ElementComponentIdArrayItem] = elementComponents

ElementComponentsWrapper.get_classinfo().add_field('elementComponents', List[ElementComponentIdArrayItem])


class ElementComponentsOrError(_ACUnionType):
    """ List of components or error.

    Attributes:
        elementComponents (:obj:`list` of :obj:`ElementComponentIdArrayItem`, optional): List of components of elements.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("elementComponents", "error", )

    constructor  = _ConstructUnion(Union[ElementComponentsWrapper, ErrorItem])

    def __new__(cls, elementComponents: Optional[List[ElementComponentIdArrayItem]] = None, error: Optional[Error] = None):
        return cls.constructor(elementComponents=elementComponents, error=error)

    def __init__(self, elementComponents: Optional[List[ElementComponentIdArrayItem]] = None, error: Optional[Error] = None):
        self.elementComponents: Optional[List[ElementComponentIdArrayItem]] = elementComponents
        self.error: Optional[Error] = error


class LayerAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        layerAttribute (:obj:`LayerAttribute`): A layer attribute

    """
    __slots__ = ("layerAttribute", )

    def __init__(self, layerAttribute: LayerAttribute):
        self.layerAttribute: LayerAttribute = layerAttribute

LayerAttributeWrapper.get_classinfo().add_field('layerAttribute', LayerAttribute)


class FillAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        fillAttribute (:obj:`FillAttribute`): A fill attribute.

    """
    __slots__ = ("fillAttribute", )

    def __init__(self, fillAttribute: FillAttribute):
        self.fillAttribute: FillAttribute = fillAttribute

FillAttributeWrapper.get_classinfo().add_field('fillAttribute', FillAttribute)


class ProfileAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        profileAttribute (:obj:`ProfileAttribute`): A profile attribute.

    """
    __slots__ = ("profileAttribute", )

    def __init__(self, profileAttribute: ProfileAttribute):
        self.profileAttribute: ProfileAttribute = profileAttribute

ProfileAttributeWrapper.get_classinfo().add_field('profileAttribute', ProfileAttribute)


class DashItemWrapper(_ACBaseType):
    """ 

    Attributes:
        dashItem (:obj:`DashItem`): A dash item.

    """
    __slots__ = ("dashItem", )

    def __init__(self, dashItem: DashItem):
        self.dashItem: DashItem = dashItem

DashItemWrapper.get_classinfo().add_field('dashItem', DashItem)


class LayerCombinationAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        layerCombinationAttribute (:obj:`LayerCombinationAttribute`): A layer combination attribute

    """
    __slots__ = ("layerCombinationAttribute", )

    def __init__(self, layerCombinationAttribute: LayerCombinationAttribute):
        self.layerCombinationAttribute: LayerCombinationAttribute = layerCombinationAttribute

LayerCombinationAttributeWrapper.get_classinfo().add_field('layerCombinationAttribute', LayerCombinationAttribute)


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
        classificationItem (:obj:`ClassificationItemDetails`): The details of a classification item.

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


class ImageWrapper(_ACBaseType):
    """ 

    Attributes:
        image (:obj:`Image`): An image encoded as a Base64 string.

    """
    __slots__ = ("image", )

    def __init__(self, image: Image):
        self.image: Image = image

ImageWrapper.get_classinfo().add_field('image', Image)


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
        boundingBox2D (:obj:`BoundingBox2D`): The 2D bounding box of an element.

    """
    __slots__ = ("boundingBox2D", )

    def __init__(self, boundingBox2D: BoundingBox2D):
        self.boundingBox2D: BoundingBox2D = boundingBox2D

BoundingBox2DWrapper.get_classinfo().add_field('boundingBox2D', BoundingBox2D)


class BoundingBox3DWrapper(_ACBaseType):
    """ 

    Attributes:
        boundingBox3D (:obj:`BoundingBox3D`): A 3D bounding box of an element.

    """
    __slots__ = ("boundingBox3D", )

    def __init__(self, boundingBox3D: BoundingBox3D):
        self.boundingBox3D: BoundingBox3D = boundingBox3D

BoundingBox3DWrapper.get_classinfo().add_field('boundingBox3D', BoundingBox3D)


class AttributeIdOrError(_ACUnionType):
    """ The attribute's identifier or an error.

    Attributes:
        attributeId (:obj:`AttributeId`, optional): The identifier of an attribute.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("attributeId", "error", )

    constructor  = _ConstructUnion(Union[AttributeIdWrapperItem, ErrorItem])

    def __new__(cls, attributeId: Optional[AttributeId] = None, error: Optional[Error] = None):
        return cls.constructor(attributeId=attributeId, error=error)

    def __init__(self, attributeId: Optional[AttributeId] = None, error: Optional[Error] = None):
        self.attributeId: Optional[AttributeId] = attributeId
        self.error: Optional[Error] = error


class LayerAttributeOrError(_ACUnionType):
    """ A layer attribute or an error.

    Attributes:
        layerAttribute (:obj:`LayerAttribute`, optional): A layer attribute
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("layerAttribute", "error", )

    constructor  = _ConstructUnion(Union[LayerAttributeWrapper, ErrorItem])

    def __new__(cls, layerAttribute: Optional[LayerAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(layerAttribute=layerAttribute, error=error)

    def __init__(self, layerAttribute: Optional[LayerAttribute] = None, error: Optional[Error] = None):
        self.layerAttribute: Optional[LayerAttribute] = layerAttribute
        self.error: Optional[Error] = error


class FillAttributeOrError(_ACUnionType):
    """ A fill attribute or an error.

    Attributes:
        fillAttribute (:obj:`FillAttribute`, optional): A fill attribute.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("fillAttribute", "error", )

    constructor  = _ConstructUnion(Union[FillAttributeWrapper, ErrorItem])

    def __new__(cls, fillAttribute: Optional[FillAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(fillAttribute=fillAttribute, error=error)

    def __init__(self, fillAttribute: Optional[FillAttribute] = None, error: Optional[Error] = None):
        self.fillAttribute: Optional[FillAttribute] = fillAttribute
        self.error: Optional[Error] = error


class SurfaceAttribute(_ACBaseType):
    """ A surface attribute.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        materialType (:obj:`str`): The material type of a surface attribute.
        ambientReflection (:obj:`int`): The ambient reflection of the surface attribute.
        diffuseReflection (:obj:`int`): The diffuse reflection of the surface attribute.
        specularReflection (:obj:`int`): The specular reflection of the surface attribute.
        transparencyAttenuation (:obj:`int`): The transparency attenuation of the surface attribute.
        emissionAttenuation (:obj:`int`): The emission attenuation of the surface attribute.
        surfaceColor (:obj:`RGBColor`): A color model represented via its red, green and blue components.
        specularColor (:obj:`RGBColor`): A color model represented via its red, green and blue components.
        emissionColor (:obj:`RGBColor`): A color model represented via its red, green and blue components.
        fillId (:obj:`AttributeIdOrError`): The attribute's identifier or an error.
        transparency (:obj:`int`): The transparency of the surface attribute.
        shine (:obj:`int`): The shininess of the surface attribute.
        texture (:obj:`Texture`, optional): A texture

    """
    __slots__ = ("attributeId", "name", "materialType", "ambientReflection", "diffuseReflection", "specularReflection", "transparencyAttenuation", "emissionAttenuation", "surfaceColor", "specularColor", "emissionColor", "fillId", "transparency", "shine", "texture", )

    def __init__(self, attributeId: AttributeId, name: str, materialType: str, ambientReflection: int, diffuseReflection: int, specularReflection: int, transparencyAttenuation: int, emissionAttenuation: int, surfaceColor: RGBColor, specularColor: RGBColor, emissionColor: RGBColor, fillId: AttributeIdOrError, transparency: int, shine: int, texture: Optional[Texture] = None):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.materialType: str = materialType
        self.ambientReflection: int = ambientReflection
        self.diffuseReflection: int = diffuseReflection
        self.specularReflection: int = specularReflection
        self.transparencyAttenuation: int = transparencyAttenuation
        self.emissionAttenuation: int = emissionAttenuation
        self.surfaceColor: RGBColor = surfaceColor
        self.specularColor: RGBColor = specularColor
        self.emissionColor: RGBColor = emissionColor
        self.fillId: AttributeIdOrError = fillId
        self.transparency: int = transparency
        self.shine: int = shine
        self.texture: Optional[Texture] = texture

SurfaceAttribute.get_classinfo().add_field('attributeId', AttributeId)
SurfaceAttribute.get_classinfo().add_field('name', str)
SurfaceAttribute.get_classinfo().add_field('materialType', str, value_set(['General', 'Simple', 'Matte', 'Metal', 'Plastic', 'Glass', 'Glowing', 'Constant']))
SurfaceAttribute.get_classinfo().add_field('ambientReflection', int, maximum(100, False))
SurfaceAttribute.get_classinfo().add_field('diffuseReflection', int, maximum(100, False))
SurfaceAttribute.get_classinfo().add_field('specularReflection', int, maximum(100, False))
SurfaceAttribute.get_classinfo().add_field('transparencyAttenuation', int, maximum(400, False))
SurfaceAttribute.get_classinfo().add_field('emissionAttenuation', int, maximum(65535, False))
SurfaceAttribute.get_classinfo().add_field('surfaceColor', RGBColor)
SurfaceAttribute.get_classinfo().add_field('specularColor', RGBColor)
SurfaceAttribute.get_classinfo().add_field('emissionColor', RGBColor)
SurfaceAttribute.get_classinfo().add_field('fillId', AttributeIdOrError)
SurfaceAttribute.get_classinfo().add_field('transparency', int, maximum(100, False))
SurfaceAttribute.get_classinfo().add_field('shine', int, maximum(10000, False))
SurfaceAttribute.get_classinfo().add_field('texture', Optional[Texture])


class ProfileAttributeOrError(_ACUnionType):
    """ A profile attribute or an error.

    Attributes:
        profileAttribute (:obj:`ProfileAttribute`, optional): A profile attribute.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("profileAttribute", "error", )

    constructor  = _ConstructUnion(Union[ProfileAttributeWrapper, ErrorItem])

    def __new__(cls, profileAttribute: Optional[ProfileAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(profileAttribute=profileAttribute, error=error)

    def __init__(self, profileAttribute: Optional[ProfileAttribute] = None, error: Optional[Error] = None):
        self.profileAttribute: Optional[ProfileAttribute] = profileAttribute
        self.error: Optional[Error] = error


class CompositeLine(_ACBaseType):
    """ A contour or separator line component for a composite attribute.

    Attributes:
        lineId (:obj:`AttributeIdOrError`): The attribute's identifier or an error.
        linePenIndex (:obj:`int`, optional): The index number of a pen.

    """
    __slots__ = ("lineId", "linePenIndex", )

    def __init__(self, lineId: AttributeIdOrError, linePenIndex: Optional[int] = None):
        self.lineId: AttributeIdOrError = lineId
        self.linePenIndex: Optional[int] = linePenIndex

CompositeLine.get_classinfo().add_field('lineId', AttributeIdOrError)
CompositeLine.get_classinfo().add_field('linePenIndex', Optional[int], maximum(255, False))


class CompositeLineListItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        compositeLine (:obj:`CompositeLine`): A contour or separator line component for a composite attribute.

    """
    __slots__ = ("compositeLine", )

    def __init__(self, compositeLine: CompositeLine):
        self.compositeLine: CompositeLine = compositeLine

CompositeLineListItem.get_classinfo().add_field('compositeLine', CompositeLine)


class CompositeSkin(_ACBaseType):
    """ A skin component for a composite attribute.

    Attributes:
        buildingMaterialId (:obj:`AttributeIdOrError`): The attribute's identifier or an error.
        thickness (:obj:`float`): The thickness of the composite skin.
        isCore (:obj:`bool`): Defines whether the composite skin is part of the core or not.
        isFinish (:obj:`bool`): Defines whether the composite skin is part of the finish or not.
        framePenIndex (:obj:`int`, optional): The index number of a pen.

    """
    __slots__ = ("buildingMaterialId", "thickness", "isCore", "isFinish", "framePenIndex", )

    def __init__(self, buildingMaterialId: AttributeIdOrError, thickness: float, isCore: bool, isFinish: bool, framePenIndex: Optional[int] = None):
        self.buildingMaterialId: AttributeIdOrError = buildingMaterialId
        self.thickness: float = thickness
        self.isCore: bool = isCore
        self.isFinish: bool = isFinish
        self.framePenIndex: Optional[int] = framePenIndex

CompositeSkin.get_classinfo().add_field('buildingMaterialId', AttributeIdOrError)
CompositeSkin.get_classinfo().add_field('thickness', float)
CompositeSkin.get_classinfo().add_field('isCore', bool)
CompositeSkin.get_classinfo().add_field('isFinish', bool)
CompositeSkin.get_classinfo().add_field('framePenIndex', Optional[int], maximum(255, False))


class CompositeSkinListItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        compositeSkin (:obj:`CompositeSkin`): A skin component for a composite attribute.

    """
    __slots__ = ("compositeSkin", )

    def __init__(self, compositeSkin: CompositeSkin):
        self.compositeSkin: CompositeSkin = compositeSkin

CompositeSkinListItem.get_classinfo().add_field('compositeSkin', CompositeSkin)


class CompositeAttribute(_ACBaseType):
    """ A composite attribute.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        totalThickness (:obj:`float`): The total thickness of the composite.
        compositeSkins (:obj:`list` of :obj:`CompositeSkinListItem`): A list of composite skins.
        compositeLines (:obj:`list` of :obj:`CompositeLineListItem`): A list of contour/separator lines for the composite.
        useWith (:obj:`list` of :obj:`str`): A list of element types.

    """
    __slots__ = ("attributeId", "name", "totalThickness", "compositeSkins", "compositeLines", "useWith", )

    def __init__(self, attributeId: AttributeId, name: str, totalThickness: float, compositeSkins: List[CompositeSkinListItem], compositeLines: List[CompositeLineListItem], useWith: List[str]):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.totalThickness: float = totalThickness
        self.compositeSkins: List[CompositeSkinListItem] = compositeSkins
        self.compositeLines: List[CompositeLineListItem] = compositeLines
        self.useWith: List[str] = useWith

CompositeAttribute.get_classinfo().add_field('attributeId', AttributeId)
CompositeAttribute.get_classinfo().add_field('name', str)
CompositeAttribute.get_classinfo().add_field('totalThickness', float)
CompositeAttribute.get_classinfo().add_field('compositeSkins', List[CompositeSkinListItem])
CompositeAttribute.get_classinfo().add_field('compositeLines', List[CompositeLineListItem])
CompositeAttribute.get_classinfo().add_field('useWith', List[str], listitem_validator(value_set(['Wall', 'Column', 'Beam', 'Window', 'Door', 'Object', 'Lamp', 'Slab', 'Roof', 'Mesh', 'Zone', 'CurtainWall', 'Shell', 'Skylight', 'Morph', 'Stair', 'Railing', 'Opening'])))


class Pen(_ACBaseType):
    """ A pen attribute.

    Attributes:
        name (:obj:`str`): The name of the pen.
        index (:obj:`int`): The index number of a pen.
        color (:obj:`RGBColor`): A color model represented via its red, green and blue components.
        weight (:obj:`float`): The thickness of the pen defined in millimeters.
        description (:obj:`str`): The description of the pen.

    """
    __slots__ = ("name", "index", "color", "weight", "description", )

    def __init__(self, name: str, index: int, color: RGBColor, weight: float, description: str):
        self.name: str = name
        self.index: int = index
        self.color: RGBColor = color
        self.weight: float = weight
        self.description: str = description

Pen.get_classinfo().add_field('name', str, min_length(1))
Pen.get_classinfo().add_field('index', int, maximum(255, False))
Pen.get_classinfo().add_field('color', RGBColor)
Pen.get_classinfo().add_field('weight', float)
Pen.get_classinfo().add_field('description', str)


class PenArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        pen (:obj:`Pen`): A pen attribute.

    """
    __slots__ = ("pen", )

    def __init__(self, pen: Pen):
        self.pen: Pen = pen

PenArrayItem.get_classinfo().add_field('pen', Pen)


class LineItem(_ACBaseType):
    """ A line item.

    Attributes:
        lineItemType (:obj:`str`): The type of a line item.
        centerOffset (:obj:`float`): The vertical distance from the origin of the symbol line. Used in separator, center dot, and centerline item types.
        length (:obj:`float`): The length of the item. Used in centerline, right angle, and parallel item types.
        begPosition (:obj:`Point2D`): EMPTY STRING
        endPosition (:obj:`Point2D`): EMPTY STRING
        radius (:obj:`float`): The radius of the item. Used in circle and arc item types.
        begAngle (:obj:`float`): The beginning angle of the item, measured from the vertical axis. Used in the arc item type.
        endAngle (:obj:`float`): The ending angle of the item, measured from the vertical axis. Used in the arc item type.

    """
    __slots__ = ("lineItemType", "centerOffset", "length", "begPosition", "endPosition", "radius", "begAngle", "endAngle", )

    def __init__(self, lineItemType: str, centerOffset: float, length: float, begPosition: Point2D, endPosition: Point2D, radius: float, begAngle: float, endAngle: float):
        self.lineItemType: str = lineItemType
        self.centerOffset: float = centerOffset
        self.length: float = length
        self.begPosition: Point2D = begPosition
        self.endPosition: Point2D = endPosition
        self.radius: float = radius
        self.begAngle: float = begAngle
        self.endAngle: float = endAngle

LineItem.get_classinfo().add_field('lineItemType', str, value_set(['IllegalItemType', 'SeparatorItemType', 'CenterDotItemType', 'CenterLineItemType', 'DotItemType', 'RightAngleItemType', 'ParallelItemType', 'LineItemType', 'CircItemType', 'ArcItemType']))
LineItem.get_classinfo().add_field('centerOffset', float)
LineItem.get_classinfo().add_field('length', float)
LineItem.get_classinfo().add_field('begPosition', Point2D)
LineItem.get_classinfo().add_field('endPosition', Point2D)
LineItem.get_classinfo().add_field('radius', float)
LineItem.get_classinfo().add_field('begAngle', float)
LineItem.get_classinfo().add_field('endAngle', float)


class ZoneCategoryAttribute(_ACBaseType):
    """ A zone category.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        categoryCode (:obj:`str`): The category code of the zone.
        stampName (:obj:`str`): The stamp name of the zone category.
        stampMainGuid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.
        stampRevisionGuid (:obj:`UUID`): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.
        color (:obj:`RGBColor`): A color model represented via its red, green and blue components.

    """
    __slots__ = ("attributeId", "name", "categoryCode", "stampName", "stampMainGuid", "stampRevisionGuid", "color", )

    def __init__(self, attributeId: AttributeId, name: str, categoryCode: str, stampName: str, stampMainGuid: UUID, stampRevisionGuid: UUID, color: RGBColor):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.categoryCode: str = categoryCode
        self.stampName: str = stampName
        self.stampMainGuid: UUID = stampMainGuid
        self.stampRevisionGuid: UUID = stampRevisionGuid
        self.color: RGBColor = color

ZoneCategoryAttribute.get_classinfo().add_field('attributeId', AttributeId)
ZoneCategoryAttribute.get_classinfo().add_field('name', str)
ZoneCategoryAttribute.get_classinfo().add_field('categoryCode', str)
ZoneCategoryAttribute.get_classinfo().add_field('stampName', str)
ZoneCategoryAttribute.get_classinfo().add_field('stampMainGuid', UUID)
ZoneCategoryAttribute.get_classinfo().add_field('stampRevisionGuid', UUID)
ZoneCategoryAttribute.get_classinfo().add_field('color', RGBColor)


class BuildingMaterialAttribute(_ACBaseType):
    """ A building material attribute

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        id (:obj:`str`): The id of the building material.
        connectionPriority (:obj:`int`): The connection priority of the building material.
        cutFillId (:obj:`AttributeIdOrError`): The attribute's identifier or an error.
        cutFillPenIndex (:obj:`int`): The index number of a pen.
        cutSurfaceId (:obj:`AttributeIdOrError`): The attribute's identifier or an error.

    """
    __slots__ = ("attributeId", "name", "id", "connectionPriority", "cutFillId", "cutFillPenIndex", "cutSurfaceId", )

    def __init__(self, attributeId: AttributeId, name: str, id: str, connectionPriority: int, cutFillId: AttributeIdOrError, cutFillPenIndex: int, cutSurfaceId: AttributeIdOrError):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.id: str = id
        self.connectionPriority: int = connectionPriority
        self.cutFillId: AttributeIdOrError = cutFillId
        self.cutFillPenIndex: int = cutFillPenIndex
        self.cutSurfaceId: AttributeIdOrError = cutSurfaceId

BuildingMaterialAttribute.get_classinfo().add_field('attributeId', AttributeId)
BuildingMaterialAttribute.get_classinfo().add_field('name', str)
BuildingMaterialAttribute.get_classinfo().add_field('id', str)
BuildingMaterialAttribute.get_classinfo().add_field('connectionPriority', int)
BuildingMaterialAttribute.get_classinfo().add_field('cutFillId', AttributeIdOrError)
BuildingMaterialAttribute.get_classinfo().add_field('cutFillPenIndex', int, maximum(255, False))
BuildingMaterialAttribute.get_classinfo().add_field('cutSurfaceId', AttributeIdOrError)


class LayerCombinationAttributeOrError(_ACUnionType):
    """ A layer combination attribute or an error.

    Attributes:
        layerCombinationAttribute (:obj:`LayerCombinationAttribute`, optional): A layer combination attribute
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("layerCombinationAttribute", "error", )

    constructor  = _ConstructUnion(Union[LayerCombinationAttributeWrapper, ErrorItem])

    def __new__(cls, layerCombinationAttribute: Optional[LayerCombinationAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(layerCombinationAttribute=layerCombinationAttribute, error=error)

    def __init__(self, layerCombinationAttribute: Optional[LayerCombinationAttribute] = None, error: Optional[Error] = None):
        self.layerCombinationAttribute: Optional[LayerCombinationAttribute] = layerCombinationAttribute
        self.error: Optional[Error] = error


class ClassificationIdOrError(_ACUnionType):
    """ EMPTY STRING

    Attributes:
        classificationId (:obj:`ClassificationId`, optional): The element classification identifier.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("classificationId", "error", )

    constructor  = _ConstructUnion(Union[ClassificationIdWrapper, ErrorItem])

    def __new__(cls, classificationId: Optional[ClassificationId] = None, error: Optional[Error] = None):
        return cls.constructor(classificationId=classificationId, error=error)

    def __init__(self, classificationId: Optional[ClassificationId] = None, error: Optional[Error] = None):
        self.classificationId: Optional[ClassificationId] = classificationId
        self.error: Optional[Error] = error


class ElementClassification(_ACBaseType):
    """ The classification of an element.

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
        classificationItem (:obj:`ClassificationItemDetails`, optional): The details of a classification item.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("classificationItem", "error", )

    constructor  = _ConstructUnion(Union[ClassificationItemDetailsWrapper, ErrorItem])

    def __new__(cls, classificationItem: Optional[ClassificationItemDetails] = None, error: Optional[Error] = None):
        return cls.constructor(classificationItem=classificationItem, error=error)

    def __init__(self, classificationItem: Optional[ClassificationItemDetails] = None, error: Optional[Error] = None):
        self.classificationItem: Optional[ClassificationItemDetails] = classificationItem
        self.error: Optional[Error] = error


class PropertyIdOrError(_ACUnionType):
    """ A property identifier or an error.

    Attributes:
        propertyId (:obj:`PropertyId`, optional): The identifier of a property.
        error (:obj:`Error`, optional): The details of an error.

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
        possibleEnumValues (:obj:`list` of :obj:`PossibleEnumValuesArrayItem`, optional): A list of enumeration values.

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
        value (:obj:`list` of :obj:`EnumValueIdWrapper`): A list of enumeration identifiers.
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


class ImageOrError(_ACUnionType):
    """ An image or an error.

    Attributes:
        image (:obj:`Image`, optional): An image encoded as a Base64 string.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("image", "error", )

    constructor  = _ConstructUnion(Union[ImageWrapper, ErrorItem])

    def __new__(cls, image: Optional[Image] = None, error: Optional[Error] = None):
        return cls.constructor(image=image, error=error)

    def __init__(self, image: Optional[Image] = None, error: Optional[Error] = None):
        self.image: Optional[Image] = image
        self.error: Optional[Error] = error


class BoundingBox2DOrError(_ACUnionType):
    """ A 2D bounding box or an error.

    Attributes:
        boundingBox2D (:obj:`BoundingBox2D`, optional): The 2D bounding box of an element.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("boundingBox2D", "error", )

    constructor  = _ConstructUnion(Union[BoundingBox2DWrapper, ErrorItem])

    def __new__(cls, boundingBox2D: Optional[BoundingBox2D] = None, error: Optional[Error] = None):
        return cls.constructor(boundingBox2D=boundingBox2D, error=error)

    def __init__(self, boundingBox2D: Optional[BoundingBox2D] = None, error: Optional[Error] = None):
        self.boundingBox2D: Optional[BoundingBox2D] = boundingBox2D
        self.error: Optional[Error] = error


class BoundingBox3DOrError(_ACUnionType):
    """ A 3D bounding box or an error.

    Attributes:
        boundingBox3D (:obj:`BoundingBox3D`, optional): A 3D bounding box of an element.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("boundingBox3D", "error", )

    constructor  = _ConstructUnion(Union[BoundingBox3DWrapper, ErrorItem])

    def __new__(cls, boundingBox3D: Optional[BoundingBox3D] = None, error: Optional[Error] = None):
        return cls.constructor(boundingBox3D=boundingBox3D, error=error)

    def __init__(self, boundingBox3D: Optional[BoundingBox3D] = None, error: Optional[Error] = None):
        self.boundingBox3D: Optional[BoundingBox3D] = boundingBox3D
        self.error: Optional[Error] = error


class SurfaceAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        surfaceAttribute (:obj:`SurfaceAttribute`): A surface attribute.

    """
    __slots__ = ("surfaceAttribute", )

    def __init__(self, surfaceAttribute: SurfaceAttribute):
        self.surfaceAttribute: SurfaceAttribute = surfaceAttribute

SurfaceAttributeWrapper.get_classinfo().add_field('surfaceAttribute', SurfaceAttribute)


class CompositeAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        compositeAttribute (:obj:`CompositeAttribute`): A composite attribute.

    """
    __slots__ = ("compositeAttribute", )

    def __init__(self, compositeAttribute: CompositeAttribute):
        self.compositeAttribute: CompositeAttribute = compositeAttribute

CompositeAttributeWrapper.get_classinfo().add_field('compositeAttribute', CompositeAttribute)


class LineItemWrapper(_ACBaseType):
    """ 

    Attributes:
        lineItem (:obj:`LineItem`): A line item.

    """
    __slots__ = ("lineItem", )

    def __init__(self, lineItem: LineItem):
        self.lineItem: LineItem = lineItem

LineItemWrapper.get_classinfo().add_field('lineItem', LineItem)


class ZoneCategoryAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        zoneCategoryAttribute (:obj:`ZoneCategoryAttribute`): A zone category.

    """
    __slots__ = ("zoneCategoryAttribute", )

    def __init__(self, zoneCategoryAttribute: ZoneCategoryAttribute):
        self.zoneCategoryAttribute: ZoneCategoryAttribute = zoneCategoryAttribute

ZoneCategoryAttributeWrapper.get_classinfo().add_field('zoneCategoryAttribute', ZoneCategoryAttribute)


class BuildingMaterialAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        buildingMaterialAttribute (:obj:`BuildingMaterialAttribute`): A building material attribute

    """
    __slots__ = ("buildingMaterialAttribute", )

    def __init__(self, buildingMaterialAttribute: BuildingMaterialAttribute):
        self.buildingMaterialAttribute: BuildingMaterialAttribute = buildingMaterialAttribute

BuildingMaterialAttributeWrapper.get_classinfo().add_field('buildingMaterialAttribute', BuildingMaterialAttribute)


class ClassificationIdsOrErrorsWrapper(_ACBaseType):
    """ 

    Attributes:
        classificationIds (:obj:`list` of :obj:`ClassificationIdOrError`): A list of element classification identifiers or errors.

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


class PenTableAttribute(_ACBaseType):
    """ A pen table attribute.

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        pens (:obj:`list` of :obj:`PenArrayItem`): A collection of pens in a pen table.

    """
    __slots__ = ("attributeId", "name", "pens", )

    def __init__(self, attributeId: AttributeId, name: str, pens: List[PenArrayItem]):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.pens: List[PenArrayItem] = pens

PenTableAttribute.get_classinfo().add_field('attributeId', AttributeId)
PenTableAttribute.get_classinfo().add_field('name', str)
PenTableAttribute.get_classinfo().add_field('pens', List[PenArrayItem])


class SurfaceAttributeOrError(_ACUnionType):
    """ A surface attribute or an error.

    Attributes:
        surfaceAttribute (:obj:`SurfaceAttribute`, optional): A surface attribute.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("surfaceAttribute", "error", )

    constructor  = _ConstructUnion(Union[SurfaceAttributeWrapper, ErrorItem])

    def __new__(cls, surfaceAttribute: Optional[SurfaceAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(surfaceAttribute=surfaceAttribute, error=error)

    def __init__(self, surfaceAttribute: Optional[SurfaceAttribute] = None, error: Optional[Error] = None):
        self.surfaceAttribute: Optional[SurfaceAttribute] = surfaceAttribute
        self.error: Optional[Error] = error


class CompositeAttributeOrError(_ACUnionType):
    """ A composite attribute or an error.

    Attributes:
        compositeAttribute (:obj:`CompositeAttribute`, optional): A composite attribute.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("compositeAttribute", "error", )

    constructor  = _ConstructUnion(Union[CompositeAttributeWrapper, ErrorItem])

    def __new__(cls, compositeAttribute: Optional[CompositeAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(compositeAttribute=compositeAttribute, error=error)

    def __init__(self, compositeAttribute: Optional[CompositeAttribute] = None, error: Optional[Error] = None):
        self.compositeAttribute: Optional[CompositeAttribute] = compositeAttribute
        self.error: Optional[Error] = error


class DashOrLineItem(_ACUnionType):
    """ A dash or line item.

    Attributes:
        dashItem (:obj:`DashItem`, optional): A dash item.
        lineItem (:obj:`LineItem`, optional): A line item.

    """
    __slots__ = ("dashItem", "lineItem", )

    constructor  = _ConstructUnion(Union[DashItemWrapper, LineItemWrapper])

    def __new__(cls, dashItem: Optional[DashItem] = None, lineItem: Optional[LineItem] = None):
        return cls.constructor(dashItem=dashItem, lineItem=lineItem)

    def __init__(self, dashItem: Optional[DashItem] = None, lineItem: Optional[LineItem] = None):
        self.dashItem: Optional[DashItem] = dashItem
        self.lineItem: Optional[LineItem] = lineItem


class LineAttribute(_ACBaseType):
    """ A line attribute

    Attributes:
        attributeId (:obj:`AttributeId`): The identifier of an attribute.
        name (:obj:`str`): The name of an attribute.
        appearanceType (:obj:`str`): The appearance type of a line or fill attribute.
        displayScale (:obj:`float`): The original scale of the line.
        period (:obj:`float`): The length of the dashed or symbol line's period.
        height (:obj:`float`): The height of the symbol line.
        lineType (:obj:`str`): The type of a line attribute.
        lineItems (:obj:`list` of :obj:`DashOrLineItem`, optional): A list of dash or line items.

    """
    __slots__ = ("attributeId", "name", "appearanceType", "displayScale", "period", "height", "lineType", "lineItems", )

    def __init__(self, attributeId: AttributeId, name: str, appearanceType: str, displayScale: float, period: float, height: float, lineType: str, lineItems: Optional[List[DashOrLineItem]] = None):
        self.attributeId: AttributeId = attributeId
        self.name: str = name
        self.appearanceType: str = appearanceType
        self.displayScale: float = displayScale
        self.period: float = period
        self.height: float = height
        self.lineType: str = lineType
        self.lineItems: Optional[List[DashOrLineItem]] = lineItems

LineAttribute.get_classinfo().add_field('attributeId', AttributeId)
LineAttribute.get_classinfo().add_field('name', str)
LineAttribute.get_classinfo().add_field('appearanceType', str, value_set(['ScaleWithPlan', 'ScaleIndependent']))
LineAttribute.get_classinfo().add_field('displayScale', float)
LineAttribute.get_classinfo().add_field('period', float)
LineAttribute.get_classinfo().add_field('height', float)
LineAttribute.get_classinfo().add_field('lineType', str, value_set(['SolidLine', 'DashedLine', 'SymbolLine']))
LineAttribute.get_classinfo().add_field('lineItems', Optional[List[DashOrLineItem]])


class ZoneCategoryAttributeOrError(_ACUnionType):
    """ A zone category attribute or an error.

    Attributes:
        zoneCategoryAttribute (:obj:`ZoneCategoryAttribute`, optional): A zone category.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("zoneCategoryAttribute", "error", )

    constructor  = _ConstructUnion(Union[ZoneCategoryAttributeWrapper, ErrorItem])

    def __new__(cls, zoneCategoryAttribute: Optional[ZoneCategoryAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(zoneCategoryAttribute=zoneCategoryAttribute, error=error)

    def __init__(self, zoneCategoryAttribute: Optional[ZoneCategoryAttribute] = None, error: Optional[Error] = None):
        self.zoneCategoryAttribute: Optional[ZoneCategoryAttribute] = zoneCategoryAttribute
        self.error: Optional[Error] = error


class BuildingMaterialAttributeOrError(_ACUnionType):
    """ A building material attribute or an error.

    Attributes:
        buildingMaterialAttribute (:obj:`BuildingMaterialAttribute`, optional): A building material attribute
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("buildingMaterialAttribute", "error", )

    constructor  = _ConstructUnion(Union[BuildingMaterialAttributeWrapper, ErrorItem])

    def __new__(cls, buildingMaterialAttribute: Optional[BuildingMaterialAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(buildingMaterialAttribute=buildingMaterialAttribute, error=error)

    def __init__(self, buildingMaterialAttribute: Optional[BuildingMaterialAttribute] = None, error: Optional[Error] = None):
        self.buildingMaterialAttribute: Optional[BuildingMaterialAttribute] = buildingMaterialAttribute
        self.error: Optional[Error] = error


class ElementClassificationOrError(_ACUnionType):
    """ Element classification identifiers or errors.

    Attributes:
        classificationIds (:obj:`list` of :obj:`ClassificationIdOrError`, optional): A list of element classification identifiers or errors.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("classificationIds", "error", )

    constructor  = _ConstructUnion(Union[ClassificationIdsOrErrorsWrapper, ErrorItem])

    def __new__(cls, classificationIds: Optional[List[ClassificationIdOrError]] = None, error: Optional[Error] = None):
        return cls.constructor(classificationIds=classificationIds, error=error)

    def __init__(self, classificationIds: Optional[List[ClassificationIdOrError]] = None, error: Optional[Error] = None):
        self.classificationIds: Optional[List[ClassificationIdOrError]] = classificationIds
        self.error: Optional[Error] = error


class PropertyDefinitionOrError(_ACUnionType):
    """ A property definition or an error.

    Attributes:
        propertyDefinition (:obj:`PropertyDefinition`, optional): A property definition.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("propertyDefinition", "error", )

    constructor  = _ConstructUnion(Union[PropertyDefinitionWrapper, ErrorItem])

    def __new__(cls, propertyDefinition: Optional[PropertyDefinition] = None, error: Optional[Error] = None):
        return cls.constructor(propertyDefinition=propertyDefinition, error=error)

    def __init__(self, propertyDefinition: Optional[PropertyDefinition] = None, error: Optional[Error] = None):
        self.propertyDefinition: Optional[PropertyDefinition] = propertyDefinition
        self.error: Optional[Error] = error


class PenTableAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        penTableAttribute (:obj:`PenTableAttribute`): A pen table attribute.

    """
    __slots__ = ("penTableAttribute", )

    def __init__(self, penTableAttribute: PenTableAttribute):
        self.penTableAttribute: PenTableAttribute = penTableAttribute

PenTableAttributeWrapper.get_classinfo().add_field('penTableAttribute', PenTableAttribute)


class LineAttributeWrapper(_ACBaseType):
    """ 

    Attributes:
        lineAttribute (:obj:`LineAttribute`): A line attribute

    """
    __slots__ = ("lineAttribute", )

    def __init__(self, lineAttribute: LineAttribute):
        self.lineAttribute: LineAttribute = lineAttribute

LineAttributeWrapper.get_classinfo().add_field('lineAttribute', LineAttribute)


class PenTableAttributeOrError(_ACUnionType):
    """ A pen table attribute or an error.

    Attributes:
        penTableAttribute (:obj:`PenTableAttribute`, optional): A pen table attribute.
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("penTableAttribute", "error", )

    constructor  = _ConstructUnion(Union[PenTableAttributeWrapper, ErrorItem])

    def __new__(cls, penTableAttribute: Optional[PenTableAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(penTableAttribute=penTableAttribute, error=error)

    def __init__(self, penTableAttribute: Optional[PenTableAttribute] = None, error: Optional[Error] = None):
        self.penTableAttribute: Optional[PenTableAttribute] = penTableAttribute
        self.error: Optional[Error] = error


class LineAttributeOrError(_ACUnionType):
    """ A line attribute or an error.

    Attributes:
        lineAttribute (:obj:`LineAttribute`, optional): A line attribute
        error (:obj:`Error`, optional): The details of an error.

    """
    __slots__ = ("lineAttribute", "error", )

    constructor  = _ConstructUnion(Union[LineAttributeWrapper, ErrorItem])

    def __new__(cls, lineAttribute: Optional[LineAttribute] = None, error: Optional[Error] = None):
        return cls.constructor(lineAttribute=lineAttribute, error=error)

    def __init__(self, lineAttribute: Optional[LineAttribute] = None, error: Optional[Error] = None):
        self.lineAttribute: Optional[LineAttribute] = lineAttribute
        self.error: Optional[Error] = error


class ClassificationItemInTree_: pass
class ClassificationItemArrayItem(_ACBaseType):
    """ EMPTY STRING

    Attributes:
        classificationItem (:obj:`ClassificationItemInTree_`): The details of a classification item.

    """
    __slots__ = ("classificationItem", )

    def __init__(self, classificationItem: ClassificationItemInTree_):
        self.classificationItem: ClassificationItemInTree_ = classificationItem


class ClassificationItemInTree(_ACBaseType):
    """ The details of a classification item.

    Attributes:
        classificationItemId (:obj:`ClassificationItemId`): The identifier of a classification item.
        id (:obj:`str`): The unique identifier of the classification item as specified by the user.
        name (:obj:`str`): The display name of the classification item.
        description (:obj:`str`): The description of the classification item.
        children (:obj:`list` of :obj:`ClassificationItemArrayItem`, optional): A list of classification items.

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
        value (:obj:`float`, :obj:`int`, :obj:`str`, :obj:`bool`, :obj:`list` of :obj:`float`, :obj:`list` of :obj:`int`, :obj:`list` of :obj:`str`, :obj:`list` of :obj:`bool`, :obj:`EnumValueId`, :obj:`list` of :obj:`EnumValueIdWrapper`): None; The identifier of a property enumeration value.; A list of enumeration identifiers.

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
    """ A property value with the identifiers of the property and its owner element.

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
        value (:obj:`float`, :obj:`int`, :obj:`str`, :obj:`bool`, :obj:`list` of :obj:`float`, :obj:`list` of :obj:`int`, :obj:`list` of :obj:`str`, :obj:`list` of :obj:`bool`, :obj:`EnumValueId`, :obj:`list` of :obj:`EnumValueIdWrapper`): None; The identifier of a property enumeration value.; A list of enumeration identifiers.

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
    """ A property value or an error

    Attributes:
        propertyValue (:obj:`PropertyValue`, optional): A normal, userUndefined, notAvailable or notEvaluated property value.
        error (:obj:`Error`, optional): The details of an error.

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
        propertyValues (:obj:`list` of :obj:`PropertyValueOrErrorItem`): A list of property values.

    """
    __slots__ = ("propertyValues", )

    def __init__(self, propertyValues: List[PropertyValueOrErrorItem]):
        self.propertyValues: List[PropertyValueOrErrorItem] = propertyValues

PropertyValuesWrapper.get_classinfo().add_field('propertyValues', List[PropertyValueOrErrorItem])


class PropertyValuesOrError(_ACUnionType):
    """ A list of property values or an error.

    Attributes:
        propertyValues (:obj:`list` of :obj:`PropertyValueOrErrorItem`, optional): A list of property values.
        error (:obj:`Error`, optional): The details of an error.

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
        navigatorItem (:obj:`NavigatorItem_`): The details of a navigator item.

    """
    __slots__ = ("navigatorItem", )

    def __init__(self, navigatorItem: NavigatorItem_):
        self.navigatorItem: NavigatorItem_ = navigatorItem


class NavigatorItem(_ACBaseType):
    """ The details of a navigator item.

    Attributes:
        navigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
        prefix (:obj:`str`): The prefix of the navigator item's name.
        name (:obj:`str`): The name of the navigator item.
        type (:obj:`str`): The types of a navigator item. The 'UndefinedItem' type is used when the actual type of the navigator item cannot be retrieved from ARCHICAD.
        sourceNavigatorItemId (:obj:`NavigatorItemId`, optional): The identifier of a navigator item.
        children (:obj:`list` of :obj:`NavigatorItemArrayItem`, optional): A list of navigator items.

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
        rootItem (:obj:`NavigatorItem`): The details of a navigator item.

    """
    __slots__ = ("rootItem", )

    def __init__(self, rootItem: NavigatorItem):
        self.rootItem: NavigatorItem = rootItem

NavigatorTree.get_classinfo().add_field('rootItem', NavigatorItem)


class Types:
    """ 
    """
    AddOnCommandId=AddOnCommandId
    AddOnCommandIdArrayItem=AddOnCommandIdArrayItem
    AddOnCommandParameters=AddOnCommandParameters
    AddOnCommandResponse=AddOnCommandResponse
    AttributeId=AttributeId
    AttributeIdWrapperItem=AttributeIdWrapperItem
    AttributeHeader=AttributeHeader
    LayerAttribute=LayerAttribute
    FillAttribute=FillAttribute
    ProfileModifier=ProfileModifier
    ProfileModifierListItem=ProfileModifierListItem
    ProfileAttribute=ProfileAttribute
    Texture=Texture
    DashItem=DashItem
    LayerCombinationAttribute=LayerCombinationAttribute
    ClassificationSystemId=ClassificationSystemId
    ClassificationSystemIdArrayItem=ClassificationSystemIdArrayItem
    ClassificationItemId=ClassificationItemId
    ClassificationItemIdArrayItem=ClassificationItemIdArrayItem
    ClassificationId=ClassificationId
    ClassificationItemDetails=ClassificationItemDetails
    ClassificationSystem=ClassificationSystem
    Point2D=Point2D
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
    NonLocalizedValueEnumId=NonLocalizedValueEnumId
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
    Image=Image
    NavigatorItemId=NavigatorItemId
    PublisherSetId=PublisherSetId
    OtherNavigatorTreeId=OtherNavigatorTreeId
    FolderParameters=FolderParameters
    NavigatorTreeId=NavigatorTreeId
    BoundingBox2D=BoundingBox2D
    BoundingBox3D=BoundingBox3D
    RGBColor=RGBColor
    Subset=Subset
    LayoutParameters=LayoutParameters
    ComponentId=ComponentId
    ElementComponentId=ElementComponentId
    ElementComponentIdArrayItem=ElementComponentIdArrayItem
    ElementComponentsWrapper=ElementComponentsWrapper
    ElementComponentsOrError=ElementComponentsOrError
    LayerAttributeWrapper=LayerAttributeWrapper
    FillAttributeWrapper=FillAttributeWrapper
    ProfileAttributeWrapper=ProfileAttributeWrapper
    DashItemWrapper=DashItemWrapper
    LayerCombinationAttributeWrapper=LayerCombinationAttributeWrapper
    ClassificationIdWrapper=ClassificationIdWrapper
    ClassificationItemDetailsWrapper=ClassificationItemDetailsWrapper
    EnumValueIdWrapper=EnumValueIdWrapper
    ImageWrapper=ImageWrapper
    NavigatorItemIdWrapper=NavigatorItemIdWrapper
    BoundingBox2DWrapper=BoundingBox2DWrapper
    BoundingBox3DWrapper=BoundingBox3DWrapper
    AttributeIdOrError=AttributeIdOrError
    LayerAttributeOrError=LayerAttributeOrError
    FillAttributeOrError=FillAttributeOrError
    SurfaceAttribute=SurfaceAttribute
    ProfileAttributeOrError=ProfileAttributeOrError
    CompositeLine=CompositeLine
    CompositeLineListItem=CompositeLineListItem
    CompositeSkin=CompositeSkin
    CompositeSkinListItem=CompositeSkinListItem
    CompositeAttribute=CompositeAttribute
    Pen=Pen
    PenArrayItem=PenArrayItem
    LineItem=LineItem
    ZoneCategoryAttribute=ZoneCategoryAttribute
    BuildingMaterialAttribute=BuildingMaterialAttribute
    LayerCombinationAttributeOrError=LayerCombinationAttributeOrError
    ClassificationIdOrError=ClassificationIdOrError
    ElementClassification=ElementClassification
    ClassificationItemOrError=ClassificationItemOrError
    PropertyIdOrError=PropertyIdOrError
    PropertyDefinition=PropertyDefinition
    NormalSingleEnumPropertyValue=NormalSingleEnumPropertyValue
    NormalMultiEnumPropertyValue=NormalMultiEnumPropertyValue
    ImageOrError=ImageOrError
    BoundingBox2DOrError=BoundingBox2DOrError
    BoundingBox3DOrError=BoundingBox3DOrError
    SurfaceAttributeWrapper=SurfaceAttributeWrapper
    CompositeAttributeWrapper=CompositeAttributeWrapper
    LineItemWrapper=LineItemWrapper
    ZoneCategoryAttributeWrapper=ZoneCategoryAttributeWrapper
    BuildingMaterialAttributeWrapper=BuildingMaterialAttributeWrapper
    ClassificationIdsOrErrorsWrapper=ClassificationIdsOrErrorsWrapper
    PropertyDefinitionWrapper=PropertyDefinitionWrapper
    PenTableAttribute=PenTableAttribute
    SurfaceAttributeOrError=SurfaceAttributeOrError
    CompositeAttributeOrError=CompositeAttributeOrError
    DashOrLineItem=DashOrLineItem
    LineAttribute=LineAttribute
    ZoneCategoryAttributeOrError=ZoneCategoryAttributeOrError
    BuildingMaterialAttributeOrError=BuildingMaterialAttributeOrError
    ElementClassificationOrError=ElementClassificationOrError
    PropertyDefinitionOrError=PropertyDefinitionOrError
    PenTableAttributeWrapper=PenTableAttributeWrapper
    LineAttributeWrapper=LineAttributeWrapper
    PenTableAttributeOrError=PenTableAttributeOrError
    LineAttributeOrError=LineAttributeOrError
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

