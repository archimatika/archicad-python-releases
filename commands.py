"""Graphisoft
"""
from typing import Dict, Any, List, Tuple, Optional, Union
from urllib.request import Request, urlopen
import json
from archicad.acbasetype import _ACBaseType, _ConstructUnion, _ListBuilder
from archicad.validators import value_set, matches, min_length, max_length, multiple_of, minimum, maximum, listitem_validator, min_items, max_items, unique_items

from .b3000types import BoundingBox2DOrError, CompositeAttributeOrError, PropertyIdArrayItem, InteriorElevationNavigatorItemOrError, PenTableAttributeOrError, ElementComponentIdArrayItem, AttributeIdOrError, ElementPropertyValue, AttributeFolder, AddOnCommandParameters, ClassificationItemArrayItem, NavigatorItemId, ClassificationItemIdArrayItem, ElementClassificationOrError, FillAttributeOrError, ClassificationSystemId, FolderParameters, PropertyUserId, Subset, BuildingMaterialAttributeOrError, AttributeIdWrapperItem, DetailNavigatorItemOrError, WorksheetNavigatorItemOrError, PropertyIdsOfElementOrError, ClassificationItemOrError, PropertyIdOrError, ElementClassification, LayerAttributeOrError, ClassificationItemId, ImageOrError, ProfileAttributeOrError, ClassificationSystem, PropertyDefinitionAvailabilityOrError, PropertyValuesOrError, AddOnCommandResponse, NavigatorItemIdWrapper, ClassificationSystemOrError, NavigatorItemIdAndTypeOrError, NavigatorTree, LayoutParameters, BoundingBox3DOrError, TypeOfElementOrError, AddOnCommandId, ZoneCategoryAttributeOrError, PropertyDefinitionOrError, BuiltInContainerNavigatorItemOrError, ElevationNavigatorItemOrError, ClassificationSystemIdArrayItem, RGBColor, StoryNavigatorItemOrError, ClassificationItemAvailabilityOrError, ExecutionResult, LineAttributeOrError, LayerCombinationAttributeOrError, PropertyGroupIdArrayItem, PropertyGroupOrError, Document3DNavigatorItemOrError, ElementIdArrayItem, SectionNavigatorItemOrError, AttributeFolderContent, NavigatorTreeId, ElementsOrError, SurfaceAttributeOrError, ElementComponentsOrError


class UnsucceededCommandCall(Exception):
    pass


def post_command(req: Request, jsonStr: str) -> Dict[str, Any]:
    response = urlopen(req, jsonStr.encode("UTF-8"))
    result = response.read()
    return json.loads(result)


class Commands:
    """Collection of the Archicad JSON interface commands
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

    def CreateAttributeFolders(self, attributeFolders: List[AttributeFolder]) -> List[ExecutionResult]:
        """Creates attribute folders. To create a folder, its full path has to be provided. The command will create all folders along the path, if they do not exist.

        Args:
            attributeFolders (:obj:`list` of :obj:`AttributeFolder`): A list of attribute folders.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: A list of execution results.

        """
        class CreateAttributeFolders_parameters(_ACBaseType):
            __slots__ = ("attributeFolders", )
            def __init__(self, attributeFolders: List[AttributeFolder]):
                self.attributeFolders: List[AttributeFolder] = attributeFolders

        CreateAttributeFolders_parameters.get_classinfo().add_field('attributeFolders', List[AttributeFolder])

        result = post_command(self.__req, json.dumps({"command": "API.CreateAttributeFolders", "parameters": CreateAttributeFolders_parameters(attributeFolders).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        executionResultsListBuilder = _ListBuilder(ExecutionResult)
        return executionResultsListBuilder(result["result"]["executionResults"])

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

    def DeleteAttributeFolders(self, attributeFolders: List[AttributeFolder]) -> List[ExecutionResult]:
        """Deletes attribute folders and all the deletable attributes and folders it contains. To delete a folder, its full path has to be provided.

        Args:
            attributeFolders (:obj:`list` of :obj:`AttributeFolder`): A list of attribute folders.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: A list of execution results.

        """
        class DeleteAttributeFolders_parameters(_ACBaseType):
            __slots__ = ("attributeFolders", )
            def __init__(self, attributeFolders: List[AttributeFolder]):
                self.attributeFolders: List[AttributeFolder] = attributeFolders

        DeleteAttributeFolders_parameters.get_classinfo().add_field('attributeFolders', List[AttributeFolder])

        result = post_command(self.__req, json.dumps({"command": "API.DeleteAttributeFolders", "parameters": DeleteAttributeFolders_parameters(attributeFolders).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        executionResultsListBuilder = _ListBuilder(ExecutionResult)
        return executionResultsListBuilder(result["result"]["executionResults"])

    def DeleteAttributes(self, attributeIds: List[AttributeIdWrapperItem]) -> List[ExecutionResult]:
        """Deletes attributes.

        Args:
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.

        Returns:
            :obj:`list` of :obj:`ExecutionResult`: A list of execution results.

        """
        class DeleteAttributes_parameters(_ACBaseType):
            __slots__ = ("attributeIds", )
            def __init__(self, attributeIds: List[AttributeIdWrapperItem]):
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds

        DeleteAttributes_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])

        result = post_command(self.__req, json.dumps({"command": "API.DeleteAttributes", "parameters": DeleteAttributes_parameters(attributeIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        executionResultsListBuilder = _ListBuilder(ExecutionResult)
        return executionResultsListBuilder(result["result"]["executionResults"])

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

    def GetAllPropertyGroupIds(self, propertyType: Optional[str] = None) -> List[PropertyGroupIdArrayItem]:
        """Returns the identifier of every property group in the current plan. The optional propertyType parameter can be used to filter the results based on the type of the property group (Built-in or User Defined).

        Args:
            propertyType (:obj:`str`, optional): The type of a property group or a property definition.

        Returns:
            :obj:`list` of :obj:`PropertyGroupIdArrayItem`: A list of property group identifiers.

        """
        class GetAllPropertyGroupIds_parameters(_ACBaseType):
            __slots__ = ("propertyType", )
            def __init__(self, propertyType: Optional[str] = None):
                self.propertyType: Optional[str] = propertyType

        GetAllPropertyGroupIds_parameters.get_classinfo().add_field('propertyType', Optional[str], value_set(['UserDefined', 'BuiltIn']))

        result = post_command(self.__req, json.dumps({"command": "API.GetAllPropertyGroupIds", "parameters": GetAllPropertyGroupIds_parameters(propertyType).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyGroupIdsListBuilder = _ListBuilder(PropertyGroupIdArrayItem)
        return propertyGroupIdsListBuilder(result["result"]["propertyGroupIds"])

    def GetAllPropertyIds(self, propertyType: Optional[str] = None) -> List[PropertyIdArrayItem]:
        """Returns the identifier of every property in the current plan. The optional propertyType parameter can be used to filter the results based on the type of the property (Built-in or User Defined).

        Args:
            propertyType (:obj:`str`, optional): The type of a property group or a property definition.

        Returns:
            :obj:`list` of :obj:`PropertyIdArrayItem`: A list of property identifiers.

        """
        class GetAllPropertyIds_parameters(_ACBaseType):
            __slots__ = ("propertyType", )
            def __init__(self, propertyType: Optional[str] = None):
                self.propertyType: Optional[str] = propertyType

        GetAllPropertyIds_parameters.get_classinfo().add_field('propertyType', Optional[str], value_set(['UserDefined', 'BuiltIn']))

        result = post_command(self.__req, json.dumps({"command": "API.GetAllPropertyIds", "parameters": GetAllPropertyIds_parameters(propertyType).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyIdsListBuilder = _ListBuilder(PropertyIdArrayItem)
        return propertyIdsListBuilder(result["result"]["propertyIds"])

    def GetAllPropertyIdsOfElements(self, elements: List[ElementIdArrayItem], propertyType: Optional[str] = None) -> List[PropertyIdsOfElementOrError]:
        """Returns all property identifiers of the given elements. The optional propertyType parameter can be used to filter the results based on the type of the property (Built-in or User Defined).

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.
            propertyType (:obj:`str`, optional): The type of a property group or a property definition.

        Returns:
            :obj:`list` of :obj:`PropertyIdsOfElementOrError`: A list of property identifiers of elements or errors.

        """
        class GetAllPropertyIdsOfElements_parameters(_ACBaseType):
            __slots__ = ("elements", "propertyType", )
            def __init__(self, elements: List[ElementIdArrayItem], propertyType: Optional[str] = None):
                self.elements: List[ElementIdArrayItem] = elements
                self.propertyType: Optional[str] = propertyType

        GetAllPropertyIdsOfElements_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])
        GetAllPropertyIdsOfElements_parameters.get_classinfo().add_field('propertyType', Optional[str], value_set(['UserDefined', 'BuiltIn']))

        result = post_command(self.__req, json.dumps({"command": "API.GetAllPropertyIdsOfElements", "parameters": GetAllPropertyIdsOfElements_parameters(elements, propertyType).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyIdsOfElementsListBuilder = _ListBuilder(PropertyIdsOfElementOrError)
        return propertyIdsOfElementsListBuilder(result["result"]["propertyIdsOfElements"])

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

    def GetAttributeFolder(self, attributeFolder: AttributeFolder) -> AttributeFolder:
        """Get an attribute folder's path and guid. To get an attribute folder guid, it's full path has to be provided and to get full path, it's guid has to be provided.

        Args:
            attributeFolder (:obj:`AttributeFolder`): Identifies an attribute folder. The path of the root folder is repesented by empty array.

        Returns:
            :obj:`AttributeFolder`: Identifies an attribute folder. The path of the root folder is repesented by empty array.

        """
        class GetAttributeFolder_parameters(_ACBaseType):
            __slots__ = ("attributeFolder", )
            def __init__(self, attributeFolder: AttributeFolder):
                self.attributeFolder: AttributeFolder = attributeFolder

        GetAttributeFolder_parameters.get_classinfo().add_field('attributeFolder', AttributeFolder)

        result = post_command(self.__req, json.dumps({"command": "API.GetAttributeFolder", "parameters": GetAttributeFolder_parameters(attributeFolder).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return AttributeFolder(**result["result"]["attributeFolder"])

    def GetAttributeFolderContent(self, attributeFolder: AttributeFolder) -> AttributeFolderContent:
        """Get attribute folder's content, subfolders and attributes. To get an attribute folder's content, it's full path or guid has to be provided.

        Args:
            attributeFolder (:obj:`AttributeFolder`): Identifies an attribute folder. The path of the root folder is repesented by empty array.

        Returns:
            :obj:`AttributeFolderContent`: An attribute folder content. Contains subfolders and attributes.

        """
        class GetAttributeFolderContent_parameters(_ACBaseType):
            __slots__ = ("attributeFolder", )
            def __init__(self, attributeFolder: AttributeFolder):
                self.attributeFolder: AttributeFolder = attributeFolder

        GetAttributeFolderContent_parameters.get_classinfo().add_field('attributeFolder', AttributeFolder)

        result = post_command(self.__req, json.dumps({"command": "API.GetAttributeFolderContent", "parameters": GetAttributeFolderContent_parameters(attributeFolder).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return AttributeFolderContent(**result["result"]["attributeFolderContent"])

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

    def GetBuiltInContainerNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[BuiltInContainerNavigatorItemOrError]:
        """Returns the details of the built-in container navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`BuiltInContainerNavigatorItemOrError`: A list of built-in container navigator items.

        """
        class GetBuiltInContainerNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetBuiltInContainerNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetBuiltInContainerNavigatorItems", "parameters": GetBuiltInContainerNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(BuiltInContainerNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

    def GetClassificationItemAvailability(self, classificationItemIds: List[ClassificationItemIdArrayItem]) -> List[ClassificationItemAvailabilityOrError]:
        """Returns the ids of property definitions available for a given classification item.

        Args:
            classificationItemIds (:obj:`list` of :obj:`ClassificationItemIdArrayItem`): A list of classification item identifiers.

        Returns:
            :obj:`list` of :obj:`ClassificationItemAvailabilityOrError`: A list of classification item avalabilities.

        """
        class GetClassificationItemAvailability_parameters(_ACBaseType):
            __slots__ = ("classificationItemIds", )
            def __init__(self, classificationItemIds: List[ClassificationItemIdArrayItem]):
                self.classificationItemIds: List[ClassificationItemIdArrayItem] = classificationItemIds

        GetClassificationItemAvailability_parameters.get_classinfo().add_field('classificationItemIds', List[ClassificationItemIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetClassificationItemAvailability", "parameters": GetClassificationItemAvailability_parameters(classificationItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationItemAvailabilityListListBuilder = _ListBuilder(ClassificationItemAvailabilityOrError)
        return classificationItemAvailabilityListListBuilder(result["result"]["classificationItemAvailabilityList"])

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

    def GetClassificationSystemIds(self) -> List[ClassificationSystemIdArrayItem]:
        """Returns the list of available classification systems.

        Returns:
            :obj:`list` of :obj:`ClassificationSystemIdArrayItem`: A list of classification system identifiers.

        """

        result = post_command(self.__req, json.dumps({"command": "API.GetClassificationSystemIds"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationSystemIdsListBuilder = _ListBuilder(ClassificationSystemIdArrayItem)
        return classificationSystemIdsListBuilder(result["result"]["classificationSystemIds"])

    def GetClassificationSystems(self, classificationSystemIds: List[ClassificationSystemIdArrayItem]) -> List[ClassificationSystemOrError]:
        """Returns the details of classification systems identified by their GUIDs.

        Args:
            classificationSystemIds (:obj:`list` of :obj:`ClassificationSystemIdArrayItem`): A list of classification system identifiers.

        Returns:
            :obj:`list` of :obj:`ClassificationSystemOrError`: A list of classification systems or errors.

        """
        class GetClassificationSystems_parameters(_ACBaseType):
            __slots__ = ("classificationSystemIds", )
            def __init__(self, classificationSystemIds: List[ClassificationSystemIdArrayItem]):
                self.classificationSystemIds: List[ClassificationSystemIdArrayItem] = classificationSystemIds

        GetClassificationSystems_parameters.get_classinfo().add_field('classificationSystemIds', List[ClassificationSystemIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetClassificationSystems", "parameters": GetClassificationSystems_parameters(classificationSystemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        classificationSystemsListBuilder = _ListBuilder(ClassificationSystemOrError)
        return classificationSystemsListBuilder(result["result"]["classificationSystems"])

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

    def GetDetailNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[DetailNavigatorItemOrError]:
        """Returns the details of the detail navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`DetailNavigatorItemOrError`: A list of detail navigator items.

        """
        class GetDetailNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetDetailNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetDetailNavigatorItems", "parameters": GetDetailNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(DetailNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

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

    def GetDocument3DNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[Document3DNavigatorItemOrError]:
        """Returns the details of the 3D document navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`Document3DNavigatorItemOrError`: A list of 3D document navigator items.

        """
        class GetDocument3DNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetDocument3DNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetDocument3DNavigatorItems", "parameters": GetDocument3DNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(Document3DNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

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

    def GetElevationNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[ElevationNavigatorItemOrError]:
        """Returns the detailed elevation navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`ElevationNavigatorItemOrError`: A list of elevation navigator items.

        """
        class GetElevationNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetElevationNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetElevationNavigatorItems", "parameters": GetElevationNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(ElevationNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

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

    def GetInteriorElevationNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[InteriorElevationNavigatorItemOrError]:
        """Returns the details of the interior elevation navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`InteriorElevationNavigatorItemOrError`: A list of interior elevation navigator items.

        """
        class GetInteriorElevationNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetInteriorElevationNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetInteriorElevationNavigatorItems", "parameters": GetInteriorElevationNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(InteriorElevationNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

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

    def GetNavigatorItemsType(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[NavigatorItemIdAndTypeOrError]:
        """Returns all navigator item types based on the navigator item identifiers given. An error is returned for each identifier that is not found.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`NavigatorItemIdAndTypeOrError`: A list of objects that consist of a navigator item identifier and a type.

        """
        class GetNavigatorItemsType_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetNavigatorItemsType_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetNavigatorItemsType", "parameters": GetNavigatorItemsType_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemIdAndTypeListListBuilder = _ListBuilder(NavigatorItemIdAndTypeOrError)
        return navigatorItemIdAndTypeListListBuilder(result["result"]["navigatorItemIdAndTypeList"])

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
        """Accesses the version information from the running Archicad.

        Returns:
            :obj:`int`: The version of the running Archicad.
            :obj:`int`: The build number of the running Archicad.
            :obj:`str`: The language code of the running Archicad.

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

    def GetPropertyDefinitionAvailability(self, propertyIds: List[PropertyIdArrayItem]) -> List[PropertyDefinitionAvailabilityOrError]:
        """Returns the ids of classification items a given property definition is available for.

        Args:
            propertyIds (:obj:`list` of :obj:`PropertyIdArrayItem`): A list of property identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyDefinitionAvailabilityOrError`: A list of classification item avalabilities.

        """
        class GetPropertyDefinitionAvailability_parameters(_ACBaseType):
            __slots__ = ("propertyIds", )
            def __init__(self, propertyIds: List[PropertyIdArrayItem]):
                self.propertyIds: List[PropertyIdArrayItem] = propertyIds

        GetPropertyDefinitionAvailability_parameters.get_classinfo().add_field('propertyIds', List[PropertyIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetPropertyDefinitionAvailability", "parameters": GetPropertyDefinitionAvailability_parameters(propertyIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyDefinitionAvailabilityListListBuilder = _ListBuilder(PropertyDefinitionAvailabilityOrError)
        return propertyDefinitionAvailabilityListListBuilder(result["result"]["propertyDefinitionAvailabilityList"])

    def GetPropertyGroups(self, propertyGroupIds: List[PropertyGroupIdArrayItem]) -> List[PropertyGroupOrError]:
        """Returns the details of property groups.

        Args:
            propertyGroupIds (:obj:`list` of :obj:`PropertyGroupIdArrayItem`): A list of property group identifiers.

        Returns:
            :obj:`list` of :obj:`PropertyGroupOrError`: A list of property groups or errors.

        """
        class GetPropertyGroups_parameters(_ACBaseType):
            __slots__ = ("propertyGroupIds", )
            def __init__(self, propertyGroupIds: List[PropertyGroupIdArrayItem]):
                self.propertyGroupIds: List[PropertyGroupIdArrayItem] = propertyGroupIds

        GetPropertyGroups_parameters.get_classinfo().add_field('propertyGroupIds', List[PropertyGroupIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetPropertyGroups", "parameters": GetPropertyGroups_parameters(propertyGroupIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        propertyGroupsListBuilder = _ListBuilder(PropertyGroupOrError)
        return propertyGroupsListBuilder(result["result"]["propertyGroups"])

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

    def GetSectionNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[SectionNavigatorItemOrError]:
        """Returns the details of the section navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`SectionNavigatorItemOrError`: A list of section navigator items.

        """
        class GetSectionNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetSectionNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetSectionNavigatorItems", "parameters": GetSectionNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(SectionNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

    def GetSelectedElements(self, onlyEditable: Optional[bool] = None) -> List[ElementIdArrayItem]:
        """Returns the identifiers of selected elements in the current plan.

        Args:
            onlyEditable (:obj:`bool`, optional): Optional parameter that defines whether the selection list should include only the editable elements or all of them. The default value is FALSE

        Returns:
            :obj:`list` of :obj:`ElementIdArrayItem`: A list of elements.

        """
        class GetSelectedElements_parameters(_ACBaseType):
            __slots__ = ("onlyEditable", )
            def __init__(self, onlyEditable: Optional[bool] = None):
                self.onlyEditable: Optional[bool] = onlyEditable

        GetSelectedElements_parameters.get_classinfo().add_field('onlyEditable', Optional[bool])

        result = post_command(self.__req, json.dumps({"command": "API.GetSelectedElements", "parameters": GetSelectedElements_parameters(onlyEditable).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        elementsListBuilder = _ListBuilder(ElementIdArrayItem)
        return elementsListBuilder(result["result"]["elements"])

    def GetStoryNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[StoryNavigatorItemOrError]:
        """Returns the details of the story navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`StoryNavigatorItemOrError`: A list of story navigator items.

        """
        class GetStoryNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetStoryNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetStoryNavigatorItems", "parameters": GetStoryNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(StoryNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

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

    def GetTypesOfElements(self, elements: List[ElementIdArrayItem]) -> List[TypeOfElementOrError]:
        """Returns the types of the given elements.

        Args:
            elements (:obj:`list` of :obj:`ElementIdArrayItem`): A list of elements.

        Returns:
            :obj:`list` of :obj:`TypeOfElementOrError`: A list of element types or errors.

        """
        class GetTypesOfElements_parameters(_ACBaseType):
            __slots__ = ("elements", )
            def __init__(self, elements: List[ElementIdArrayItem]):
                self.elements: List[ElementIdArrayItem] = elements

        GetTypesOfElements_parameters.get_classinfo().add_field('elements', List[ElementIdArrayItem])

        result = post_command(self.__req, json.dumps({"command": "API.GetTypesOfElements", "parameters": GetTypesOfElements_parameters(elements).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        typesOfElementsListBuilder = _ListBuilder(TypeOfElementOrError)
        return typesOfElementsListBuilder(result["result"]["typesOfElements"])

    def GetWorksheetNavigatorItems(self, navigatorItemIds: List[NavigatorItemIdWrapper]) -> List[WorksheetNavigatorItemOrError]:
        """Returns the details of the worksheet navigator items identified by their Ids.

        Args:
            navigatorItemIds (:obj:`list` of :obj:`NavigatorItemIdWrapper`): A list of navigator item identifiers.

        Returns:
            :obj:`list` of :obj:`WorksheetNavigatorItemOrError`: A list of worksheet navigator items.

        """
        class GetWorksheetNavigatorItems_parameters(_ACBaseType):
            __slots__ = ("navigatorItemIds", )
            def __init__(self, navigatorItemIds: List[NavigatorItemIdWrapper]):
                self.navigatorItemIds: List[NavigatorItemIdWrapper] = navigatorItemIds

        GetWorksheetNavigatorItems_parameters.get_classinfo().add_field('navigatorItemIds', List[NavigatorItemIdWrapper])

        result = post_command(self.__req, json.dumps({"command": "API.GetWorksheetNavigatorItems", "parameters": GetWorksheetNavigatorItems_parameters(navigatorItemIds).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        navigatorItemsListBuilder = _ListBuilder(WorksheetNavigatorItemOrError)
        return navigatorItemsListBuilder(result["result"]["navigatorItems"])

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
        """Checks if the Archicad connection is alive.

        Returns:
            :obj:`bool`: Returns true if the connection is alive.

        """

        result = post_command(self.__req, json.dumps({"command": "API.IsAlive"}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)
        return result["result"]["isAlive"]

    def MoveAttributesAndFolders(self, folders: List[AttributeFolder], attributeIds: List[AttributeIdWrapperItem], targetFolder: AttributeFolder):
        """Moves attributes and attribute folders.

        Args:
            folders (:obj:`list` of :obj:`AttributeFolder`): A list of attribute folders.
            attributeIds (:obj:`list` of :obj:`AttributeIdWrapperItem`): A list of attribute identifiers.
            targetFolder (:obj:`AttributeFolder`): Identifies an attribute folder. The path of the root folder is repesented by empty array.

        """
        class MoveAttributesAndFolders_parameters(_ACBaseType):
            __slots__ = ("folders", "attributeIds", "targetFolder", )
            def __init__(self, folders: List[AttributeFolder], attributeIds: List[AttributeIdWrapperItem], targetFolder: AttributeFolder):
                self.folders: List[AttributeFolder] = folders
                self.attributeIds: List[AttributeIdWrapperItem] = attributeIds
                self.targetFolder: AttributeFolder = targetFolder

        MoveAttributesAndFolders_parameters.get_classinfo().add_field('folders', List[AttributeFolder])
        MoveAttributesAndFolders_parameters.get_classinfo().add_field('attributeIds', List[AttributeIdWrapperItem])
        MoveAttributesAndFolders_parameters.get_classinfo().add_field('targetFolder', AttributeFolder)

        result = post_command(self.__req, json.dumps({"command": "API.MoveAttributesAndFolders", "parameters": MoveAttributesAndFolders_parameters(folders, attributeIds, targetFolder).to_dict()}))
        if not result["succeeded"]:
            raise UnsucceededCommandCall(result)


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


    def RenameAttributeFolder(self, attributeFolder: AttributeFolder, newName: str):
        """Rename attribute folder.

        Args:
            attributeFolder (:obj:`AttributeFolder`): Identifies an attribute folder. The path of the root folder is repesented by empty array.
            newName (:obj:`str`): The requested new name of the attribute folder.

        """
        class RenameAttributeFolder_parameters(_ACBaseType):
            __slots__ = ("attributeFolder", "newName", )
            def __init__(self, attributeFolder: AttributeFolder, newName: str):
                self.attributeFolder: AttributeFolder = attributeFolder
                self.newName: str = newName

        RenameAttributeFolder_parameters.get_classinfo().add_field('attributeFolder', AttributeFolder)
        RenameAttributeFolder_parameters.get_classinfo().add_field('newName', str, min_length(1))

        result = post_command(self.__req, json.dumps({"command": "API.RenameAttributeFolder", "parameters": RenameAttributeFolder_parameters(attributeFolder, newName).to_dict()}))
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

