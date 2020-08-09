# Copyright (C) 2020 Respyrator
# This file is part of Respyrator <https://respyrator.github.io>.
#
# Respyrator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrator.  If not, see <http://www.gnu.org/licenses/>.

# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
from .content import GuiContent
from .tabs import GuiTabs
# Program ---------------------------------------------------------------------
LOG = 'CONTAINER:'
load_kv(__file__)


class GuiContainer(BoxLayout):
    content = ObjectProperty()
    tabs = ObjectProperty()
    block_tab_modes = BooleanProperty(False)

    def unblock_tabs(self):
        self.block_tab_modes = False

    def ui_modes(self):
        self.block_tab_modes = True
        self.content.ui_modes()
        self.tabs.tab_modes_selected()

    def ui_params(self):
        if not self.block_tab_modes:
            self.content.ui_params()
            self.tabs.tab_params_selected()
        else:
            self.ui_modes()

    def ui_alarms(self):
        if not self.block_tab_modes:
            self.content.ui_alarms()
            self.tabs.tab_alarms_selected()
        else:
            self.ui_modes()
