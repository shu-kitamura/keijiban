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

    st.sidebar.title("スレッド検索")
    haystack = st.sidebar.text_input("スレッド名を入力", key="thread_input")
    st.sidebar.subheader("スレッドの検索結果")
    st.sidebar.markdown(f"- {haystack}")

    print_posts(st.session_state.posts)

    msg = st.chat_input("チャットを開始", key="chat_input")
    if msg:
        st.session_state.posts.append({"text": msg, "time": st.session_state.get("time", datetime.now())})
        st.toast("投稿を受け付けました")
        st.rerun()
