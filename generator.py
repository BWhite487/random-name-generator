import random
import string
valid_input = False

while not valid_input:
    user_input = input('What is the number of EC2 instances you want to create names for? ')
    
    if user_input.isdigit():
        name_quantity = int(user_input)
        valid_input = True
    else:
        print("Please enter a valid number.")
department_name = input('What is your department?')
# Loop for 'name_quantity' iterations
for _ in range(name_quantity):
    # Generate a string of 3 random letters and characters
    random_chars = ''.join(random.choices(string.ascii_letters, k=3))
    
    # Generate a random integer up to 4 digits starting at 1000 up to 9999
    random_numbers = random.randint(1000, 9999)
# Construct the instance name using the department name, random characters, underscore, and random numbers
    random_id = f"{department_name} {random_chars}_{random_numbers}"
    print(random_id)
    
    # Print the constructed instance name
    print(random_id)    
        