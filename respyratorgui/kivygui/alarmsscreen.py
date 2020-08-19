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
from kivy.properties import ObjectProperty, DictProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
# Coded -----------------------------------------------------------------------
from respyratorgui import logapp
from . import load_kv
# Program ---------------------------------------------------------------------
LOG = 'AlarmsScreen:'

load_kv(__file__)


class AlarmsScreen(Screen):
    alarms_layout: GridLayout = ObjectProperty()
    alarms = DictProperty({})

    def load_alarms(self, alarms: dict):
        self.alarms.update(alarms)
        # Clean alarms matrix
        self.alarms_layout.clear_widgets()
        # Get each alarm
        for _, v in alarms.items():
            alarm = Alarm()
            alarm.load_alarm(v)
            self.alarms_layout.add_widget(alarm)


class Alarm(BoxLayout):
    alarm_label: Label = ObjectProperty()
    alarm_value_min: Slider = ObjectProperty()
    alarm_value_max: Slider = ObjectProperty()
    data = DictProperty({})

    def update_parent(self):
        self.data['value'] = self.alarm_value_min.value
        alarm = self.data['name']
        value = self.data['value']
        App.get_running_app().update_alarms(alarm, value)

    def set_text(self, value):
        print(f'value = {value}')
        text = f"{self.data['acronym']}: {value:.2f} ({self.data['units']})"
        self.alarm_label.text = text
        self.update_parent()

    def load_alarm(self, data: dict):
        print(f'alarm = {data}')
        self.data.update(data)
        # Set slider
        self.alarm_value_min.step = float(data['step'])
        self.alarm_value_min.min = float(data['min'])
        self.alarm_value_min.max = float(data['max'])
        # <value> need to be the last because when set <min> you have an event
        self.alarm_value_min.value = float(data['default'])
