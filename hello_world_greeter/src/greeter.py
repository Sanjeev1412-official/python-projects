
def greeter(name: str) -> str:

    cleaned_name = name.strip()
    if cleaned_name == "":
        raise ValueError("Name cannot be empty")
    return f"It is great to meet you, {cleaned_name}!"