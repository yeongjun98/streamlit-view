import streamlit as st

# 전남대학교 포털 사이트 테마 설정
def set_jnu_theme():
    st.markdown(
        """
        <style>
        /* 전남대학교 포털 사이트 테마 스타일 */
        body {
            font-family: '맑은 고딕', 'Malgun Gothic', '돋움', Dotum, sans-serif;
            background-color: #F1F1F1;
        }
        .stApp {
            max-width: 800px;
            margin: 0 auto;
        }
        .stContainer {
            padding: 1rem;
        }
        .stButton button {
            background-color: #0070C0;
            color: #ffffff;
        }
        .stTextInput div div input {
            background-color: #ffffff;
            color: #333333;
        }
        .stSelectbox div div div[role="button"] {
            background-color: #ffffff;
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# 메인 페이지
def main_page():
    st.title("전남대학교 포털 사이트")
    st.write("메인 페이지 내용을 여기에 작성하세요.")

# 공지사항 페이지
def announcements_page():
    st.title("공지사항")
    st.write("공지사항 페이지 내용을 여기에 작성하세요.")

# 학사일정 페이지
def academic_calendar_page():
    st.title("학사일정")
    st.write("학사일정 페이지 내용을 여기에 작성하세요.")

# 학과소개 페이지
def department_introduction_page():
    st.title("학과소개")
    st.write("학과소개 페이지 내용을 여기에 작성하세요.")

# 메인 애플리케이션
def main():
    set_jnu_theme()

    # 네비게이션 메뉴 설정
    pages = {
        "메인": main_page,
        "공지사항": announcements_page,
        "학사일정": academic_calendar_page,
        "학과소개": department_introduction_page
    }

    # 네비게이션 바
    st.sidebar.title("메뉴")
    selected_page = st.sidebar.radio("페이지 선택", list(pages.keys()))

    # 선택한 페이지 실행
    pages[selected_page]()

if __name__ == "__main__":
    main()
