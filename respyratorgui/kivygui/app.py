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
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import NoTransition
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
# Program ---------------------------------------------------------------------
LOG = 'APP:'
load_kv(__file__)


class GuiContainer(BoxLayout):
    pass


class GuiApp(App):
    sm = ObjectProperty()
    tabs = ObjectProperty()

    def build(self):
        logapp.debug(f'{LOG} build()')
        #Clock.schedule_once(lambda x: self.setup())
        container = GuiContainer()
        return container

    def setup(self):
        print("mi polla en tu boca")
        self.root.sm.transition = NoTransition()

    def tab_selected(self, tab=''):
        screens = {
            'modes': 'modes_screen',
            'alarms': 'alarms_screen',
            'params': 'params_screen',
            'monitoring': 'monitoring_screen'
        }
        self.root.sm.current = screens.get(tab, 'loading_screen')


if __name__ == "__main__":
    GuiApp().run()
