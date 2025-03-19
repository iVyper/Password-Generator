# Import the string module so we can get all ASCII characters without typing them out.
import string
# Import the random module so we can generate a random character from a list of characters.
import random

# Get the string of all ASCII letters and turn it into a list called letters.
letters = list(string.ascii_letters)
# Get the string of all ASCII symbols and turn it into a list called symbols.
symbols = list(string.punctuation)

# Welcome the user to the Password Generator program.
print("Welcome to the Password Generator!")

# Prompt the user for the amount of letters they would like in their password and store it in a variable called
# letters_in_password.
letters_in_password = int(input("How many letters would you like in your password?\n"))
# Prompt the user for the amount of symbols they would like in their password and store it in a variable called
# symbols_in_password.
symbols_in_password = int(input("How many symbols would you like in your password?\n"))
# Prompt the user for the amount of numbers they would like in their password and store it in a variable called
# numbers_in_password.
numbers_in_password = int(input("How many numbers would you like in your password?\n"))

# Initialize a variable generated_password where the program generated password will be stored.
generated_password = ""
randomized_password = ""

# For loop iterating letters_in_password times to add a random character from the letters list and appending it to
# generated_password.
for i in range(letters_in_password):
    generated_password += random.choice(letters)
# For loop iterating symbols_in_password times to add a random character from the symbols list and appending it to
# generated_password.
for i in range(symbols_in_password):
    generated_password += random.choice(symbols)
# For loop iterating numbers_in_password times to add a random number generated from the randint function from the
# random module and appending it to generated_password.
for i in range(numbers_in_password):
    generated_password += str(random.randint(0,9))

# For loop for iterating the length of generated_password times to take a random character from generated_password
# add it to randomized_password, then also removing it from generated_password so it does not get used again.
for i in range(len(generated_password)):
    character_select = random.choice(generated_password)
    randomized_password += character_select
    # The count variable ensures that we don't replace 2 or more occurrences of a character in one removal.
    generated_password = generated_password.replace(character_select, "",1)

# Print the randomized password in randomized_password to the console for the user.
print(randomized_password)
