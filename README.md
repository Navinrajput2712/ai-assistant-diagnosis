# AI Assistant Diagnosis Tool

## 📌 Overview
This project is an AI-powered diagnosis tool with a **Streamlit frontend** and a **Django REST API backend**. It allows patients to submit their details, doctors to analyze medical records, and assistants to manage appointments.

---

## 🏗️ Project Structure
```
/ai-assistant-diagnosis
│── backend/          # Django Backend (REST API)
│   ├── api/          # API App with Models, Views, Serializers
│   ├── backend/      # Django Project Configuration
│   ├── db.sqlite3    # Database (SQLite3)
│   ├── manage.py     # Django Management Script
│── frontend/         # Streamlit Frontend
│   ├── app.py        # Main Streamlit Application
│   ├── requirements.txt # Dependencies
│── README.md         # Project Documentation
│── .gitignore        # Ignore unnecessary files
```

---

## 🚀 Features
### ✅ Patient Interface
- Register with basic details and medical history
- Upload medical reports (X-ray, CT scans, etc.)
- AI-powered chatbot for initial diagnosis
- Book an appointment

### ✅ Doctor Assistant Interface
- View and manage patient details
- Update medical parameters (Blood Pressure, Temperature, Diabetes Status)
- Organize and manage appointments

### ✅ Doctor Interface
- Access full patient history
- AI-assisted diagnosis suggestions
- Video call & chat with patients
- Finalize treatment plan

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-assistant-diagnosis.git
cd ai-assistant-diagnosis
```

### 2️⃣ Backend Setup (Django)
```bash
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate it (Windows: venv\Scripts\activate)
pip install -r requirements.txt  # Install dependencies
python manage.py migrate  # Apply migrations
python manage.py createsuperuser  # Create an admin user
python manage.py runserver  # Start the server
```
👉 API runs at **http://127.0.0.1:8000/**

### 3️⃣ Frontend Setup (Streamlit)
```bash
cd frontend
python -m venv venv  # Create virtual environment
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py  # Start Streamlit frontend
```
👉 Frontend runs at **http://localhost:8501/**

---

## 🔗 API Endpoints
| **Action** | **Method** | **Endpoint** |
|------------|----------|------------------------|
| Get all patients | `GET` | `/api/patients/` |
| Add new patient | `POST` | `/api/patients/` |
| Get patient details | `GET` | `/api/patients/{id}/` |
| Add medical data | `POST` | `/api/medical/` |
| Submit diagnosis | `POST` | `/api/diagnosis/` |
| Get all diagnoses | `GET` | `/api/diagnosis/` |

---

## 🛠️ Technologies Used
- **Backend:** Django, Django REST Framework
- **Frontend:** Streamlit
- **Database:** SQLite3
- **Authentication:** JWT (for future enhancements)

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to GitHub (`git push origin feature-branch`)
5. Open a Pull Request 🚀

---

## 📜 License
This project is licensed under the MIT License.

---

## 📩 Contact
For questions or suggestions, reach out at: 
📧 Email: npininofsec@gmail.com
📞 Phone: 9714017994
