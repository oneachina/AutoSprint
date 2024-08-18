# coding:utf-8
import sys
from enum import Enum
from PyQt5.QtCore import QLocale
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            OptionsValidator, RangeConfigItem, RangeValidator,
                            Theme, ConfigSerializer)


class Language(Enum):
    """ Language enumeration """
    CHINESE_SIMPLIFIED = QLocale(QLocale.Chinese, QLocale.China)
    CHINESE_TRADITIONAL = QLocale(QLocale.Chinese, QLocale.HongKong)
    ENGLISH = QLocale(QLocale.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """
    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


class Config(QConfig):
    """ Config of application """
    # main window
    micaEnabled = ConfigItem("MainWindow", "MicaEnabled", isWin11(), BoolValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    language = OptionsConfigItem(
        "MainWindow", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)

    # Material
    blurRadius = RangeConfigItem("Material", "AcrylicBlurRadius", 15, RangeValidator(0, 40))


YEAR = 2024
AUTHOR = "onea"
VERSION = "1.0.0"
HELP_URL = "https://github.com/oneachina/AutoSprint/"
REPO_URL = "https://github.com/oneachina/AutoSprint/"
FEEDBACK_URL = "https://github.com/oneachina/AutoSprint/issues"
RELEASE_URL = "https://github.com/oneachina/AutoSprint/releases"
ZH_SUPPORT_URL = "https://github.com/oneachina/AutoSprint/"
EN_SUPPORT_URL = "https://github.com/oneachina/AutoSprint/"

cfg = Config()
cfg.themeMode.value = Theme.AUTO
qconfig.load('config/setting.json', cfg)
