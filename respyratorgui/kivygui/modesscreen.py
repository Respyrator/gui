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
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
# Coded -----------------------------------------------------------------------
from respyratorgui import logapp
from . import load_kv
# Program ---------------------------------------------------------------------
LOG = 'ModesScreen:'

load_kv(__file__)


class ModesScreen(Screen):
    modes_buttons_layout = ObjectProperty()

    def mode_selected(self, mode: str):
        logapp.info(f'{LOG} mode_selected({mode})')
        App.get_running_app().mode = mode

    def load_modes(self, modes: list[dict]):
        self.modes_buttons_layout.clear_widgets()
        ventilation = ''
        for mode in modes:
            if ventilation != mode[ventilation]:
                v = 


class VentilationButtonsLayout(BoxLayout):
    pass


class ControlButtonsLayout(BoxLayout):
    pass
