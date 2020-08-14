def get_modes() -> dict:
    # TODO: get modes supported by the ventilator
    modes = [
        # TODO: Ordenadorlo por ventilaciones -> control -> name
        "pressure_control": {
            "name": "Control Presión",
            "ventilation": "controlled",
            "control": "pressure",
        },
        "pressure_assisted": {
            "name": "Asistido Presión",
            "ventilation": "assisted",
            "control": "pressure"
        },
        "pressure_support": {
            "name": "Soporte Presión",
            "ventilation": "support",
            "control": "pressure"
        },
        "volume_control": {
            "name": "Control Volumen",
            "ventilation": "controlled",
            "control": "volume"
        },
        "volume_assisted": {
            "name": "Asistido Volumen",
            "ventilation": "assisted",
            "control": "volume"
        },
        "spontaneous": {
            "name": "Espontáneo",
            "ventilation": "spontaneous",
            "control": "both"
        }
    ]
    return modes
