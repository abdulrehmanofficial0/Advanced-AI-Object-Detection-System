import streamlit as st

USER_CREDENTIALS = {
    "admin": "1234",
    "student": "1234"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.sidebar.title("🔐 Login")

    with st.sidebar.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.logged_in = True
                st.success("Login Successful")
            else:
                st.error("Invalid Credentials")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.success("Logged out successfully")

def check_login():
    return st.session_state.logged_in