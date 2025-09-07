def get_number(message):
    """Ask for a number until the user gives a valid integer"""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter digits only.")


def get_rate(message):
    """Ask for a rate (can be int or float)"""
    while True:
        try:
            rate = input(message)
            if "." in rate:
                return float(rate)  # decimal value
            else:
                return int(rate)    # whole number
        except ValueError:
            print("Invalid input! Enter only numbers (e.g. 5 or 5.5).")


def calculate_total(rent, food, units, per_unit):
    """Calculate the total expenses"""
    return rent + food + (units * per_unit)


def calculate_share(total, members):
    """Divide total among members, avoid divide by zero"""
    if members == 0:
        return None
    else:
        return total / members


# -------- Main Program --------

rent = get_number("Enter total flat rent: ")
food = get_number("Enter total food/snacking expense: ")
units = get_number("Enter total electricity units used: ")
per_unit = get_rate("Enter per unit electricity rate: ")

# Calculate total expenses
total = calculate_total(rent, food, units, per_unit)
print("Total expenses:", total)

# Divide among members
members = get_number("Enter total number of flat members: ")
share = calculate_share(total, members)

if share is None:
    print("Members cannot be zero.")
else:
    print(f"Total expenses divided among {members} members.")
    print(f"Each person’s share: {share}")