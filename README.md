
# EchoSync 🚀  
*A Smart Project Scheduler by EchoMinds Innovations*  

EchoFlow is a **Streamlit-based project management and scheduling tool** designed to help you balance multiple projects, deadlines, and milestones with ease.  
It sends you **smart reminders 30 minutes before tasks**, allows you to **reschedule on the fly**, and leverages **AI assistance** to optimize your time.  

---

## ✨ Features
- 📅 **Project Dashboard** – View all projects, milestones, and timeframes in one place.  
- ⏰ **Smart Notifications** – Get reminders 30 minutes before important tasks.  
- 🔄 **Dynamic Rescheduling** – Easily adjust tasks when plans change.  
- 🤖 **AI Integration** – Suggestions for time allocation and conflict resolution.  
- 🗂 **Data Storage** – Lightweight SQLite backend for saving your tasks.  

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – for the interactive dashboard  
- [SQLite](https://www.sqlite.org/) – to store tasks and schedules  
- [APScheduler](https://apscheduler.readthedocs.io/) – for scheduling reminders  
- [Email SMTP] – for notifications  
- [Gemini] – for AI-based scheduling assistance  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/antonie-riziki/echosync.git
cd echosync

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # for Mac/Linux
venv\Scripts\activate      # for Windows


3. Install Dependencies
pip install -r requirements.txt


4. Run the App
streamlit run app.py


⚡ Future Enhancements
Mobile push notifications

Calendar integration (Google Calendar, Outlook)

Team collaboration features

Advanced AI assistant for workload optimization

👩🏽‍💻 Contributing
Contributions are welcome! Please fork the repo and create a pull request with your improvements.

📜 License
This project is licensed under the MIT License.
