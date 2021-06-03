import os, sys, subprocess
from typing import Optional, Union, Tuple, List, Callable, Any
from archicad.releases.ac24.b3000types import *
from archicad.releases.ac24.b3000commands import *


def _find_in_tree(treeRootItem, itemattr, childrenattr, criterion) -> list:
    result = []
    if criterion(treeRootItem):
        result.append(treeRootItem)
    if treeRootItem.__getattribute__(childrenattr):
        for node in treeRootItem.__getattribute__(childrenattr):
            result.extend(_find_in_tree(node.__getattribute__(itemattr), itemattr, childrenattr, criterion))
    return result


class Utilities:
    """ Utility functions for the archicad module.
    """
    def __init__(self, actypes: Types, accommands: Commands):
        self.actypes = actypes
        self.accommands = accommands

    @staticmethod
    def OpenFile(filepath: str):
        """Opens the given file with the default application."""
        if sys.platform == "win32":
            os.startfile(filepath)
        else:
            subprocess.call(["open" if sys.platform == "darwin" else "xdg-open", filepath])

    @staticmethod
    def FindInNavigatorItemTree(treeRootItem: NavigatorItem,
                                criterion: Callable[[NavigatorItem], bool]) -> List[NavigatorItem]:
        """Finds items in a navigator tree.
        
        Args:
            treeRootItem (:obj:`NavigatorItem`): The root item of the navigator tree.
            criterion (Callable[[NavigatorItem], bool]): The criterion function.
        
        Returns:
            :obj:`List[NavigatorItem]`: The list of navigator items, which fulfill the criterion function.
        """
        return _find_in_tree(treeRootItem, 'navigatorItem', 'children', criterion)

    @staticmethod
    def FindInClassificationItemTree(treeRootItem: ClassificationItemInTree,
                                     criterion: Callable[[ClassificationItemInTree], bool]) -> List[ClassificationItemInTree]:
        """Finds items in a navigator tree.
        
        Args:
            treeRootItem (:obj:`ClassificationItemInTree`): The root item of the classification tree.
            criterion (Callable[[ClassificationItemInTree], bool]): The criterion function.
        
        Returns:
            :obj:`List[ClassificationItemInTree]`: The list of classification items, which fulfill the criterion function.
        """
        return _find_in_tree(treeRootItem, 'classificationItem', 'children', criterion)


    def FindClassificationSystem(self, systemName: str) -> Optional[ClassificationSystemId]:
        """Finds the classification system."""
        return next(system.classificationSystemId for system in
                            self.accommands.GetAllClassificationSystems() if system.name == systemName)


    def FindClassificationItemInSystem(self, system_name: str, item_id: str) -> Optional[ClassificationItemId]:
        """Finds the classification item in a system."""
        classifications_tree = self.accommands.GetAllClassificationsInSystem(self.FindClassificationSystem(system_name))
        for tree in classifications_tree:
            classification_ids = Utilities.FindInClassificationItemTree(tree.classificationItem, lambda c: c.id == item_id)
            assert len(classification_ids) <= 1
            if classification_ids:
                return classification_ids[0]
        return None

    
    def GetBuiltInPropertyId(self, name: str) -> PropertyId:
        """Returns the PropertyId of the corresponding built-in property."""
        return self.accommands.GetPropertyIds([BuiltInPropertyUserId(name)])[0].propertyId


    def GetUserDefinedPropertyId(self, groupName: str, name: str) -> PropertyId:
        """Returns the PropertyId of the corresponding user-defined property."""
        return self.accommands.GetPropertyIds([UserDefinedPropertyUserId([groupName, name])])[0].propertyId


    def GetDisplayValueFromPropertyEnumValueId(self, propertyId: PropertyId, enumValueId: EnumValueId) -> str:
        """Returns the display value of an enumeration property value.
        
        Args:
            propertyId (:obj:`PropertyId`): The identifier of the property.
            enumValueId (:obj:`EnumValueId`): The enumeration value identifier.
        
        Returns:
            :obj:`str`: The display value of the enumeration property value.
        """
        return next(p.enumValue.displayValue for p in self.accommands.GetDetailsOfProperties ([propertyId])[0].propertyDefinition.possibleEnumValues if p.enumValue.enumValueId == enumValueId)


    def GetValueFromPropertyValue(self, propertyId: PropertyId, propertyValue: PropertyValue) -> Any:
        """Returns the display value of a property value.
        
        Args:
            propertyId (:obj:`PropertyId`): The identifier of the property.
            propertyValue (:obj:`PropertyValue`): The property value.
        
        Returns:
            :obj:`Any`: The value unwrapped from the property value.
        """
        if propertyValue.status == "normal":
            if propertyValue.type == "singleEnum":
                return self.GetDisplayValueFromPropertyEnumValueId(propertyId, propertyValue.value)
            elif propertyValue.type == "multiEnum":
                return [self.GetDisplayValueFromPropertyEnumValueId(propertyId, enumValue.enumValueId) for enumValue in propertyValue.value]
            else:
                return propertyValue.value
        else:
            return propertyValue.status # "userUndefined" / "notEvaluated" / "notAvailable"


    def GetPropertyValuesDictionary(self, elements: List[ElementId], propertyIds: List[PropertyId]) -> Dict[ElementId, Dict[PropertyId, Any]]:
        """Returns the values of the given elements' given properties.
        
        Args:
            elements (:obj:`List[ElementId]`): The identifier of the property.
            propertyIds (:obj:`List[PropertyId]`): The property value.
        
        Returns:
            :obj:`Dict[ElementId, Dict[PropertyId, Any]]`: A dictionary for the property values with two key-levels: the first key is the elementId, the second key is the propertyId.
        """
        propertyValuesForElements = dict(zip(elements, self.accommands.GetPropertyValuesOfElements(elements, propertyIds)))
        propertyValuesDictionary = {}
        for element, propertyValuesForElement in propertyValuesForElements.items():
            propertyValuesDictionary[element] = {}
            for propertyId, propertyValue in dict(zip(propertyIds, propertyValuesForElement.propertyValues)).items():
                if propertyValue.propertyValue.status != "notAvailable":
                    propertyValuesDictionary[element][propertyId] = self.GetValueFromPropertyValue(propertyId, propertyValue.propertyValue)
        return propertyValuesDictionary
