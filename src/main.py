import streamlit as st

from thread import thread_page
from database import select_threads, insert_thread


def main_page():
    st.title("Keijiban App")

    with st.container():
        option_map = {
            0: ":material/add:",
            1: ":material/search:",
        }
        selection = st.pills(
            "モードを選択",
            options=option_map.keys(),
            format_func=lambda option: option_map[option],
            selection_mode="single",
        )

        match selection:
            case 0:
                create_mode()
            case 1:
                search_mode()
  
def search_mode():
    heystack = st.text_input("スレッドを検索", key="thread_search")

    if heystack:
        for thread_row in select_threads(heystack):
            id = thread_row[0]
            name = thread_row[1]
            st.button(name, on_click=lambda id=id, name=name: st.session_state.update({"page": "thread", "thread_title": name, "thread_id": id}))

def create_mode():
    thread_name = st.text_input("スレッド名を入力", key="thread_name")

    if thread_name:
        st.button(
            "スレッドを作成",
            on_click=lambda name=thread_name: st.session_state.update(
                {"page": "thread", "thread_title": name, "thread_id": insert_thread(name)}
            )
        )

if __name__ == "__main__":
    st.set_page_config(page_title="Keijiban App", layout="centered")

    st.session_state.setdefault("page", "main")
    st.session_state.setdefault("thread_title", "")
    st.session_state.setdefault("thread_id", "")
    st.session_state.setdefault("posts", [])

    match st.session_state.page:
        case "main":
            main_page()
        case "thread":
            thread_page(st.session_state.thread_title, st.session_state.thread_id)
