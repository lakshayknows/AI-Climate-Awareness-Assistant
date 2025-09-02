import streamlit as st
from utils import loaders, formatter
from chains.summarizer import summarize_text
from chains.quiz_generator import generate_quiz
from chains.recommender import recommender
from dotenv import load_dotenv

load_dotenv()
# --------------------
# Streamlit Page Config
# --------------------
st.set_page_config(
    page_title="Climate Awareness Assistant",
    page_icon="🌱",
    layout="wide"
)

st.title("🌍 Climate Awareness Assistant")
st.caption("Summarize climate articles, take quizzes, and discover eco-action steps.")

# --------------------
# Sidebar Input Section
# --------------------
st.sidebar.header("📂 Input Article")

uploaded_file = st.sidebar.file_uploader("Upload a file", type=["txt", "pdf", "docx"])
manual_input = st.sidebar.text_area("Or paste article text here")

# Persist article across tabs
if "article" not in st.session_state:
    st.session_state.article = None

if uploaded_file:
    st.session_state.article = loaders.load_from_upload(uploaded_file)
elif manual_input.strip():
    st.session_state.article = manual_input.strip()

article_text = st.session_state.article

# --------------------
# Main Content
# --------------------
if not article_text:
    st.info("👆 Upload a file or paste an article in the sidebar to get started.")
else:
    tab1, tab2, tab3 = st.tabs(["📝 Summary", "🎯 Quiz", "🌍 Actions"])

    # --- Summary Tab ---
    with tab1:
        with st.spinner("Generating summary..."):
            try:
                summary = summarize_text(article_text)
                formatter.display_summary(summary)
            except Exception as e:
                st.error(f"❌ Failed to generate summary: {e}")

    # --- Quiz Tab ---
    with tab2:
        with st.spinner("Generating quiz..."):
            try:
                quiz = generate_quiz(article_text)
                formatter.display_quiz(quiz)
            except Exception as e:
                st.error(f"❌ Failed to generate quiz: {e}")

    # --- Actions Tab ---
    with tab3:
        with st.spinner("Recommending eco-actions..."):
            try:
                actions = recommender(article_text)
                formatter.display_actions(actions)
            except Exception as e:
                st.error(f"❌ Failed to generate eco-actions: {e}")

# --------------------
# Footer
# --------------------
st.markdown("---")
st.caption("⚡ Built with LangChain, Streamlit & OpenRouter — by Lakshay 🌱")
