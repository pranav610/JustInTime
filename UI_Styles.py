

class Style():

    style_bt_standard = (
        """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(255,137,0);
        background-color: rgb(255,137,0);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(255,137,0);
        border-right: 5px solid rgb(247,240,231);
        background-color: rgb(255,137,0);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(252,207,140);
        border-left: 28px solid rgb(252,207,140);
    }
    QPushButton:pressed {
        background-color: rgb(255,0,26);
        border-left: 28px solid rgb(255,0,26);
    }
    """
    )
