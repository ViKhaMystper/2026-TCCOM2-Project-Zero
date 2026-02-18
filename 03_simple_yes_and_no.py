# Functions go here
def yes_no(question):
    """Check user enter yes / y or no / n"""
    while True:
        response = input(question).lower()
        if response == "yes" or "y":
            return "yes"
        elif response == "no" or "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")

# main routine goes here

# loop for test ing purpose
while True:
    want_instruction = yes_no("Do you want to read the instructions? ")
    print(f" You choose {want_instruction}. \n")