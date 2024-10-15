# Face Recognition Attendance System

An automated solution for tracking attendance using facial recognition technology.

## Overview

The Face Recognition Attendance System is designed to simplify the process of taking attendance. It uses webcam input to recognize individuals and automatically mark their attendance, generating both daily and consolidated reports.

## Features

- Real-time face detection and recognition
- Automated attendance marking
- Daily attendance reports in Excel format
- Consolidated attendance report across multiple days
- User-friendly command-line interface

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6 or higher
- Webcam (built-in or external)
- Internet connection (for initial setup)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Project Structure

```
face-recognition-attendance/
│
├── faceRecognition.py      # Main script for face recognition
├── excel_report.py         # Generates daily Excel reports
├── course_attendance_report.py  # Creates consolidated reports
├── run.py                  # Runs all components sequentially
├── ImagesAttendance/       # Stores known face images
├── attendance.txt          # Daily attendance record (temporary)
├── attendance.xlsx         # Excel file with attendance reports
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation
```

## Usage

1. Add images of known individuals to the `ImagesAttendance` directory. Name each image file with the person's name or ID (e.g., "John_Doe.jpg").

2. Run the system:
   ```
   python run.py
   ```

3. The system will activate your webcam and start recognizing faces.

4. To stop the face recognition process, press 'q' in the webcam window.

5. The system will automatically generate the daily attendance report and update the consolidated report.

6. Check the `attendance.xlsx` file for the attendance reports.

## How It Works

1. **Face Recognition (faceRecognition.py):**
   - Loads known faces from the `ImagesAttendance` directory
   - Captures video from the webcam
   - Detects and recognizes faces in real-time
   - Marks attendance for recognized individuals

2. **Excel Report Generation (excel_report.py):**
   - Creates or updates the `attendance.xlsx` file
   - Adds a new sheet for the current date with attendance data

3. **Consolidated Report (course_attendance_report.py):**
   - Creates a consolidated view of attendance across all recorded days
   - Adds or updates the "Consolidated" sheet in `attendance.xlsx`

4. **Run Script (run.py):**
   - Executes all components sequentially
   - Provides feedback on the execution status of each script

## Troubleshooting

- Ensure adequate lighting for proper face recognition.
- If you encounter "module not found" errors, verify that all dependencies are installed.
- Close the Excel file before running the system to avoid write permission errors.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
