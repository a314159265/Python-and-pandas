from pathlib import Path
from datetime import datetime
from datetime import date

ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "expenses_sample.csv"

expenses = []


class DateError(Exception):
    """Raised when a date has an error."""


def is_valid_date(date_text: str) -> bool:
    """Checks if a string matches the given format and is a valid real-world date."""
    date_format = "%Y-%m-%d"
    try:
        parsed_datetime = datetime.strptime(date_text, date_format)
        parsed_date = parsed_datetime.date()
        if parsed_date > date.today():
            print("date can't be in future")
            return False
        return True
    except ValueError:
        return False


def save():
    """Saves the current list of expenses to a CSV file."""
    with open(FILE_PATH, "w") as f:
        f.writelines(expenses)


def load():
    """Loads expenses from a CSV file into the expenses list."""
    try:
        with open(FILE_PATH, "r") as file:
            # .read().splitlines() splits lines cleanly and strips \r or \n
            lines = file.read().splitlines()

            if not lines:
                print("--- File is completely empty ---")
                return

            # Clear previous data so you don't double your list
            expenses.clear()

            # Use a manual slice to skip the first header line safely
            for line in lines[1:]:
                if line.strip():  # Skip empty rows
                    # Re-add newline for consistency with show_full()
                    expenses.append(line + "\n")

            print(f"--- Successfully loaded {len(expenses)} rows of data! ---")

    except FileNotFoundError:
        print(f"--- Error: System cannot find the file at {FILE_PATH} ---")


def show_full():
    """Displays all expenses in the list."""
    for expense in expenses:
        print(expense)


def show_summary():
    """Displays a summary of the expenses."""
    summary = {}
    min_amount = 1000000  # Set to a high value to ensure it gets replaced
    max_amount = 0
    no_expenses = len(expenses)
    avg_amount = 0

    for expense in expenses:
        date, category, amount, description = expense.strip().split(",")
        if category not in summary:
            summary[category] = 0
        amount = float(amount)
        summary[category] += amount
        if amount < min_amount:
            min_amount = amount
        if amount > max_amount:
            max_amount = amount

    if no_expenses > 0:
        avg_amount = sum(summary.values()) / no_expenses

    print(summary)
    print(f"Minimum amount: {min_amount}")
    print(f"Maximum amount: {max_amount}")
    print(f"Average amount: {avg_amount}")


def add(date: str, category: str, amount: float, description: str):
    """Adds a new expense to the list."""
    if is_valid_date(date):
        expenses.append(f"{date},{category},{amount},{description}\n")
    else:
        print('please enter vaild date')


def main():
    while True:
        menu_text = (
            "Enter what you would like to do \n"
            " type 1 for adding bill\n"
            " type 2 for showing all bills \n"
            " type 3 for showing summary \n"
            " type 4 for save \n"
            " type 5 for load \n"
            " type 6 to quit \n"
        )
        response = input(menu_text)

        if response == "1":
            user_date = input("Enter the date of the bill (YYYY-MM-DD): ")
            if is_valid_date(user_date):
                pass
            else:
                print('not valid date, please try again')
                continue
            category = input("Enter the category of the bill: ")
            amount = float(input("Enter the amount of the bill: "))

            if amount <= 0:
                print("Amount cannot be negative or zero. Please try again.")
                continue

            description = input("Enter a description for the bill: ")
            add(user_date, category, amount, description)

        elif response == "2":
            show_full()

        elif response == "3":
            show_summary()

        elif response == "4":
            save()

        elif response == "5":
            load()

        elif response == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()