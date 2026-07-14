import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
FILE_PATH = ROOT_DIR / "data" / "orders.csv"
df = pd.read_csv(FILE_PATH)




def question_1(df: pd.DataFrame) -> str:
    """summarizes sales by product category showing total and average sales"""
    # 1. Calculate revenue per row
    df['revenue'] = df['price'] * df['quantity']
    # 2. Group by product and sum the revenue
    product_revenue = df.groupby('product')['revenue'].sum()
    
    return product_revenue.to_string()

def question_2(df:pd.DataFrame) -> None:
    """adds size column to indicate wether revenue is large/med/small"""
    df['is_large'] = df['revenue'].apply(lambda x: 'is_large' if x>100 else ('medium' if x>50 else 'small'))
    
question_1(df)
question_2(df)
print(df)