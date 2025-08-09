"""
This module handles the drawing of thread page.
"""

import streamlit as st

from database import select_posts, insert_post

def thread_page(thread_title: str, thread_id: str) -> None:
    col1, col2 = st.columns(2, gap=None)

    if col1.button("", icon=":material/arrow_back:"):
        st.session_state.update({"page": "main"})
        st.rerun()
    if col2.button("", icon=":material/refresh:"):
        st.rerun()


    st.title(thread_title)

    print_posts(thread_id)

    msg = st.chat_input("チャットを開始", max_chars=1000)
    if msg:
        write_post(thread_id, msg)

def print_posts(thread_id: str) -> None:
    for post in select_posts(thread_id):
        timestamp = post[0]
        content = post[1]
        with st.container(border=True):
            st.caption(timestamp.strftime("%Y-%m-%d %H:%M:%S"))
            st.markdown(content)

def write_post(thread_id: str, content: str) -> None:
    insert_post(thread_id, content)
    st.toast("投稿を受け付けました")
    st.rerun()