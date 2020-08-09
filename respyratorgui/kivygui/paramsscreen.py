
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
from kivy.app import App
from kivy.properties import StringProperty, BoundedNumericProperty, \
    ObjectProperty, NumericProperty
# Coded -----------------------------------------------------------------------
from respyratorgui import logapp
from . import load_kv
# Program ---------------------------------------------------------------------
LOG = 'ParamsScreen:'

load_kv(__file__)


class Param(BoxLayout):
    param = StringProperty()
    acronym = StringProperty()
    units = StringProperty()
    value_min = NumericProperty()
    value_max = NumericProperty()
    value = NumericProperty()
    text_value = StringProperty(f'{acronym} ({units}): {value}')

    def on_value(self, instance, data):
        self.text_value = f'{self.acronym} ({self.units}): {data}'
        App.get_running_app().param_selected(self.param, data)


class ParamsScreen(Screen):
    params = ObjectProperty()
