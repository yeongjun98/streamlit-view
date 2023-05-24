import streamlit as st
import datetime

# 페이지: 과목추천
def page_subject_recommendation():
    st.title("과목 추천")
    major = st.text_input("학과를 입력하세요.")
    name = st.text_input("이름을 입력하세요.")
    student_id = st.text_input("학번을 입력하세요.")
    remaining_credits = st.number_input("잔여학점을 입력하세요.", min_value=0)
    theme = st.selectbox("테마를 선택하세요.", ["밝은 테마", "어두운 테마"])

    if st.button("추천 과목 확인"):
        st.write(f"학과: {major}")
        st.write(f"이름: {name}")
        st.write(f"학번: {student_id}")
        st.write(f"잔여학점: {remaining_credits}")
        st.write(f"선택한 테마: {theme}")

# 페이지: 전남대학교 스케쥴
def page_university_schedule():
    st.title("전남대학교 스케쥴")
    selected_date = st.date_input("날짜를 선택하세요.", datetime.date.today())

    if st.button("스케쥴 확인"):
        st.write(f"선택한 날짜: {selected_date}")

# 페이지: 공지사항
def page_announcements():
    st.title("공지사항")
    st.write("현재 공지사항이 없습니다.")

# 메인 애플리케이션
def main():
    # 네비게이션 메뉴 설정
    pages = {
        "과목 추천": page_subject_recommendation,
        "전남대학교 스케쥴": page_university_schedule,
        "공지사항": page_announcements
    }

    # 네비게이션 바
    st.sidebar.title("메뉴")
    selected_page = st.sidebar.radio("페이지 선택", list(pages.keys()))

    # 선택한 페이지 실행
    pages[selected_page]()

if __name__ == "__main__":
    main()
