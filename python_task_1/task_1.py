from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "expenses_sample.csv"

expenses = []

def save():
    with open(FILE_PATH, "w") as f:
        f.writelines(expenses)

def load():
    with open(FILE_PATH, 'r') as file:
        next(file)
        for line in file:
            expenses.append(line)

def show_full():
    
    for expense in expenses:
        print(expense)
    

def show_summary():
    summary = {}
    min = 100000
    max = -100000
    no_expenses = len(expenses)
    for expense in expenses:
        date, category, amount,  description = expense.strip().split(',')
        if category not in summary:
            summary[category] = 0
        amount = float(amount)
        summary[category] += amount
        if amount < min:
            min = amount
        if amount > max:
            max = amount
        avg = sum(summary.values()) / no_expenses if no_expenses > 0 else 0
    print(summary)
    print(f"Minimum amount: {min}")
    print(f"Maximum amount: {max}")
    print(f"Average amount: {avg}")

def add(date:str, category:str, amount:float, description:str):
    expenses.append(f'{date},{category},{amount},{description}\n')
    

def main():
    response = input('Enter what you would like to do \n type 1 for adding bill' \
    '\n type 2 for showing all bills \n type 3 for showing summary \n type 4 for save \n type 5 for load \n type 6 to quit \n')
    while response != '6':
        if response == '1':
            date = input('Enter the date of the bill (YYYY-MM-DD): ')
            category = input('Enter the category of the bill: ')
            amount = float(input('Enter the amount of the bill: '))
            description = input('Enter a description for the bill: ')
            add(date, category, amount, description)
        elif response == '2':
            show_full()
        elif response == '3':
            show_summary()
        elif response == '4':
            save()
        elif response == '5':
            load()
        else:
            print('Invalid option. Please try again.')
        
        main()

main()