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
from kivy.properties import ObjectProperty, StringProperty
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

    def ui_modes(self):
        self.content.ui_modes()
        self.tabs.tab_modes_on()


class GuiApp(App):
    mode = StringProperty()

    def build(self):
        logapp.debug(f'{LOG} build()')
        Clock.schedule_once(lambda dt: self.setup(), 5.0)
        return GuiContainer()

    def setup(self):
        self.root.ui_modes()

    def mode_selected(self, mode: str):
        self.mode = mode


if __name__ == "__main__":
    GuiApp().run()
