# Function go here
def int_check(question):
    """Check users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            response = int(input(question)) # Return the response if it's an integer

            return response

        except ValueError:
            print(error)


# main routine goes here

# loop for testing purpose
while True:
    print()

    # ask users for their names
    name= input("Name: ") # replace with call to 'not blank' function

    # ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")