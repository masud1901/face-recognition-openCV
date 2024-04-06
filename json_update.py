import os
import json
from datetime import datetime
import pandas as pd

# Configuration
attendance_data_dir = "attendance_data"

# Read recognized students data from the Excel file
df = pd.read_excel("attendance.xlsx")

# Update JSON files with attendance data
for _, row in df.iterrows():
    name = row["name"]
    timestamp = row["timestamp"]
    student_file = os.path.join(attendance_data_dir, f"{name}.json")

    if os.path.exists(student_file):
        with open(student_file, "r") as f:
            attendance_data = json.load(f)
        attendance_data["attendance"].append(f"Present at {timestamp}")
        with open(student_file, "w") as f:
            json.dump(attendance_data, f, indent=4)
    else:
        print(f"Attendance data file not found for {name}")