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
    # TODO: params are orde -> [PEEP, FiO2, I:E, ...]
    print(f'mode to params is {mode}')
    params = {
        'peep': {
            'acronym': 'PEEP',
            'units': 'cmH2O',
            'text': 'PEEP',
            'default': 80,
            'min': 20,
            'max': 100,
            'step': 5,
        },
        'tidal_volume': {
            'acronym': 'Vt',
            'units': 'L',
            'text': 'Volumen Tidal',
            'default': 3,
            'min': 1.5,
            'max': 5,
            'step': 0.5,
        }
    }
    return params
