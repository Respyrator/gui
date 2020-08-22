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
    alarm_label_min: Label = ObjectProperty()
    alarm_value_min: Slider = ObjectProperty()
    alarm_label_max: Label = ObjectProperty()
    alarm_value_max: Slider = ObjectProperty()
    data = DictProperty({})

    def _adjust_limits(self, value: str):
        if value == 'min':
            # Greatest min value is the lowest max value
            if self.alarm_value_min.value > self.alarm_value_max.value:
                self.alarm_value_min.value = self.alarm_value_max.value
        else:
            # Lowest max value is the greatest min value
            if self.alarm_value_max.value < self.alarm_value_min.value:
                self.alarm_value_max.value = self.alarm_value_min.value

    def _set_text(self, value: str):
        acronym = self.data['acronym']
        units = self.data['units']
        if value == 'min':
            v = self.alarm_value_min.value
            self.alarm_label_min.text = f'MIN {acronym}: {v:.2f} ({units})'
        else:
            v = self.alarm_value_max.value
            self.alarm_label_max.text = f'MAX {acronym}: {v:.2f} ({units})'

    def _update_parent(self, value: str):
        if value == 'min':
            self.data['value_min'] = self.alarm_value_min.value
            v = self.alarm_value_min.value
        else:
            self.data['value_max'] = self.alarm_value_max.value
            v = self.alarm_value_max.value
        alarm = self.data['name']
        App.get_running_app().update_alarms(alarm, value, v)

    def updated_value(self, value: str, instance: Slider):
        self._adjust_limits(value)
        self._set_text(value)
        self._update_parent(value)
        logapp.debug(f'{value} updated to {instance.value}')

    def load_alarm(self, data: dict):
        self.data.update(data)
        # Set slider Min
        # <value> need to be the last because when set <min> you have an event
        self.alarm_value_min.step = float(data['step'])
        self.alarm_value_min.max = float(data['max'])
        self.alarm_value_min.min = float(data['min'])
        self.alarm_value_min.value = float(data['default'])
        # Set slider Max
        # <value> need to be the last because when set <min> you have an event
        self.alarm_value_max.step = float(data['step'])
        self.alarm_value_max.max = float(data['max'])
        self.alarm_value_max.min = float(data['min'])
        self.alarm_value_max.value = float(data['default'])
        # TODO: double assignation is a bug because event but this solved it
        self.alarm_value_min.value = self.data['default']
        self.alarm_value_max.value = self.data['default']
