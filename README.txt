# Process Monitor

A Django + REST Framework project to monitor and display system processes dynamically.  
Includes an agent script (using `psutil`) that collects process details and sends them to the backend API.  

---

# Project Structure

process_monitor/
│── backend/         # Django project (APIs, database, admin)
    - monitor         # app
│── agent.py         # Script to collect and send process data
│── requirements.txt # Dependencies
│── README.md        # Project documentation
│──env
│──manage.py


---

##  Setup Instructions

 1. Clone the repository
```bash
git clone <your-repo-link>
cd process_monitor
```

### 2. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows
```

# 3. Install dependencies
bash
pip install -r requirements.txt



##  Running the Project

### **Option A: Run from source**
1. Start :
   bash
   
   python manage.py runserver
   ```
   Runs at `http://127.0.0.1:8000`

2. In another terminal, run the agent:
   ```bash
   python agent.py
   ```
   This will collect system processes and send them to the API.

3. Open the frontend (if included) or use browser/Postman at:
   ```
   http://127.0.0.1:8000/process-data/
   ```

---

### **Option B: Run as Executable (optional)**
If you want to try the agent as an `.exe` (Windows only):

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build executable:
   ```bash
   pyinstaller --onefile agent.py
   ```

3. Run generated exe (inside `dist/` folder):
   ```bash
   dist/agent.exe
   ```

---
###API Specification---
Purpose: Accepts a list of process records from the Agent and stores them in the database.

Authentication: Requires header Authorization: Api-Key <YOUR_API_KEY>.

Request Body: JSON array; each item should contain:

hostname

pid

ppid

name

cpu

memory

Response (Success):

201 Created → {"message": "Process data saved successfully"}

Error Responses:

403 Forbidden → Missing or invalid API key

400 Bad Request → Validation error (missing or invalid fields)

2) GET /api/process-data/

Purpose: Returns all process records across all hosts.

Response:

200 OK → JSON list of process objects

3) GET /api/process-data/<hostname>/

Purpose: Returns process records for a specific host.

Response:

200 OK → JSON list of process objects filtered by hostname


##  Tech Stack
- **Django 5.2.5**
- **Django REST Framework**
- **psutil** (process monitoring)
- **requests** (agent to API communication)
- **CORS Headers**
