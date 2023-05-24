import streamlit as st
import datetime

# 배너 1: 과목추천
def show_subject_recommendation():
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

# 배너 2: 전남대학교 스케쥴
def show_university_schedule():
    st.title("전남대학교 스케쥴")
    selected_date = st.date_input("날짜를 선택하세요.", datetime.date.today())

    if st.button("스케쥴 확인"):
        st.write(f"선택한 날짜: {selected_date}")

# 배너 3: 공지사항
def show_announcements():
    st.title("공지사항")
    st.write("현재 공지사항이 없습니다.")

# 웹 페이지 타이틀 설정
st.title("다기능 웹사이트")

# 배너 1: 과목추천
show_subject_recommendation()

# 배너 2: 전남대학교 스케쥴
show_university_schedule()

# 배너 3: 공지사항
show_announcements()
