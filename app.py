import streamlit as st
from backend import query_engine  # Import the query engine from the backend file

# Set the page configuration
st.set_page_config(
    page_title="BINI Fan Page Query App",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="expanded",
)

# CSS for custom styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background-color: #f9f9f9;
    }
    .title {
        font-size: 3em;
        color: #ff1493;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #ff69b4;
        text-align: center;
        margin-bottom: 30px;
    }
    .button {
        background-color: #ff69b4;
        color: white;
        font-size: 1.2em;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        text-align: center;
        margin-top: 20px;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #ff1493;
    }
    .answer {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: #333;
        font-size: 1.2em;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .footer {
        text-align: center;
        padding: 20px;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #ff69b4;
        color: white;
        font-size: 1em;
    }
    .sidebar .sidebar-content {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.markdown("<h2 class='sidebar-content'>About BINI</h2>", unsafe_allow_html=True)
st.sidebar.write("""
BINI is a Filipino girl group formed by Star Hunt Academy and ABS-CBN Star Magic. The group consists of members Aiah, Colet, Maloi, Gwen, Stacey, Mikha, Sheena, and Jhoanna. They debuted on June 11, 2021, with their single "Born to Win". BINI is known for their synchronized dance moves, powerful vocals, and inspirational messages.
""")

st.sidebar.markdown("<h2 class='sidebar-content'>Follow BINI</h2>", unsafe_allow_html=True)
st.sidebar.write("""
- [Twitter](https://twitter.com/BINI_ph)
- [Instagram](https://www.instagram.com/bini_ph)
- [YouTube](https://www.youtube.com/c/BINIph)
- [Facebook](https://www.facebook.com/BINIph/)
""")

# Main content
st.markdown("<h1 class='title'>BINI Fan Page Query App</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Ask any question about BINI and get an answer!</p>", unsafe_allow_html=True)

# Input box
st.markdown("<div class='input-box'>", unsafe_allow_html=True)
question = st.text_input("Enter your question:")
st.markdown("</div>", unsafe_allow_html=True)

# Button and response
if st.button("Ask", key="ask_button", help="Click to get the answer"):
    if question:
        response = query_engine.query(question)
        st.markdown(f"<div class='answer'>Answer: {response.response}</div>", unsafe_allow_html=True)
    else:
        st.write("Please enter a question.")

# Footer
st.markdown("<div class='footer'>BINI Chat.</div>", unsafe_allow_html=True)
