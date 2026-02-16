#Team Name - Synapse_Squad
def convert_temperature(value : float,unit :str)->float:
    if unit == 'C':
        return round((value *9/5)+32,1)
    elif unit == 'F':
        return round((value-32)*5/9,1)
    else:
        return 'Invalid Unit'
