import streamlit as st

def display_summary(summary: str):
    st.subheader("📝 Article Summary")
    st.write(summary)

def display_quiz(quiz):
    st.subheader("🎯 Awareness Quiz")
    for i, q in enumerate(quiz.quiz, 1):
        with st.expander(f"Q{i}: {q.question}"):
            st.markdown(f"**Answer:** {q.answer}")
            st.caption(f"Difficulty: {q.difficulty}")

def display_actions(actions):
    st.subheader("🌍 Eco-Friendly Actions")
    for action in actions.actions:
        st.markdown(f"✅ **{action.step}**")
        st.caption(f"Category: {action.category}")
        if action.impact:
            st.write(f"_Impact: {action.impact}_")
