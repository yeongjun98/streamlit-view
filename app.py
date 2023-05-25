import streamlit as st

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('hello')
    
with tab2:
  #tab B를 누르면 표시될 내용 
  st.write('hi')

col1,col2 = st.columns([2,3])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

with col1 :
  # column 1 에 담을 내용
  st.title('here is column1')
with col2 :
  # column 2 에 담을 내용
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')


# with 구문 말고 다르게 사용 가능 
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ') 
#=>위에 with col2: 안의 내용과 같은 기능을합니다
