import random
import string

def generate_password(num_letter,num_digits,num_symbols):
    
    #define the character set
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    #specify the number of character for each
    password_letters = [random.choice(string.ascii_lowercase)]+[random.choice(string.ascii_uppercase)]+[random.choice(letters) for i in range(num_letter)]
    password_digits = [random.choice(numbers) for i in range(num_digits)]
    password_punctuations = [random.choice(symbols) for i in range(num_symbols)]

    #combine all selected characters into one list
    password_list = password_letters + password_digits + password_punctuations

    #shuffle the list to randomize the order of characters
    random.shuffle(password_list)

    #joint the list into a single string to form the final password
    password = ''.join(password_list)
    
    return password

# Ask for the number of each type of character
try:
    num_letter = int(input("Enter the number of letters: "))
    num_digits = int(input("Enter the number of Digits: "))
    num_symbols = int(input("Enter the number of Symbols: "))

    #check if the input are positive
    if num_letter < 0 or num_digits < 0 or num_symbols < 0:
        raise ValueError("Number must be positive.")
    
    #generate the password
    password = generate_password(num_letter, num_digits, num_symbols)
    print("Your password is:", password)

except ValueError as e:
    print(f"Invalid Input: {e}")