def get_user_yes_or_no(question):
    while True:
        response = input(f"{question} (y/n): ").strip().lower()

        # check if the response is valid
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please answer with 'y' or 'n'.")
