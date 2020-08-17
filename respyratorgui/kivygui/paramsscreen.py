
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
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
# Coded -----------------------------------------------------------------------
from respyratorgui import logapp
from . import load_kv
# Program ---------------------------------------------------------------------
LOG = 'ParamsScreen:'

load_kv(__file__)


class ParamsScreen(Screen):
    params_layout = ObjectProperty()

    def load_params(self, params: dict):
        print(f'params = {params}')
        # Clean params matrix
        self.params_layout.clear_widgets()
        # Get each param



class Param(BoxLayout):
    #acronym = StringProperty('Param')
    #txt = StringProperty()
    #val = NumericProperty()
    #units = StringProperty('units')

    def get_value(self):
        print(f'{self.acronym} - {self.val}')
        self.txt = f'{self.acronym}: {self.val} ({self.units})'
