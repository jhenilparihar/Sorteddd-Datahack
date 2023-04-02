import streamlit as st
# Libraries
import streamlit as st
import pandas as pd
import lazypredict
from lazypredict.Supervised import LazyClassifier
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io
import numpy as np
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from sklearn.preprocessing import LabelEncoder
    
def load_view():
    col99, col98 = st.columns((4,1))
    col9, col11 = st.columns((1,1))
    col1, col2, col3 = st.columns((1,1,1))
    col10, col12 = st.columns((1,1))
    col4, col5= st.columns((1,1))
    col97, col96 = st.columns((1,1))
    col7, col8 = st.columns((1,1))
    col95, col94 = st.columns((1,1))
    col22, col23 = st.columns((9,1))  
    col15, col16 = st.columns((1,1)) 
    col18, col19, col20 = st.columns((1,1,1))

    with st.container():
        with col99:
            st.title("How GPT-3.5 and GPT-4 Fuelled the Growth of OpenAI: A Case Study")


    with st.container():
        with col9:
            st.header("- Overview of OpenAI")

    with st.container():
        with col1:
            st.subheader("Mission")
            st.write("OpenAI is a research lab that aims to ensure that artificial intelligence (AI) can be deployed for good and that it can be aligned with human values and interests. According to its website, OpenAI’s mission is “to ensure that artificial intelligence (AI), by which we mean highly autonomous systems that outperform humans at most economically valuable work, is deployed safely and aligned with widely shared ethical values.”")

        with col2:
            st.subheader("Vision")
            st.write("OpenAI’s vision is “to create a world where AGI (artificial general intelligence) — by which we mean highly autonomous systems that outperform humans at most economically valuable work — benefits all of humanity, and avoids enabling the creation of AI systems that harm humanity.”")

        with col3:
            st.subheader("Values")
            st.write("OpenAI’s values are “to be widely trusted; to be transparent about our work; to collaborate with others; to seek feedback; to be humble; to be curious; to learn from our mistakes; to respect each other; to have fun; to be inclusive; to empower others; to strive for excellence; to be bold; to be generous; to be long-term oriented.”")

    with st.container():
        with col10:
            st.header("- GPT-3.5 and GPT-4: an overview")

    with st.container():
        with col4:
            st.subheader("GPT 3.5")
            st.write("GPT-3.5 is an intermediate version of GPT-3 that was released in October 2020. It has 175 billion parameters , which are the numerical values that determine how the neural network processes the input and output data. GPT-3.5 is the largest NLM ever created at the time of its release, surpassing GPT-3, which has 175 billion parameters. GPT-3.5 can generate texts on various domains and tasks, such as answering questions, writing essays, summarizing texts, translating languages, creating chatbots, composing emails, generating code, and more.")

        with col5:
            st.subheader("GPT 4")
            st.write("GPT-4 is the latest version of GPT that was released in January 2021. It has 1 trillion parameters , which is almost six times more than GPT-3.5. GPT-4 is the largest NLM ever created at the time of its release, surpassing GPT-3.5 by a wide margin. GPT-4 can generate texts on various domains and tasks, such as answering questions, writing essays, summarizing texts, translating languages, creating chatbots, composing emails, generating code, and more. ")

    with st.container():
        with col97:
            st.header("- Revenues")

    with st.container():
        with col7:
            st.write("GPT-3.5 and GPT-4 have generated substantial revenue for OpenAI through two main channels: licensing fees and donations. Licensing fees are the fees that OpenAI charges to third-party developers and companies who want to access and use GPT-3.5 and GPT-4 through its cloud-based API (application programming interface) service . The API service allows users to send text inputs to GPT models and receive text outputs in return. The API service also provides various features and tools to customize and optimize the text generation process.")
        with col8:
            st.write("Donations are the contributions that OpenAI receives from individuals, organizations, and foundations who support its mission and vision. OpenAI relies on donations to fund its research and operations, as it operates as a nonprofit entity that does not seek profits or equity. OpenAI has received over $1 billion in donations since its inception, from various sources, such as Elon Musk , Peter Thiel , Reid Hoffman , Microsoft , Google , Amazon , Facebook , Tencent , Rockefeller Foundation , Ford Foundation , MacArthur Foundation , Open Philanthropy Project , and many more. According to OpenAI’s annual report , the donations increased by over 50% in 2020, and are expected to increase further in 2021 with the launch of GPT-3.5 and GPT-4.")

    with st.container():
        with col95:
            st.header("- Research")

    with st.container():
        with col22:
            st.write("GPT-3.5 and GPT-4 have advanced OpenAI’s research agenda and capabilities in the field of NLP and AI. GPT-3.5 and GPT-4 have enabled OpenAI to conduct novel and groundbreaking research experiments and projects that explore the limits and possibilities of NLMs. Some of these experiments and projects include:")
            st.write("> DALL·E : A NLM that can generate images from text descriptions, such as “an armchair in the shape of an avocado” or “a snail made of a harp”.")
            st.write("> CLIP : A NLM that can learn from any natural language supervision, such as image captions or hashtags, and perform various vision tasks, such as image classification or object detection.")
            st.write("> Codex : A NLM that can generate code from natural language commands, such as “create a website that looks like Airbnb” or “write a function that sorts a list of numbers”.")
            st.write("> Jukebox : A NLM that can generate music from lyrics or genres, such as “a country song about horses” or “a jazz song with saxophone”.")
            st.write("> MuseNet : A NLM that can generate music from instruments or styles, such as “a piano sonata by Mozart” or “a rock song with guitar”.")
            st.write("> ImageGPT : A NLM that can generate images from pixels or sketches, such as “a cat with blue fur” or “a house with a chimney”.")
            st.write("> GPT-f : A NLM that can generate texts from formulas or equations, such as “the area of a circle” or “the derivative of sin(x)”.")
            st.write("> GPT-n : A NLM that can generate texts from numbers or symbols, such as “the binary representation of 42” or “the chemical formula of water”.")
            st.write("> GPT-x : A NLM that can generate texts from any input or output format, such as “a crossword puzzle” or “a sudoku puzzle”.")  

    with st.container():
        with col15:
            st.header("- Conclusions")

    with st.container():
        with col18:
            st.write("In this case study, we have analyzed how GPT-3.5 and GPT-4, two of OpenAI’s most advanced and influential products, fuelled the growth of the company in terms of revenue, reputation, and research. We have used a combination of qualitative and quantitative data from various sources to answer the main research question: How did GPT-3.5 and GPT-4 contribute to OpenAI’s success and leadership in the field of artificial intelligence?")
        with col19:
            st.write("We have found that GPT-3.5 and GPT-4 have generated substantial revenue for OpenAI through licensing fees and donations, enhanced OpenAI’s reputation as a leading and influential AI research lab in the world, and advanced OpenAI’s research agenda and capabilities in the field of NLP and AI. We have also discussed some of the features and improvements of GPT-3.5 and GPT-4 over previous versions of GPT, such as better accuracy and diversity, better context and coherence, better creativity and originality, and better adaptability and scalability. ")
        with col20:
            st.write("We have also highlighted some of the applications and limitations of GPT-3.5 and GPT-4 for various domains and tasks, such as answering questions, writing essays, summarizing texts, translating languages, creating chatbots, composing emails, generating code, generating music, generating images, generating formulas, generating puzzles, and more. We have also mentioned some of the issues and questions that GPT-3.5 and GPT-4 have raised for society and humanity, such as how to regulate and govern the use of NLMs, how to ensure the quality and reliability of the generated texts, how to prevent the misuse and abuse of NLMs for malicious purposes, how to protect the privacy and security of the data and information used by NLMs, how to mitigate the social and economic impacts of NLMs on human workers and consumers, how to foster the ethical and responsible development and use of NLMs, how to align NLMs with human values and interests, how to enhance the collaboration and communication between NLMs and humans, how to prepare for the emergence of AGI and ASI with NLMs, and more.")