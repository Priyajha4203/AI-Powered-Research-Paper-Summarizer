from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate,load_prompt
import os
import base64

load_dotenv()

model = ChatOpenAI(
    model = 'qwen/qwen3-30b-a3b:free',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

#set background 
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("logo/background4.png")

# Load logo
def get_image_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
logo_base64 = get_image_base64("logo/Research_tool_logo.png")

st.markdown(f"""
<div style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-top: 20px; margin-bottom: 30px;">
    <img src="data:image/png;base64,{logo_base64}" width="60" />
    <h1 style="margin: 0; font-size: 2.0em;">AI-Powered Research Paper Summarizer</h1>
</div>
""", unsafe_allow_html=True)


research_papers = {
    "Natural Language Processing (NLP)": [
        "1. Attention Is All You Need – Vaswani et al. (2017)",
        "2. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding – Devlin et al. (2018)",
        "3. GPT-3: Language Models are Few-Shot Learners – Brown et al. (2020)",
        "4. T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer – Raffel et al. (2020)",
        "5. LoRA: Low-Rank Adaptation of Large Language Models – Hu et al. (2021)",
        "6. PaLM: Scaling Language Models with Pathways – Chowdhery et al. (2022)",
        "7. LLaMA: Open and Efficient Foundation Language Models – Meta AI (2023)",
        "8. An Interactive Chatbot for College Enquiry (2023)",
        "9. Mixtral: Mixture of Experts (MoE) LLMs (2024)"
    ],
    
    "Computer Vision": [
        "1. ImageNet Classification with Deep Convolutional Neural Networks (AlexNet) – Krizhevsky et al. (2012)",
        "2. Deep Residual Learning for Image Recognition (ResNet) – He et al. (2015)",
        "3. YOLOv3: An Incremental Improvement – Redmon et al. (2018)",
        "4. Vision Transformers (ViT) – Dosovitskiy et al. (2020)",
        "5. Segment Anything – Kirillov et al. (Meta AI, 2023)"
    ],
    "Diffusion Models & Generative Models": [
        "1. Denoising Diffusion Probabilistic Models – Ho et al. (2020)",
        "2. Score-Based Generative Modeling through SDEs – Song et al. (2020)",
        "3. Diffusion Models Beat GANs on Image Synthesis – Dhariwal & Nichol (2021)",
        "4. Stable Diffusion – CompVis (2022)",
        "5. Genie: Generative Interactive Environments (2024)",
    ],
    "Multimodal & General AI": [
        "1. CLIP: Learning Transferable Visual Models From Natural Language Supervision – Radford et al. (2021)",
        "2. DALL·E: Creating Images from Text – OpenAI (2021)",
        "3. Gato: A Generalist Agent – DeepMind (2022)",
        "4. Flamingo: Multimodal Few-Shot Learner – DeepMind (2022)",
        "5. Gemini: A Family of Multimodal Models – Google DeepMind (2023)",
        "6. Perception, Reason, Think, and Plan: A Survey on Large Multimodal Reasoning Models(2025)"
    ],
    "Reinforcement Learning & Agents": [
        "1. Human-level control through deep reinforcement learning (DQN) – Mnih et al. (2015)",
        "2. AlphaGo – Silver et al. (2016)",
        "3. Proximal Policy Optimization Algorithms (PPO) – Schulman et al. (2017)",
        "4. AutoGPT: Autonomous GPT-4 agents – Significant Gravitas (2023)",
    ]
}

#category selection
selected_category = st.selectbox("Select Category of Research Paper", list(research_papers.keys()))

# Paper selection based on category
paper_input = st.selectbox("Select Research Paper Name", research_papers[selected_category])   
 
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)
