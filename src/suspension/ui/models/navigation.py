# src/suspension/ui/models/navigation.py
from typing import List, Optional

from pydantic import BaseModel


class NavigationItem(BaseModel):
    """Model for a navigation menu item."""

    text: str
    item_id: str
    icon: Optional[str] = None
    children: List["NavigationItem"] = []


class NavigationStructure(BaseModel):
    """Model for the complete navigation menu structure."""

    items: List[NavigationItem]


# Example structure
DEFAULT_NAVIGATION = NavigationStructure(
    items=[
        NavigationItem(
            text="Suspension",
            item_id="suspension",
            icon="SUSPENSION",
            children=[
                NavigationItem(text="Geometry", item_id="suspension-geometry"),
                NavigationItem(text="Springs", item_id="suspension-springs"),
                NavigationItem(text="Dampers", item_id="suspension-dampers"),
                NavigationItem(text="Links", item_id="suspension-links"),
                NavigationItem(text="Pitch", item_id="suspension-pitch"),
                NavigationItem(text="Driveshaft", item_id="suspension-driveshaft"),
            ],
        ),
        NavigationItem(text="Materials", item_id="materials", icon="GEOMETRY"),
        NavigationItem(text="Settings", item_id="settings", icon="SETTINGS"),
    ]
)
