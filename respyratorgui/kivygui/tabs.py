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
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.togglebutton import ToggleButton
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
# Program ---------------------------------------------------------------------
LOG = 'TABS:'
load_kv(__file__)


class GuiTabs(BoxLayout):
    modes_state = StringProperty('normal')
    params_state = StringProperty('normal')
    alarms_state = StringProperty('normal')
    modes_enabled = BooleanProperty(False)

    def _togglebutton_always_selected(self, tb: ToggleButton):
        if tb:
            tb.state = 'down'

    def tab_selected(self, tab: str, tb: ToggleButton = None):
        logapp.info(f'{LOG} tab_selected({tab})')
        if self.modes_enabled:
            self.modes()
        else:
            self._togglebutton_always_selected(tb)

    def modes(self):
        logapp.debug(f'{LOG} modes()')
        self.modes_enabled = True
        self.modes_state = 'down'
        self.params_state = 'normal'
        self.alarms_state = 'normal'

    def params(self):
        logapp.debug(f'{LOG} params()')
        self.modes_enabled = False
        self.modes_state = 'normal'
        self.params_state = 'down'
        self.alarms_state = 'normal'

    def alarms(self):
        logapp.debug(f'{LOG} alarms()')
        self.modes_enabled = False
        self.modes_state = 'normal'
        self.params_state = 'normal'
        self.alarms_state = 'down'
