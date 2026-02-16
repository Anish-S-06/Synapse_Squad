#Team Name - Synapse_Squad
def count_inventory(fruit_list: list[str])->dict[str,int]:
    dictionary ={}
    for fruit in fruit_list:
        if fruit in dictionary:
            dictionary[fruit]+=1
        else:
            dictionary[fruit]=1
    return dictionary
