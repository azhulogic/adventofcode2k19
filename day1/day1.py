import math
total_fuel = 0

def mod_fuel(m_mass):
    global total_fuel
    mod_fuel = math.floor(m_mass / 3) - 2
    total_fuel += mod_fuel + fuel_fuel(mod_fuel)

def fuel_fuel(f_mass):
    f_fuel = math.floor(f_mass / 3) - 2

    if f_fuel > 0:
        return fuel_fuel(f_fuel) + f_fuel
    else:
        return 0

with open('input.txt') as openfileobject:
    for line in openfileobject:
        mod_fuel(int(line))

print(total_fuel)
