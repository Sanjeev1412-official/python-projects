from typing import Dict, Tuple

LENGTH_REGISTRY: Dict[str, Dict[str, float]] = {
    "meters": {"to_base": 1.0, "from_base": 1.0},
    "kilometers": {"to_base": 1000.0, "from_base": 0.001},
    "miles": {"to_base": 1609.344, "from_base": 1 / 1609.344},
    "feet": {"to_base": 0.3048, "from_base": 1 / 0.3048},
    "inches": {"to_base": 0.0254, "from_base": 1 / 0.0254}
}

WEIGHT_REGISTRY: Dict[str, Dict[str, float]] = {
    "kilograms": {"to_base": 1.0, "from_base": 1.0},
    "grams": {"to_base": 0.001, "from_base": 1000.0},
    "pounds": {"to_base": 0.453592, "from_base": 1 / 0.453592},
    "ounces": {"to_base": 0.0283495, "from_base": 1 / 0.0283495}
}

TEMPERATURE_UNITS: Tuple[str, ...] = ("celsius", "fahrenheit", "kelvin")

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    clean_from = from_unit.strip().lower()
    clean_to = to_unit.strip().lower()

    if clean_from not in LENGTH_REGISTRY or clean_to not in LENGTH_REGISTRY:
        supported = ", ".join(LENGTH_REGISTRY.keys())
        raise ValueError(f"Unsupported unit type requested. Supported units: {supported}")

    if value < 0:
        raise ValueError("Length value scales cannot be negative numbers.")

    base_value = value * LENGTH_REGISTRY[clean_from]["to_base"]
    converted_value = base_value * LENGTH_REGISTRY[clean_to]["from_base"]

    return converted_value

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    clean_from = from_unit.strip().lower()
    clean_to = to_unit.strip().lower()

    if clean_from not in WEIGHT_REGISTRY or clean_to not in WEIGHT_REGISTRY:
        supported = ", ".join(WEIGHT_REGISTRY.keys())
        raise ValueError(f"Unsupported unit type requested. Supported units: {supported}")

    if value < 0:
        raise ValueError("Weight value scales cannot be negative numbers.")

    base_value = value * WEIGHT_REGISTRY[clean_from]["to_base"]
    converted_value = base_value * WEIGHT_REGISTRY[clean_to]["from_base"]

    return converted_value

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    clean_from = from_unit.strip().lower()
    clean_to = to_unit.strip().lower()

    if clean_from not in TEMPERATURE_UNITS or clean_to not in TEMPERATURE_UNITS:
        supported = ", ".join(TEMPERATURE_UNITS)
        raise ValueError(f"Unsupported unit type requested. Supported units: {supported}")
    
    if clean_from == clean_to:
        return value

    # Convert everything to Celsius as base
    if clean_from == "celsius":
        celsius_value = value
    elif clean_from == "fahrenheit":
        celsius_value = (value - 32) * 5.0 / 9.0
    elif clean_from == "kelvin":
        if value < 0:
            raise ValueError("Kelvin cannot be negative.")
        celsius_value = value - 273.15

    # Convert from Celsius to target
    if clean_to == "celsius":
        return celsius_value
    elif clean_to == "fahrenheit":
        return (celsius_value * 9.0 / 5.0) + 32
    elif clean_to == "kelvin":
        kelvin_val = celsius_value + 273.15
        return max(kelvin_val, 0.0) # To avoid -0.0