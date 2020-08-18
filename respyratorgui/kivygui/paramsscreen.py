
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
from functools import partial
# Installed -------------------------------------------------------------------
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, DictProperty
# Coded -----------------------------------------------------------------------
from respyratorgui import logapp
from . import load_kv
# Program ---------------------------------------------------------------------
LOG = 'ParamsScreen:'

load_kv(__file__)


class ParamsScreen(Screen):
    params_layout: GridLayout = ObjectProperty()
    params = DictProperty({})

    def load_params(self, params: dict):
        self.params.update(params)
        # Clean params matrix
        self.params_layout.clear_widgets()
        # Get each param
        for _, v in params.items():
            param = Param()
            param.load_param(v)
            self.params_layout.add_widget(param)


class Param(BoxLayout):
    param_label: Label = ObjectProperty()
    param_value: Slider = ObjectProperty()
    data = DictProperty({})

    def update_parent(self):
        self.data['value'] = self.param_value.value
        param = self.data['name']
        value = self.data['value']
        App.get_running_app().update_params(param, value)

    def set_text(self, value):
        print(f'value = {value}')
        text = f"{self.data['acronym']}: {value:.2f} ({self.data['units']})"
        self.param_label.text = text
        self.update_parent()

    def load_param(self, data: dict):
        print(f'param = {data}')
        self.data.update(data)
        # Set slider
        self.param_value.step = float(data['step'])
        self.param_value.min = float(data['min'])
        self.param_value.max = float(data['max'])
        # <value> need to be the last because when set <min> you have an event
        self.param_value.value = float(data['default'])
