"""GRAPHISOFT
"""
from typing import Dict, Any, List, Tuple, Optional, Union
from urllib.request import Request, urlopen
import json
from archicad.acbasetype import _ACBaseType, _ConstructUnion, _ListBuilder
from archicad.validators import value_set, matches, min_length, max_length, multiple_of, minimum, maximum, listitem_validator, min_items, max_items, unique_items

from .b2255types import NavigatorItemId, LayoutParameters, Subset, FolderParameters, NavigatorItemIdWrapper, ExecutionResult, AddOnCommandId, AddOnCommandParameters, AddOnCommandResponse, ElementIdArrayItem, BoundingBox2DOrError, BoundingBox3DOrError, AttributeIdOrError, AttributeIdOrError, ClassificationSystemId, ClassificationItemArrayItem, ClassificationSystem, PropertyUserId, AttributeIdWrapperItem, AttributeIdWrapperItem, BuildingMaterialAttributeOrError, ClassificationSystemIdArrayItem, ElementClassificationOrError, ElementComponentsOrError, CompositeAttributeOrError, ClassificationItemIdArrayItem, ClassificationItemOrError, PropertyIdArrayItem, PropertyDefinitionOrError, ClassificationItemId, ElementsOrError, FillAttributeOrError, LayerAttributeOrError, LayerCombinationAttributeOrError, LineAttributeOrError, NavigatorTreeId, NavigatorTree, PenTableAttributeOrError, RGBColor, ImageOrError, ProfileAttributeOrError, PropertyIdOrError, ElementComponentIdArrayItem, PropertyValuesOrError, PropertyValuesOrError, SurfaceAttributeOrError, ZoneCategoryAttributeOrError, ElementClassification, ElementPropertyValue


class UnsucceededCommandCall(Exception):
    pass


def post_command(req: Request, jsonStr: str) -> Dict[str, Any]:
    response = urlopen(req, jsonStr.encode("UTF-8"))
    result = response.read()
    return json.loads(result)


class Commands:
    """Collection of the ARCHICAD JSON interface commands
    """
    def __init__(self, req: Request):
        assert req is not None
        self.__req = req

    def CloneProjectMapItemToViewMap(self, projectMapNavigatorItemId: NavigatorItemId, parentNavigatorItemId: NavigatorItemId) -> NavigatorItemId:
        """Clones a project map item to the view map.

        Args:
            projectMapNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
            parentNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

        Returns:
            :obj:`NavigatorItemId`: The identifier of a navigator item.

        """
        class CloneProjectMapItemToViewMap_parameters(_ACBaseType):
            __slots__ = ("projectMapNavigatorItemId", "parentNavigatorItemId", )
            def __init__(self, projectMapNavigatorItemId: NavigatorItemId, parentNavigatorItemId: NavigatorItemId):
                self.projectMapNavigatorItemId: NavigatorItemId = projectMapNavigatorItemId
                self.parentNavigatorItemId: NavigatorItemId = parentNavigatorItemId

        CloneProjectMapItemToViewMap_parameters.get_classinfo().add_field('projectMapNavigatorItemId', NavigatorItemId)
        CloneProjectMapItemToViewMap_parameters.get_classinfo().add_field('parentNavigatorItemId', NavigatorItemId)

        result = post_command(self.__req, json.dumps({"command": "API.CloneProjectMapItemToViewMap", "parameters": CloneProjectMapItemToViewMap_parameters(projectMapNavigatorItemId, parentNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return NavigatorItemId(**result["result"]["createdNavigatorItemId"])

    def CreateLayout(self, layoutName: str, layoutParameters: LayoutParameters, masterNavigatorItemId: NavigatorItemId, parentNavigatorItemId: NavigatorItemId) -> NavigatorItemId:
        """Creates a new layout.

        Args:
            layoutName (:obj:`str`): The name of the layout.
            layoutParameters (:obj:`LayoutParameters`): The parameters of the layout.
            masterNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
            parentNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

        Returns:
            :obj:`NavigatorItemId`: The identifier of a navigator item.

        """
        class CreateLayout_parameters(_ACBaseType):
            __slots__ = ("layoutName", "layoutParameters", "masterNavigatorItemId", "parentNavigatorItemId", )
            def __init__(self, layoutName: str, layoutParameters: LayoutParameters, masterNavigatorItemId: NavigatorItemId, parentNavigatorItemId: NavigatorItemId):
                self.layoutName: str = layoutName
                self.layoutParameters: LayoutParameters = layoutParameters
                self.masterNavigatorItemId: NavigatorItemId = masterNavigatorItemId
                self.parentNavigatorItemId: NavigatorItemId = parentNavigatorItemId

        CreateLayout_parameters.get_classinfo().add_field('layoutName', str, min_length(1))
        CreateLayout_parameters.get_classinfo().add_field('layoutParameters', LayoutParameters)
        CreateLayout_parameters.get_classinfo().add_field('masterNavigatorItemId', NavigatorItemId)
        CreateLayout_parameters.get_classinfo().add_field('parentNavigatorItemId', NavigatorItemId)

        result = post_command(self.__req, json.dumps({"command": "API.CreateLayout", "parameters": CreateLayout_parameters(layoutName, layoutParameters, masterNavigatorItemId, parentNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return NavigatorItemId(**result["result"]["createdNavigatorItemId"])

    def CreateLayoutSubset(self, subsetParameters: Subset, parentNavigatorItemId: NavigatorItemId) -> NavigatorItemId:
        """Creates a new layout subset.

        Args:
            subsetParameters (:obj:`Subset`): A set of options used to assign IDs to the layouts contained in the subset.
            parentNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

        Returns:
            :obj:`NavigatorItemId`: The identifier of a navigator item.

        """
        class CreateLayoutSubset_parameters(_ACBaseType):
            __slots__ = ("subsetParameters", "parentNavigatorItemId", )
            def __init__(self, subsetParameters: Subset, parentNavigatorItemId: NavigatorItemId):
                self.subsetParameters: Subset = subsetParameters
                self.parentNavigatorItemId: NavigatorItemId = parentNavigatorItemId

        CreateLayoutSubset_parameters.get_classinfo().add_field('subsetParameters', Subset)
        CreateLayoutSubset_parameters.get_classinfo().add_field('parentNavigatorItemId', NavigatorItemId)

        result = post_command(self.__req, json.dumps({"command": "API.CreateLayoutSubset", "parameters": CreateLayoutSubset_parameters(subsetParameters, parentNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return NavigatorItemId(**result["result"]["createdSubsetId"])

    def CreateViewMapFolder(self, folderParameters: FolderParameters, parentNavigatorItemId: Optional[NavigatorItemId] = None, previousNavigatorItemId: Optional[NavigatorItemId] = None) -> NavigatorItemId:
        """Creates a view folder item at the given position in the navigator tree.

        Args:
            folderParameters (:obj:`FolderParameters`): The parameters of a folder.
            parentNavigatorItemId (:obj:`NavigatorItemId`, optional): The identifier of a navigator item.
            previousNavigatorItemId (:obj:`NavigatorItemId`, optional): The identifier of a navigator item.

        Returns:
            :obj:`NavigatorItemId`: The identifier of a navigator item.

        """
        class CreateViewMapFolder_parameters(_ACBaseType):
            __slots__ = ("folderParameters", "parentNavigatorItemId", "previousNavigatorItemId", )
            def __init__(self, folderParameters: FolderParameters, parentNavigatorItemId: Optional[NavigatorItemId] = None, previousNavigatorItemId: Optional[NavigatorItemId] = None):
                self.folderParameters: FolderParameters = folderParameters
                self.parentNavigatorItemId: Optional[NavigatorItemId] = parentNavigatorItemId
                self.previousNavigatorItemId: Optional[NavigatorItemId] = previousNavigatorItemId

        CreateViewMapFolder_parameters.get_classinfo().add_field('folderParameters', FolderParameters)
        CreateViewMapFolder_parameters.get_classinfo().add_field('parentNavigatorItemId', Optional[NavigatorItemId])
        CreateViewMapFolder_parameters.get_classinfo().add_field('previousNavigatorItemId', Optional[NavigatorItemId])

        result = post_command(self.__req, json.dumps({"command": "API.CreateViewMapFolder", "parameters": CreateViewMapFolder_parameters(folderParameters, parentNavigatorItemId, previousNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return NavigatorItemId(**result["result"]["createdFolderNavigatorItemId"])

    def DeleteNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[ExecutionResult]:
        """Deletes items from navigator tree.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: A list of execution results.

        """
        class DeleteNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        DeleteNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.DeleteNavigatorItems", "parameters": DeleteNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        executionResultsListBuilder = _ListBuilder(ExecutionResult)
        return executionResultsListBuilder(result["result"]["executionResults"])

    def ExecuteAddOnCommand(self, addOnCommandId: AddOnCommandId, addOnCommandParameters: Optional[AddOnCommandParameters] = None) -> AddOnCommandResponse:
        """Executes a command registered in an Add-On.

        Args:
            addOnCommandId (:obj:`AddOnCommandId`): The identifier of an Add-On command.
            addOnCommandParameters (:obj:`AddOnCommandParameters`, optional): The input parameters of an Add-On command.

        Returns:
            :obj:`AddOnCommandResponse`: The response returned by an Add-On command.

        """
        class ExecuteAddOnCommand_parameters(_ACBaseType):
            __slots__ = ("addOnCommandId", "addOnCommandParameters", )
            def __init__(self, addOnCommandId: AddOnCommandId, addOnCommandParameters: Optional[AddOnCommandParameters] = None):
                self.addOnCommandId: AddOnCommandId = addOnCommandId
                self.addOnCommandParameters: Optional[AddOnCommandParameters] = addOnCommandParameters

        ExecuteAddOnCommand_parameters.get_classinfo().add_field('addOnCommandId', AddOnCommandId)
        ExecuteAddOnCommand_parameters.get_classinfo().add_field('addOnCommandParameters', Optional[AddOnCommandParameters])

        result = post_command(self.__req, json.dumps({"command": "API.ExecuteAddOnCommand", "parameters": ExecuteAddOnCommand_parameters(addOnCommandId, addOnCommandParameters).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return result["result"]["addOnCommandResponse"]

    def Get2DBoundingBoxes(self, elements: List[ElementIdArrayItem]) -> List[BoundingBox2DOrError]:
        """Get the 2D bounding box of elements identified by their GUIDs. The bounding box is calculated from the global origin on the floor plan view. The output is the array of the bounding boxes respective to the input GUIDs. Only works for elements detailed in <i>Element Information</i>.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.

        Returns:
            :obj:`list` of :obj:`BoundingBox2DOrError`: A list of 2D bounding boxes.

        """
        class Get2DBoundingBoxes_parameters(_ACBaseType):
            __slots__ = ("elements", )
            def __init__(self, elements: List[ElementIdArrayItem]):
                self.elements: List[ElementIdArrayItem] = elements

        Get2DBoundingBoxes_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.Get2DBoundingBoxes", "parameters": Get2DBoundingBoxes_parameters(elements).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        boundingBoxes2DListBuilder = _ListBuilder(BoundingBox2DOrError)
        return boundingBoxes2DListBuilder(result["result"]["boundingBoxes2D"])

    def Get3DBoundingBoxes(self, elements: List[ElementIdArrayItem]) -> List[BoundingBox3DOrError]:
        """Get the 3D bounding box of elements identified by their GUIDs. The bounding box is calculated from the global origin in the 3D view. The output is the array of the bounding boxes respective to the input GUIDs. Only works for elements detailed in <i>Element Information</i>.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.

        Returns:
            :obj:`list` of :obj:`BoundingBox3DOrError`: A list of 3D bounding boxes.

        """
        class Get3DBoundingBoxes_parameters(_ACBaseType):
            __slots__ = ("elements", )
            def __init__(self, elements: List[ElementIdArrayItem]):
                self.elements: List[ElementIdArrayItem] = elements

        Get3DBoundingBoxes_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.Get3DBoundingBoxes", "parameters": Get3DBoundingBoxes_parameters(elements).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        boundingBoxes3DListBuilder = _ListBuilder(BoundingBox3DOrError)
        return boundingBoxes3DListBuilder(result["result"]["boundingBoxes3D"])

    def GetActivePenTables(self) -> Tuple[AttributeIdOrError, AttributeIdOrError]:
        """Returns the model view and layout book pen table identifiers.

        Returns:
            :obj:`AttributeIdOrError`: The attribute's identifier or an error.
            :obj:`AttributeIdOrError`: The attribute's identifier or an error.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetActivePenTables"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return AttributeIdOrError(**result["result"]["modelViewPenTableId"]), AttributeIdOrError(**result["result"]["layoutBookPenTableId"])

    def GetAllClassificationsInSystem(self, classificationSystemId: ClassificationSystemId) -> List[ClassificationItemArrayItem]:
        """Returns the tree of classifications in the given classification system.

        Args:
            classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.

        Returns:
            :obj:`list` of :obj:`ClassificationItemArrayItem`: A list of classification items.

        """
        class GetAllClassificationsInSystem_parameters(_ACBaseType):
            __slots__ = ("classificationSystemId", )
            def __init__(self, classificationSystemId: ClassificationSystemId):
                self.classificationSystemId: ClassificationSystemId = classificationSystemId

        GetAllClassificationsInSystem_parameters.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)

        result = post_command(self.__req, json.dumps({"command": "API.GetAllClassificationsInSystem", "parameters": GetAllClassificationsInSystem_parameters(classificationSystemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationItemsListBuilder = _ListBuilder(ClassificationItemArrayItem)
        return classificationItemsListBuilder(result["result"]["classificationItems"])

    def GetAllClassificationSystems(self) -> List[ClassificationSystem]:
        """Returns the list of available classification systems.

        Returns:
            :obj:`list` of :obj:`ClassificationSystem`: A list of classification systems.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetAllClassificationSystems"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationSystemsListBuilder = _ListBuilder(ClassificationSystem)
        return classificationSystemsListBuilder(result["result"]["classificationSystems"])

    def GetAllElements(self) -> List[ElementIdArrayItem]:
        """Returns the identifier of every element in the current plan.

        Returns:
            :obj:`list` of :obj:`ElementIdArrayItem`: A list of elements.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetAllElements"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementsListBuilder = _ListBuilder(ElementIdArrayItem)
        return elementsListBuilder(result["result"]["elements"])

    def GetAllPropertyNames(self) -> List[PropertyUserId]:
        """Returns the human-readable names of available Property definitions for debug and development purposes.

        Returns:
            :obj:`list` of :obj:`PropertyUserId`: A list of PropertyUserId objects.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetAllPropertyNames"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertiesListBuilder = _ListBuilder(PropertyUserId)
        return propertiesListBuilder(result["result"]["properties"])

    def GetAttributesByType(self, attributeType: str) -> List[AttributeIdWrapperItem]:
        """Returns the identifier of every attribute of the given type.

        Args:
            attributeType (:obj:`str`): The type of an attribute.

        Returns:
            :obj:`list` of :obj:`AttributeIdWrapperItem`: A list of attribute identifiers.

        """
        class GetAttributesByType_parameters(_ACBaseType):
            __slots__ = ("attributeType", )
            def __init__(self, attributeType: str):
                self.attributeType: str = attributeType

        GetAttributesByType_parameters.get_classinfo().add_field('attributeType', str, value_set(['BuildingMaterial', 'Composite', 'Fill', 'Layer', 'LayerCombination', 'Line', 'PenTable', 'Profile', 'Surface', 'ZoneCategory']))

        result = post_command(self.__req, json.dumps({"command": "API.GetAttributesByType", "parameters": GetAttributesByType_parameters(attributeType).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributeIdsListBuilder = _ListBuilder(AttributeIdWrapperItem)
        return attributeIdsListBuilder(result["result"]["attributeIds"])

    def GetBuildingMaterialAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[BuildingMaterialAttributeOrError]:
        """Returns the detailed building material attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`BuildingMaterialAttributeOrError`: A list of building material attributes and potential errors.

        """
        class GetBuildingMaterialAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetBuildingMaterialAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetBuildingMaterialAttributes", "parameters": GetBuildingMaterialAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(BuildingMaterialAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetClassificationsOfElements(self, elements: List[ElementIdArrayItem], classificationSystemIds: List[ClassificationSystemIdArrayItem]) -> List[ElementClassificationOrError]:
        """Returns the classification of the given elements in the given classification systems.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.
            classificationSystemIds (:obj:`list` of :obj:`ClassificationSystemIdArrayItem`): A list of classification system identifiers.

        Returns:
            :obj:`list` of :obj:`ElementClassificationOrError`: A list of element classification identifiers or errors.

        """
        class GetClassificationsOfElements_parameters(_ACBaseType):
            __slots__ = ("elements", "classificationSystemIds", )
            def __init__(self, elements: List[ElementIdArrayItem], classificationSystemIds: List[ClassificationSystemIdArrayItem]):
                self.elements: List[ElementIdArrayItem] = elements
                self.classificationSystemIds: List[ClassificationSystemIdArrayItem] = classificationSystemIds

        GetClassificationsOfElements_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])
        GetClassificationsOfElements_parameters.get_classinfo().add_field('classificationSystemIds', List[ClassificationSystemIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetClassificationsOfElements", "parameters": GetClassificationsOfElements_parameters(elements, classificationSystemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementClassificationsListBuilder = _ListBuilder(ElementClassificationOrError)
        return elementClassificationsListBuilder(result["result"]["elementClassifications"])

    def GetComponentsOfElements(self, elements: List[ElementIdArrayItem]) -> List[ElementComponentsOrError]:
        """Returns the identifier of every component for a list of elements. The order of the returned list is the same as the given elements.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.

        Returns:
            :obj:`list` of :obj:`ElementComponentsOrError`: Array of component list or error.

        """
        class GetComponentsOfElements_parameters(_ACBaseType):
            __slots__ = ("elements", )
            def __init__(self, elements: List[ElementIdArrayItem]):
                self.elements: List[ElementIdArrayItem] = elements

        GetComponentsOfElements_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetComponentsOfElements", "parameters": GetComponentsOfElements_parameters(elements).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        componentsOfElementsListBuilder = _ListBuilder(ElementComponentsOrError)
        return componentsOfElementsListBuilder(result["result"]["componentsOfElements"])

    def GetCompositeAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[CompositeAttributeOrError]:
        """Returns the detailed composite attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`CompositeAttributeOrError`: A list of the composite attributes and potential errors.

        """
        class GetCompositeAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetCompositeAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetCompositeAttributes", "parameters": GetCompositeAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(CompositeAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetDetailsOfClassificationItems(self, classificationItemIds: List[ClassificationItemIdArrayItem]) -> List[ClassificationItemOrError]:
        """Returns the details of classification items.

        Args:
            classificationItemIds (:obj:`list` of :obj:`ClassificationItemIdArrayItem`): A list of classification item identifiers.

        Returns:
            :obj:`list` of :obj:`ClassificationItemOrError`: A list of classification items or errors.

        """
        class GetDetailsOfClassificationItems_parameters(_ACBaseType):
            __slots__ = ("classificationItemIds", )
            def __init__(self, classificationItemIds: List[ClassificationItemIdArrayItem]):
                self.classificationItemIds: List[ClassificationItemIdArrayItem] = classificationItemIds

        GetDetailsOfClassificationItems_parameters.get_classinfo().add_field('classificationItemIds', List[ClassificationItemIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetDetailsOfClassificationItems", "parameters": GetDetailsOfClassificationItems_parameters(classificationItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationItemsListBuilder = _ListBuilder(ClassificationItemOrError)
        return classificationItemsListBuilder(result["result"]["classificationItems"])

    def GetDetailsOfProperties(self, properties: List[PropertyIdArrayItem]) -> List[PropertyDefinitionOrError]:
        """Returns the details of property definitions.

        Args:
            properties (:obj:`list` of :obj:`PropertyIdArrayItem`): A list of property identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyDefinitionOrError`: A list of property definitions or errors.

        """
        class GetDetailsOfProperties_parameters(_ACBaseType):
            __slots__ = ("properties", )
            def __init__(self, properties: List[PropertyIdArrayItem]):
                self.properties: List[PropertyIdArrayItem] = properties

        GetDetailsOfProperties_parameters.get_classinfo().add_field('properties', List[PropertyIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetDetailsOfProperties", "parameters": GetDetailsOfProperties_parameters(properties).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyDefinitionsListBuilder = _ListBuilder(PropertyDefinitionOrError)
        return propertyDefinitionsListBuilder(result["result"]["propertyDefinitions"])

    def GetElementsByClassification(self, classificationItemId: ClassificationItemId) -> List[ElementIdArrayItem]:
        """Returns the identifier of every element with the given classification identifier.

        Args:
            classificationItemId (:obj:`ClassificationItemId`): The identifier of a classification item.

        Returns:
            :obj:`list` of :obj:`ElementIdArrayItem`: A list of elements.

        """
        class GetElementsByClassification_parameters(_ACBaseType):
            __slots__ = ("classificationItemId", )
            def __init__(self, classificationItemId: ClassificationItemId):
                self.classificationItemId: ClassificationItemId = classificationItemId

        GetElementsByClassification_parameters.get_classinfo().add_field('classificationItemId', ClassificationItemId)

        result = post_command(self.__req, json.dumps({"command": "API.GetElementsByClassification", "parameters": GetElementsByClassification_parameters(classificationItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementsListBuilder = _ListBuilder(ElementIdArrayItem)
        return elementsListBuilder(result["result"]["elements"])

    def GetElementsByType(self, elementType: str) -> List[ElementIdArrayItem]:
        """Returns the identifier of every element of the given type on the plan.

        Args:
            elementType (:obj:`str`): The type of an element.

        Returns:
            :obj:`list` of :obj:`ElementIdArrayItem`: A list of elements.

        """
        class GetElementsByType_parameters(_ACBaseType):
            __slots__ = ("elementType", )
            def __init__(self, elementType: str):
                self.elementType: str = elementType

        GetElementsByType_parameters.get_classinfo().add_field('elementType', str, value_set(['Wall', 'Column', 'Beam', 'Window', 'Door', 'Object', 'Lamp', 'Slab', 'Roof', 'Mesh', 'Zone', 'CurtainWall', 'Shell', 'Skylight', 'Morph', 'Stair', 'Railing', 'Opening']))

        result = post_command(self.__req, json.dumps({"command": "API.GetElementsByType", "parameters": GetElementsByType_parameters(elementType).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementsListBuilder = _ListBuilder(ElementIdArrayItem)
        return elementsListBuilder(result["result"]["elements"])

    def GetElementsRelatedToZones(self, zones: List[ElementIdArrayItem], elementTypes: Optional[List[str]] = None) -> List[ElementsOrError]:
        """Returns related elements of the given zones. The related elements will be grouped by type. If multiple zones was given, then the order of the returned list is that of the given zones.

        Args:
            zones (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.
            elementTypes (:obj:`list` of :obj:`str`, optional): A list of element types.

        Returns:
            :obj:`list` of :obj:`ElementsOrError`: A list of ElementsOrError items.

        """
        class GetElementsRelatedToZones_parameters(_ACBaseType):
            __slots__ = ("zones", "elementTypes", )
            def __init__(self, zones: List[ElementIdArrayItem], elementTypes: Optional[List[str]] = None):
                self.zones: List[ElementIdArrayItem] = zones
                self.elementTypes: Optional[List[str]] = elementTypes

        GetElementsRelatedToZones_parameters.get_classinfo().add_field('zones', List[ElementIdArrayItem])
        GetElementsRelatedToZones_parameters.get_classinfo().add_field('elementTypes', Optional[List[str]], listitem_validator(value_set(['Wall', 'Column', 'Beam', 'Window', 'Door', 'Object', 'Lamp', 'Slab', 'Roof', 'Mesh', 'Zone', 'CurtainWall', 'Shell', 'Skylight', 'Morph', 'Stair', 'Railing', 'Opening'])))

        result = post_command(self.__req, json.dumps({"command": "API.GetElementsRelatedToZones", "parameters": GetElementsRelatedToZones_parameters(zones, elementTypes).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementsRelatedToZonesListBuilder = _ListBuilder(ElementsOrError)
        return elementsRelatedToZonesListBuilder(result["result"]["elementsRelatedToZones"])

    def GetFillAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[FillAttributeOrError]:
        """Returns the detailed fill attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`FillAttributeOrError`: A list of fill attributes and potential errors.

        """
        class GetFillAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetFillAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetFillAttributes", "parameters": GetFillAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(FillAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetLayerAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[LayerAttributeOrError]:
        """Returns the detailed layer attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`LayerAttributeOrError`: A list of layer attributes and potential errors.

        """
        class GetLayerAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetLayerAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetLayerAttributes", "parameters": GetLayerAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(LayerAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetLayerCombinationAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[LayerCombinationAttributeOrError]:
        """Returns the detailed layer combination attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`LayerCombinationAttributeOrError`: A list of layer combination attributes and potential errors.

        """
        class GetLayerCombinationAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetLayerCombinationAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetLayerCombinationAttributes", "parameters": GetLayerCombinationAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(LayerCombinationAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetLayoutSettings(self, layoutNavigatorItemId: NavigatorItemId) -> LayoutParameters:
        """Returns the parameters (settings) of the given layout.

        Args:
            layoutNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

        Returns:
            :obj:`LayoutParameters`: The parameters of the layout.

        """
        class GetLayoutSettings_parameters(_ACBaseType):
            __slots__ = ("layoutNavigatorItemId", )
            def __init__(self, layoutNavigatorItemId: NavigatorItemId):
                self.layoutNavigatorItemId: NavigatorItemId = layoutNavigatorItemId

        GetLayoutSettings_parameters.get_classinfo().add_field('layoutNavigatorItemId', NavigatorItemId)

        result = post_command(self.__req, json.dumps({"command": "API.GetLayoutSettings", "parameters": GetLayoutSettings_parameters(layoutNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return LayoutParameters(**result["result"]["layoutParameters"])

    def GetLineAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[LineAttributeOrError]:
        """Returns the detailed line attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`LineAttributeOrError`: A list of line attributes and potential errors.

        """
        class GetLineAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetLineAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetLineAttributes", "parameters": GetLineAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(LineAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetNavigatorItemTree(self, navigatorTreeId: NavigatorTreeId) -> NavigatorTree:
        """Returns the tree of navigator items.

        Args:
            navigatorTreeId (:obj:`NavigatorTreeId`): The identifier of a navigator item tree.

        Returns:
            :obj:`NavigatorTree`: A tree of navigator items.

        """
        class GetNavigatorItemTree_parameters(_ACBaseType):
            __slots__ = ("navigatorTreeId", )
            def __init__(self, navigatorTreeId: NavigatorTreeId):
                self.navigatorTreeId: NavigatorTreeId = navigatorTreeId

        GetNavigatorItemTree_parameters.get_classinfo().add_field('navigatorTreeId', NavigatorTreeId)

        result = post_command(self.__req, json.dumps({"command": "API.GetNavigatorItemTree", "parameters": GetNavigatorItemTree_parameters(navigatorTreeId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return NavigatorTree(**result["result"]["navigatorTree"])

    def GetPenTableAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[PenTableAttributeOrError]:
        """Returns the detailed pen table attributes (including their pens) identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`PenTableAttributeOrError`: A list of pen table attributes and potential errors.

        """
        class GetPenTableAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetPenTableAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetPenTableAttributes", "parameters": GetPenTableAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(PenTableAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetProductInfo(self) -> Tuple[int, int, str]:
        """Accesses the version information from the running ARCHICAD.

        Returns:
            :obj:`int`: The version of the running ARCHICAD.
            :obj:`int`: The build number of the running ARCHICAD.
            :obj:`str`: The language code of the running ARCHICAD.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetProductInfo"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return result["result"]["version"], result["result"]["buildNumber"], result["result"]["languageCode"]

    def GetProfileAttributePreview(self, attributeIds: List[AttributeIdWrapperItem], imageWidth: int, imageHeight: int, backgroundColor: Optional[RGBColor] = None) -> List[ImageOrError]:
        """Returns the preview image of each requested profile attribute in a base64 string format.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.
            imageWidth (:obj:`int`): The width of the preview image.
            imageHeight (:obj:`int`): The height of the preview image.
            backgroundColor (:obj:`RGBColor`, optional): A color model represented via its red, green and blue components.

        Returns:
            :obj:`list` of :obj:`ImageOrError`: A list of images and potential errors.

        """
        class GetProfileAttributePreview_parameters(_ACBaseType):
            __slots__ = ("attributeIds", "imageWidth", "imageHeight", "backgroundColor", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem], imageWidth: int, imageHeight: int, backgroundColor: Optional[RGBColor] = None):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds
                self.imageWidth: int = imageWidth
                self.imageHeight: int = imageHeight
                self.backgroundColor: Optional[RGBColor] = backgroundColor

        GetProfileAttributePreview_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])
        GetProfileAttributePreview_parameters.get_classinfo().add_field('imageWidth', int)
        GetProfileAttributePreview_parameters.get_classinfo().add_field('imageHeight', int)
        GetProfileAttributePreview_parameters.get_classinfo().add_field('backgroundColor', Optional[RGBColor])

        result = post_command(self.__req, json.dumps({"command": "API.GetProfileAttributePreview", "parameters": GetProfileAttributePreview_parameters(attributeIds, imageWidth, imageHeight, backgroundColor).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        previewImagesListBuilder = _ListBuilder(ImageOrError)
        return previewImagesListBuilder(result["result"]["previewImages"])

    def GetProfileAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[ProfileAttributeOrError]:
        """Returns the detailed profile attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`ProfileAttributeOrError`: A list of the profile attributes and potential errors.

        """
        class GetProfileAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetProfileAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetProfileAttributes", "parameters": GetProfileAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(ProfileAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetPropertyIds(self, properties: List[PropertyUserId]) -> List[PropertyIdOrError]:
        """Returns the identifiers of property definitions for the requested property names.

        Args:
            properties (:obj:`list` of :obj:`PropertyUserId`): A list of PropertyUserId objects.

        Returns:
            :obj:`list` of :obj:`PropertyIdOrError`: A list of property identifiers or errors.

        """
        class GetPropertyIds_parameters(_ACBaseType):
            __slots__ = ("properties", )
            def __init__(self, properties: List[PropertyUserId]):
                self.properties: List[PropertyUserId] = properties

        GetPropertyIds_parameters.get_classinfo().add_field('properties', List[PropertyUserId])

        result = post_command(self.__req, json.dumps({"command": "API.GetPropertyIds", "parameters": GetPropertyIds_parameters(properties).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertiesListBuilder = _ListBuilder(PropertyIdOrError)
        return propertiesListBuilder(result["result"]["properties"])

    def GetPropertyValuesOfElementComponents(self, elementComponents: List[ElementComponentIdArrayItem], properties: List[PropertyIdArrayItem]) -> List[PropertyValuesOrError]:
        """Returns the property values of the components for the given property.

        Args:
            elementComponents (:obj:`list` of :obj:`ElementComponentIdArrayItem`): List of components of elements.
            properties (:obj:`list` of :obj:`PropertyIdArrayItem`): A list of property identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyValuesOrError`: A list of property value lists.

        """
        class GetPropertyValuesOfElementComponents_parameters(_ACBaseType):
            __slots__ = ("elementComponents", "properties", )
            def __init__(self, elementComponents: List[ElementComponentIdArrayItem], properties: List[PropertyIdArrayItem]):
                self.elementComponents: List[ElementComponentIdArrayItem] = elementComponents
                self.properties: List[PropertyIdArrayItem] = properties

        GetPropertyValuesOfElementComponents_parameters.get_classinfo().add_field('elementComponents', List[ElementComponentIdArrayItem])
        GetPropertyValuesOfElementComponents_parameters.get_classinfo().add_field('properties', List[PropertyIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetPropertyValuesOfElementComponents", "parameters": GetPropertyValuesOfElementComponents_parameters(elementComponents, properties).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyValuesForElementComponentsListBuilder = _ListBuilder(PropertyValuesOrError)
        return propertyValuesForElementComponentsListBuilder(result["result"]["propertyValuesForElementComponents"])

    def GetPropertyValuesOfElements(self, elements: List[ElementIdArrayItem], properties: List[PropertyIdArrayItem]) -> List[PropertyValuesOrError]:
        """Returns the property values of the elements for the given property.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.
            properties (:obj:`list` of :obj:`PropertyIdArrayItem`): A list of property identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyValuesOrError`: A list of property value lists.

        """
        class GetPropertyValuesOfElements_parameters(_ACBaseType):
            __slots__ = ("elements", "properties", )
            def __init__(self, elements: List[ElementIdArrayItem], properties: List[PropertyIdArrayItem]):
                self.elements: List[ElementIdArrayItem] = elements
                self.properties: List[PropertyIdArrayItem] = properties

        GetPropertyValuesOfElements_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])
        GetPropertyValuesOfElements_parameters.get_classinfo().add_field('properties', List[PropertyIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetPropertyValuesOfElements", "parameters": GetPropertyValuesOfElements_parameters(elements, properties).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyValuesForElementsListBuilder = _ListBuilder(PropertyValuesOrError)
        return propertyValuesForElementsListBuilder(result["result"]["propertyValuesForElements"])

    def GetPublisherSetNames(self) -> List[str]:
        """Returns the names of available publisher sets.

        Returns:
            :obj:`list` of :obj:`str`: The names of available publisher sets.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetPublisherSetNames"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        publisherSetNamesListBuilder = _ListBuilder(str)
        return publisherSetNamesListBuilder(result["result"]["publisherSetNames"])

    def GetSurfaceAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[SurfaceAttributeOrError]:
        """Returns the detailed surface attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`SurfaceAttributeOrError`: A list of surface attributes and potential errors.

        """
        class GetSurfaceAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetSurfaceAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetSurfaceAttributes", "parameters": GetSurfaceAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(SurfaceAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def GetZoneCategoryAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[ZoneCategoryAttributeOrError]:
        """Returns the detailed zone category attributes identified by their GUIDs.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`ZoneCategoryAttributeOrError`: A list of zone category attributes and potential errors.

        """
        class GetZoneCategoryAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        GetZoneCategoryAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetZoneCategoryAttributes", "parameters": GetZoneCategoryAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        attributesListBuilder = _ListBuilder(ZoneCategoryAttributeOrError)
        return attributesListBuilder(result["result"]["attributes"])

    def IsAddOnCommandAvailable(self, addOnCommandId: AddOnCommandId) -> bool:
        """Checks if the command is available or not.

        Args:
            addOnCommandId (:obj:`AddOnCommandId`): The identifier of an Add-On command.

        Returns:
            :obj:`bool`: Returns true if the command is available.

        """
        class IsAddOnCommandAvailable_parameters(_ACBaseType):
            __slots__ = ("addOnCommandId", )
            def __init__(self, addOnCommandId: AddOnCommandId):
                self.addOnCommandId: AddOnCommandId = addOnCommandId

        IsAddOnCommandAvailable_parameters.get_classinfo().add_field('addOnCommandId', AddOnCommandId)

        result = post_command(self.__req, json.dumps({"command": "API.IsAddOnCommandAvailable", "parameters": IsAddOnCommandAvailable_parameters(addOnCommandId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return result["result"]["available"]

    def IsAlive(self) -> bool:
        """Checks if the ARCHICAD connection is alive.

        Returns:
            :obj:`bool`: Returns true if the connection is alive.

        """

        result = post_command(self.__req, json.dumps({"command": "API.IsAlive"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return result["result"]["isAlive"]

    def MoveNavigatorItem(self, navigatorItemIdToMove: NavigatorItemId, parentNavigatorItemId: NavigatorItemId, previousNavigatorItemId: Optional[NavigatorItemId] = None):
        """Moves the given navigator item under the <i>parentNavigatorItemId</i> in the navigator tree. If <i>previousNavigatorItemId</i> is not given then inserts it at the first place under the new parent. If it is given then inserts it after this navigator item.

        Args:
            navigatorItemIdToMove (:obj:`NavigatorItemId`): The identifier of a navigator item.
            parentNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
            previousNavigatorItemId (:obj:`NavigatorItemId`, optional): The identifier of a navigator item.

        """
        class MoveNavigatorItem_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIdToMove", "parentNavigatorItemId", "previousNavigatorItemId", )
            def __init__(self, navigatorItemIdToMove: NavigatorItemId, parentNavigatorItemId: NavigatorItemId, previousNavigatorItemId: Optional[NavigatorItemId] = None):
                self.navigatorItemIdToMove: NavigatorItemId = navigatorItemIdToMove
                self.parentNavigatorItemId: NavigatorItemId = parentNavigatorItemId
                self.previousNavigatorItemId: Optional[NavigatorItemId] = previousNavigatorItemId

        MoveNavigatorItem_parameters.get_classinfo().add_field('navigatorItemIdToMove', NavigatorItemId)
        MoveNavigatorItem_parameters.get_classinfo().add_field('parentNavigatorItemId', NavigatorItemId)
        MoveNavigatorItem_parameters.get_classinfo().add_field('previousNavigatorItemId', Optional[NavigatorItemId])

        result = post_command(self.__req, json.dumps({"command": "API.MoveNavigatorItem", "parameters": MoveNavigatorItem_parameters(navigatorItemIdToMove, parentNavigatorItemId, previousNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)


    def RenameNavigatorItem(self, navigatorItemId: NavigatorItemId, newName: Optional[str] = None, newId: Optional[str] = None):
        """Renames an existing navigator item by specifying either the name or the ID, or both.

        Args:
            navigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
            newName (:obj:`str`, optional): New name of the navigator item.
            newId (:obj:`str`, optional): New ID of the navigator item.

        """
        class RenameNavigatorItem_parameters1(_ACBaseType):
            __slots__ = ("navigatorItemId", "newName", )
            def __init__(self, navigatorItemId: NavigatorItemId, newName: str):
                self.navigatorItemId: NavigatorItemId = navigatorItemId
                self.newName: str = newName

        RenameNavigatorItem_parameters1.get_classinfo().add_field('navigatorItemId', NavigatorItemId)
        RenameNavigatorItem_parameters1.get_classinfo().add_field('newName', str)

        class RenameNavigatorItem_parameters2(_ACBaseType):
            __slots__ = ("navigatorItemId", "newId", )
            def __init__(self, navigatorItemId: NavigatorItemId, newId: str):
                self.navigatorItemId: NavigatorItemId = navigatorItemId
                self.newId: str = newId

        RenameNavigatorItem_parameters2.get_classinfo().add_field('navigatorItemId', NavigatorItemId)
        RenameNavigatorItem_parameters2.get_classinfo().add_field('newId', str)

        class RenameNavigatorItem_parameters3(_ACBaseType):
            __slots__ = ("navigatorItemId", "newName", "newId", )
            def __init__(self, navigatorItemId: NavigatorItemId, newName: str, newId: str):
                self.navigatorItemId: NavigatorItemId = navigatorItemId
                self.newName: str = newName
                self.newId: str = newId

        RenameNavigatorItem_parameters3.get_classinfo().add_field('navigatorItemId', NavigatorItemId)
        RenameNavigatorItem_parameters3.get_classinfo().add_field('newName', str)
        RenameNavigatorItem_parameters3.get_classinfo().add_field('newId', str)

        parametersConstructUnion = _ConstructUnion(Union[RenameNavigatorItem_parameters1, RenameNavigatorItem_parameters2, RenameNavigatorItem_parameters3])
        paramatersObject = parametersConstructUnion(navigatorItemId=navigatorItemId, newName=newName, newId=newId)

        result = post_command(self.__req, json.dumps({"command": "API.RenameNavigatorItem", "parameters": paramatersObject.to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)


    def SetClassificationsOfElements(self, elementClassifications: List[ElementClassification]) -> List[ExecutionResult]:
        """Sets the classifications of elements. In order to set the classification of an element to unclassified, omit the classificationItemId field.

        Args:
            elementClassifications (:obj:`list` of :obj:`ElementClassification`): A list of element classification identifiers.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: A list of execution results.

        """
        class SetClassificationsOfElements_parameters(_ACBaseType):
            __slots__ = ("elementClassifications", )
            def __init__(self, elementClassifications: List[ElementClassification]):
                self.elementClassifications: List[ElementClassification] = elementClassifications

        SetClassificationsOfElements_parameters.get_classinfo().add_field('elementClassifications', List[ElementClassification])

        result = post_command(self.__req, json.dumps({"command": "API.SetClassificationsOfElements", "parameters": SetClassificationsOfElements_parameters(elementClassifications).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        executionResultsListBuilder = _ListBuilder(ExecutionResult)
        return executionResultsListBuilder(result["result"]["executionResults"])

    def SetLayoutSettings(self, layoutParameters: LayoutParameters, layoutNavigatorItemId: NavigatorItemId):
        """Sets the parameters (settings) of the given layout.

        Args:
            layoutParameters (:obj:`LayoutParameters`): The parameters of the layout.
            layoutNavigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

        """
        class SetLayoutSettings_parameters(_ACBaseType):
            __slots__ = ("layoutParameters", "layoutNavigatorItemId", )
            def __init__(self, layoutParameters: LayoutParameters, layoutNavigatorItemId: NavigatorItemId):
                self.layoutParameters: LayoutParameters = layoutParameters
                self.layoutNavigatorItemId: NavigatorItemId = layoutNavigatorItemId

        SetLayoutSettings_parameters.get_classinfo().add_field('layoutParameters', LayoutParameters)
        SetLayoutSettings_parameters.get_classinfo().add_field('layoutNavigatorItemId', NavigatorItemId)

        result = post_command(self.__req, json.dumps({"command": "API.SetLayoutSettings", "parameters": SetLayoutSettings_parameters(layoutParameters, layoutNavigatorItemId).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)


    def SetPropertyValuesOfElements(self, elementPropertyValues: List[ElementPropertyValue]) -> List[ExecutionResult]:
        """Sets the property values of elements.

        Args:
            elementPropertyValues (:obj:`list` of :obj:`ElementPropertyValue`): A list of element property values.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: A list of execution results.

        """
        class SetPropertyValuesOfElements_parameters(_ACBaseType):
            __slots__ = ("elementPropertyValues", )
            def __init__(self, elementPropertyValues: List[ElementPropertyValue]):
                self.elementPropertyValues: List[ElementPropertyValue] = elementPropertyValues

        SetPropertyValuesOfElements_parameters.get_classinfo().add_field('elementPropertyValues', List[ElementPropertyValue])

        result = post_command(self.__req, json.dumps({"command": "API.SetPropertyValuesOfElements", "parameters": SetPropertyValuesOfElements_parameters(elementPropertyValues).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        executionResultsListBuilder = _ListBuilder(ExecutionResult)
        return executionResultsListBuilder(result["result"]["executionResults"])

