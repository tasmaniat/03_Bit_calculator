# Function goes here

# Puts series of symbolys at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# checks user choice is "integer", "text" or "image"
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


# Main Routine goes here

# Heading 
statement_generator("Bit calcultor for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session 
keep_going = ""
while keep_going == "":

    # Ask the user for the file type 
    data_type = user_choice()
    print("you chose", data_type)
    
    # For interders, ask fro integer
    # (must be an interger more than / equal to 0)

    # For images, ask for width and height
    # 