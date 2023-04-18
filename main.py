# Set the maximum number of lines that can be bet on
MAX_LINES = 3
# Defining the minimum and maximum bet amounts as constants
MAX_BET = 100
MIN_BET = 1

# The deposit function is responsible for collecting the user input which is the deposit from the user
def deposit():
    # Continue prompting the user until a valid deposit amount is entered
    while True:
        # Prompt the user to enter a deposit amount
        amount = input("What would you like to deposit? $")
        
        # Check if the input is a valid positive integer
        if amount.isdigit():
            amount = int(amount)
            # Check if the amount is greater than zero
            if amount > 0:
                # Break out of the while loop and return the valid deposit amount
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please Enter a number and it must be graeter than 0")
    
    return amount

# The get_number_of_lines function is responsible for asking the user how many lines She/He wants to bet on
def get_number_of_lines():
    # Continue prompting the user until a valid number of lines is entered
    while True:
        # Prompt the user to enter the number of lines they want to bet on
        lines = input("Enter the number of lines to bet on (1 - %s)? " % str(MAX_LINES))
        
        # Check if the input is a valid positive integer
        if lines.isdigit():
            lines = int(lines)
            # Check if the number of lines is within the allowed range
            if MIN_BET <= lines <= MAX_BET:
                # Break out of the while loop and return the valid number of lines
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please Enter a number and it must be graeter than 0")
    
    return lines

# The get_bet function prompts the user to enter a bet amount for each line
def get_bet():
    # Continue prompting the user until a valid bet amount is entered
    while True:
        # Prompt the user to enter a bet amount
        amount = input("What would you like to bet on each line? $")
        
        # Check if the input is a valid positive integer
        if amount.isdigit():
            amount = int(amount)
            # Check if the bet amount is within the allowed range
            if MIN_BET <= amount <= MAX_BET:
                # Break out of the while loop and return the valid bet amount
                break
            else:
                print(f'Amount must be between {MIN_BET} - {MAX_BET}.')
        else:
            print("Please enter a number")
    
    return amount

# The main function is the entry point of the program
def main():
    # Call the deposit function to get the user's initial balance
    balance = deposit()
    # Call the get_number_of_lines function to get the number of lines the user wants to bet on
    lines = get_number_of_lines()
    # Enter a loop to get the bet amount for each line and check if the total bet amount is greater than the user's balance
    while True:
        # Call the get_bet function to get the bet amount for each line
        bet = get_bet()
        # Calculate the total bet amount
        total_bet = bet * lines

        # Check if the total bet amount is greater than the user's balance
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else: 
            # If the total bet amount is less than or equal to the user's balance, break out of the loop
            break
    
    # Print the bet amount, number of lines, and total bet amount
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")



main()