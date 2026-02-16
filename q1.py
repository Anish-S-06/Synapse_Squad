#Team name - Synapse_Squad
def calculate_total_bill(amount: float,tip_percent: int) -> float:
    total = (amount * tip_percent) / 100
    return total + amount
