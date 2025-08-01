import streamlit as st
from datetime import datetime

def thread_page(title: str):

    msg = st.chat_input("チャットを開始", key="chat_input")
    if msg:
        st.toast("投稿を受け付けました")
        st.rerun()


page_title = "スレッドページ"
st.title(page_title)
thread_page(page_title)