import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


# 웹 페이지 타이틀 설정
st.title("간단한 웹 사이트 샘플")

# 텍스트 입력
name = st.text_input("이름을 입력하세요.")

# 숫자 입력
age = st.number_input("나이를 입력하세요.", min_value=0, max_value=100)

# 체크박스
agree = st.checkbox("개인정보 수집에 동의합니다.")

# 버튼 클릭
button_clicked = st.button("제출")

# 제출 버튼을 클릭했을 때 동작
if button_clicked:
    st.write(f"이름: {name}")
    st.write(f"나이: {age}")
    if agree:
        st.write("개인정보 수집에 동의하셨습니다.")
    else:
        st.write("개인정보 수집에 동의하지 않으셨습니다.")
