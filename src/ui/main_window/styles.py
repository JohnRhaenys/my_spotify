from src.ui import colors

LEFT_AREA = f"""QWidget {{
    background-color: {colors.BLACK};
}}"""

RIGHT_AREA = f"""QWidget {{
    background-color: {colors.DARK_GRAY};
}}"""

BOTTOM_AREA = f"""QWidget {{
    background-color: {colors.MEDIUM_GRAY};
}}"""

SPLITTER = f"""QWidget {{
    background-color: {colors.LIGHT_GRAY};
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

PLAYLIST_BUTTON = f"""QWidget{{
        background-color: {colors.GREEN};
        color: {colors.BLACK};
        font-weight: bold;
        border-radius: 20px;
        border: 2px solid;
        border-color: {colors.BLACK};
    }}
    
    QWidget::hover{{
        border: 1px solid;
        font-size: 16px;
        border-color: {colors.BLACK};
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


SONGS_LIST = f"""QWidget {{
        background-color: {colors.DARK_GRAY};
    }}
    
    QWidget::item:selected {{ 
        background-color: {colors.DARK_GRAY};
    }}
"""

PLAYLIST_LIST = f"""QWidget {{
        background-color: {colors.BLACK};
    }}

    QWidget::item:selected {{ 
        background-color: {colors.BLACK};
    }}
"""

PLAYLIST_TITLE = f"""QWidget{{
    color: {colors.WHITE};
    font-size: 52px;
    font-weight: bold;
}}"""
