
def loud(l_text):
    return l_text.upper()


def quiet(q_text):
    return q_text.lower()


def text(a_function):                        # a funtion as the parameter
    user_text = input("\nInput text to say: ").lower()
    if user_text.isdigit():                  # input should not be digit
        return " Invalid input - string only "
    else:
        returned_text = a_function(user_text)
        return returned_text

