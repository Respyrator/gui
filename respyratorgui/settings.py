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
from datetime import datetime
from pathlib import Path
import logging
# Installed -------------------------------------------------------------------
# Coded -----------------------------------------------------------------------
# Program ---------------------------------------------------------------------
PROJECT_DIR = Path(__file__).resolve().parents[1]
BASE_DIR = Path(__file__).resolve().parents[0]
# PARSE CONFIGURATION ---------------------------------------------------------
CONF_FILE = BASE_DIR / 'configuration.ini'
cfg = ConfigParser()
cfg.read(str(CONF_FILE))
# LOG -------------------------------------------------------------------------
LOG_DIR = PROJECT_DIR / 'log'
LOG_DIR.mkdir(parents=True, exist_ok=True)
# Loggers
logapp = logging.getLogger('app')
logapp.setLevel(logging.DEBUG)
# Handlers
timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
LOG_APP_FILE = LOG_DIR / f'app_{timestamp}.log'
app_filehandler = logging.FileHandler(filename=str(LOG_APP_FILE))
app_filehandler.setLevel(logging.DEBUG)
LOG_MCU_FILE = LOG_DIR / f'mcu_{timestamp}.log'
console_streamhandler = logging.StreamHandler()
console_streamhandler.setLevel(logging.DEBUG)
# Formatter
fmt = '%(asctime)s | %(levelname)s | %(module)s | %(funcName)s ' \
    '| %(message)s'
formatter = logging.Formatter(fmt)
app_filehandler.setFormatter(formatter)
console_streamhandler.setFormatter(formatter)
# Add handlers to loggers
logapp.addHandler(app_filehandler)
logapp.addHandler(console_streamhandler)
# First message
LOG = 'SETTINGS:'
logapp.debug(f'{LOG} Log settings completed ')
