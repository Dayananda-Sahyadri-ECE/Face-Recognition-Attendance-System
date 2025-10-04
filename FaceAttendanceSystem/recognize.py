import cv2
import numpy as np
import sqlite3
import datetime
import csv
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def getProfile(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE ID=?", (id,))
    profile = cursor.fetchone()
    conn.close()
    return profile

if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Date", "Time"])

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 50:
            profile = getProfile(id)
            if profile:
                name = profile[1]
                now = datetime.datetime.now()
                dt = now.strftime("%Y-%m-%d")
                tm = now.strftime("%H:%M:%S")

                with open("attendance.csv", "a", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([id, name, dt, tm])

                cv2.putText(img, f"{name}", (x, y-10), font, 1, (0, 255, 0), 2)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            cv2.putText(img, "Unknown", (x, y-10), font, 1, (0, 0, 255), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Recognizing Face", img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
