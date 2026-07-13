from dataclasses import dataclass
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "expenses_sample.csv"

with open(FILE_PATH, "r") as f:
    data = f.read()

print(data)
@dataclass
class Expense:
    date: str
    category: str
    amount: float

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def show_summary(self):
        summary = {}
        for expense in self.expenses:
            if expense.category not in summary:
                summary[expense.category] = 0
            summary[expense.category] += expense.amount
        return summary
    
    def save_expenses_to_csv(self, file_path: Path):
        with open(file_path, "w") as f:
            f.write("date,category,amount\n")
            for expense in self.expenses:
                f.write(f"{expense.date},{expense.category},{expense.amount}\n")

    def load_expenses_from_csv(self, file_path: Path):
        with open(file_path, "r") as f:
            next(f)  # Skip header
            for line in f:
                date, category, amount, description = line.strip().split(",")
                self.add_expense(Expense(date, category, float(amount)))

def main():
    manager = ExpenseManager()
    manager.load_expenses_from_csv(FILE_PATH)
    print("Total Expenses:", manager.get_total_expenses())
    print("Expense Summary:", manager.show_summary())

if __name__ == "__main__":
    main()

    