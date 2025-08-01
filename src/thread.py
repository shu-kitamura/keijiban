import streamlit as st
from datetime import datetime

def thread_page(title: str):
    st.title(title)

    msg = st.chat_input("チャットを開始", key="chat_input")
    if msg:
        st.session_state.posts.append({"text": msg, "time": st.session_state.get("time", datetime.now())})
        st.toast("投稿を受け付けました")
        st.rerun()
