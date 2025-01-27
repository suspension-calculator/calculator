# src/suspension/ui/constants/themes.py

"""
Predefined themes for the Suspension Calculator.
"""
from suspension.ui.models.theme import (
    Theme,
    ThemeMode,
    ThemeMetadata,
    ColorScheme,
    Typography,
    Spacing,
    Shadows,
)

# Light theme color scheme
LIGHT_THEME = Theme(
    metadata=ThemeMetadata(
        name="Light",
        description="Light theme preset",
        version="1.0.0",
        author="Suspension Calculator Team",
    ),
    mode=ThemeMode.LIGHT,
    colors=ColorScheme(
        # Base colors
        primary="#007AFF",
        secondary="#5856D6",
        background="#F2F2F7",
        surface="#FFFFFF",
        # Text colors
        text_primary="#000000",
        text_secondary="#3C3C43",
        text_disabled="#3C3C4399",
        # UI element colors
        border="#C6C6C8",
        divider="#C6C6C8",
        # State colors
        error="#FF3B30",
        warning="#FF9500",
        success="#34C759",
        info="#5856D6",
        # Component colors
        toolbar="#F9F9F9",
        toolbar_text="#000000",
        sidebar="#F2F2F7",
        sidebar_text="#000000",
    ),
    typography=Typography(
        font_family="Segoe UI",
        mono_family="Consolas",
    ),
    spacing=Spacing(),
    shadows=Shadows(),
    border_radius=4,
    icon_size=16,
)

# Dark theme color scheme
DARK_THEME = Theme(
    metadata=ThemeMetadata(
        name="Dark",
        description="Dark theme preset",
        version="1.0.0",
        author="Suspension Calculator Team",
    ),
    mode=ThemeMode.DARK,
    colors=ColorScheme(
        # Base colors
        primary="#0A84FF",
        secondary="#5E5CE6",
        background="#000000",
        surface="#1C1C1E",
        # Text colors
        text_primary="#FFFFFF",
        text_secondary="#EBEBF599",
        text_disabled="#EBEBF54C",
        # UI element colors
        border="#38383A",
        divider="#38383A",
        # State colors
        error="#FF453A",
        warning="#FF9F0A",
        success="#32D74B",
        info="#5E5CE6",
        # Component colors
        toolbar="#1C1C1E",
        toolbar_text="#FFFFFF",
        sidebar="#2C2C2E",
        sidebar_text="#FFFFFF",
    ),
    typography=Typography(
        font_family="Segoe UI",
        mono_family="Consolas",
    ),
    spacing=Spacing(),
    shadows=Shadows(),
    border_radius=4,
    icon_size=16,
)

# Irate4x4 theme
IRATE_THEME = Theme(
    metadata=ThemeMetadata(
        name="Irate",
        description="Irate4x4 inspired dark theme",
        version="1.0.0",
        author="Irate4x4 & Suspension Calculator Team",
    ),
    mode=ThemeMode.DARK,
    colors=ColorScheme(
        # Base colors
        primary="#8dc63f",  # Irate logo green
        secondary="#455e0f",  # Banner dark green
        background="#000000",  # Main black background
        surface="#2a2a2a",  # Alternative background
        # Text colors
        text_primary="#c2c2c2",  # Main text color
        text_secondary="#909090",  # Secondary text
        text_disabled="#606060",  # Disabled text
        # UI element colors
        border="#353535",  # Subtle borders
        divider="#353535",  # Matching dividers
        # State colors
        error="#ff3b30",  # Error red
        warning="#ffb74d",  # Warning orange
        success="#8dc63f",  # Success (using logo green)
        info="#4a90e2",  # Info blue
        # Component specific colors
        toolbar="#2a2a2a",  # Toolbar background
        toolbar_text="#c2c2c2",  # Toolbar text
        sidebar="#1a1a1a",  # Slightly darker than alt background
        sidebar_text="#c2c2c2",  # Sidebar text
    ),
    typography=Typography(
        font_family="Segoe UI",
        mono_family="Consolas",
        base_size=12,
        h1=24,
        h2=20,
        h3=16,
        h4=14,
        button=12,
        caption=11,
        small=10,
    ),
    spacing=Spacing(),
    shadows=Shadows(
        none="none",
        small="0 2px 4px rgba(0,0,0,0.3)",
        medium="0 4px 8px rgba(0,0,0,0.4)",
        large="0 8px 16px rgba(0,0,0,0.5)",
    ),
    border_radius=2,  # Slightly tighter corners to match Irate style
    icon_size=16,
    animation_duration_fast=100,
    animation_duration_normal=200,
    animation_duration_slow=300,
)
