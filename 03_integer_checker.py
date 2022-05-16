# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than (or equal to)  {}".format(low) 

        try:

            # ask user to enter a number
            response = int(input(question))

            # check number more than zero
            if response >= low:
                return response

            # outputs error if input is iinvalid
            else:          
                print(error)
                print()

        except ValueError:
            print(error)


# Main Routine goes here

keep_going = ""
while keep_going == "":
    print()
    # ask the user for an integer (must be more than / equal to 0).
    var_integer = num_check ("Enter an integer: ", 0)
    print()

    # ask for width & height of an image 
    # (must be more than / equal to 1)
    image_width = num_check ("Image width? ", 1)
    print()
    image_height = num_check ("Image height? ",1)
