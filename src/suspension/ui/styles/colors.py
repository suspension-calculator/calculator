# src/suspension/ui/styles/colors.py


class BaseColors:
    """Base UI colors used throughout the application"""

    BACKGROUND = "#060606"
    INPUT = "#272727"
    BUTTON = "#2c2c2c"
    BUTTON_PRESSED = "#c9c9c9"
    TEXT_ENTRY = "#272727"
    ENTRY_TEXT = "#afafaf"


class ComponentColors:
    """Colors for different suspension components"""

    UPPER = "#0000ff"
    LOWER = "#ff0000"
    PANHARD = "#ffff00"
    SHOCK_PRIMARY = "#00B050"
    SHOCK_SECONDARY = "#7030A0"
    PANHARD_FRAME = "#ab8100"
    VEHICLE = "#afafaf"
    IC = "#ffffff"


class AnalysisColors:
    """Colors used in analysis visualizations"""

    RIDE_ANTI = "#66FF66"
    ANTI_100 = "#66FFFF"
    ROLL = "#ED7D31"
    BODY_ROLL = "#F4B183"


class PlotColors:
    """Colors used in plotting"""

    MAIN = "#88c53f"
    SECONDARY = "#1f77b4"


class StatusColors:
    """Colors indicating different statuses"""

    PASS = "#D8E4BC"
    FAIL = "#FFC7CE"
