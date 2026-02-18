# Function go here
def number_check(question, num_type, exit_code = None):
    """Check users enter an integer / float that is more than zero
    (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - Please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - Please enter an integer between zero and zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here

# loop for testing purpose...
while True:
    print()

    my_float = number_check("Please enter a number more than 0: ", "float")
    print(f"Thanks. You chose {my_float}.")
    print()
    my_int = number_check("Please enter an integer more than 0: ",
                          "integer", "")

    if my_int == "":
        print("You have chosen a infinite mode")
    else:
        print(f"Thanks. You chose {my_int}.")