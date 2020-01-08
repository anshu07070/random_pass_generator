import random

from string import punctuation

# our values to create a passcode
recommended_pass = "1234567890!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

# variable to store the password
random_pass = ""


# asking for type
print("How do you want to generate your random password?")
print("1. By providing raw input")
print("2. Use our recommended password (recommended)")
print("3. Create password from a txt file")

# taking response
response = input("==> ")

# Validating response
if response == "1":
    try:
        # taking characters input to be converted into password
        chars = input("Enter the characters : ").replace(" ", "")

        # taking user input for password length
        length1 = int(input("Enter the maximum length of password you want : "))

        if length1 > 0:
            # creating password
            for i in range(length1):
                random_pass += str(random.choice(chars))

            # printing password
            print("Your random password is :", random_pass)
        else:
            print("Length should be greater than 0")


    # handling exception
    except Exception as e:
        print(f"Error occured : {e}")

elif response == "2":
    try:
        # taking length input
        length2 = int(input("Enter the maximum length you want : "))

        if length2 > 0:
            for i in range(length2):
                random_pass += str(random.choice(recommended_pass))
        
        # printing password
            print("Your random password is :", random_pass)

        else:
            print("Password length should be greater than 0")

    # handling exception
    except Exception as e:
        print(f"Error occured : {e}")

elif response == "3":

    try:
        # taking length input
        lenght3 = int(input("Enter the length of the password : "))

        if lenght3 > 0:
        
            # taking file input
            filename = input("Enter txt file name with path : ")

            # checking if a file is .txt or not
            if ".txt" in filename:
                try:
                    file = open(filename, "r")
                    file_open = file.read().replace("\n","")
                    for i in range(lenght3):
                        random_pass += str(random.choice(file_open))

                    # printing password
                    print("Your random password is : " + random_pass.replace(" ", ""))
                except FileNotFoundError:
                    print("File not found")
                finally:
                    file.close()
            
            else:
                print("Please enter a .txt file")

        else:
            print("Length should be greater than 0")
else:
    print("Invalid option selected")
