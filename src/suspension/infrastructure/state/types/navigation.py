# src/suspension/infrastructure/state/types/navigation.py
from typing import Optional, Set, Dict

from pydantic import BaseModel


class NavigationItem(BaseModel):
    id: str
    text: str
    parent_id: Optional[str] = None
    is_expanded: bool = False
    is_active: bool = False
    icon: Optional[str] = None


class NavigationState(BaseModel):
    selected_item_id: Optional[str] = None
    active_item_id: Optional[str] = None
    expanded_item_ids: Set[str] = set()
    nav_pane_visible: bool = True
    current_page: Optional[str] = None
    previous_page: Optional[str] = None
    items: Dict[str, NavigationItem] = {}
