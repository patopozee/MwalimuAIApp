import streamlit as st
from app import ask_mwalimu

st.title("📚 Mwalimu AI")
st.write("Welcome! Ask me any school question.")

# 1. Initialize session state to remember the Q&A across page reruns
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "current_answer" not in st.session_state:
    st.session_state.current_answer = ""

# 2. Answer Container (Stays at the very top)
answer_container = st.container()

with answer_container:
    if st.session_state.current_answer:
        st.write(f"**Your Question:** {st.session_state.current_question}")
        st.write("### Teacher's Answer")
        st.write(st.session_state.current_answer)
        st.markdown("---")

# 3. Input and Submit Form (Middle section)
# We use clear_on_submit=True to instantly wipe out the typed text upon submission
with st.form(key="mwalimu_form", clear_on_submit=True):
    question = st.text_input("Ask your question")
    submit_button = st.form_submit_button(label="Submit")

# 4. Processing & Spinner (Stays at the very bottom, below the form)
if submit_button:
    if question.strip():
        # The spinner is called here, rendering it physically below the form elements
        with st.spinner("Mwalimu AI is thinking..."):
            answer = ask_mwalimu(question)
            
            # Save the results to state
            st.session_state.current_answer = answer
            st.session_state.current_question = question
            
        # Forces Streamlit to rerun the script immediately so the new answer 
        # pops up in the top answer_container right away
        st.rerun()
    else:
        st.warning("Please type a question.")