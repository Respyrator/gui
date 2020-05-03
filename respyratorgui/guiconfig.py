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
from configparser import ConfigParser
from pathlib import Path
# Installed -------------------------------------------------------------------
# Coded -----------------------------------------------------------------------
from respyratorgui.settings import logapp
# Program ---------------------------------------------------------------------
LOG = 'GUI:'

GUI_CONFIG = Path(__file__).resolve().parents[0] / 'guiconfig.ini'
cfg = ConfigParser()
cfg.read(str(GUI_CONFIG))
# COLORs
gui_colors = {k: v for k, v in cfg['COLORs'].items()}
# IMGs
gui_imgs = {k: v for k, v in cfg['IMGs'].items()}
# TXTs
gui_txts = {k: v for k, v in cfg['TXTs'].items()}

logapp.debug(f'COLORS = {gui_colors}')
logapp.debug(f'IMGS = {gui_imgs}')
logapp.debug(f'TXTS = {gui_txts}')

logapp.info(f'{LOG} configuration completed')
