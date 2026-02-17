#Team name - Synapse_Squad
def calculate_total_bill(amount: float,tip_percent: int) -> float:
    tip = (amount * tip_percent) / 100
    total = tip + amount
    return round(total,2)

