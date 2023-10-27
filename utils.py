<<<<<<< HEAD
=======

from langchain.llms import AzureOpenAI
>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa
from transformers import pipeline
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
import os

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2022-12-01"
os.environ["OPENAI_API_BASE"] = "https://pubsec-careerpathways-openai.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "19ac6255a55b448e92190c0e5e75156e"


<<<<<<< HEAD
from langchain.llms import AzureOpenAI

def get_audio_text(file):
    text = "Thank you for calling the Office of People Transfer you're speaking with. Existing again. I don't have the number. It's about a box request. I have the student ID. No problem. How can I help you to help you with that? Can I get your name and the student ID please? My name is Carolina Carla and the student ID is 257468439. #10 is 257468439 alright? Thank you. Then how can I help you today, Catalina? We'll put it out on the bus. Um, but for some reason he was kicked out of the system. Couple of almost always ago we put in a request again and I just wanted to know if it was already approved. Alright, alright, alright. Highlands be able to take a look into that. Can I get this doing the same please? Ohh. Thank you. And can you confirm his date of birth? October 28th, 2016. And his address. 1444 Boston Rd. Apt. 4N as in Nancy Banks, New York, 10/4. 6/1 Thank you. Are you calling? Are you sorry? Are you calling from the school or are you back? I'm the mother. I'm OK. Sorry. Thank you. Alright, I'm just pulling up an account here. Give me one moment please. Thank you. And when was it that you called in to report the initial 10 off of the bus they were put in? Let me give you a start, OK? It wasn't the 16th they put in the request. Alright. And I'm seeing that you called and again to follow up on it. Is that right? Yeah. Yes. OK. Alright. Just hold for me a moment, please. I'm just gonna take a further look into that. I'll come right back here. Thank you. Thank you very much for holding. OK, alright, so I'm seeing that there isn't a signed route at the moment. When was the last time that you spoke with your school bus coordinator? The last time that I spoke recording under was on the 20th. On the 20th, yeah, OK, and it is your system. What? He was on the bus all the way up to the 15th and for some reason when I got the phone call in the morning from the medication, she informed me that he was no longer on the list. So when I call you guys, I was informed that he wasn't umm, he was um what was the word that they used? Umm. Uh, he he wasn't. He didn't. So how it which was the translation company, they told me he was late for their system so he was nowhere to be found in transportation system. So we had to put in the request again on the same you know and that's when the put in the request. Umm. I was hoping that, you know, the situation was going to be resolved right away, but obviously has not, so yeah. Yes, and everything all the way up to the 15 and this has caused me issues with work. So, but you know, I work, that's why he got on the bus. I'm at 6 1/2 to be late for work and get out early so that I could drop him off and pick him up and then the next week since then. The week after that like the last week of class before the break. So I'm trying to get this situation resolved. The slash to start again on Tuesday and. I don't want anymore issues with work. And it's done, yeah. So I have to get things resolved as fast as possible for this. Nobody's requested for him to be kicked out of the system like because he was receiving his service with no issue and for some reason, I don't know why, nobody apparently knows the reason why he was kicked out of the system and. He wasn't. You know he was. Add. Exactly. So we have to go ahead and put in the request one more time. So I don't understand the reason why. Yeah, I I wouldn't be able to see why it wasn't thought that it does seem to be something that might have been an error. Since no one is able to see why I I'm going to make it another second. But I think recommend just following up with this school bus coordinator. Just to see if they have maybe a particular risks and not the other high bus or on the side route as of yet. But I am seeing that he is is probably still in the process of being reviewed. So it probably will take some time but most likely it's it would be the case where on Tuesday he gets service but I cannot say for sure because nothing happened yet when, when when they're on break. I see that you guys work but do the independent. The transportation company. Are all for this. It might not be able to know this, but they're still working like in their offices. I am not sure for the offices that some of the companies in the schools are open because they do service multiple schools. They would be open as well. OK. Alright, so just follow up your school bus coordinator just to make sure because they are the ones who actually who would be able to give you a bit more information. OK. OK. Alright. Thank you for calling. Have a great day. Thank you for your help. Bye. Bye."
    if file == 'samplefile1.mp3':
        text = "Thank you for calling the Office of People Transfer you're speaking with. Existing again. I don't have the number. It's about a box request. I have the student ID. No problem. How can I help you to help you with that? Can I get your name and the student ID please? My name is Carolina Carla and the student ID is 257468439. #10 is 257468439 alright? Thank you. Then how can I help you today, Catalina? We'll put it out on the bus. Um, but for some reason he was kicked out of the system. Couple of almost always ago we put in a request again and I just wanted to know if it was already approved. Alright, alright, alright. Highlands be able to take a look into that. Can I get this doing the same please? Ohh. Thank you. And can you confirm his date of birth? October 28th, 2016. And his address. 1444 Boston Rd. Apt. 4N as in Nancy Banks, New York, 10/4. 6/1 Thank you. Are you calling? Are you sorry? Are you calling from the school or are you back? I'm the mother. I'm OK. Sorry. Thank you. Alright, I'm just pulling up an account here. Give me one moment please. Thank you. And when was it that you called in to report the initial 10 off of the bus they were put in? Let me give you a start, OK? It wasn't the 16th they put in the request. Alright. And I'm seeing that you called and again to follow up on it. Is that right? Yeah. Yes. OK. Alright. Just hold for me a moment, please. I'm just gonna take a further look into that. I'll come right back here. Thank you. Thank you very much for holding. OK, alright, so I'm seeing that there isn't a signed route at the moment. When was the last time that you spoke with your school bus coordinator? The last time that I spoke recording under was on the 20th. On the 20th, yeah, OK, and it is your system. What? He was on the bus all the way up to the 15th and for some reason when I got the phone call in the morning from the medication, she informed me that he was no longer on the list. So when I call you guys, I was informed that he wasn't umm, he was um what was the word that they used? Umm. Uh, he he wasn't. He didn't. So how it which was the translation company, they told me he was late for their system so he was nowhere to be found in transportation system. So we had to put in the request again on the same you know and that's when the put in the request. Umm. I was hoping that, you know, the situation was going to be resolved right away, but obviously has not, so yeah. Yes, and everything all the way up to the 15 and this has caused me issues with work. So, but you know, I work, that's why he got on the bus. I'm at 6 1/2 to be late for work and get out early so that I could drop him off and pick him up and then the next week since then. The week after that like the last week of class before the break. So I'm trying to get this situation resolved. The slash to start again on Tuesday and. I don't want anymore issues with work. And it's done, yeah. So I have to get things resolved as fast as possible for this. Nobody's requested for him to be kicked out of the system like because he was receiving his service with no issue and for some reason, I don't know why, nobody apparently knows the reason why he was kicked out of the system and. He wasn't. You know he was. Add. Exactly. So we have to go ahead and put in the request one more time. So I don't understand the reason why. Yeah, I I wouldn't be able to see why it wasn't thought that it does seem to be something that might have been an error. Since no one is able to see why I I'm going to make it another second. But I think recommend just following up with this school bus coordinator. Just to see if they have maybe a particular risks and not the other high bus or on the side route as of yet. But I am seeing that he is is probably still in the process of being reviewed. So it probably will take some time but most likely it's it would be the case where on Tuesday he gets service but I cannot say for sure because nothing happened yet when, when when they're on break. I see that you guys work but do the independent. The transportation company. Are all for this. It might not be able to know this, but they're still working like in their offices. I am not sure for the offices that some of the companies in the schools are open because they do service multiple schools. They would be open as well. OK. Alright, so just follow up your school bus coordinator just to make sure because they are the ones who actually who would be able to give you a bit more information. OK. OK. Alright. Thank you for calling. Have a great day. Thank you for your help. Bye. Bye."
    elif file == 'samplefile2.mp3':
         text = "sample2"

    return text

=======
>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa
def get_llm():
    llm = AzureOpenAI(
        deployment_name="CareerPathwaysPOC",
        model_name="gpt-35-turbo",
        temperature=0,
        max_tokens=2000
    )
    return llm


# def get_audio_text(file):

#    # specify a model, here its BASE
#     model = whisper.load_model("base")

#     # transcribe audio file
#     result = model.transcribe(file)
#     print(result["text"])
<<<<<<< HEAD
    
#     return result["text"]

=======

#     return result["text"]

>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa
#     # Send email using zapier
#     #agent.run("Send an Email to sharathraju489@gmail.com via gmail summarizing the following text provided below : "+result["text"])


def get_audio_senti(file):

<<<<<<< HEAD
    pipe = pipeline("audio-classification", model="nickmuchi/distilroberta-finetuned-financial-text-classification")
=======
    pipe = pipeline("audio-classification",
                    model="hackathon-pln-es/wav2vec2-base-finetuned-sentiment-classification-MESD")
>>>>>>> 09566744a0f1e125051deb67ef676a0e8d470baa
    result = pipe(file)
    return result


def get_summary_using_chatprompt(user_input):

    chat_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=(
                    "You are a helpful assistant that write a summary of the conversation between a user and the Education call center in bullet point"
                    "Extract all relevant information from the text and check whether the agent has violated any rules during the call."
                    "The summary should include key details such as the user's inquiry, the agent's responses, any requests made by the user, and any potential violations of call center rules or policies. Additionally, highlight any specific actions or follow-up steps discussed during the call."
                )
            ),
            HumanMessagePromptTemplate.from_template("{text}"),
        ]
    )

    # llm = ChatOpenAI(openai_api_key= openai_api_key)
    llm = get_llm()
    summary = llm(chat_template.format_messages(text=user_input))
    return summary


def get_summary_using_prompt(user_input):

    llm = get_llm()

    template = "Please provide me the summary of the below conversion between user and agent.\n {uses_conversion}.\n\nSummary:\n"
    prompt = PromptTemplate(
        input_variables=["uses_conversion"],
        template=template
    )
    summary_prompt = prompt.format(uses_conversion=user_input)

    print(summary_prompt)
    summary = llm(summary_prompt)
    return summary


def get_summary_response(uses_conversion, userqueries):

    llm = get_llm()

    role = "You are a conversation analyst responsible for examining and assessing interactions between users and agents."
    instructions = "Provide responses to the specific questions posed within the given conversation. \n Refrain from answering if the answer is not explicitly present in the provided text. \n Avoid offering explanations in your responses."
    conversation_history = ""
    template = "|im_start|>system\n {role} \n Instructions \n {instructions} \n conversation \n ${templateMessage} \n <|im_end|>\n ${conversation_history}\n <|im_start|>user\n${query}\n <|im_end|>\n"

    # template = "Please answer this question : {userqueries} ? Please don't provide the Explanation for answer. If you don't find the answer in the below text , please don't answer. \n \n\n {uses_conversion} \n\n"

    prompt = PromptTemplate(
        input_variables=["role", "instructions",
                         "templateMessage", "conversation_history", "query"],
        template=template
    )
    summary_prompt = prompt.format(templateMessage=uses_conversion, query=userqueries,
                                   role=role, instructions=instructions, conversation_history=conversation_history)
    print(summary_prompt)
    summary = llm(summary_prompt)
    summary = summary.replace('<|im_end|>', '')
    print(summary)
    return summary
