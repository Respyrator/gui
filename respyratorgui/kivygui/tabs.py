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
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
# Program ---------------------------------------------------------------------
LOG = 'TABS:'
load_kv(__file__)


class GuiTabs(BoxLayout):
    tab_selected = ''
    tab_modes = ObjectProperty()
    tab_params = ObjectProperty()
    tab_alarms = ObjectProperty()
    tab_modes_blocked = BooleanProperty(False)

    def _tab_clicked(self, tab: str, tab_obj):
        if tab != self.tab_selected:
            self.parent.tab_clicked(tab)
        else:
            tab_obj.state = 'down'

    def tab_modes_selected(self):
        self.tab_modes.state = 'down'
        self.tab_params.state = 'normal'
        self.tab_alarms.state = 'normal'
        self.tab_selected = 'modes'

    def tab_params_selected(self):
        self.tab_modes.state = 'normal'
        self.tab_params.state = 'down'
        self.tab_alarms.state = 'normal'
        self.tab_selected = 'params'

    def tab_alarms_selected(self):
        self.tab_modes.state = 'normal'
        self.tab_params.state = 'normal'
        self.tab_alarms.state = 'down'
        self.tab_selected = 'alarms'

    def tab_nothing_selected(self):
        self.tab_modes.state = 'normal'
        self.tab_params.state = 'normal'
        self.tab_alarms.state = 'normal'
        self.tab_selected = ''
