#Team Name - Synapse_Squad
def generate_threes(start: int, end: int)->list[int]:
	if(start>=end):
		return []
	threes = [i for i in range(start,end,3)]
	return threes
	
