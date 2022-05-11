
def num_check(question):
        valid = False
        while not valid:

            error = "please enter a number that is more that zero"

            try:

                # ask user to enter a number
                response = float(input(question))

                # check number more than zero
                if response > 0:
                    return response

                # outputs error if input is iinvalid
                else:          
                    print(error)
                    print()

            except ValueError:
                print(error)
 