# coding:utf-8
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF

class autosprintInterface:
    def __init__(self):
        super().__init__(self)
        self.aboutCard = PrimaryPushSettingCard(
            self.tr('En'),
            FIF.INFO,
            self.tr('About'),
            self.aboutGroup
        )