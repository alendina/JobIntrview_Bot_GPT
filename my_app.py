import streamlit as st
from openai import OpenAI
from streamlit_js_eval import streamlit_js_eval

general_masseges_counter = 4

def complete_setup():
    # Update session state to indicate setup completion
    st.session_state.setup_complete = True

def show_feedback():
    # Update session state to indicate feedback shown
    st.session_state.feedback_shown = True  

# Setting up the Streamlit page configuration
st.set_page_config(page_title="StreamlitChatMessageHistory", page_icon="💬")
st.title(":red[Interiew Chatbot]")


# Initialize session state variable to track setup completion
if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "user_messages_counter" not in st.session_state:
    st.session_state.user_messages_counter = 0
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False

# First phase. Collecting user information
if not st.session_state.setup_complete:

    st.subheader("Personel information", divider="rainbow")

    # Initialize session state for company and position information and setting default values 
    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    st.session_state["name"] = st.text_input("Name", max_chars=50, value=st.session_state["name"], placeholder="Enter your name")
    st.session_state["experience"] = st.text_area("Experience", value=st.session_state["experience"], height=None, max_chars=400, placeholder="Describe your experience")
    st.session_state["skills"] = st.text_area("Skills", value=st.session_state["skills"], height=None, max_chars=400, placeholder="List your skills")

    st.subheader("Company and Position", divider="rainbow")

    # Initialize session state for company and position information and setting default values 
    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Meta"

    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio(
            "Choose level",
            key="visibility",
            options=["Trainee", "Junior", "Mid-level", "Senior"],
            index=["Trainee", "Junior", "Mid-level", "Senior"].index(st.session_state["level"])
        )

    with col2:
        st.session_state["position"] = st.selectbox(
            "Choose a position",
            ("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "Financial Analyst"),
            index=("Data Scientist", "Data Engineer", "ML Engineer", "BI Analyst", "Financial Analyst").index(st.session_state["position"])
        )
        st.session_state["company"] = st.selectbox(
            "Select a Company",
            ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify"),
            index=("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify").index(st.session_state["company"])
            )
    
    # Button to complete setup
    if st.button("Start Interview", on_click=complete_setup):
        st.write("Setup complete. Starting interview...")

# Second phase. Interview
if st.session_state.setup_complete and not st.session_state.chat_complete and not st.session_state.feedback_shown:
    st.subheader("Additional information", divider="rainbow")
    st.info(
    """
    Start by introducing yourself
    """,
    icon="👋",
    )
    
    # st.write(f"**Your Name**: {st.session_state['name']}")
    # st.write(f"**Your Experience**: {st.session_state['experience']}")
    # st.write(f"**Your Skills**: {st.session_state['skills']}")
    # st.write(f"**Your information**: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}")
    # st.subheader("", divider="rainbow")
    
    # Initialize OpenAI client
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Setting OpenAI model if not already initialized
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"

    # Initializing the system prompt for the chatbot
    if not st.session_state.messages:
        st.session_state.messages = [{
            "role": "system",
            "content": (f"You are an HR executive that interviews an interviewee called {st.session_state['name']} "
                        f"with experience {st.session_state['experience']} and skills {st.session_state['skills']}. "
                        f"You should interview him for the position {st.session_state['level']} {st.session_state['position']} "
                        f"at the company {st.session_state['company']}")
        }]

    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Collect user input and display it
    if st.session_state.user_messages_counter < general_masseges_counter:
        if prompt := st.chat_input("Your answer", max_chars=1000):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            if st.session_state.user_messages_counter < (general_masseges_counter - 1):
                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    )

                    response = st.write_stream(stream)
                st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.user_messages_counter += 1
            print("counter :", st.session_state.user_messages_counter)
            # st.rerun()
    
    if st.session_state.user_messages_counter >= general_masseges_counter:
        st.session_state.chat_complete = True
        # ------     
        st.session_state.messages.append({"role": "system", "content": "Say goodbye to the interviewee."})  
        chat_goobay = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": "Say goodbye to the interviewee."},
            ],
        )
        st.session_state.messages.append({"role": "assistent", "content": chat_goobay.choices[0].message.content})
        with st.chat_message("assistant"):
             st.markdown(chat_goobay.choices[0].message.content)
        # ----

        # st.session_state.chat_complete = True
        print("Chat complete;", "counter :", st.session_state.user_messages_counter)
        st.write("Chat complete. Thank you for your time!")

if st.session_state.chat_complete and not st.session_state.feedback_shown:
    # st.rerun()
    if st.button("Get Feedback", on_click=show_feedback):
        st.write("Fetching feedback...")

# Third phase. Feedback
if st.session_state.feedback_shown:
    st.subheader("Feedback", divider="rainbow")

    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

    feedback_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    feedback = feedback_client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": "system", 
             "content": """You are a helpful tool that provides feedback on an interviewee performance.
             Before the Feedback give a score of 1 to 10.
             Follow this format:
             Overal Score: //Your score + "from 10"
             Feedback: //Here you put your feedback
             Give only the feedback do not ask any additional questins.
              """},
            {"role": "user", "content": f"This is the interview you need to evaluate. Keep in mind that you are only a tool. And you shouldn't engage in any converstation: {conversation_history}"}
        ],
    )
    st.write(feedback.choices[0].message.content)

    # write feedback to the file
    f = open("feedback.txt", "a")
    f.write("\n==========\nINTERIEW\n==========\n")
    f.write(f"Your Name: {st.session_state['name']}\n")
    f.write(f"Your Experience: {st.session_state['experience']}\n")
    f.write(f"Your Skills: {st.session_state['skills']}\n")
    f.write(f"Your information: {st.session_state['level']} {st.session_state['position']} at {st.session_state['company']}\n\n")
    f.write(f"Conversation history:\n{conversation_history}\n\n")
    f.write(f"Conversation history:\n{feedback.choices[0].message.content}\n")
    f.close()


    # Button to restart the interview
    if st.button("Restart Interview", type="primary"):
            # pass
            streamlit_js_eval(js_expressions="parent.window.location.reload()")