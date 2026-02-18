# Function go here
def string_check(question, valid_ans_list, num_letters):
    """Check that a user enter the full word or the 'n' letter/s of the word from
    a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

            print(f"Please choose an option from {valid_ans_list} ")


# main routine goes here
yes_no_list = ["yes", "no"]
payment_list =["cash", "credit"]

Like_coffee = string_check("Do you like Coffee? ", yes_no_list, 1)

print(f"You chose {Like_coffee}")
play_method = string_check("Payment method: ", payment_list, 2)
print(f"You chose {play_method}")