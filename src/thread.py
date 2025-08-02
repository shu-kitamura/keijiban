import streamlit as st
from datetime import datetime

def thread_page(thread_title: str):
    st.button("検索に戻る", on_click=lambda: st.session_state.update({"page": "main"}))
    st.title(thread_title)

    print_posts(st.session_state.posts)

    msg = st.chat_input("チャットを開始", key="chat_input")
    if msg:
        write_post(msg)

def print_posts(posts: list):
    # 将来的にはDBから読み込み、表示する形にする
    for post in posts:
        with st.container(border=True):
            st.caption(post["time"].strftime("%Y-%m-%d %H:%M:%S"))
            st.markdown(post["text"])

def write_post(text: str):
    # 将来的にはDB書き込みにする
    st.session_state.posts.append({"text": text, "time": datetime.now()})
    st.toast("投稿を受け付けました")
    st.rerun()