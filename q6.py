#Team Name - Synapse_Squad
def convert_temperature(value : float,unit :str)->float | str:
    if unit.upper() == 'C':
        return round((value*9/5)+32,1)
    elif unit.upper() == 'F':
        return round((value-32)*5/9,1)
    else:
        return 'Invalid Unit'
