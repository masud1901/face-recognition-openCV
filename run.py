import subprocess

# Define the scripts to run
scripts = [
    ["python", "faceRecognition.py"],
    ["python", "excel_report.py"],
    ["python", "course_attendance_report.py"],
]


# Function to run a script and capture its output
def run_script(script):
    result = subprocess.run(
        script,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout = result.stdout.decode()
    stderr = result.stderr.decode()
    return result.returncode, stdout, stderr


# Run the scripts sequentially
for script in scripts:
    returncode, stdout, stderr = run_script(script)
    print(f"Running {' '.join(script)}")
    print("Output:\n", stdout)
    if returncode != 0:
        print("Error:\n", stderr)
        print("Script failed. Stopping execution.")
        break
    else:
        print("Script executed successfully.\n")
