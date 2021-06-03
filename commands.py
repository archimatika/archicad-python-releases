"""GRAPHISOFT
"""
from typing import Dict, Any, List, Tuple, Optional, Union
from urllib.request import Request, urlopen
import json
from archicad.acbasetype import _ACBaseType, _ConstructUnion, _ListBuilder
from archicad.validators import value_set, matches, min_length, max_length, multiple_of, minimum, maximum, listitem_validator, min_items, max_items, unique_items

from .b3000types import NavigatorItemId, LayoutParameters, Subset, FolderParameters, NavigatorItemIdWrapper, ExecutionResult, ElementIdArrayItem, BoundingBox2DOrError, BoundingBox3DOrError, ClassificationSystemId, ClassificationItemArrayItem, ClassificationSystem, PropertyUserId, ClassificationSystemIdArrayItem, ElementClassificationOrError, ClassificationItemIdArrayItem, ClassificationItemOrError, PropertyIdArrayItem, PropertyDefinitionOrError, ClassificationItemId, ElementsOrError, NavigatorTreeId, NavigatorTree, PropertyIdOrError, PropertyValuesOrError, ElementClassification, ElementPropertyValue


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
            subsetParameters (:obj:`Subset`): Provides a way to assign IDs to the layouts contained in the subset.
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
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): List of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: Execution result for each input case.

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

    def Get2DBoundingBoxes(self, elements: List[ElementIdArrayItem]) -> List[BoundingBox2DOrError]:
        """Get the 2D bounding box of elements identified by their GUIDs. The bounding box is calculated from the global origin on the floor plan view. The output is the array of the bounding boxes respective to the input GUIDs. Only works for elements detailed in <i>Element Information</i>.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): List of the elements.

        Returns:
            :obj:`list` of :obj:`BoundingBox2DOrError`: List of element's 2D bounding boxes.

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
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): List of the elements.

        Returns:
            :obj:`list` of :obj:`BoundingBox3DOrError`: List of element's 3D bounding boxes

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

    def GetAllClassificationsInSystem(self, classificationSystemId: ClassificationSystemId) -> List[ClassificationItemArrayItem]:
        """Returns the tree of classifications in the given classification system.

        Args:
            classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.

        Returns:
            :obj:`list` of :obj:`ClassificationItemArrayItem`: The list of classification items.

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
            :obj:`list` of :obj:`ClassificationSystem`: The list of classification systems.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetAllClassificationSystems"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationSystemsListBuilder = _ListBuilder(ClassificationSystem)
        return classificationSystemsListBuilder(result["result"]["classificationSystems"])

    def GetAllElements(self) -> List[ElementIdArrayItem]:
        """Returns the identifier of every element in the current plan.

        Returns:
            :obj:`list` of :obj:`ElementIdArrayItem`: List of the elements.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetAllElements"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementsListBuilder = _ListBuilder(ElementIdArrayItem)
        return elementsListBuilder(result["result"]["elements"])

    def GetAllPropertyNames(self) -> List[PropertyUserId]:
        """Returns the human-readable names of available Property definitions for debug and development purposes.

        Returns:
            :obj:`list` of :obj:`PropertyUserId`: List of PropertyUserId objects.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetAllPropertyNames"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertiesListBuilder = _ListBuilder(PropertyUserId)
        return propertiesListBuilder(result["result"]["properties"])

    def GetClassificationsOfElements(self, elements: List[ElementIdArrayItem], classificationSystemIds: List[ClassificationSystemIdArrayItem]) -> List[ElementClassificationOrError]:
        """Returns the classification of the given elements in the given classification systems.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): List of the elements.
            classificationSystemIds (:obj:`list` of :obj:`ClassificationSystemIdArrayItem`): The list of classification system identifiers.

        Returns:
            :obj:`list` of :obj:`ElementClassificationOrError`: The list of element classification identifiers or errors.

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

    def GetDetailsOfClassificationItems(self, classificationItemIds: List[ClassificationItemIdArrayItem]) -> List[ClassificationItemOrError]:
        """Returns the details of classification items.

        Args:
            classificationItemIds (:obj:`list` of :obj:`ClassificationItemIdArrayItem`): The list of classification item identifiers.

        Returns:
            :obj:`list` of :obj:`ClassificationItemOrError`: The list of classification items or errors.

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
            properties (:obj:`list` of :obj:`PropertyIdArrayItem`): The list of property identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyDefinitionOrError`: The list of property definitions or errors.

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
            :obj:`list` of :obj:`ElementIdArrayItem`: List of the elements.

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
            :obj:`list` of :obj:`ElementIdArrayItem`: List of the elements.

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
            zones (:obj:`list` of :obj:`ElementIdArrayItem`): List of the elements.
            elementTypes (:obj:`list` of :obj:`str`, optional): List of element types.

        Returns:
            :obj:`list` of :obj:`ElementsOrError`: List of elements or error.

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

    def GetPropertyIds(self, properties: List[PropertyUserId]) -> List[PropertyIdOrError]:
        """Returns the identifiers of property definitions for the requested property names.

        Args:
            properties (:obj:`list` of :obj:`PropertyUserId`): List of PropertyUserId objects.

        Returns:
            :obj:`list` of :obj:`PropertyIdOrError`: The list of property identifiers or errors.

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

    def GetPropertyValuesOfElements(self, elements: List[ElementIdArrayItem], properties: List[PropertyIdArrayItem]) -> List[PropertyValuesOrError]:
        """Returns the property values of the elements for the given property.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): List of the elements.
            properties (:obj:`list` of :obj:`PropertyIdArrayItem`): The list of property identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyValuesOrError`: List of property value lists.

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
            elementClassifications (:obj:`list` of :obj:`ElementClassification`): The list of element classification identifiers.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: Execution result for each input case.

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
            elementPropertyValues (:obj:`list` of :obj:`ElementPropertyValue`): List of element property values.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: Execution result for each input case.

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

