def create_character(name, strength, intelligence, charisma):
    # 1. Validate name type
    if not isinstance(name, str):
        return "The character name should be a string."
    
    # 2. Validate name is not empty
    if name == "":
        return "The character should have a name."
    
    # 3. Validate name length
    if len(name) > 10:
        return "The character name is too long."
    
    # 4. Validate name doesn't contain spaces
    if " " in name:
        return "The character name should not contain spaces."
    
    # Put stats into a list for easier iteration and validation
    stats = [strength, intelligence, charisma]
    
    # 5. Validate stats are integers
    # Note: We use type(stat) is int because isinstance(True, int) is True in Python,
    # and we want to ensure strictly integer inputs.
    if any(type(stat) is not int for stat in stats):
        return "All stats should be integers."
    
    # 6. Validate minimum stat value
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1."
    
    # 7. Validate maximum stat value
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4."
    
    # 8. Validate the sum of stats
    if sum(stats) != 7:
        return "The character should start with 7 points."
    
    # 9. Format and return the valid character sheet
    # Total dots per line is 10
    str_dots = "●" * strength + "○" * (10 - strength)
    int_dots = "●" * intelligence + "○" * (10 - intelligence)
    cha_dots = "●" * charisma + "○" * (10 - charisma)
    
    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"
