import streamlit as st 
import os

from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


url: str = os.getenv("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)



with st.form("task_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        task_id = st.text_input("Task ID")
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

    submitted = st.form_submit_button("Add Task", use_container_width=True, type="primary")


if submitted:
    try:
        response = (
            supabase.table("new_tasks").insert({
                "task_id": task_id,
                "project_name": project_name,
                "task_title": task_title,
                "description": description,
                "milestone": milestone,
                "priority": priority,
                "collaborators": collaborators,
                "start_time": start_time.isoformat(),
                "deadline": deadline.isoformat(),
                "reminder": reminder,
                "status": status,
                "notes": notes
            }).execute()
        )

        st.success("✅ Task added successfully to Supabase!")
        st.json(response.data)  # show what was inserted

    except Exception as e:
        st.error(f"❌ Failed to insert task: {e}")