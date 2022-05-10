#checks user choice is "integer", "text" or "image"
def user_choice ():

    # Lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#" "number"]
    image_ok = ["image", "img", "pix", "picture", "pic", "p"]

    valid = False
    while not valid:

        # ask user for choice and change responce to lowercase
        response = input("File type (integer / text / image): ").lower()

        # Checks for valid respondse and returns text, integer or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"
        
        elif response == "i":
            want_interger = input("press <enter> for an integer or any key for an image: ")
            if want_interger == "":
                return "integer"
            else:
                return "image"

        else:
            # if responce is not valid, output an error
            print("please choose a vaild file type!")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("you chose", data_type)

    print()