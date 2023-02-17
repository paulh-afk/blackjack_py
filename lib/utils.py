def user_input(
    sentence: str, exit_message: str = "Incorrect value the program closes"
) -> str:
    try:
        input_value = input(sentence)
        return input_value.strip()
    except EOFError:
        print(exit_message)
        exit()
    except KeyboardInterrupt:
        print(exit_message)
        exit()


def user_input_int(sentence: str) -> int:
    input_value = user_input(sentence)

    if not input_value.isdigit():
        print("Invalid type value, this value must be an integer!")
        exit()

    return int(input_value)
