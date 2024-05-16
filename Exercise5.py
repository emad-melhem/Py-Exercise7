user_name = input("Hello traveler!\nWelcome to my program ^-^\nEnter your name :")
pass_word =''
while True:
    pass_word = input("Creat a password! :")
    if len(pass_word.strip()) < 6:
        print("That does not fulfill the requirements, try again")
    else:
        print("Valid password")
        break

print(f"Hii {user_name}!")
input_password=''
while input_password != pass_word:
    input_password = input("Enter your password :")
    if input_password == pass_word:
        print("That is correct")
    else:
        if input("That is incorrect,\ndo you want to try again? (Y/N)").lower() == 'n':
            break

# Exercise 5.2
try:
    num_shift = int(input('Enter a number of shift :'))
    encrypted_password = ""
    for letter in pass_word:
        encrypted_password += chr(ord(letter) + num_shift)
    
    print(f"password = {pass_word}")
    print(f"Shift = {num_shift}")
    print(f"Encrypted password = {encrypted_password}")
    
except ValueError:
    print("Input error!!\nYou must enter numbers only.")
except Exception as ex:
    print(ex.args[0])