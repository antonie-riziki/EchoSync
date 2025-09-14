import streamlit as st 
import os
import sqlite3
import pandas as pd
import ydata_profiling

from streamlit_pandas_profiling import st_profile_report

from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


url: str = os.getenv("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# Connect (creates file if it doesn't exist)
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()


# Create table (only run once)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        task_title TEXT,
        description TEXT,
        milestone TEXT,
        priority TEXT,
        collaborators TEXT,
        start_time TEXT,
        deadline TEXT,
        reminder INTEGER,
        status TEXT,
        notes TEXT
    )
""")

conn.commit()
conn.close()


# Function to fetch tasks (latest first)
def fetch_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")  # newest first
    rows = cursor.fetchall()
    conn.close()
    # Convert to dataframe
    df = pd.DataFrame(
        rows,
        columns=[
            "ID", "Task ID", "Project Name", "Task Title", "Description",
            "Milestone", "Priority", "Collaborators", "Start Time", "Deadline",
            "Reminder (min)", "Status", "Notes"
        ]
    )
    return df





with st.form("task_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        # task_id = st.text_input("Task ID")
        project_name = st.text_input("Project Name")
        task_title = st.text_input("Task Title")
        milestone = st.text_input("Milestone")

    with col2:
        description = st.text_area("Description")
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        status = st.selectbox("Status", ["Planned", "In Progress", "Done"])
        notes = st.text_area("Notes")

    with col3:
        start_time = st.date_input("Start Date/Time", datetime.now())
        deadline = st.date_input("Deadline / Submission", datetime.now())
        reminder = st.number_input("Reminder (mins before)", min_value=0, value=30)
        collaborators = st.text_input("Collaborators/Partners")

    add_new_task_btn = st.form_submit_button("Add Task", use_container_width=True, type="primary")


# if submitted:
#     try:
#         response = (
#             supabase.table("new_tasks").insert({
#                 "task_id": task_id,
#                 "project_name": project_name,
#                 "task_title": task_title,
#                 "description": description,
#                 "milestone": milestone,
#                 "priority": priority,
#                 "collaborators": collaborators,
#                 "start_time": start_time.isoformat(),
#                 "deadline": deadline.isoformat(),
#                 "reminder": reminder,
#                 "status": status,
#                 "notes": notes
#             }).execute()
#         )

#         st.success("✅ Task added successfully to Supabase!")
#         st.json(response.data)  # show what was inserted

#     except Exception as e:
#         st.error(f"❌ Failed to insert task: {e}")


if add_new_task_btn:
    try:
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (project_name, task_title, description, milestone, priority, collaborators, start_time, deadline, reminder, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            
            project_name,
            task_title,
            description,
            milestone,
            priority,
            collaborators,
            str(start_time),
            str(deadline),
            reminder,
            status,
            notes
        ))
        conn.commit()
        conn.close()
        st.toast(f"✅ Task '{task_title}' saved successfully!")
    except Exception as e:
        st.error(f"❌ Failed to save task: {e}")



# Show current tasks at the top
st.subheader("📋 All Tasks")
task_df = fetch_tasks()
st.dataframe(task_df, use_container_width=True)


pr = df.profile_report()

st_profile_report(pr)

# col1, col2