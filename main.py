MAX_LINES = 3

# The deposit function is responsible for collecting the user input which is the deposit from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # Check if its a valid Number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please Enter a number and it must be graeter than 0")
    return amount

# The get_number_of_lines function is responsible for asking the user how many lines She/He wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - %s)? " % str(MAX_LINES))
        if lines.isdigit():
            lines = int(lines)
            # Check if the lines are in the bound that I have
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please Enter a number and it must be graeter than 0")
    return lines