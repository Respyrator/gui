def get_modes() -> dict:
    # TODO: get modes supported by the ventilator
    # TODO: Ordenadorlo por ventilaciones -> control -> name
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
