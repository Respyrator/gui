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
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
# Coded -----------------------------------------------------------------------
from respyratorgui import logapp
from . import load_kv
# Program ---------------------------------------------------------------------
LOG = 'ModesScreen:'

load_kv(__file__)


class ModesScreen(Screen):
    modes_buttons_layout = ObjectProperty()

    def mode_selected(self, mode: str, instance):
        logapp.info(f'{LOG} mode_selected({mode})')
        App.get_running_app().mode = mode

    def _add_buttons(self, layout, buttons: list):
        for button in buttons:
            btn = Button(text=button['text'])
            btn.bind(on_press=partial(self.mode_selected, button['name']))
            layout.add_widget(btn)

    def _pressure_volume_buttons(self, layout, pressure: list, volume: list):
        if len(pressure) + len(volume):
            vent_btns = VentilationButtonsLayout()
            # Add buttons pressure to ControlButtonsLayout
            ctrl_btns = ControlButtonsLayout()
            self._add_buttons(ctrl_btns, pressure)
            vent_btns.add_widget(ctrl_btns)
            # Add buttons volume to ControlButtonsLayout
            ctrl_btns = ControlButtonsLayout()
            self._add_buttons(ctrl_btns, volume)
            vent_btns.add_widget(ctrl_btns)
            # Add row to ModeButtonsLayout
            layout.add_widget(vent_btns)

    def _both_buttons(self, layout, both: list):
        if len(both):
            self._add_buttons(layout, both)

    def _load_row_buttons(self, row: dict):
        modes_btns = ModeButtonsLayout()
        # Routine for control pressure and control volume
        column_pressure: list = row['control_pressure']
        column_volume: list = row['control_volume']
        self._pressure_volume_buttons(
            modes_btns, column_pressure, column_volume)
        # Routine for both control
        column_both: list = row['control_both']
        self._both_buttons(modes_btns, column_both)
        # Load buttons
        self.modes_buttons_layout.add_widget(modes_btns)

    def load_modes(self, modes: dict):
        # Clean buttons matrix
        self.modes_buttons_layout.clear_widgets()
        # Pass each ventilation row
        self._load_row_buttons(modes['ventilation_control'])
        self._load_row_buttons(modes['ventilation_assisted'])
        self._load_row_buttons(modes['ventilation_support'])
        self._load_row_buttons(modes['ventilation_spontaneous'])


class ModeButtonsLayout(BoxLayout):
    pass


class VentilationButtonsLayout(BoxLayout):
    pass


class ControlButtonsLayout(BoxLayout):
    pass
