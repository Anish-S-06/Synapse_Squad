#Team Name - Synapse_Squad
def get_ticket_price ( age : int , is_student : bool ) -> int :
 if age < 12 :
  return 8
 elif 12 <= age <= 64:
    if is_student :
     return 12
    else :
     return 15
 else :
    return 10
