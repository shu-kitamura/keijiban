import streamlit as st
from datetime import datetime


def print_posts(posts: list):
    for post in posts:
        with st.container(border=True):
            st.caption(post["time"].strftime("%Y-%m-%d %H:%M:%S"))
            st.markdown(post["text"])
        
def search_threads(haystack: str):
    # This function would normally search a database or an API for threads
    # For this example, we will return a static list
    return [f"{haystack}-1", f"{haystack}-2", f"{haystack}-3"]

if __name__ == "__main__":

    if "posts" not in st.session_state:
        st.session_state.posts = []

    if "search_results" not in st.session_state:
        st.session_state.search_results = None

    st.title("Keijiban App")

    st.sidebar.title("スレッド検索")
    
    haystack = st.sidebar.text_input("スレッド名を入力", key="thread_input")
    
    if st.session_state.get("search_results") is None and not haystack:
        st.sidebar.subheader("スレッドを検索してください")
    else:
        st.sidebar.subheader("スレッドの検索結果")        

        st.session_state.search_results = search_threads(haystack) if haystack else []
        if not st.session_state.search_results:
            st.sidebar.write("スレッドが見つかりませんでした")
        else:
            for result in st.session_state.search_results:
                if st.sidebar.button(result):
                    st.toast(f"{result} を選択しました")
                    st.rerun()

    print_posts(st.session_state.posts)

    msg = st.chat_input("チャットを開始", key="chat_input")
    if msg:
        st.session_state.posts.append({"text": msg, "time": st.session_state.get("time", datetime.now())})
        st.toast("投稿を受け付けました")
        st.rerun()
