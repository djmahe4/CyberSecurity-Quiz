import streamlit as st
import json,random
from time import sleep
import datetime
import re,os
import random
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
from pylatexenc.latex2text import LatexNodes2Text

def run():
    st.set_page_config(
        page_title="Streamlit quizz app",
        page_icon="❓",
    )

if __name__ == "__main__":
    run()

# Custom CSS for the buttons
st.markdown("""
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
</style>
""", unsafe_allow_html=True)

# Initialize session variables if they do not exist
default_values = {'current_index': 0, 'current_question': 0, 'score': 0, 'selected_option': None,
                  'answer_submitted': False,"questions":None}
for key, value in default_values.items():
    st.session_state.setdefault(key, value)
def latex_to_unicode(latex_str):
    return LatexNodes2Text().latex_to_text(latex_str)
def init():
    # Find or create .env file
    env_path = find_dotenv()
    if env_path == "":
        with open('.env', 'w') as f:
            pass
    env_path = find_dotenv()

    # Load existing .env file or create one if it doesn't exist
    load_dotenv(find_dotenv(), override=True)

    # Check if API key is in environment variables
    api_key = os.getenv('GENERATIVE_AI_KEY')
    if api_key is None:
        # If API key is not set, ask the user for it
        api_key = input('Please enter your API key from https://ai.google.dev: ')
        # Store the API key in the .env file
        with open(find_dotenv(), 'a') as f:
            f.write(f'GENERATIVE_AI_KEY={api_key}\n')
        print("API key stored successfully!")

    load_dotenv()
    genai.configure(api_key=os.environ["GENERATIVE_AI_KEY"])

    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 0,
        "response_mime_type": "text/plain"
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        safety_settings=safety_settings,
        generation_config=generation_config
    )

    chat_session = model.start_chat(history=[])
    return chat_session

#st.title("Quiz App based on cybersecurity")
#username = st.text_input("Enter username")
# Quiz logic
def append_pqrst_markdown(subject, section, content):
  """
  Appends a markdown section to a file for studying using the PQrst method.

  Args:
      subject (str): The subject of the study material.
      section (str): The PQrst section (e.g., "P", "Q", "R", "S", "T").
      content (str): The content for the specified section.
  """
  # Create timestamp for clarity
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  filename = f"{subject}.md"

  # Construct markdown text with section heading
  markdown_text = f"""

## {subject} - {timestamp}

**{section}:**

{content}

"""

  # Open the file in append mode (a+) to create it if it doesn't exist
  try:
      with open(filename, "a+",encoding='utf-8') as file:
        file.write(markdown_text)
  except FileNotFoundError:
      filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
      with open(filename, "a+",encoding='utf-8') as file:
        file.write(markdown_text)
def generate_questions(query,chat_session):
    # This function will communicate with Gemini AI to get the output
    # Replace with actual Gemini AI API calls
    global question_answer
    try:
        while True:
            response = chat_session.send_message(query)
            # Extract the question and answer from the generated text
            question_answer = response.text.replace("*","").replace("**","")

            # Define a pattern to extract the question, options, and answer
            #pattern = r"\d+\.(.*?)\n\((a)\)(.*?)\n\((b)\)(.*?)\n\((c)\)(.*?)\n\((d)\)(.*?)\n\n\*\*AnswerKey:\*\*\n(\d+)\.\((.)\)"

            # Find all matches in the input text
            #matches = re.findall(pattern, question_answer, re.DOTALL)
            matches=question_answer.split("\n")

            # Create a list of dictionaries, each containing question, options, and answer
            questions_list = []

            diction={
                'question':"",
                'options':['','','','']
            }
            questions_list.append(diction)
            for match in matches:
                if match==" " or match=="" :#or "answer" in match.lower():
                    continue
                if 'answer' in match.lower():
                    match2 = re.search(r"\((.)\)", match)
                    if match2:
                        extracted_character = match2.group(1)
                        diction.update({"answer": extracted_character})
                #if type(match[0])==int:
                try:
                    if int(match[0]) and len(match)>10:
                        diction["question"]=match[3:]
                        print(match[3:])
                except ValueError:
                    pass
                if diction["question"]=="" and match.endswith("?"):
                    diction["question"]=match
                if match[1]=='a':
                    diction['options'][0]=match
                if match[1]=='b':
                    diction['options'][1]=match
                if match[1]=='c':
                    diction['options'][2]=match
                if match[1]=='d':
                    diction['options'][3] = match
                    diction = {
                        'question': "",
                        'options': ['','','','']
                    }
                    questions_list.append(diction)
                qmatch = re.match(r"(\d+)\.\s*\((\w)\)", match)
                if qmatch:
                    question_number, answer = qmatch.groups()
                    question_number=int(question_number)
                    print(f"Question {question_number}: Answer = {answer}")
                    # options=questions_list[question_number]["options"]
                    diction=questions_list[question_number-1]
                    diction.update({"answer": answer})
                    questions_list[question_number-1]=diction
                #else:
                    #diction["question"]+=match
            break
    except questions_list==[] or questions_list[0]['question']=='' or len(questions_list)>=3:
        sleep(10)
        print("retrying..")

    # Print the list of dictionaries
    print(questions_list)
    append_pqrst_markdown(query,"Test",question_answer)
    #else:
    #return response.text.replace("*","")
    return questions_list
cybersecurity_topics = [
    # Blockchain Security
    "Smart Contract Vulnerabilities",
    "Blockchain Data Encryption",
    "Cryptographic Hash Functions",
    "Digital Signature Algorithms",
    "Blockchain Network Consensus Mechanisms",
    "Blockchain Scalability and Performance",
    "Blockchain Regulatory Compliance",
    "Blockchain Identity Management",
    "Blockchain Access Control",
    "Blockchain Data Integrity",

    # IoT Security
    "IoT Device Authentication",
    "IoT Network Security Protocols",
    "IoT Data Encryption Methods",
    "IoT Device Vulnerability Management",
    "IoT Secure Communication Protocols",
    "IoT Data Analytics Security",
    "IoT Cloud Security",
    "IoT Endpoint Security",
    "IoT Firmware Security",
    "IoT Secure Boot Mechanisms",

    # Cryptography
    "Public-Key Cryptography",
    "Symmetric-Key Cryptography",
    "Hash Functions",
    "Digital Signatures",
    "Key Exchange Algorithms",
    "Elliptic Curve Cryptography",
    "Quantum Cryptography",
    "Homomorphic Encryption",
    "Zero-Knowledge Proofs",
    "Secure Multi-Party Computation",

    # Network Security
    "Firewall Configuration",
    "Intrusion Detection Systems",
    "Virtual Private Networks (VPNs)",
    "Network Segmentation",
    "Wireless Network Security",
    "Network Access Control",
    "Secure Sockets Layer/Transport Layer Security (SSL/TLS)",
    "Secure Shell (SSH) Protocol",
    "Network Monitoring and Analysis",
    "Denial-of-Service (DoS) Attack Prevention",
# Threat Intelligence
    "Threat Modeling",
    "Vulnerability Assessment",
    "Penetration Testing",
    "Incident Response",
    "Malware Analysis",
    "Phishing Attack Prevention",
    "Social Engineering Attack Prevention",
    "Advanced Persistent Threats (APTs)",
    "Insider Threats",
    "Cyber Threat Intelligence Sharing",

    # Cloud Security
    "Cloud Access Security Broker (CASB)",
    "Cloud Security Gateways",
    "Cloud Encryption",
    "Cloud Identity and Access Management",
    "Cloud Compliance and Governance",
    "Cloud Network Security",
    "Cloud Storage Security",
    "Cloud Computing Security Standards",
    "Cloud Security Architecture",
    "Cloud Security Monitoring",

    # Artificial Intelligence and Machine Learning Security
    "AI/ML Model Security",
    "AI/ML Data Security",
    "AI/ML Explainability",
    "AI/ML Transparency",
    "AI/ML Bias and Fairness",
    "AI/ML Robustness",
    "AI/ML Adversarial Attacks",
    "AI/ML Security Analytics",
    "AI/ML Incident Response",
    "AI/ML Security Standards"
]
ans={'a':0,'b':1,'c':2,'d':3}
def main_funct(topic):
    chat = init()
    # Load quiz data
    if st.session_state.questions == None:

        quiz_data=generate_questions(f"Formulate mcq quiz on {topic} with answers",chat)
        quiz_data.pop()
        for i, qa in enumerate(quiz_data):
            try:
                if qa["options"] == [] or qa["options"][0] == "" or qa["question"] == "" or qa["answer"] == "":
                    st.write("It seems like some error..Please click start again..")
                    main_funct(topic)
            except KeyError:
                st.write("It seems like some error..Please click start again..")
                main_funct(topic)
        st.session_state.questions = quiz_data
        return quiz_data
    else:
        print(st.session_state.questions)
        return st.session_state.questions
#quiz_data=st.session_state.questions

def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False
    st.session_state.questions = None

def submit_answer():

    # Check if an option has been selected
    if st.session_state.selected_option is not None:
        # Mark the answer as submitted
        st.session_state.answer_submitted = True
        # Check if the selected option is correct
        if st.session_state.selected_option == quiz_data[st.session_state.current_index]['answer']:
            st.session_state.score += 10
    else:
        # If no option selected, show a message and do not mark as submitted
        st.warning("Please select an option before submitting.")

def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False
topic=random.choice(cybersecurity_topics)
# Title and description
st.title(f"Quiz App based on {topic}")
quiz_data=main_funct(topic)
# Progress bar
progress_bar_value = (st.session_state.current_index + 1) / len(quiz_data)
st.metric(label="Score", value=f"{st.session_state.score} / {len(quiz_data) * 10}")
st.progress(progress_bar_value)

# Display the question and answer options
question_item = quiz_data[st.session_state.current_index]
st.subheader(f"Question {st.session_state.current_index + 1}")
st.title(f"{question_item['question']}")
#st.write(question_item['information'])

st.markdown(""" ___""")

# Answer selection
options = question_item['options']
correct_answer = question_item['options'][ans[question_item['answer']]]

if st.session_state.answer_submitted:
    for i, option in enumerate(options):
        label = option
        if option == correct_answer:
            st.success(f"{label} (Correct answer)")
            st.session_state.score+=10
        elif option == st.session_state.selected_option:
            st.error(f"{label} (Incorrect answer)")
        else:
            st.write(label)
else:
    for i, option in enumerate(options):
        if st.button(option, key=i, use_container_width=True):
            st.session_state.selected_option = option

st.markdown(""" ___""")

# Submission button and response logic
if st.session_state.answer_submitted:
    if st.session_state.current_index < len(quiz_data) - 1:
        st.button('Next', on_click=next_question)
    else:
        st.write(f"Quiz completed! Your score is: {st.session_state.score-10} / {len(quiz_data) * 10}")
        if st.button('Restart', on_click=restart_quiz):
            pass
else:
    if st.session_state.current_index < len(quiz_data):
        st.button('Submit', on_click=submit_answer)
