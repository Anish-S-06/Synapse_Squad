#Team Name - Synapse_Squad
def average_passing_grades ( grades : list [ int ]) -> float :
 average=0.0
 count=0
 for grade in grades :
        if grade >= 50 :
            average += grade
            count += 1
 if count == 0 :
    return 0.0
 return average / count
