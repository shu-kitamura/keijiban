import streamlit as st



def main_page():
    st.title("Keijiban App")

    with st.container():
        heystack = st.text_input("スレッドを検索", key="thread_search")

        if heystack:
            for thread in search_thread(heystack):
                if st.button(thread):
                    st.query_params.update(t=thread)
                    st.switch_page("pages/thread.py")


def search_thread(heystack: str) -> list:
    return ["thread1", "thread2", "thread3"]



if __name__ == "__main__":
    st.set_page_config(page_title="Keijiban App", layout="centered")
    main_page()    
