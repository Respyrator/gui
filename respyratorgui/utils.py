def get_modes() -> dict:
    # TODO: get modes supported by the ventilator
    # TODO: modes are order by
    # 1. ventilation control > assisted > support > spontaneous
    # 2. Control pressure > volume > both
    modes = {
        'ventilation_control': {
            'control_pressure': [
                {
                    "name": "pressure_control",
                    "text": "Control Presión"
                }
            ],
            'control_volume': [
                {
                    "name": "volume_control",
                    "text": "Control Volumen"
                },
            ],
            'control_both': []
        },
        'ventilation_assisted': {
            'control_pressure': [
                {
                    "name": "pressure_assisted",
                    "text": "Asistido Presión"
                }
            ],
            'control_volume': [
                {
                    "name": "volume_assisted",
                    "text": "Asistido Volumen"
                }
            ],
            'control_both': []
        },
        'ventilation_support': {
            'control_pressure': [
                {
                    "name": "pressure_support",
                    "text": "Soporte Presión"
                }
            ],
            'control_volume': [],
            'control_both': []
        },
        'ventilation_spontaneous': {
            'control_pressure': [],
            'control_volume': [],
            'control_both': [
                {
                    "name": "spontaneous",
                    "text": "Espontánea"
                }
            ]
        }
    }
    return modes


def get_params(mode: str) -> dict:
    # TODO: Ask for params of the specific <mode>
    # TODO: params are order by -> [PEEP, FiO2, I:E, ...]
    print(f'mode to params is {mode}')
    params = {
        'peep': {
            'name': 'peep',
            'acronym': 'PEEP',
            'units': 'cmH2O',
            'text': 'PEEP',
            'default': 80,
            'value': 0,
            'min': 20,
            'max': 100,
            'step': 5,
        },
        'pip': {
            'name': 'pip',
            'acronym': 'PIP',
            'units': 'cmH2O',
            'text': 'Presion de Pico',
            'default': 180,
            'value': 0,
            'min': 60,
            'max': 200,
            'step': 20,
        },
        'tidal_volume': {
            'name': 'tidal_volume',
            'acronym': 'Vt',
            'units': 'L',
            'text': 'Volumen Tidal',
            'default': 3,
            'value': 0,
            'min': 1.5,
            'max': 5,
            'step': 0.5,
        },
        'flux': {
            'name': 'flux',
            'acronym': 'F',
            'units': 'mL/cm2',
            'text': 'Flujo',
            'default': 6,
            'value': 0,
            'min': 2,
            'max': 10,
            'step': 1,
        }
    }
    return params


def get_alarms(mode: str) -> dict:
    # TODO: Ask for alarms of the specific <mode>
    # TODO: alarms are order by -> [PEEP, FiO2, I:E, ...]
    print(f'mode to alarms is {mode}')
    params = {
        'peep': {
            'name': 'peep',
            'acronym': 'PEEP',
            'units': 'cmH2O',
            'text': 'PEEP',
            'default': 80,
            'value_min': 0,
            'value_max': 0,
            'min': 20,
            'max': 100,
            'step': 5,
        },
        'pip': {
            'name': 'pip',
            'acronym': 'PIP',
            'units': 'cmH2O',
            'text': 'Presion de Pico',
            'default': 180,
            'value_min': 0,
            'value_max': 0,
            'min': 60,
            'max': 200,
            'step': 20,
        },
        'tidal_volume': {
            'name': 'tidal_volume',
            'acronym': 'Vt',
            'units': 'L',
            'text': 'Volumen Tidal',
            'default': 3,
            'value_min': 0,
            'value_max': 0,
            'min': 1.5,
            'max': 5,
            'step': 0.5,
        },
        'flux': {
            'name': 'flux',
            'acronym': 'F',
            'units': 'mL/cm2',
            'text': 'Flujo',
            'default': 6,
            'value_min': 0,
            'value_max': 0,
            'min': 2,
            'max': 10,
            'step': 1,
        }
    }
    return params
