#checks user choice is "integer", "text" or "image"
def user_choice ():

    valid = False
    while not valid:

        # ask user for choice and change responce to lowercase
        response = input("File type (integer / text / image): ").lower()

        # if they choose "t" or "text", return "text"
        if response == "text"or response == "t":
            return "text"

        else:
            # if responce is not valid, output an error
            print("please choose a vaild file type!")
            print()


# Main routine goes here
data_type = user_choice()
print("you chose", data_type)

print()