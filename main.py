import streamlit as st

from pages.thread import thread_page


def main_page():
    st.title("Keijiban App")

    with st.container():
        heystack = st.text_input("スレッドを検索", key="thread_search")

        if heystack:
            for thread in search_thread(heystack):
                st.button(thread, on_click=lambda t=thread: st.session_state.update({"page": "thread", "thread_title": t}))


def search_thread(heystack: str) -> list:
    return [f"{heystack}1", f"{heystack}2", f"{heystack}3"]



if __name__ == "__main__":
    st.set_page_config(page_title="Keijiban App", layout="centered")
    st.session_state.setdefault("page", "main")
    st.session_state.setdefault("thread_title", "")
    st.session_state.setdefault("posts", [])

    match st.session_state.page:
        case "main":
            main_page()
        case "thread":
            thread_page(st.session_state.thread_title)
