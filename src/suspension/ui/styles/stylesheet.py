"""
StylesheetGenerator for the Suspension Calculator.
"""

from typing import Dict, Protocol

from ..models.theme import Theme


class StyleGenerator(Protocol):
    """Protocol defining the stylesheet generator interface."""

    def __call__(self) -> str: ...


class StylesheetGenerator:
    """
    Generates Qt stylesheets from Theme objects.
    """

    def __init__(self, theme: Theme) -> None:
        """Initialize the stylesheet generator with a theme."""
        self.theme = theme
        self._component_styles: Dict[str, StyleGenerator] = {
            "drawer": self._generate_drawer_style,
            "navigation": self._generate_navigation_style,
            "toolbar": self._generate_toolbar_style,
            "content": self._generate_content_style,
            "dialog": self._generate_dialog_style,
            "table": self._generate_table_style,
            "tab": self._generate_tab_style,
        }

    def generate_global_stylesheet(self) -> str:
        """Generate the base application stylesheet."""
        return "\n".join(
            [
                self._generate_global_styles(),
                self._generate_button_styles(),
                self._generate_input_styles(),
                self._generate_menu_styles(),
                self._generate_scrollbar_styles(),
            ]
        )

    def generate_component_stylesheet(self, component_name: str) -> str:
        """
        Generate stylesheet for specific components.

        Args:
            component_name: Name of the component to generate styles for

        Returns:
            Component-specific stylesheet string
        """
        style_generator = self._component_styles.get(component_name)
        if style_generator is not None:
            return style_generator()
        return ""

    def _generate_drawer_style(self) -> str:
        """Generate drawer-specific styles."""
        # src/suspension/ui/styles/stylesheet.py
        return f"""
        /* Main container - should be light like the toolbar */
        QMainWindow {{
            background-color: {self.theme.colors.toolbar};
        }}

        /* Base drawer container */
        QWidget#base_drawer {{
            background-color: {self.theme.colors.sidebar};
            border-right: 1px solid {self.theme.colors.border};
        }}

        /* All navigation tree items should inherit the sidebar color */
        QWidget#base_drawer QTreeView {{
            background-color: {self.theme.colors.sidebar};
            color: {self.theme.colors.sidebar_text};
        }}

        /* Button container should match the toolbar */
        QWidget#button_container {{
            background-color: {self.theme.colors.toolbar};
            border-bottom: 1px solid {self.theme.colors.border};
            max-height: 48px;
            min-height: 48px;
            padding: 0px;
            margin: 0px;
        }}

        /* Drawer content area */
        QFrame#drawer_frame {{
            background-color: {self.theme.colors.sidebar};
            margin-top: 0px;
            padding-top: 0px;
        }}

        /* Toggle button styling */
        QPushButton#drawer_toggle {{
            background-color: transparent;
            border: none;
            border-radius: {self.theme.border_radius}px;
            padding: 4px;
            margin: 8px;
            qproperty-iconSize: 16px;
            width: 32px;
            height: 32px;
        }}

        QPushButton#drawer_toggle:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        /* Make sure button container doesn't act like a button */
        QWidget#button_container > QPushButton {{
            position: absolute;
        }}
        """

    def _generate_global_styles(self) -> str:
        """Generate global widget styles."""
        return f"""
        /* Global styles */
        QWidget {{
            background-color: {self.theme.colors.background};
            color: {self.theme.colors.text_primary};
            font-family: "{self.theme.typography.font_family}";
            font-size: {self.theme.typography.base_size}px;
            border: none;
        }}

        /* Heading styles */
        QLabel[heading="h1"] {{
            font-size: {self.theme.typography.h1}px;
            font-weight: bold;
            margin-bottom: {self.theme.spacing.medium}px;
        }}

        QLabel[heading="h2"] {{
            font-size: {self.theme.typography.h2}px;
            font-weight: bold;
            margin-bottom: {self.theme.spacing.small}px;
        }}

        QLabel[heading="h3"] {{
            font-size: {self.theme.typography.h3}px;
            font-weight: bold;
            margin-bottom: {self.theme.spacing.small}px;
        }}

        /* Error states */
        QLabel[type="error"] {{
            color: {self.theme.colors.error};
        }}

        QLabel[type="warning"] {{
            color: {self.theme.colors.warning};
        }}

        QLabel[type="success"] {{
            color: {self.theme.colors.success};
        }}

        QLabel[type="info"] {{
            color: {self.theme.colors.info};
        }}
        """

    def _generate_button_styles(self) -> str:
        """Generate button styles."""
        return f"""
        /* Button styles */
        QPushButton {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
            border-radius: {self.theme.border_radius}px;
            padding: {self.theme.spacing.small}px {self.theme.spacing.medium}px;
            font-size: {self.theme.typography.button}px;
            min-height: {self.theme.spacing.xlarge}px;
            border: none;
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

        /* Secondary button variant */
        QPushButton[variant="secondary"] {{
            background-color: transparent;
            border: 1px solid {self.theme.colors.primary};
            color: {self.theme.colors.primary};
        }}

        /* Text button variant */
        QPushButton[variant="text"] {{
            background-color: transparent;
            color: {self.theme.colors.primary};
            padding: {self.theme.spacing.xsmall}px {self.theme.spacing.small}px;
        }}
        """

    def _generate_input_styles(self) -> str:
        """Generate input field styles."""
        return f"""
        /* Input styles */
        QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox {{
            background-color: {self.theme.colors.surface};
            color: {self.theme.colors.text_primary};
            border: 1px solid {self.theme.colors.border};
            border-radius: {self.theme.border_radius}px;
            padding: {self.theme.spacing.small}px;
            selection-background-color: {self.theme.colors.primary};
            selection-color: {self.theme.colors.text_primary};
        }}

        QLineEdit:focus, QTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus {{
            border: 2px solid {self.theme.colors.primary};
            background-color: {self.theme.colors.background};
        }}

        QLineEdit:disabled,
        QTextEdit:disabled,
        QSpinBox:disabled,
        QDoubleSpinBox:disabled {{
            background-color: {self.theme.colors.divider};
            color: {self.theme.colors.text_disabled};
        }}
        """

    def _generate_menu_styles(self) -> str:
        """Generate menu and menu bar styles."""
        return f"""
        /* Menu styles */
        QMenuBar {{
            background-color: {self.theme.colors.toolbar};
            color: {self.theme.colors.toolbar_text};
            border-bottom: 1px solid {self.theme.colors.border};
        }}

        QMenuBar::item:selected {{
            background-color: {self.theme.colors.primary};
        }}

        QMenu {{
            background-color: {self.theme.colors.surface};
            border: 1px solid {self.theme.colors.border};
        }}

        QMenu::item {{
            padding: {self.theme.spacing.small}px {self.theme.spacing.medium}px;
        }}

        QMenu::item:selected {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
        }}
        """

    def _generate_scrollbar_styles(self) -> str:
        """Generate scrollbar styles."""
        return f"""
        /* Scrollbar styles */
        QScrollBar:vertical {{
            background-color: {self.theme.colors.background};
            width: {self.theme.spacing.medium}px;
            margin: 0px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {self.theme.colors.divider};
            border-radius: {self.theme.border_radius}px;
            min-height: {self.theme.spacing.xlarge}px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}

        QScrollBar:horizontal {{
            background-color: {self.theme.colors.background};
            height: {self.theme.spacing.medium}px;
            margin: 0px;
        }}

        QScrollBar::handle:horizontal {{
            background-color: {self.theme.colors.divider};
            border-radius: {self.theme.border_radius}px;
            min-width: {self.theme.spacing.xlarge}px;
        }}

        QScrollBar::handle:horizontal:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
            width: 0px;
        }}
        """

    def _generate_navigation_style(self) -> str:
        """Generate navigation-specific styles."""
        return f"""
        QTreeView {{
            background-color: {self.theme.colors.sidebar};
            color: {self.theme.colors.sidebar_text};
            border: none;
            font-size: {self.theme.typography.base_size}px;
            padding: {self.theme.spacing.small}px;
        }}

        QTreeView::item {{
            padding: {self.theme.spacing.small}px;
            border-radius: {self.theme.border_radius}px;
        }}

        QTreeView::item:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QTreeView::item:selected {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
        }}

        QTreeView::branch:has-children:!has-siblings:closed,
        QTreeView::branch:closed:has-children:has-siblings {{
            image: url(:/icons/chevron-right.png);
        }}

        QTreeView::branch:open:has-children:!has-siblings,
        QTreeView::branch:open:has-children:has-siblings {{
            image: url(:/icons/chevron-down.png);
        }}
        """

    def _generate_toolbar_style(self) -> str:
        """Generate toolbar-specific styles."""
        return f"""
        QToolBar {{
            background-color: {self.theme.colors.toolbar};
            border-bottom: 1px solid {self.theme.colors.border};
            spacing: {self.theme.spacing.small}px;
            padding: {self.theme.spacing.xsmall}px;
        }}

        QToolButton {{
            background-color: transparent;
            border-radius: {self.theme.border_radius}px;
            padding: {self.theme.spacing.small}px;
            min-width: {self.theme.spacing.xlarge}px;
            min-height: {self.theme.spacing.xlarge}px;
        }}

        QToolButton:hover {{
            background-color: {self.theme.colors.secondary};
        }}

        QToolButton:pressed {{
            background-color: {self.theme.colors.primary};
        }}

        QToolButton:checked {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
        }}

        QToolButton:disabled {{
            color: {self.theme.colors.text_disabled};
        }}
        """

    def _generate_content_style(self) -> str:
        """Generate content area styles."""
        return f"""
        QWidget#ContentArea {{
            background-color: {self.theme.colors.surface};
            border: none;
        }}

        QSplitter {{
            background-color: {self.theme.colors.background};
        }}

        QSplitter::handle {{
            background-color: {self.theme.colors.divider};
        }}

        QSplitter::handle:horizontal {{
            width: {self.theme.spacing.xsmall}px;
        }}

        QSplitter::handle:vertical {{
            height: {self.theme.spacing.xsmall}px;
        }}

        QFrame#ContentPanel {{
            background-color: {self.theme.colors.surface};
            border: 1px solid {self.theme.colors.border};
            border-radius: {self.theme.border_radius}px;
        }}

        QLabel#ContentHeader {{
            font-size: {self.theme.typography.h2}px;
            font-weight: bold;
            color: {self.theme.colors.text_primary};
            padding: {self.theme.spacing.medium}px;
            background-color: transparent;
        }}

        QStackedWidget {{
            background-color: transparent;
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
            min-width: {self.theme.spacing.xxlarge}px;
        }}

        QDialog QLineEdit {{
            min-width: {self.theme.spacing.xxlarge * 4}px;
        }}
        """

    def _generate_table_style(self) -> str:
        """Generate table styles."""
        return f"""
        QTableView {{
            background-color: {self.theme.colors.surface};
            border: 1px solid {self.theme.colors.border};
            gridline-color: {self.theme.colors.divider};
        }}

        QTableView::item {{
            padding: {self.theme.spacing.small}px;
        }}

        QTableView::item:selected {{
            background-color: {self.theme.colors.primary};
            color: {self.theme.colors.text_primary};
        }}

        QHeaderView::section {{
            background-color: {self.theme.colors.background};
            padding: {self.theme.spacing.small}px;
            border: none;
            border-right: 1px solid {self.theme.colors.border};
            border-bottom: 1px solid {self.theme.colors.border};
        }}
        """

    def _generate_tab_style(self) -> str:
        """Generate tab widget styles."""
        return f"""
        QTabWidget::pane {{
            border: 1px solid {self.theme.colors.border};
            background-color: {self.theme.colors.surface};
            top: -{self.theme.border_radius}px;
        }}

        QTabBar::tab {{
            background-color: {self.theme.colors.background};
            color: {self.theme.colors.text_secondary};
            padding: {self.theme.spacing.small}px {self.theme.spacing.medium}px;
            border: 1px solid {self.theme.colors.border};
            border-bottom: none;
            border-top-left-radius: {self.theme.border_radius}px;
            border-top-right-radius: {self.theme.border_radius}px;
        }}

        QTabBar::tab:selected {{
            background-color: {self.theme.colors.surface};
            color: {self.theme.colors.text_primary};
            border-bottom: none;
        }}

        QTabBar::tab:hover {{
            background-color: {self.theme.colors.secondary};
        }}
        """
