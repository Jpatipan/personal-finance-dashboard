import pandas as pd
import random
from datetime import datetime, timedelta

# กำหนดตัวเลือกข้อมูล
accounts = ['Wallet', 'Bank Account', 'Credit Card']
categories_income = ['Salary', 'Investment', 'Freelance']
categories_expense = ['Food', 'Shopping', 'Transport', 'Health', 'Entertainment', 'Investment']
subcategories = {
    'Food': ['Coffee', 'Restaurant', 'Groceries', 'Takeout', 'Snacks'],
    'Shopping': ['Clothing', 'Electronics', 'Home Decor', 'Books', 'Beauty Products'],
    'Transport': ['Taxi', 'Bus', 'Fuel', 'Grab', 'BTS'],
    'Health': ['Medicine', 'Gym', 'Doctor Visit', 'Insurance'],
    'Entertainment': ['Netflix', 'Cinema', 'Games', 'Concert'],
    'Investment': ['Mutual Fund', 'Stock Purchase', 'Cryptocurrency'],
    'Salary': ['Main Job'],
    'Freelance': ['Project Work', 'Consulting']
}
currency = 'THB'

# สร้างฟังก์ชันสุ่มวันที่
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# สร้างข้อมูล
records = []
start_date = datetime(2024, 11, 1)
end_date = datetime(2025, 4, 30)

for _ in range(200):  # สร้าง 200 แถว
    is_income = random.choice([True, False, False, False])  # รายได้มีน้อยกว่ารายจ่าย (1:3)
    
    date = random_date(start_date, end_date)
    account = random.choice(accounts)
    
    if is_income:
        category = random.choice(categories_income)
        subcategory = random.choice(subcategories[category]) if category != 'Salary' else 'Main Job'
        note = f"Income from {subcategory}"
        amount = random.randint(15000, 80000)  # รายได้จาก 15,000 ถึง 80,000 บาท (ส่วนมาก)
        income_expense = 'Income'
    else:
        category = random.choice(categories_expense)
        subcategory = random.choice(subcategories[category])
        note = f"Spent on {subcategory}"
        if category == 'Food':
            amount = random.randint(50, 1500)  # รายจ่ายสำหรับอาหาร: 50–1,500 บาท
        elif category == 'Shopping':
            amount = random.randint(200, 10000)  # รายจ่ายสำหรับช็อปปิ้ง: 200–10,000 บาท
        elif category == 'Transport':
            amount = random.randint(30, 5000)  # รายจ่ายการขนส่ง: 30–5,000 บาท
        elif category == 'Health':
            amount = random.randint(100, 5000)  # รายจ่ายสุขภาพ: 100–5,000 บาท
        elif category == 'Entertainment':
            amount = random.randint(100, 3000)  # รายจ่ายบันเทิง: 100–3,000 บาท
        elif category == 'Investment':
            amount = random.randint(500, 10000)  # รายจ่ายการลงทุน: 500–10,000 บาท
        income_expense = 'Expense'
        
    record = {
        'Date': date.strftime('%Y-%m-%d'),
        'Account': account,
        'Category': category,
        'Subcategory': subcategory,
        'Note': note,
        'Amount (THB)': amount,
        'Income/Expense': income_expense,
        'Currency': currency
    }
    
    records.append(record)

# สร้าง DataFrame
df = pd.DataFrame(records)

# บันทึกเป็นไฟล์ CSV
df.to_csv('data/raw/personal_finance_dataset.csv', index=False)

print('✅ Dataset สร้างเสร็จแล้ว: personal_finance_dataset_thb.csv')
