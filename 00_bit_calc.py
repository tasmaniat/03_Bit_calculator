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


#  calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # calculate # of bits (length of sting x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters...".format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return""


# finds # bits for 24 bit colour
def image_bits():

    # get width and height...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working 
    print()
    print("# of pixels = {} x {} = {}".format(image_height,
                                              image_width, num_pixels ))
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""


# converts decimal to binary and states how
# many bits are needed to represent the original integer
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    # source for code below is 
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

     # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""



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

    # For interders, ask for integer
    if data_type =="integer":
        int_bits()

    # For images, ask for width and height
    # (must be an interger more than / equal to 0)
    elif data_type == "image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("")
    print()


