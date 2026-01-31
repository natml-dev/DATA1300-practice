def celsius_to_fahrenheit(celsius:float) -> float:
    return celsius*9/5+32

def fahrenheit_to_celsius(fahrenheit: float)-> float:
    return (fahrenheit-32)/1.8

def celsius_to_kelvin (celsius:float)-> float:
    return celsius+273.15

if __name__=="__main__":
    print("Temperature converter test")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"32°F = {fahrenheit_to_celsius(32)}°C")
    print(f"0°C = {celsius_to_kelvin(0)}K")