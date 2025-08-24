import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Constants
DAY_RANGE_MIN = 0
DAY_RANGE_MAX = 240
SEED = 42
ID_RANGE_MIN = 10001
ID_RANGE_MAX = 10016

# Set seed for reproducibility
random.seed(SEED)
np.random.seed(SEED)

# Create fake employee data
employee_ids = list(range(ID_RANGE_MIN, ID_RANGE_MAX))
names = ['Alice E.', 'Jake L.', 'Lana S.', 'Bruce I.', 'Mira C.',
        'Ethan Z.', 'Nina O.', 'Leo R.', 'Grace W.', 'Omar J.',
        'Tina U.', 'Raj V.', 'Chloe Y.', 'Ivan D.', 'Sara G.']
departments = ['Asssembly', 'QA', 'Packaging']
types_of_leave = ['Vacation', 'Sick', 'PTO']

# Create time-off records
time_off_records = []
for _ in range(120):
    emp_id = random.choice(employee_ids)
    name = names[employee_ids.index(emp_id)]
    dept = random.choice(departments)
    leave_type = random.choice(types_of_leave)
    date = datetime(2025, 1, 1) + timedelta(days=random.randint(DAY_RANGE_MIN, DAY_RANGE_MAX))
    hours = random.choice([4, 8, 16])
    time_off_records.append([emp_id, name, dept, date.strftime('%Y-%m-%d'), leave_type, hours])

# Create productivity records (weekly)
productivity_records = []
start_date = datetime(2025, 1, 1)
for week in range(35): # 35 weeks of data
    for emp_id in employee_ids:
        name = names[employee_ids.index(emp_id)]
        dept = random.choice(departments)
        date = start_date + timedelta(weeks=week)
        tasks_completed = random.randint(30, 70)
        hours_worked = 40
        quality_score = random.randint(85, 100)
        productivity_records.append([emp_id, name, dept, date.strftime('%Y-%m-%d'), 
            tasks_completed, hours_worked, f"{quality_score}%"
        ])

# Convert to DataFrames
df_time_off = pd.DataFrame(time_off_records, columns=["employee_id", "name", "department", "date", "type", "hours"])
df_productivity = pd.DataFrame(productivity_records, columns=["employee_id", "name", "department", "date", "tasks_completed", "hours_worked", "quality_score"])

# Export to CSV
df_time_off.to_csv("output/time_off_data.csv", index=False)
df_productivity.to_csv("output/productivity_data.csv", index=False)