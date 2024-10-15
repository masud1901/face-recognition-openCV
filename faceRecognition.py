import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Configuration
path = "./ImagesAttendance"

# Load known images and get class names
images = []
classNames = []
for img_file in os.listdir(path):
    cur_img = cv2.imread(os.path.join(path, img_file))
    images.append(cur_img)
    classNames.append(os.path.splitext(img_file)[0])

# Compute face encodings
encodeListknown = []
for img in images:
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_img)
    if encodings:
        encodeListknown.append(encodings[0])
    else:
        print(f"No face found in {classNames[len(encodeListknown)]}")

print("Encoding Complete")

# Open webcam
cap = cv2.VideoCapture(0)

# Create a dictionary to store attendance data
attendance = {name: {"Attendance": "Absent", "Timestamp": None} for name in classNames}

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

            # Update attendance only if the student has not been marked present yet
            if attendance[name]["Attendance"] == "Absent":
                attendance[name]["Attendance"] = "Present"
                attendance[name]["Timestamp"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(
                img,
                (x1, y2 - 35),
                (x2, y2),
                (0, 255, 0),
                cv2.FILLED,
            )
            cv2.putText(
                img,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2,
            )

    cv2.imshow("Webcam", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Save recognized students data to a file
with open("attendance.txt", "w") as f:
    for name, data in attendance.items():
        f.write(f"{name},{data['Attendance']},{data['Timestamp']}\n")
