from ..models.theme import Theme


class StylesheetGenerator:
    """
    Generates Qt stylesheets from Theme objects.

    This class converts our Theme model into Qt stylesheets,
    providing consistent styling across the application.
    """

    def __init__(self, theme: Theme):
        self.theme = theme

    def generate_global_stylesheet(self) -> str:
        """Generate the base application stylesheet."""
        return f"""
        /* Global styles */
        QWidget {{
            background-color: {self.theme.colors.background};
            color: {self.theme.colors.text_primary};
            font-family: "{self.theme.typography.font_family}";
            font-size: {self.theme.typography.base_size}px;
        }}

        /* Button styles */
        QPushButton {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
            border: none;
            border-radius: {self.theme.border_radius}px;
            padding: {self.theme.spacing.small}px {self.theme.spacing.medium}px;
        }}

        QPushButton:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QPushButton:pressed {{
            background-color: {self.theme.colors.primary};
        }}

        QPushButton:disabled {{
            background-color: {self.theme.colors.divider};
            color: {self.theme.colors.text_disabled};
        }}

        /* Menu and toolbar styles */
        QMenuBar {{
            background-color: {self.theme.colors.toolbar};
            color: {self.theme.colors.toolbar_text};
        }}

        QToolBar {{
            background-color: {self.theme.colors.toolbar};
            border: none;
            spacing: {self.theme.spacing.small}px;
        }}

        /* Status bar styles */
        QStatusBar {{
            background-color: {self.theme.colors.surface};
            color: {self.theme.colors.text_secondary};
        }}

        /* Scroll bar styles */
        QScrollBar:vertical {{
            background-color: {self.theme.colors.background};
            width: 12px;
            margin: 0px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {self.theme.colors.divider};
            border-radius: 6px;
            min-height: 20px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: {self.theme.colors.secondary};
        }}
        """

    def generate_component_stylesheet(self, component_name: str) -> str:
        """Generate stylesheet for specific components."""
        component_styles = {
            "navigation": self._generate_navigation_style,
            "toolbar": self._generate_toolbar_style,
            "content": self._generate_content_style,
            "dialog": self._generate_dialog_style,
        }

        style_generator = component_styles.get(component_name)
        if style_generator:
            return style_generator()
        return ""

    def _generate_navigation_style(self) -> str:
        """Generate navigation-specific styles."""
        return f"""
        QTreeView {{
            background-color: {self.theme.colors.sidebar};
            color: {self.theme.colors.sidebar_text};
            border: none;
            font-size: {self.theme.typography.base_size}px;
        }}

        QTreeView::item {{
            padding: {self.theme.spacing.small}px;
        }}

        QTreeView::item:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QTreeView::item:selected {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
        }}
        """

    def _generate_toolbar_style(self) -> str:
        """Generate toolbar-specific styles."""
        return f"""
        QToolButton {{
            background-color: transparent;
            border: none;
            padding: {self.theme.spacing.small}px;
            border-radius: {self.theme.border_radius}px;
        }}

        QToolButton:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QToolButton:pressed {{
            background-color: {self.theme.colors.primary};
        }}
        """

    def _generate_content_style(self) -> str:
        """Generate content area styles."""
        return f"""
        QWidget#ContentArea {{
            background-color: {self.theme.colors.surface};
            border: none;
        }}

        QLabel {{
            color: {self.theme.colors.text_primary};
            font-size: {self.theme.typography.base_size}px;
        }}

        QLabel[heading="true"] {{
            font-size: {self.theme.typography.h2}px;
            font-weight: bold;
        }}
        """

    def _generate_dialog_style(self) -> str:
        """Generate dialog styles."""
        return f"""
        QDialog {{
            background-color: {self.theme.colors.surface};
        }}

        QDialog QLabel {{
            color: {self.theme.colors.text_primary};
        }}

        QDialog QPushButton {{
            min-width: 80px;
        }}
        """
