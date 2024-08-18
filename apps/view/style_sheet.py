# coding: utf-8
from enum import Enum

from qfluentwidgets import StyleSheetBase, Theme, isDarkTheme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """
    HOME_INTERFACE = "home_interface"
    SETTING_INTERFACE = "SettingInterface"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"D:/desktop/AutoSprint/Resource/qss/{theme.value.lower()}/{self.value}.qss"
