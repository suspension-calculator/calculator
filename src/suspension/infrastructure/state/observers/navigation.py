# src/suspension/infrastructure/state/observers/navigation.py
from .store import ObservableStore
from ..types.navigation import NavigationState


class NavigationStore(ObservableStore[NavigationState]):
    def set_nav_pane_visible(self, visible: bool) -> None:
        new_state = NavigationState(
            **{**self.state.dict(), "nav_pane_visible": visible}
        )
        self.set_state(new_state)
