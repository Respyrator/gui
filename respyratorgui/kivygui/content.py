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
from kivy.uix.screenmanager import ScreenManager
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
# Program ---------------------------------------------------------------------
LOG = 'CONTENT:'
load_kv(__file__)


class GuiContent(ScreenManager):
    def _set_screen(self, screen: str = ''):
        screens = {
            'modes': 'modes_screen',
            'params': 'params_screen',
            'alarms': 'alarms_screen',
            'monitoring': 'monitoring_screen'
        }
        screen = screens.get(screen, 'loading_screen')
        if self.current != screen:
            self.current = screen

    def load_modes(self, modes: dict):
        screen_modes = self.get_screen('modes_screen')
        screen_modes.load_modes(modes)

    def ui_loading(self):
        self._set_screen()

    def ui_modes(self):
        self._set_screen('modes')

    def ui_params(self, params: dict):
        screen_params = self.get_screen('params_screen')
        screen_params.load_params(params)
        self._set_screen('params')

    def ui_alarms(self):
        self._set_screen('alarms')

    def ui_monitoring(self):
        self._set_screen('monitoring')
