📌 โจทย์: Personal Finance Dashboard
### Business Scenario:
ต้องการเข้าใจ **พฤติกรรมการใช้เงิน** ของตัวเองในช่วง 6 เดือนที่ผ่านมา เพื่อปรับปรุงการออมและการบริหารการเงินส่วนตัว

---

# 📌 KPI ที่ต้องวิเคราะห์

1. **Saving Rate (%)**
2. **Total Income per Month**
3. **Total Expense per Month**
4. **Top 5 Expense Categories**
5. **Average Daily Expense**
6. **Net Income (Income - Expense) Trend**

---

# 📌 Task List

## เตรียมข้อมูล
- ออกแบบตาราง dataset (ใช้ Excel / Google Sheets / Pandas)
- กรอกข้อมูลตัวอย่าง (อย่างน้อย 100 แถว)
- ตั้งค่ารูปแบบวันที่, ตัวเลข, Currency ให้ถูกต้อง

## Data Cleaning
- Import ข้อมูลเข้า Python (ใช้ Pandas)
- เช็ก Missing Value, Duplicate
- Convert Date เป็น datetime type
- สร้างคอลัมน์ Month-Year (สำหรับ group รายเดือน)

## Data Analysis - Summary
- คำนวณ
    - Total Income per Month
    - Total Expense per Month
    - Net Income per Month
- Saving Rate per Month

## Data Analysis - Detail
- Group รายจ่ายตาม Category
- หาว่าใช้เงินกับ Subcategory อะไรมากที่สุด
- คำนวณ Daily Average Spending

## Visualization
- Line Chart: Income / Expense / Net Income per Month
- Bar Chart: Top 5 Expense Categories
- KPI Cards: Saving Rate %, Average Daily Spending
- Pie Chart: % รายจ่ายตาม Category

## Dashboard Building
- เอา Chart ทั้งหมดมารวมใน Power BI
- ออกแบบ Layout สวย ๆ
- ใส่ filter วันที่ ได้ (optional)

# 📌 สรุป Mini Project Output
- 1 dataset (.csv)
- 1 Jupyter Notebook หรือ .py script (Data Cleaning + Analysis)
- 1 Dashboard (Power BI / Tableau / Excel)
- 1 README.md (สรุปเรื่องที่วิเคราะห์)

---