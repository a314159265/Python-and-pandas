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
    for expense in expenses:
        date, category, amount,  description = expense.strip().split(',')
        if category not in summary:
            summary[category] = 0
        summary[category] += float(amount)
    print(summary)

def add(date:str, category:str, amount:float, description:str):
    expenses.append(f'{date},{category},{amount},{description}\n')
    

def main():
    load()
    show_summary()
    add("2023-10-01", "Food", 50.0, "Grocery shopping")
    save()
    show_summary()

main()