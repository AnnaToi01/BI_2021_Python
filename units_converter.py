# American measurement system to SI Units

class UnitsError(Exception):
    pass

def inch_to_cm(value):
    """
    Converts inches to centimeter (Distance)
    """
    if value < 0:
        return "Distance cannot be less than 0"
    return value*2.54


def feet_to_m(value):
    """
    Converts feet to meter (Distance)
    """
    if value < 0:
        return "Distance cannot be less than 0"
    return value/3.281


def mile_to_km(value):
    """
    Converts mile to kilometer (Distance)
    """
    if value < 0:
        return "Distance cannot be less than 0"
    return value*1.60934


def fahrenheit_to_kelvin(value):
    """
    Converts fahrenheit to kelvin (Temperature)
    """
    if value < -459.67:
        return "You've reached the absolute minimum of temperature"
    return (value - 32)*5/9 + 273.15


def cup_to_ml(value):
    """
    Converts cup to milliliter (Volume)
    """
    if value < 0:
        return "Volume cannot be less than 0"
    return value*236.588


def pound_to_kilogram(value):
    """
    Converts pounds to kilograms
    """
    if value < 0:
        return "Mass of an object cannot be less than 0"
    return value/2.205


dic_func = {
    "inch": inch_to_cm,
    "feet": feet_to_m,
    "mile": mile_to_km,
    "fahrenheit": fahrenheit_to_kelvin,
    "cup": cup_to_ml,
    "pound": pound_to_kilogram
}


in_units = ["inch", "feet", "mile", "fahrenheit", "cup", "pound"]
out_units = ["centimeter", "meter", "kilometer", "kelvin", "milliliter", "kilogram"]

try:
    in_unit = input("Enter an input unit: ").lower()
    out_unit = input("Enter an output unit: ").lower()
    in_value = float(input("Enter the value: "))

    if in_unit not in in_units or out_unit not in out_units:
        raise UnitsError
    elif in_units.index(in_unit) == out_units.index(out_unit):
        print(dic_func[in_unit](in_value))
    else:
        raise UnitsError
except UnitsError:
    print("False units. Possible unit conversions are:"
          "\ninch to centimeter\nfeet to meter\nmile to kilometer"
          "\nfahrenheit to kelvin"
          "\ncup to milliliter\npound to kilogram")