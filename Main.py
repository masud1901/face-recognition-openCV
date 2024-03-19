import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, timedelta
import pandas as pd

# Configuration
path = "ImagesAttendance"
attendance_file = "attendancefile.csv"
num_days = 1

# Load known images and get class names
images = []
classNames = []

for img_file in os.listdir(path):
    cur_img = cv2.imread(os.path.join(path, img_file))
    images.append(cur_img)
    classNames.append(os.path.splitext(img_file)[0])

# Compute face encodings
encodeListknown = [face_recognition.face_encodings(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))[0] for img in images]

print("Encoding Complete")

# Create attendance DataFrame
start_date = datetime.now().date()
dates = [start_date + timedelta(days=i) for i in range(num_days)]
columns = ["Name"] + [date.strftime("%Y-%m-%d") for date in dates]
attendance_df = pd.DataFrame(columns=columns)
attendance_df["Name"] = classNames
attendance_df = attendance_df.fillna(False)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListknown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListknown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            # Update attendance flag for the current date
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d")
            attendance_df.loc[attendance_df["Name"] == name, date_string] = True

    cv2.imshow("Webcam", img)
    key = cv2.waitKey(1) & 0xFF

    # Press 'q' to quit
    if key == ord('q'):
        break

# Export attendance data to CSV file
attendance_df.to_csv(attendance_file, index=False)

# Release resources
cap.release()
cv2.destroyAllWindows()