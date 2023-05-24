import streamlit as st

# 과목 추천 함수
def recommend_subjects(major):
    subjects = {
        "전자공학": ["회로이론", "디지털시스템", "신호 및 시스템"],
        "컴퓨터공학": ["프로그래밍 기초", "자료구조", "알고리즘"],
        "경영학": ["경영학원론", "마케팅", "재무관리"]
    }
    if major in subjects:
        return subjects[major]
    else:
        return []

# 웹 페이지 타이틀 설정
st.title("과목 추천 시스템")

# 입력 폼
major = st.text_input("학과를 입력하세요.")
name = st.text_input("이름을 입력하세요.")
student_id = st.text_input("학번을 입력하세요.")

# 입력에 대한 출력
if st.button("추천 과목 확인"):
    if major and name and student_id:
        st.write(f"학과: {major}")
        st.write(f"이름: {name}")
        st.write(f"학번: {student_id}")

        recommended_subjects = recommend_subjects(major)
        if recommended_subjects:
            st.write("추천 과목:")
            for subject in recommended_subjects:
                st.write(subject)
        else:
            st.write("해당 학과에 대한 추천 과목이 없습니다.")
    else:
        st.write("입력값을 모두 입력해주세요.")
