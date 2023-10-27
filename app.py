import streamlit as st
from utils import *
from streamlit_chat import message

<<<<<<< HEAD
if 'conversation' not in st.session_state:
    st.session_state['conversation'] =None
if 'messages' not in st.session_state:
    st.session_state['messages'] =[]
        
st.set_page_config(page_title="Helpdesk Call Insight", layout="wide")
new_title = '<p style="font-family:sans-serif; color:#47d7ac; font-size: 42px; text-align:center">Helpdesk Call Summarization</p>'
st.markdown('<style> .st-d4  p { font-size: 24px;} .st-at {height: 600px;overflow-y: overlay}</style>', unsafe_allow_html=True)
st.markdown(new_title, unsafe_allow_html=True)

# Define the Streamlit app
def main():
    #speech_to_text("CallRecording1.wav")
=======
if "conversation" not in st.session_state:
    st.session_state["conversation"] = None
if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.set_page_config(page_title="Helpdesk Call Summarization")


# Define the Streamlit app
def main():
    st.title("Helpdesk Call Summarization")
    # speech_to_text("CallRecording1.wav")
>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa

    # Upload multiple files
    uploaded_files = st.file_uploader(
        "Upload recorded .mp3 files", type=["wav"], accept_multiple_files=True
    )

    if uploaded_files:
        # st.write("Uploaded Files:")

        # Display uploaded files and buttons in a tabular form
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name

            # audio_text = get_audio_text(file_name)

<<<<<<< HEAD
            
            #Transcribe text
            #st.text_area("Transcribe text", audio_text, height=400)
=======
            audio_text = "Thank you for calling the Office of People Transfer you're speaking with. Existing again. I don't have the number. It's about a box request. I have the student ID. No problem. How can I help you to help you with that? Can I get your name and the student ID please? My name is Carolina Carla and the student ID is 257468439. #10 is 257468439 alright? Thank you. Then how can I help you today, Catalina? We'll put it out on the bus. Um, but for some reason he was kicked out of the system. Couple of almost always ago we put in a request again and I just wanted to know if it was already approved. Alright, alright, alright. Highlands be able to take a look into that. Can I get this doing the same please? Ohh. Thank you. And can you confirm his date of birth? October 28th, 2016. And his address. 1444 Boston Rd. Apt. 4N as in Nancy Banks, New York, 10/4. 6/1 Thank you. Are you calling? Are you sorry? Are you calling from the school or are you back? I'm the mother. I'm OK. Sorry. Thank you. Alright, I'm just pulling up an account here. Give me one moment please. Thank you. And when was it that you called in to report the initial 10 off of the bus they were put in? Let me give you a start, OK? It wasn't the 16th they put in the request. Alright. And I'm seeing that you called and again to follow up on it. Is that right? Yeah. Yes. OK. Alright. Just hold for me a moment, please. I'm just gonna take a further look into that. I'll come right back here. Thank you. Thank you very much for holding. OK, alright, so I'm seeing that there isn't a signed route at the moment. When was the last time that you spoke with your school bus coordinator? The last time that I spoke recording under was on the 20th. On the 20th, yeah, OK, and it is your system. What? He was on the bus all the way up to the 15th and for some reason when I got the phone call in the morning from the medication, she informed me that he was no longer on the list. So when I call you guys, I was informed that he wasn't umm, he was um what was the word that they used? Umm. Uh, he he wasn't. He didn't. So how it which was the translation company, they told me he was late for their system so he was nowhere to be found in transportation system. So we had to put in the request again on the same you know and that's when the put in the request. Umm. I was hoping that, you know, the situation was going to be resolved right away, but obviously has not, so yeah. Yes, and everything all the way up to the 15 and this has caused me issues with work. So, but you know, I work, that's why he got on the bus. I'm at 6 1/2 to be late for work and get out early so that I could drop him off and pick him up and then the next week since then. The week after that like the last week of class before the break. So I'm trying to get this situation resolved. The slash to start again on Tuesday and. I don't want anymore issues with work. And it's done, yeah. So I have to get things resolved as fast as possible for this. Nobody's requested for him to be kicked out of the system like because he was receiving his service with no issue and for some reason, I don't know why, nobody apparently knows the reason why he was kicked out of the system and. He wasn't. You know he was. Add. Exactly. So we have to go ahead and put in the request one more time. So I don't understand the reason why. Yeah, I I wouldn't be able to see why it wasn't thought that it does seem to be something that might have been an error. Since no one is able to see why I I'm going to make it another second. But I think recommend just following up with this school bus coordinator. Just to see if they have maybe a particular risks and not the other high bus or on the side route as of yet. But I am seeing that he is is probably still in the process of being reviewed. So it probably will take some time but most likely it's it would be the case where on Tuesday he gets service but I cannot say for sure because nothing happened yet when, when when they're on break. I see that you guys work but do the independent. The transportation company. Are all for this. It might not be able to know this, but they're still working like in their offices. I am not sure for the offices that some of the companies in the schools are open because they do service multiple schools. They would be open as well. OK. Alright, so just follow up your school bus coordinator just to make sure because they are the ones who actually who would be able to give you a bit more information. OK. OK. Alright. Thank you for calling. Have a great day. Thank you for your help. Bye. Bye."
>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa

            # Transcribe text
            # st.text_area("Transcribe text", audio_text, height=400)

            # Sentiment text
            # st.write("Sentiment based on Audio", get_audio_senti(file_name))

            st.subheader("Call Information", divider="blue")
            user_name_queries = (
                "what is user name? please provide only the name in your response."
            )
            user_Name = get_summary_response(audio_text, user_name_queries)
            agent_Name = "Jessica"
            call_duration = "5 min 2 sec"
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Agent")
                st.subheader("User")
                st.subheader("Call Duration")
                # your_html_design_as_string = """<svg xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="50" fill="red" /><text x="18" y="20.35" class="percentage">30%</text></svg>"""
                # st.markdown(your_html_design_as_string, unsafe_allow_html=True)
            with col2:
                st.subheader(agent_Name)
                st.subheader(user_Name)
                st.subheader(call_duration)

            st.divider()
            col1_1, col2_1  = st.columns(2)
            with col2_1:
                st.subheader("Conversation", divider='blue')
                summary_response = get_summary_response(audio_text, "Format the above conversation which is happend between an agent and user into separate dialogues. This conversation is started by Agent . clearly distinguishing the user name's messages from the agent's responses:. Don't change the text and word. Use the User name as "+ user_Name +" and Agent Name as " + agent_Name +". should be in markdown language and make the headlines bold")
                summary = summary_response.replace('Agent', agent_Name)
                st.info(summary)

<<<<<<< HEAD
            with col1_1:
                st.subheader("1. What was the user's inquiry or request during the call?", divider='blue')
                user_query_Prompt = "Identify the user's problem or issue based on the following conversation text. Please provide a clear and concise description of the problem without including any other information"
                user_query_response = get_summary_response(audio_text, user_query_Prompt)
                st.success(user_query_response)
            
                st.subheader("2. How was the agent's performance during the call?", divider='blue')
                agent_performance_Prompt = "Please evaluate whether the agent has accurately identified the user's problem from the conversation text provided. Rate the agent's problem identification on a scale of 1 to 10, with 1 being very poor and 10 being excellent. Consider factors such as the agent's ability to understand and address the user's issue effectively."
                agent_performance_response = get_summary_response(audio_text, agent_performance_Prompt)
                st.success(agent_performance_response)

                st.subheader("3. Agent's performance in greeting on a scale of 1 to 10.", divider='blue')
                opening_Prompt = "Please evaluate the agent's greeting on a scale of 1 to 10 only numerical, with 1 being very poor and 10 being excellent, based on the following conversation text. Consider factors such as politeness, clarity, and friendliness in your evaluation. Provide the answer in numerical rating first and explain your evaluation in the next line."
                opening_score = get_summary_response(audio_text, opening_Prompt)
                st.success(opening_score)

                st.subheader("4. What was the prevailing sentiment or emotional tone during the call?", divider='blue')
                sentiment = "Please analyze the sentiment of the following conversation between a user and an agent. Provide an assessment of the overall sentiment in the conversation and any notable shifts in sentiment if present. You can use terms such as 'positive,' 'negative,' 'neutral,' or provide a sentiment score if available. Also, include any specific phrases or cues that led to this sentiment analysis"
                summary_response = get_summary_response(audio_text, sentiment)
                st.success(summary_response)

                st.subheader("5. Summary of the conversation", divider='blue')
                summary_Prompt = "Provide the summary of the above text"
                summary_response = get_summary_response(audio_text, summary_Prompt)
                st.success(summary_response)
 
            st.subheader("Still have any question", divider='blue')
            
            response_container = st.container()
            # Here we will have a container for user input text box
            container = st.container()


            with container:

                with st.form(key='my_form', clear_on_submit=True):
                    user_input = st.text_area("Ask your queires here :", key='input', height=100)
                    submit_button = st.form_submit_button(label='Send')
                    if submit_button:
                        st.session_state['messages'].append(user_input)
                        model_response=get_summary_response(audio_text, user_input)
                        st.session_state['messages'].append(model_response)
                        

                        with response_container:
                            for i in range(len(st.session_state['messages'])):
                                    if (i % 2) == 0:
                                        message(st.session_state['messages'][i], key=str(i) + '_Agent')
                                    else:
                                        message(st.session_state['messages'][i], is_user=True, key=str(i) + '_User')
                    
=======
            st.subheader("1. User's Query", divider="blue")
            user_query_Prompt = "Identify the user's problem or issue based on the following conversation text. Please provide a clear and concise description of the problem without including any other information"
            user_query_response = get_summary_response(audio_text, user_query_Prompt)
            st.info(user_query_response)

            col1, col2 = st.columns(2)

            st.subheader("2.Agent performance", divider="blue")
            agent_performance_Prompt = "Please evaluate whether the agent has accurately identified the user's problem from the conversation text provided. Rate the agent's problem identification on a scale of 1 to 10, with 1 being very poor and 10 being excellent. Consider factors such as the agent's ability to understand and address the user's issue effectively."
            agent_performance_response = get_summary_response(
                audio_text, agent_performance_Prompt
            )
            st.info(agent_performance_response)

            st.subheader("3.Agent performance based on Greeting", divider="blue")
            opening_Prompt = "Please evaluate the agent's greeting on a scale of 1 to 10 only numerical, with 1 being very poor and 10 being excellent, based on the following conversation text. Consider factors such as politeness, clarity, and friendliness in your evaluation. Provide the answer in numerical rating first and explain your evaluation in the next line."
            opening_scrore = get_summary_response(audio_text, opening_Prompt)
            st.info(opening_scrore)

            st.subheader("4.Summary", divider="blue")
            st.info(
                get_summary_response(
                    audio_text,
                    "Format the above conversation which is happend between an agent and user into separate dialogues. This conversation is started by Agent . clearly distinguishing the user name's messages from the agent's responses:. Don't change the text and word. Use the User name as "
                    + user_Name
                    + " and Agent Name is "
                    + agent_Name
                    + "",
                )
            )

            st.subheader("Still any question", divider="blue")

    response_container = st.container()
    # Here we will have a container for user input text box
    container = st.container()

    with container:
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Ask your queires here :", key="input", height=100
            )
            submit_button = st.form_submit_button(label="Send")
            if submit_button:
                st.session_state["messages"].append(user_input)
                model_response = get_summary_response(audio_text, user_input)
                st.session_state["messages"].append(model_response)

                with response_container:
                    for i in range(len(st.session_state["messages"])):
                        if (i % 2) == 0:
                            message(
                                st.session_state["messages"][i],
                                is_user=True,
                                key=str(i) + "_user",
                            )
                        else:
                            message(
                                st.session_state["messages"][i], key=str(i) + "_Agent"
                            )


>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa
# Run the Streamlit app
if __name__ == "__main__":
    main()
