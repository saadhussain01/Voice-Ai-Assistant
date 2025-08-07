import streamlit as st
from utils.speech_to_text import transcribe_audio
from utils.text_to_speech import speak_text
from utils.pdf_reader import extract_text_from_pdf

from tools.notes_tool import add_note, view_notes
from tools.todo_tool import add_task, view_tasks
from tools.datetime_tool import get_current_date, get_current_time

import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_input(user_input):
    user_input_lower = user_input.lower()

    # Tool handling
    if "add note" in user_input_lower:
        note = user_input_lower.replace("add note", "").strip()
        return add_note(note)
    elif "view notes" in user_input_lower or "show notes" in user_input_lower:
        return view_notes()
    elif "add task" in user_input_lower:
        task = user_input_lower.replace("add task", "").strip()
        return add_task(task)
    elif "view tasks" in user_input_lower or "show tasks" in user_input_lower:
        return view_tasks()
    elif "date" in user_input_lower:
        return get_current_date()
    elif "time" in user_input_lower:
        return get_current_time()
    else:
        # Fallback to OpenAI GPT-4
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"

st.set_page_config(page_title="Voice AI Assistant with Tools")
st.title("🛠️ Voice AI Assistant with Tools and Memory")

# Voice Assistant
if st.button("🎧 Start Talking"):
    user_input = transcribe_audio()
    st.write(f"🗣️ You said: {user_input}")

    with st.spinner("Thinking..."):
        reply = process_input(user_input)
        st.success(f"🤖 Assistant: {reply}")
        speak_text(reply)

# File Upload Section
st.subheader("📄 Upload a PDF to Summarize")
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
if pdf_file:
    with st.spinner("Reading PDF..."):
        text = extract_text_from_pdf(pdf_file)
        summary = process_input(f"""Summarize this:{text}""")
        st.write("📝 Summary:")
        st.success(summary)
        speak_text(summary)
