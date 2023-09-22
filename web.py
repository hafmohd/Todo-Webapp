import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("Todo-List Web App")
st.subheader("First local web-app")
st.write("Increasing productivity with modern tools")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a to-do item here", placeholder="Add",
              on_change=add_todo, key="new_todo")

#print("hello")
#st.session_state


