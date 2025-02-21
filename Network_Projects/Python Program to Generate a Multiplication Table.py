# Prompt the user to enter the number for which they want the multiplication table
print("Enter the number of the math table: ", end="")
table_number = int(input())  # Get the user input and convert it to an integer

# Print a message to indicate the table number chosen by the user
print(f"Here, you will get the multiplication table of {table_number}")

# Loop through numbers 1 to 10 to generate the multiplication table
for i in range(1, 11):
    # Calculate the product of the current number (i) and the table number
    multiplication_answer = i * table_number

    # Print the multiplication result in a formatted way
    print(f"{i} X {table_number} = {multiplication_answer}")

# Optional: Remove redundant or inconsistent lines to keep the output clean and clear
