from src.ui import colors

REGULAR_GRAY_TEXT_18 = f"""QWidget{{
    color: {colors.GRAY};
    font-weight: bold;
    font-size: 18px;
}}"""

REGULAR_GRAY_TEXT_14 = f"""QWidget{{
    color: {colors.GRAY};
    font-weight: bold;
    font-size: 14px;
}}"""


REGULAR_WHITE_TEXT_14 = f"""QWidget{{
    color: {colors.WHITE};
    font-size: 14px;
}}"""


GRAY_TEXT_BOLD = f"""QWidget{{
    color: {colors.GRAY};
    font-weight: bold;
}}"""

GRAY_TEXT = f"""QWidget{{
    color: {colors.GRAY};
}}"""

LIGHT_TEXT = f"""QWidget{{
    color: {colors.LIGHTEST_GRAY};
}}"""

REMOVE_BUTTON = f"""QWidget{{
        background-color: {colors.DARK_GRAY};
        color: {colors.WHITE};
        font-weight: bold;
        border-radius: 20px;
        border: 1px solid;
        border-color: {colors.WHITE};
    }}

    QWidget::hover{{
        background-color: {colors.DARK_GRAY};
        color: {colors.WHITE};
        font-weight: bold;
        border-radius: 20px;
        border: 2px solid;
        border-color: {colors.WHITE};
        font-size: 16px;
    }}
"""

LINE = f"""QWidget{{
        background-color: {colors.LIGHT_GRAY};
    }}
"""

SEARCH_BOX = f"""QWidget{{
        background-color: {colors.WHITE};
        border-radius: 12px;
    }}
"""

HIDDEN_BUTTON_NEXT = f"""QWidget{{
        background-color: {colors.MEDIUM_GRAY};
        color: {colors.BLACK};
        font-weight: bold;
        border: 2px solid;
        border-color: {colors.MEDIUM_GRAY};
    }}
"""

HIDDEN_BUTTON_PREVIOUS = f"""QWidget {{
        background-color: {colors.MEDIUM_GRAY};
        color: {colors.BLACK};
        font-weight: bold;
        border: 2px solid;
        border-color: {colors.MEDIUM_GRAY};
    }}
"""

ROUND_BUTTON = f"""QWidget{{
        background-color: {colors.WHITE};
        color: {colors.BLACK};
        font-weight: bold;
        border-radius: 20px;
        border: 1px solid;
        border-color: {colors.MEDIUM_GRAY};
    }}

    QWidget:pressed{{
        border: 2px solid;
        border-color: {colors.MEDIUM_GRAY};
    }}
"""

# Groove is the color of the slot
# Handle is the color of the button
# Add-page is the color of the front
# Sub-page is the color of the back
# If the groove and add-page and sub-page are the same,
# then the color of the groove will be overwritten Off
SLIDER = f"""
    QSlider::groove:horizontal {{
    background: #B3B3B3;
    height: 5px;
    border-radius: 2px;
    }}

    QSlider::groove:horizontal:hover {{
    background: {colors.GREEN};
    }}

    QSlider::add-page:horizontal {{
    background: #535353;
    }}

    QSlider::handle:horizontal {{
    width: 12px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 5px;
    }}

    QSlider::handle:horizontal:hover {{
    background: #FFFFFF;
    }}
"""

LIST = f"""QWidget {{
        background-color: {colors.DARK_GRAY};
    }}
"""
