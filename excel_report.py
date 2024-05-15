import pandas as pd
from datetime import datetime

# Read the attendance data from the text file
attendance_data = []
with open("attendance.txt", "r") as f:
    for line in f:
        roll_no, attendance_status, timestamp = line.strip().split(",")
        attendance_data.append(
            {
                "Roll No": roll_no,
                "Attendance": attendance_status,
                "Timestamp": timestamp,
            }
        )

# Convert the data to a DataFrame
attendance_df = pd.DataFrame(attendance_data)

# Get the current date
current_date = datetime.now().date().strftime("%Y-%m-%d")

# Create or open the Excel file
attendance_file = "attendance.xlsx"
writer = pd.ExcelWriter(
    attendance_file,
    engine="openpyxl",
    mode="a",
    if_sheet_exists="overlay",
)

# Check if the sheet for the current date exists, create a new sheet if not
if current_date not in writer.sheets:
    attendance_df.to_excel(writer, sheet_name=current_date, index=False)
else:
    start_row = writer.sheets[current_date].max_row + 1
    attendance_df.to_excel(
        writer,
        sheet_name=current_date,
        startrow=start_row,
        header=False,
        index=False,
    )

writer._save()
writer.close()
