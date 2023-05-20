import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "과목 구분을 선택하세요",
    ("전공", "일선", "교양")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "학기 구분을 선택하세요",
        ("하계 계절학기", "동계 계절학기")
    )


# 웹 페이지 타이틀 설정
st.title("계절학기 과목")

# 텍스트 입력
name = st.text_input("이름을 입력하세요")

# 숫자 입력
num = st.number_input("학번을 입력하세요", value=int)

# 체크박스
agree = st.checkbox("개인정보 수집에 동의합니다.")

# 버튼 클릭
button_clicked = st.button("제출")

# 제출 버튼을 클릭했을 때 동작
if button_clicked:
    st.write(f"이름: {name}")
    st.write(f"학번: {num}")
    if agree:
        st.write("개인정보 수집에 동의하셨습니다.")
        view = [1, 2, 3]
        st.write('# 계절학기 교과목 추천')
        st.write('## 수강 가능 교과목')
        view
        st.write('## 수강 후기')
        st.bar_chart(view)
        import pandas as pd
        st.write('## 교과목 세부 정보')
        sview = pd.Series(view)
        sview

    else:
        st.write("개인정보 수집에 동의하지 않으셨습니다.")
