def format_name(f_name, l_name):
    #considered a comment unless assigned to a variable and also shows as function description
    """Takes the first and last name and returns the title case version of full name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)





