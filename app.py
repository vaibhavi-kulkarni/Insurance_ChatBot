import streamlit as st
from utils.chatbot import generate_response
import random

# Streamlit UI settings
st.set_page_config(page_title="Insurance Chatbot", layout="wide")

# Custom CSS for styling (horizontal navbar, colors, and more)
st.markdown("""
    <style>
    body {
        background-color: #000000;  /* Black background */
        color: #FFFFFF;  /* White text color for everything else */
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        color: #00FFFF;  /* Cyan for titles */
        font-size: 30px;
    }
    .stWrite {
        font-size: 16px;
        color: #FFFFFF;  /* White text for general content */
    }
    .stMarkdown {
        color: #FFFFFF;  /* White text for markdown */
    }
    /* Horizontal Navbar Style */
    .navbar {
        background-color: #00796b;  /* Green background */
        padding: 10px;
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        font-family: 'Arial', sans-serif;
        color: white;
        border-radius: 15px;  /* Rounded corners */
    }
    .navbar a {
        color: white;
        text-decoration: none;
        font-size: 18px;
        margin: 0 15px;
        padding: 10px 20px;
        border-radius: 10px;  /* Rounded corners for links */
        transition: background-color 0.3s;
    }
    .navbar a:hover {
        background-color: #004d40;  /* Darker green on hover */
    }
    /* Styling for the sidebar and content */
    .sidebar .sidebar-content {
        background-color: #000000;
        color: #FFFFFF;
    }
    .stTextInput input {
        background-color: #333;
        color: #FFFFFF;
        border: 1px solid #00796b;
    }
    .stButton>button {
        background-color: #00796b;
        color: white;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #004d40;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar Options
menu = ["Home", "Chatbot", "Contact Us", "Insurance Terms", "About Us"]

# Create horizontal navbar using selectbox (so user can click and select)
navbar_option = st.selectbox('Select a page', menu, index=1)  # Default to Chatbot

# Company Information (Single Company Info)
def show_home_page():
    st.title("Welcome to ABC Insurance!")
    st.write("ABC Insurance provides a wide range of insurance policies to help protect you and your loved ones.")
    st.write("### Insurance Plans Offered:")
    st.write("1. **Health Insurance**: Comprehensive coverage for hospitalization, maternity, and critical illnesses.")
    st.write("2. **Life Insurance**: Ensure long-term financial security for your family with flexible premium options.")
    st.write("3. **Motor Insurance**: Coverage for your car or bike against accidents, theft, and third-party liabilities.")
    st.write("4. **Home Insurance**: Protect your home from fire, natural disasters, theft, and accidental damage.")
    st.write("5. **Travel Insurance**: Global coverage for trip cancellations, lost baggage, flight delays, and emergency medical expenses.")

# Chatbot page
def show_chatbot_page():
    st.title("Insurance Chatbot")
    st.write("Hello! How can I assist you with your insurance policy?")

    # Chat loop
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask me anything about insurance:")

    if user_input:
        response = generate_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

    # Display the conversation
    for speaker, text in st.session_state.chat_history:
        st.write(f"**{speaker}:** {text}")

# Contact Us page with a simple contact form
def show_contact_page():
    st.title("Contact Us")
    st.write("Have any questions or need assistance? Feel free to reach out to us!")
    
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            st.write(f"Thank you, {name}! We have received your message and will get back to you at {email}.")
            # You can also implement email functionality or store the message in a database if needed.

# Insurance Terms page with common insurance terms
def show_insurance_terms_page():
    st.title("Insurance Terms")
    st.write("Here are some important insurance-related terms that you should know:")
    st.write("### 1. Premium")
    st.write("The amount you pay for an insurance policy, usually on a monthly, quarterly, or annual basis.")
    
    st.write("### 2. Deductible")
    st.write("The amount you need to pay out of pocket before the insurance company starts covering the rest.")
    
    st.write("### 3. Beneficiary")
    st.write("A person or entity that receives the benefits from an insurance policy after the policyholder's death or other covered event.")
    
    st.write("### 4. Claim")
    st.write("A request made by the policyholder to the insurance company to receive benefits for a covered event.")
    
    st.write("### 5. Underwriting")
    st.write("The process through which an insurance company evaluates the risks and determines the premium rates for policies.")
    
    st.write("### 6. Exclusions")
    st.write("Certain conditions or situations not covered by an insurance policy, typically listed in the fine print.")
    
    st.write("### 7. Waiting Period")
    st.write("A set period after purchasing an insurance policy during which certain benefits may not be available, such as for pre-existing conditions.")

# About Us page
def show_about_page():
    st.title("About Us")
    st.write("ABC Insurance is committed to providing a wide variety of insurance products to suit your needs. Our goal is to help protect your future, your assets, and your family.")
    st.write("We offer transparent policies, affordable premiums, and personalized support. With over 20 years in the industry, ABC Insurance is a trusted partner in protecting your loved ones and your property.")

# Handle page navigation
if navbar_option == "Home":
    show_home_page()
elif navbar_option == "Chatbot":
    show_chatbot_page()
elif navbar_option == "Contact Us":
    show_contact_page()
elif navbar_option == "Insurance Terms":
    show_insurance_terms_page()
elif navbar_option == "About Us":
    show_about_page()
