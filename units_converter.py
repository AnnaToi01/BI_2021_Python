# American measurement system to SI Units


def inch_to_cm(value):
    """
    Converts inches to kilometer (Distance)
    """
    if value < 0:
        return "Measured distance cannot be less than 0"
    return value*2.54


def feet_to_m(value):
    """
    Converts feet to meter (Distance)
    """
    if value < 0:
        return "Measured distance cannot be less than 0"
    return value/3.281


def mile_to_km(value):
    """
    Converts mile to kilometer (Distance)
    """
    if value < 0:
        return "Measured distance cannot be less than 0"
    return value*1.60934


def fahrenheit_to_celsius(value):
    """
    Converts fahrenheit to kelvin (Temperature)
    """
    if value < -459.67:
        return "You've reached the absolute minimum of temperature"
    return (value - 32)*5/9


def cup_to_cubicmeter(value):
    """
    Converts cup to cubic meter (Volume)
    """
    if value < 0:
        return "Volume cannot be less than 0"
    return value/4427


def gallon_to_liter(value):
    """
    Converts cup to cubic meter (Volume)
    """
    if value < 0:
        return "Volume cannot be less than 0"
    return value*3.78541


dic_func = {
    "fahrenheit": fahrenheit_to_celsius,
    "inch": inch_to_cm,
    "feet": feet_to_m,
    "mile": mile_to_km,
    "cup": cup_to_cubicmeter,
    "gallon": gallon_to_liter
}


in_units = ["inch", "feet", "mile", "fahrenheit", "cup", "gallon"]
out_units = ["centimeter", "meter", "kilometer", "celsius", "cubicmeter", "liter"]

try:
    in_unit = input("Enter an input unit: ").lower()
    out_unit = input("Enter an output unit: ").lower()
    in_value = float(input("Enter the value: "))
    if in_units.index(in_unit) == out_units.index(out_unit):
        print(dic_func[in_unit](in_value))
    else:
        Exception
except Exception:
    print("False units. Possible unit conversions are:"
          "\ninch to centimeter\nfeet to meter\nmile to kilometer"
          "\nfahrenheit to celsius"
          "\ncup to cubicmeter\ngallon to liter")
