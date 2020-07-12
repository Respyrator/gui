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
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import NoTransition
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
from .content import GuiContent
from .tabs import GuiTabs
# Program ---------------------------------------------------------------------
LOG = 'APP:'
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


class GuiApp(App):
    mode = StringProperty()

    def build(self):
        logapp.debug(f'{LOG} build()')
        Clock.schedule_once(lambda dt: self.setup(), 5.0)
        return GuiContainer()

    def setup(self):
        self.ui_selected('modes')

    def ui_selected(self, screen: str):
        ui = {
            'modes': self.root.ui_modes,
            'params': self.root.ui_params,
            'alarms': self.root.ui_alarms,
        }
        ui[screen]()

    def mode_selected(self, mode: str):
        self.mode = mode
        self.root.unblock_tabs()
        self.ui_selected('params')


if __name__ == "__main__":
    GuiApp().run()
