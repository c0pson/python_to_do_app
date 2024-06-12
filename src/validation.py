def validate_input(new_value, max_length: int) -> bool:
    if new_value.isdigit()  and len(new_value) <= max_length:
        return True
    elif new_value == '':
        return True
    return False
