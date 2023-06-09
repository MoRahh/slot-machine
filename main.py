import random

# Set the maximum number of lines that can be bet on as a constant
MAX_LINES = 3
# Defining the minimum and maximum bet amounts as constants
MAX_BET = 100
MIN_BET = 1

# Define the number of rows and columns for the slot machine as constants
ROWS = 3
COLS = 3

# Define the count of each symbol for the slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Define a function to check for wins based on the slot machine spin
def check_wins(columns, lines, bet, values):
    wins = 0
    win_lines = []
    # Iterate over each line that the player has bet on
    for line in range(lines):
        symbol = columns[0][line]
        # Iterate over the columns in the line to check if all symbols match
        for column in columns:
            symbol_to_check = column[line]
            # If the symbol does not match the first symbol in the line, break out of the loop
            if symbol != symbol_to_check:
                break
        # If the loop completes without finding a non-matching symbol, calculate the win for that line
        else:
            wins += values[symbol] * bet
            win_lines.append(line + 1)
    # Return the total wins
    return wins, win_lines


# The get_slot_machine_spin function generates a random spin of the slot machine
def get_slot_machine_spin(rows,cols,symbols):
    # Create a list of all symbols based on their count
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Create a list of columns, each containing a random selection of symbols
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # Randomly select a symbol from the current symbols and add it to the column
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        # Add the completed column to the list of columns
        columns.append(column)

    return columns



# The print_slot_machine function prints out the current spin of the slot machine
def print_slot_machine(columns):
    # Print out each row of the slot machine
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            # Print out the symbol in the current row of the current column
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        # Move to the next line after printing the current row
        print()




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
            if 1 <= lines <= MAX_LINES:
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




    
def spin(balance):
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
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    wins, win_lines = check_wins(slots, lines, bet, symbol_value)
    print(f"You won ${wins}.")
    print("You won on lines:", *win_lines)
    return wins - total_bet


def main():
    balance = deposit()
    while True:
        print("Current balance is: %d"% balance)
        answer = input("Press enter to play (q to quit).  ")
        if answer == "q":
            break
        balance += spin(balance)

    print("You left with %d" % balance)

main()