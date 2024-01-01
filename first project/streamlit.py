import streamlit as s
import functions
import time

def todo():
    k12 = functions.reading()
    j = s.session_state["new_val"] + "\n"
    k12.append(j)
    functions.writing(k12)

def time_store():
    return time.strftime("%c")

s.title("First App")
s.subheader("Hey, this is my new app")
s.write("Let's see how it turns out")

# Display existing todos and their timestamps
k = functions.reading()
for i, j in enumerate(k):
    timestamp_key = f"{j}_timestamp"
    
    # Check if timestamp is already stored in session state
    if timestamp_key not in s.session_state:
        s.session_state[timestamp_key] = time_store()

    # Display checkbox and stored timestamp
    check = s.checkbox(f"{j} - {s.session_state[timestamp_key]}", key=f"{j}_{i}")
    
    if check:
        k.pop(i)
        functions.writing(k)
        del s.session_state[j]
        s.rerun()

# Text input for adding a new todo
s.text_input(label="", placeholder="Add a new todo", on_change=todo, key="new_val")
