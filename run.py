import subprocess

# Run faceRecognition.py and capture its output
result = subprocess.run(
    ["python", "faceRecognition.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
print(result.stdout.decode())
print(result.stderr.decode())

# Run another script after faceRecognition.py has finished
subprocess.run(["python", "excel_report.py"])
