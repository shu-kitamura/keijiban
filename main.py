import streamlit as st
from datetime import datetime


def print_posts(posts: list):
    for post in posts:
        with st.container(border=True):
            st.caption(post["time"].strftime("%Y-%m-%d %H:%M:%S"))
            st.markdown(post["text"])

if __name__ == "__main__":

    if "posts" not in st.session_state:
        st.session_state.posts = []

    st.title("Keijiban App")

    print_posts(st.session_state.posts)

    # チャット入力フォーム
    msg = st.chat_input("チャットを開始", key="chat_input")
    if msg:
        st.session_state.posts.append({"text": msg, "time": st.session_state.get("time", datetime.now())})
        st.toast("投稿を受け付けました")
        st.rerun()
