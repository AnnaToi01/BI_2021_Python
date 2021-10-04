# Pressure converter

def atm_to_bar(value):
    """
    Converts atmosphere to bar
    """
    return value*1.01325

def bar_to_atm(value):
    """
    Converts bar to atmosphere
    """
    return value/1.01325

def bar_to_pascal(value):
    """
    Converts bar to pascal
    """
    return value*10**5

def atm_to_pascal(value):
    """
    Converts atmosphere to pascal
    """
    return atm_to_bar(bar_to_pascal(value))

#American measurement system to SI Units

def inch_to_km(value):
    """
    Converts inches to kilometer (Distance)
    """
    return value/39370

def feet_to_km(value):
    """
    Converts feet to kilometer (Distance)
    """
    return value/3281

def mile_to_km(value):
    """
    Converts mile to kilometer (Distance)
    """
    return value*1.60934

def yard_to_km(value):
    """
    Converts yards to kilometer (Distance)
    """
    return value/1094

def fahrenheit_to_kelvin(value):
    """
    Converts fahrenheit to kelvin (Temperature)
    """
    return (value - 32)*5/9+ 273.15

def cup_to_ml(value):
    """
    Converts cup to milliliter (Volume)
    """
    return value*236.588

def pound_to_kilogram(value):
    """
    Converts pounds to kilograms
    """
    return value/2.205
