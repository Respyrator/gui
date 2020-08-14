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
from kivy.app import App
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

    def _unblock_tabs(self):
        self.block_tab_modes = False

    def tab_clicked(self, tab: str):
        if tab == 'modes':
            App.get_running_app().mode = ''
        elif App.get_running_app().mode != '':
            self.ui_params() if tab == 'params' else self.ui_alarms()
        else:
            self.ui_modes()

    def load_modes(self, modes: dict):
        self.content.load_modes(modes)

    def ui_loading(self):
        self.content.ui_loading()
        self.tabs.tab_nothing_selected()

    def ui_modes(self):
        self.content.ui_modes()
        self.tabs.tab_modes_selected()

    def ui_params(self):
        self.content.ui_params()
        self.tabs.tab_params_selected()

    def ui_alarms(self):
        self.content.ui_alarms()
        self.tabs.tab_alarms_selected()
