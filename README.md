# 🎯 Face Recognition Attendance System  

## 🧠 Overview  
This project is an **Automated Attendance System** that uses **Face Recognition** to identify and mark the attendance of individuals in real-time. It removes the need for manual attendance and ensures accurate, tamper-proof record keeping.  

The system detects faces through a webcam, compares them with stored images, and logs the name, date, and time of recognized faces into an **SQLite database** or **CSV file**.  

---

## ⚙️ Features  
✅ Real-time face detection and recognition  
✅ Automatic attendance marking with timestamp  
✅ Stores attendance in SQLite database or CSV  
✅ Easy registration of new users  
✅ Simple and lightweight design  

---

## 🧰 Tech Stack  
- **Language:** Python  
- **Libraries:**  
  - `opencv-python` – for camera and image handling  
  - `face_recognition` – for encoding and recognizing faces  
  - `numpy` – for numerical operations  
  - `datetime` – for timestamping  
  - `sqlite3` – for database management  

---

## 🧩 Workflow  
1. **Register Faces** – Capture faces and store them in a `dataset` folder.  
2. **Encode Faces** – Generate encodings using the `face_recognition` library.  
3. **Recognize Faces** – Use webcam feed to detect and compare faces.  
4. **Mark Attendance** – If recognized, log name, date, and time.  

---

## 🖥️ How to Run  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/yourusername/Face-Recognition-Attendance-System.git
cd Face-Recognition-Attendance-System
