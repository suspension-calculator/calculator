# src/suspension/ui/styles/system.py

from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication

from ..models.theme import (
    Spacing,
    Shadows,
)
from ..models.theme import (
    Theme,
    ThemeMode,
    ColorScheme,
    Typography,
    ThemeMetadata,
)


def _get_windows_system_colors() -> Dict[str, str]:
    """Get system colors from Windows registry."""
    if platform.system() != "Windows":
        return {}

    try:
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
        ) as key:
            is_dark = winreg.QueryValueEx(key, "AppsUseDarkTheme")[0] == 1

        color_key_path = r"Software\Microsoft\Windows\DWM"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, color_key_path) as key:
            accent_color = winreg.QueryValueEx(key, "ColorizationColor")[0]

        # Convert Windows accent color to hex
        accent = f"#{accent_color & 0xFFFFFF:06x}"

        return {"is_dark": is_dark, "accent": accent}
    except Exception:
        return {}


def _get_macos_system_colors() -> Dict[str, str]:
    """Get system colors from macOS."""
    if platform.system() != "Darwin":
        return {}

    try:
        import subprocess

        # Get macOS appearance setting
        cmd = ["defaults", "read", "-g", "AppleInterfaceStyle"]
        is_dark = (
            subprocess.run(cmd, capture_output=True, text=True).stdout.strip() == "Dark"
        )

        # Get accent color (requires additional permissions)
        return {"is_dark": is_dark}
    except Exception:
        return {}


def _get_linux_system_colors() -> Dict[str, str]:
    """Get system colors from Linux desktop environment."""
    if platform.system() != "Linux":
        return {}

    try:
        import subprocess

        # Try to detect desktop environment
        desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

        if "gnome" in desktop:
            # Get GNOME theme settings
            cmd = ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]
            theme_name = (
                subprocess.run(cmd, capture_output=True, text=True)
                .stdout.strip()
                .lower()
            )
            is_dark = "dark" in theme_name

            # Get accent color
            cmd = ["gsettings", "get", "org.gnome.desktop.interface", "accent-color"]
            accent = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()

            return {"is_dark": is_dark, "accent": accent if accent else None}

        elif "kde" in desktop:
            # TODO: Add KDE Plasma theme detection
            pass

    except Exception:
        return {}

    return {}


def get_system_colors() -> ColorScheme:
    """Get colors from system palette with platform-specific enhancements."""
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before getting system colors")

    app = cast(QApplication, app)
    palette = app.palette()

    # Get platform-specific colors
    os_colors = {}
    if sys.platform == "win32":
        os_colors = _get_windows_system_colors()
    elif sys.platform == "darwin":
        os_colors = _get_macos_system_colors()
    else:
        os_colors = _get_linux_system_colors()

    # Use OS accent color if available, otherwise use palette
    primary_color = os_colors.get("accent", palette.button().color().name())

    # Adjust colors based on light/dark mode
    is_dark = os_colors.get("is_dark", _is_palette_dark(palette))

    return ColorScheme(
        # Base colors
        primary=primary_color,
        secondary=_adjust_color(
            primary_color, lightness=0.1
        ),  # Slightly lighter/darker than primary
        background=palette.window().color().name(),
        surface=palette.base().color().name(),
        # Text colors
        text_primary=palette.windowText().color().name(),
        text_secondary=palette.text().color().name(),
        text_disabled=palette.color(
            QPalette.ColorRole.Disabled, QPalette.ColorRole.Text
        ).name(),
        # UI element colors
        border=palette.mid().color().name(),
        divider=palette.mid().color().name(),
        # State colors (consistent across themes)
        error="#DC3545",
        warning="#FFC107",
        success="#28A745",
        info="#17A2B8",
        # Component specific colors
        toolbar=palette.window().color().name(),
        toolbar_text=palette.windowText().color().name(),
        sidebar=_adjust_color(
            palette.window().color().name(), lightness=-0.05 if is_dark else 0.05
        ),
        sidebar_text=palette.windowText().color().name(),
    )


def _adjust_color(color: str, lightness: float = 0.0) -> str:
    """
    Adjust a color's lightness.

    Args:
        color: Hex color string
        lightness: Amount to adjust (-1.0 to 1.0)

    Returns:
        Adjusted hex color string
    """
    # Convert hex to RGB
    color = color.lstrip("#")
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)

    # Adjust lightness
    if lightness > 0:
        r = min(255, int(r * (1 + lightness)))
        g = min(255, int(g * (1 + lightness)))
        b = min(255, int(b * (1 + lightness)))
    else:
        r = max(0, int(r * (1 + lightness)))
        g = max(0, int(g * (1 + lightness)))
        b = max(0, int(b * (1 + lightness)))

    return f"#{r:02x}{g:02x}{b:02x}"


def _is_palette_dark(palette: QPalette) -> bool:
    """Determine if a palette is dark based on background color."""
    background = palette.color(QPalette.ColorRole.Window)
    brightness = (
        background.red() * 299 + background.green() * 587 + background.blue() * 114
    ) / 1000
    return brightness < 128


def get_system_font() -> Typography:
    """Get system font settings"""
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before getting system font")

    default_font = app.font()
    base_size = default_font.pointSize()

    return Typography(
        font_family=default_font.family(),
        mono_family="Consolas" if default_font.family() == "Segoe UI" else "Menlo",
        base_size=base_size,
        h1=base_size + 12,  # 24px if base is 12
        h2=base_size + 8,  # 20px if base is 12
        h3=base_size + 4,  # 16px if base is 12
        h4=base_size + 2,  # 14px if base is 12
        button=base_size,
        caption=base_size - 1,
        small=base_size - 2,
    )


def create_system_theme() -> Theme:
    """
    Creates a theme that matches the current system settings.
    Uses Qt's palette to detect system colors and font settings.
    """
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before creating system theme")

    return Theme(
        metadata=ThemeMetadata(
            name="System Default",
            description="Automatically matches system appearance",
            version="1.0.0",
        ),
        mode=ThemeMode.SYSTEM,
        colors=get_system_colors(),
        typography=get_system_font(),
        spacing=Spacing(),  # Use default spacing
        shadows=Shadows(),  # Use default shadows
        border_radius=4,
        icon_size=16,
        animation_duration_fast=100,
        animation_duration_normal=200,
        animation_duration_slow=300,
    )


def detect_system_theme_mode() -> ThemeMode:
    """
    Detect if the system is using light or dark mode.
    Returns ThemeMode.SYSTEM if unable to detect.
    """
    app = QApplication.instance()
    if not app:
        return ThemeMode.SYSTEM

    palette = app.palette()
    background = palette.color(QPalette.ColorRole.Window)

    # Calculate perceived brightness
    brightness = (
        background.red() * 299 + background.green() * 587 + background.blue() * 114
    ) / 1000

    if brightness < 128:
        return ThemeMode.DARK
    return ThemeMode.LIGHT
