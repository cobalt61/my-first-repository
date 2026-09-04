"""Bob responds depending on what you tell him."""
def response(hey_bob):
    """Bob responds depending on what you tell him."""
    if hey_bob.strip().endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.strip().endswith("?"):
        return "Sure."
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
    
