#checks user choice is "integer", "text" or "image"
def user_choice ():

    valid = False
    while not valid:

        response = input("File type (integer / text / image): ").lower()

        if response == "text"or response == "t":
            return response 

        else:
            print("please choose a vaild file type!")
            print()


# Main routine goes here
data_type = user_choice()