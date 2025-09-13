import streamlit as st 

from st_social_media_links import SocialMediaIcons
from streamlit.components.v1 import html
from datetime import datetime, timedelta

# reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
# signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
home_page = st.Page("./pgs/main.py", title="Getting Started", icon=":material/home:")
# dashboard_page = st.Page("./pgs/dashboard.py", title="Dashboard", icon=":material/app_registration:")
scheduling_page = st.Page("./pgs/scheduling.py", title="Project Scheduling", icon=":material/apk_install:")
# sms_service_page = st.Page("./pgs/sms_service.py", title="Messaging", icon=":material/sms:")
# airtime_page = st.Page("./pgs/airtime.py", title="Airtime", icon=":material/redeem:")
# mobile_data_page = st.Page("./pgs/mobile_data.py", title="Mobile Data", icon=":material/lte_plus_mobiledata_badge:")
# ussd_page = st.Page("./pgs/ussd.py", title="USSD", icon=":material/linked_services:")
# chatbot_page = st.Page("./pgs/chatbot.py", title="Ask EcoShield", icon=":material/chat:")


pg = st.navigation([home_page, scheduling_page])



st.set_page_config(
    page_title="EcoSync",
    page_icon="⏳",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': """
            **EchoSync** is a project management and scheduling tool designed to help
            you balance multiple projects, deadlines, and milestones with ease.

            It sends you smart reminders 30 minutes before tasks, allows you to reschedule on the fly, and leverages AI assistance to optimize your time.  

        """
    }
)



with st.sidebar:
    button = """
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="echominds" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
        """

    html(button, height=70, width=220)
    st.markdown(
        """
        <style>
            iframe[width="220"] {
                position: fixed;
                bottom: 60px;
                right: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


    social_media_links = [
        "https://www.x.com/am_tonie",
        "https://www.youtube.com/@echobytes-ke",
        "https://www.instagram.com/antonie_generall",
        "https://www.github.com/antonie-riziki",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()

pg.run()

