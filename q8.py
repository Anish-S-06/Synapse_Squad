#Team Name - Synapse_Squad
def sanitize_email(raw_input: str) -> str:
	stripped_email = raw_input.strip()
	lowered_email = stripped_email.lower()
	count = lowered_email.count('@')
	if count == 1:
		return lowered_email
	else:
		return "Invalid Email"
