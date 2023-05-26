import streamlit as st
import pandas as pd
import datetime

# 페이지: 과목추천
def page_subject_recommendation():
    st.title("과목 추천")
    major = st.text_input("학과를 입력하세요.")
    name = st.text_input("이름을 입력하세요.")
    student_id = st.text_input("학번을 입력하세요.")
    select_multi_species = st.radio(
        '교과구분을 선택하세요.',
        ['전공','일선','교양']
    )
    select_multi_species2 = st.multiselect(
        '원하는 분야를 고르세요',
        ['컴퓨터','경제','사회와지리', '심리', '역사', '언어', '수학', '기초과학', '철학', '정보', '교육','복지','국어와문학','의학','기타','말하기와쓰기']
    )

    if st.button("추천 과목 확인"):
        st.write(f"학과: {major}")
        st.write(f"이름: {name}")
        st.write(f"학번: {student_id}")
        st.write("추천 교과목")

        # 추천과목 데이터

        df = pd.DataFrame(
            [
                {'': '1', '교과목': '공학을위한컴퓨터과학적사고', 'tel': '062-530-4206', '교과구분': '교선', '교과코드': 'CLT0797', '학점': '3.0', '강의실': 'AI융합-401', '개설학과': '인공지능학부', '강의타입': '일반과목', '분야' : '컴퓨터'}, 
                {'': '2', '교과목': 'C프로그래밍및실습', 'tel': '062-530-4206', '교과구분': '전선', '교과코드': 'CIS9017', '학점': '3.0', '강의실': '공7-222', '개설학과': '인공지능학부', '강의타입': '실험실습과목', '분야' : '컴퓨터'}, 
                {'': '3', '교과목': '인공지능기초', 'tel': '062-530-4206', '교과구분': '교선', '교과코드': 'CLT0961', '학점': '3.0', '강의실': '이러닝', '개설학과': '인공지능학부', '강의타입': '이러닝과목', '분야' : '컴퓨터'}, 
                {'': '4', '교과목': '경영통계', 'tel': '062-530-1430', '교과구분': '전선', '교과코드': 'BUS2001', '학점': '3.0', '강의실': '경2-201', '개설학과': '경영학부', '강의타입': '일반과목', '분야' : '경제'}, 
                {'': '5', '교과목': '재무관리', 'tel': '062-530-1430', '교과구분': '전필', '교과코드': 'BUS2017', '학점': '3.0', '강의실': '경1-210', '개설학과': '경영학부', '강의타입': '일반과목', '분야' : '경제'}, 
                {'': '6', '교과목': '기업윤리', 'tel': '062-530-1430', '교과구분': '전선', '교과코드': 'BUS4028', '학점': '3.0', '강의실': '경2-301', '개설학과': '경영학부', '강의타입': '일반과목', '분야' : '경제'},
                {'': '7', '교과목': '조직행동론', 'tel': '062-530-1430', '교과구분': '전필', '교과코드': 'BUS2012', '학점': '3.0', '강의실': '경1-210', '개설학과': '경영학부', '강의타입': '일반과목', '분야' : '경제'}, 
                {'': '8', '교과목': '노사관계론', 'tel': '062-530-1430', '교과구분': '전선', '교과코드': 'BUS4003', '학점': '3.0', '강의실': '경2-302', '개설학과': '경영학부', '강의타입': '일반과목', '분야' : '경제'}, 
                {'': '9', '교과목': '경제학개론', 'tel': '062-530-1540', '교과구분': '교선', '교과코드': 'CLT0763', '학점': '3.0', '강의실': '경1-150', '개설학과': '경제학과', '강의타입': '일반과목', '분야' : '경제'}, 
                {'': '10', '교과목': '경제학개론', 'tel': '062-530-1541', '교과구분': '교선', '교과코드': 'CLT0764', '학점': '3.0', '강의실': '경1-150', '개설학과': '경제학과', '강의타입': '일반과목', '분야' : '경제'}, 
                {'': '11', '교과목': '현장실습1', 'tel': '062-530-1660', '교과구분': '전선', '교과코드': 'MAE4081', '학점': '2.0', '강의실': '현장실습', '개설학과': '기계공학부', '강의타입': '현장실습과목'}, 
                {'': '12', '교과목': '현장실습2', 'tel': '062-530-1660', '교과구분': '전선', '교과코드': 'MAE4082', '학점': '3.0', '강의실': '현장실습', '개설학과': '기계공학부', '강의타입': '현장실습과목'}, 
                {'': '13', '교과목': '생활응용컴퓨터', 'tel': '062-530-3420', '교과구분': '교선', '교과코드': 'CLT0670', '학점': '3.0', '강의실': '이러닝', '개설학과': '소프트웨어공학과', '강의타입': '이러닝과목', '분야' : '컴퓨터'}, 
                {'': '14', '교과목': '지능형ICT융합현장실습', 'tel': '062-530-1750', '교과구분': '전선', '교과코드': 'ECE9041', '학점': '2.0', '강의실': '(4주과정 현장실습)', '개설학과': '소프트웨어공학과', '강의타입': '현장실습과목'}, 
                {'': '15', '교과목': '공학을위한컴퓨터과학적사고', 'tel': '062-530-3420', '교과구분': '교선', '교과코드': 'CLT0868', '학점': '3.0', '강의실': '공7-222', '개설학과': '소프트웨어공학과', '강의타입': '일반과목', '분야' : '컴퓨터'}, 
                {'': '16', '교과목': '실무소프트웨어프로젝트1', 'tel': '062-530-1750', '교과구분': '전선', '교과코드': 'SWE0001', '학점': '3.0', '강의실': '공7-217', '개설학과': '소프트웨어공학과', '강의타입': '일반과목', '분야' : '컴퓨터'}, 
                {'': '17', '교과목': '현장실습', 'tel': '062-530-1700', '교과구분': '전선', '교과코드': 'MSE1006', '학점': '2.0', '강의실': '현장실습', '개설학과': '신소재공학부', '강의타입': '현장실습과목'}, 
                {'': '18', '교과목': '클라우드컴퓨팅', 'tel': '062-530-1751', '교과구분': '전선', '교과코드': 'ECE9054', '학점': '3.0', '강의실': '공7-118', '개설학과': '컴퓨터정보통신공학과', '강의타입': '일반과목', '분야' : '컴퓨터'}, 
                {'': '19', '교과목': '지능형ICT융합현장실습', 'tel': '062-530-1751', '교과구분': '전선', '교과코드': 'ECE9041', '학점': '2.0', '강의실': '현장실습', '개설학과': '컴퓨터정보통신공학과', '강의타입': '현장실습과목'}, 
                {'': '20', '교과목': '어드벤쳐프로젝트', 'tel': '062-530-1751', '교과구분': '전선', '교과코드': 'ECE9053', '학점': '3.0', '강의실': '공7-118', '개설학과': '컴퓨터정보통신공학과', '강의타입': '일반과목', '분야' : '컴퓨터'}, 
                {'': '21', '교과목': '화학공학현장실습1', 'tel': '062-530-1850', '교과구분': '전선', '교과코드': 'CHE9027', '학점': '2.0', '강의실': '현장실습', '개설학과': '화학공학부', '강의타입': '현장실습과목'}, 
                {'': '22', '교과목': 'CAD 3D', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SPC6002', '학점': '3.0', '강의실': '이609', '개설학과': '기계IT융합공학과', '강의타입': '실험실습과목'}, 
                {'': '23', '교과목': '어드벤처디자인1', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SPC6006', '학점': '3.0', '강의실': '이604', '개설학과': '기계IT융합공학과', '강의타입': '일반과목'}, 
                {'': '24', '교과목': '플랜트CAD2', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'MIC2008', '학점': '3.0', '강의실': '이501', '개설학과': '기계IT융합공학과', '강의타입': '실험실습과목'}, 
                {'': '25', '교과목': '플랜트검사공학', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'MIC3001', '학점': '3.0', '강의실': '2공108', '개설학과': '기계IT융합공학과', '강의타입': '일반과목'}, 
                {'': '26', '교과목': '현장실습1', 'tel': '061-659-7710', '교과구분': '전공', '교과코드': 'MTS0019', '학점': '2.0', '강의실': '현장실습', '개설학과': '메카트로닉스공학과', '강의타입': '현장실습과목'}, 
                {'': '27', '교과목': 'CAD 3D', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SPC6002', '학점': '3.0', '강의실': '이609', '개설학과': '스마트융합공정공학과', '강의타입': '실험실습과목'}, 
                {'': '28', '교과목': '어드벤처디자인1', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SPC6006', '학점': '3.0', '강의실': '2공302', '개설학과': '스마트융합공정공학과', '강의타입': '일반과목'}, 
                {'': '29', '교과목': '공정계장설계', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SCP3014', '학점': '3.0', '강의실': '이605', '개설학과': '스마트융합공정공학과', '강의타입': '일반과목'}, 
                {'': '30', '교과목': '창의융합설계', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SCP3023', '학점': '3.0', '강의실': '이603', '개설학과': '스마트융합공정공학과', '강의타입': '실험실습과목'}, 
                {'': '31', '교과목': '전기전자기초실험', 'tel': '061-659-6896', '교과구분': '전필', '교과코드': 'SEC1040', '학점': '3.0', '강의실': '이603', '개설학과': '스마트전기제어공학과', '강의타입': '일반과목'}, 
                {'': '32', '교과목': '문제탐색프로젝트', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SPC6003', '학점': '3.0', '강의실': '이619', '개설학과': '스마트전기제어공학과', '강의타입': '일반과목'}, 
                {'': '33', '교과목': '플랜트설계공학', 'tel': '061-659-6896', '교과구분': '전선', '교과코드': 'SEC2005', '학점': '3.0', '강의실': '이619', '개설학과': '스마트전기제어공학과', '강의타입': '일반과목'}, 
                {'': '34', '교과목': '스마트센서공학', 'tel': '061-659-6896', '교과구분': '전필', '교과코드': 'SEC3001', '학점': '3.0', '강의실': '이604', '개설학과': '스마트전기제어공학과', '강의타입': '일반과목'}, 
                {'': '35', '교과목': '식품공학전공현장실습1', 'tel': '062-530-2140', '교과구분': '전선', '교과코드': 'FST9034', '학점': '2.0', '강의실': '현장실습', '개설학과': '식품공학과', '강의타입': '현장실습과목'}, 
                {'': '36', '교과목': '원예생명공학현장실습 1', 'tel': '062-530-2060', '교과구분': '전선', '교과코드': 'HRT4037', '학점': '5.0', '강의실': '현장실습', '개설학과': '원예생명공학과', '강의타입': '현장실습과목'}, 
                {'': '37', '교과목': '원예생명공학현장실습 2', 'tel': '062-530-2060', '교과구분': '전선', '교과코드': 'HRT4027', '학점': '5.0', '강의실': '현장실습', '개설학과': '원예생명공학과', '강의타입': '현장실습과목'}, 
                {'': '38', '교과목': '중국문화의이해', 'tel': '061-659-7580', '교과구분': '전선', '교과코드': 'CHS7018', '학점': '3.0', '강의실': '인424', '개설학과': '국제학부 중국학전공', '강의타입': '일반과목'}, 
                {'': '39', '교과목': '물류개론', 'tel': '061-659-7340', '교과구분': '전필', '교과코드': 'LOG6001', '학점': '3.0', '강의실': '인218', '개설학과': '물류교통학과', '강의타입': '일반과목'}, 
                {'': '40', '교과목': '교육심리', 'tel': '062-530-2340', '교과구분': '전공', '교과코드': 'EDU2062 ', '학점': '2.0', '강의실': '교육303', '개설학과': '교육학과', '강의타입': '일반과목', '분류' : '교육'}, 
                {'': '41', '교과목': '교육평가', 'tel': '062-530-2340', '교과구분': '전공', '교과코드': 'EUD2057', '학점': '2.0', '강의실': '교육333', '개설학과': '교육학과', '강의타입': '일반과목', '분류' : '교육'}, 
                {'': '42', '교과목': '영미문화교육', 'tel': '062-530-2430', '교과구분': '전공', '교과코드': 'EEL2007', '학점': '3.0', '강의실': '교육425', '개설학과': '영어교육과', '강의타입': '일반과목', '분류' : '교육'}, 
                {'': '43', '교과목': '전문업무실습', 'tel': '062-530-2660', '교과구분': '전필', '교과코드': 'LIS4001', '학점': '3.0', '강의실': '현장실습', '개설학과': '문헌정보학과', '강의타입': '현장실습과목', '분야':'정보'}, 
                {'': '44', '교과목': '정보문화사', 'tel': '062-530-2660', '교과구분': '전선', '교과코드': 'LIS1003', '학점': '3.0', '강의실': '이러닝', '개설학과': '문헌정보학과', '강의타입': '이러닝과목', '분야':'정보'}, 
                {'': '45', '교과목': '현대사회의이해', 'tel': '062-530-2640', '교과구분': '교선', '교과코드': 'CLT0594', '학점': '3.0', '강의실': '사회274', '개설학과': '사회학과', '강의타입': '일반과목', '분야' : '사회와지리'}, 
                {'': '46', '교과목': '심리학개론', 'tel': '062-530-2650', '교과구분': '교선', '교과코드': 'CLT0046', '학점': '3.0', '강의실': '사회대별관11', '개설학과': '심리학과', '강의타입': '일반과목', '분야' : '심리'}, 
                {'': '47', '교과목': '성격심리학', 'tel': '062-530-2650', '교과구분': '전선', '교과코드': 'PSY2006', '학점': '3.0', '강의실': '사회174', '개설학과': '심리학과', '강의타입': '일반과목', '분야' : '심리'}, 
                {'': '48', '교과목': '조직심리학', 'tel': '062-530-2650', '교과구분': '전선', '교과코드': 'PSY3008', '학점': '3.0', '강의실': '사회177', '개설학과': '심리학과', '강의타입': '일반과목', '분야' : '심리'}, 
                {'': '49', '교과목': '이상심리학', 'tel': '062-530-2650', '교과구분': '전선', '교과코드': 'PSY2003', '학점': '3.0', '강의실': '사회174', '개설학과': '심리학과', '강의타입': '일반과목', '분야' : '심리'}, 
                {'': '50', '교과목': '관광여가지리학', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR2026', '학점': '3.0', '강의실': '사회대별관14', '개설학과': '지리학과', '강의타입': '일반과목','분야':'사회와지리'}, 
                {'': '51', '교과목': '지역개발의이해', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR4055', '학점': '3.0', '강의실': '사회428', '개설학과': '지리학과', '강의타입': '일반과목','분야':'사회와지리'}, 
                {'': '52', '교과목': '문화역사지리학', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR4035', '학점': '3.0', '강의실': '사회대별관14', '개설학과': '지리학과', '강의타입': '일반과목','분야':'사회와지리'}, 
                {'': '53', '교과목': 'The Environment and Human Life(환경과 인간생활)', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR3039', '학점': '3.0', '강의실': '사회428', '개설학과': '지리학과', '강의타입': '일반과목','분야':'사회와지리'}, 
                {'': '54', '교과목': '분쟁의세계지리', 'tel': '062-530-2680', '교과구분': '교선', '교과코드': 'CLT0833', '학점': '3.0', '강의실': '이러닝', '개설학과': '지리학과', '강의타입': '이러닝과목','분야':'사회와지리'}, 
                {'': '55', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교307', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '56', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교308', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '57', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교309', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '58', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교310', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '59', '교과목': '소비자학', 'tel': '062-530-1320', '교과구분': '전선', '교과코드': 'HMM3006', '학점': '3.0', '강의실': '이러닝', '개설학과': '생활복지학과', '강의타입': '이러닝과목', '분야':'복지'}, 
                {'': '60', '교과목': '노인복지', 'tel': '062-530-1320', '교과구분': '전선', '교과코드': 'HMM4029', '학점': '3.0', '강의실': '이러닝', '개설학과': '생활복지학과', '강의타입': '이러닝과목', '분야':'복지'}, 
                {'': '61', '교과목': '영양사현장실습', 'tel': '062-530-1330', '교과구분': '전선', '교과코드': 'FDN4019', '학점': '2.0', '강의실': '현장실습', '개설학과': '식품영양과학부', '강의타입': '현장실습과목'}, 
                {'': '62', '교과목': '수산해양교육론', 'tel': '061-659-7190', '교과구분': '전필', '교과코드': 'MIT0003', '학점': '3.0', '강의실': '이학관506호', '개설학과': '수산해양산업관광레저융합학과', '강의타입': '일반과목'}, 
                {'': '63', '교과목': '수산해양학 및 실습', 'tel': '061-659-7190', '교과구분': '전필', '교과코드': 'MIT0007', '학점': '3.0', '강의실': '수산해양대학813호', '개설학과': '수산해양산업관광레저융합학과', '강의타입': '일반과목'}, 
                {'': '64', '교과목': '레저스포츠관광론', 'tel': '061-659-7190', '교과구분': '전필', '교과코드': 'MIT0008', '학점': '3.0', '강의실': '이학관506호', '개설학과': '수산해양산업관광레저융합학과', '강의타입': '일반과목'}, 
                {'': '65', '교과목': '의학통계학', 'tel': '062-530-4191', '교과구분': '전선', '교과코드': 'MED4092', '학점': '3.0', '강의실': '진리관102', '개설학과': '의예과', '강의타입': '일반과목','분야':'의학'}, 
                {'': '66', '교과목': '국어어문규범의이해', 'tel': '062-530-3130', '교과구분': '전필', '교과코드': 'KLL4024', '학점': '3.0', '강의실': '인1-108', '개설학과': '국어국문학과', '강의타입': '일반과목', '분야': '국어와문학'}, 
                {'': '67', '교과목': '한국고전문학개론', 'tel': '062-530-3131', '교과구분': '전선', '교과코드': 'KLL1002', '학점': '3.0', '강의실': '인1-206', '개설학과': '국어국문학과', '강의타입': '일반과목', '분야': '국어와문학'}, 
                {'': '68', '교과목': '한문', 'tel': '062-530-3132', '교과구분': '교선', '교과코드': 'CLT0002', '학점': '3.0', '강의실': '인1-206', '개설학과': '국어국문학과', '강의타입': '일반과목', '분야':'언어'}, 
                {'': '69', '교과목': '한국인의삶과문학', 'tel': '062-530-3133', '교과구분': '교선', '교과코드': 'CLT0829', '학점': '3.0', '강의실': '인1-108', '개설학과': '국어국문학과', '강의타입': '일반과목','분야':'국어와문학'}, 
                {'': '70', '교과목': '말하기의전략', 'tel': '062-530-3134', '교과구분': '교선', '교과코드': 'CLT0887', '학점': '3.0', '강의실': '인1-209', '개설학과': '국어국문학과', '강의타입': '일반과목', '분야':'말하기와쓰기'}, 
                {'': '71', '교과목': '서양의역사와문화', 'tel': '062-530-3240', '교과구분': '교선', '교과코드': 'CLT0836', '학점': '3.0', '강의실': '인3-301', '개설학과': '사학과', '강의타입': '일반과목','분야':'역사'}, 
                {'': '72', '교과목': '문화유산의이해', 'tel': '062-530-3240', '교과구분': '전선', '교과코드': 'HIS1001', '학점': '3.0', '강의실': '인3-301', '개설학과': '사학과', '강의타입': '일반과목', '분야': '역사'}, 
                {'': '73', '교과목': '논리학', 'tel': '062-530-3220', '교과구분': '교선', '교과코드': 'CLT0591', '학점': '3.0', '강의실': '인1-106', '개설학과': '철학과', '강의타입': '일반과목', '분야':'철학'}, 
                {'': '74', '교과목': '호남의역사와문화', 'tel': '062-530-3240', '교과구분': '교선', '교과코드': 'CLT0566', '학점': '3.0', '강의실': '이러닝', '개설학과': '사학과', '강의타입': '이러닝과목', '분야':'역사'}, 
                {'': '75', '교과목': '동양고대사', 'tel': '062-530-3240', '교과구분': '전선', '교과코드': 'HIS2002', '학점': '3.0', '강의실': '이러닝', '개설학과': '사학과', '강의타입': '이러닝과목', '분야':'역사'}, 
                {'': '76', '교과목': '철학과 삶', 'tel': '062-530-3220', '교과구분': '교선', '교과코드': 'CLT0041', '학점': '3.0', '강의실': '이러닝', '개설학과': '철학과', '강의타입': '이러닝과목', '분야':'철학'}, 
                {'': '77', '교과목': '생명윤리', 'tel': '062-530-3220', '교과구분': '교선', '교과코드': 'CLT0863', '학점': '3.0', '강의실': '인3-306', '개설학과': '철학과', '강의타입': '일반과목', '분야':'철학'}, 
                {'': '78', '교과목': '긍정적학습동기유발전략세미나', 'tel': '062-530-2340', '교과구분': '전공', '교과코드': 'GR24575', '학점': '3.0', '강의실': '교육304', '개설학과': '교육학과', '강의타입': '일반과목', '분야':'교육'}, 
                {'': '79', '교과목': '일반물리1', 'tel': '062-530-3351', '교과구분': '교선', '교과코드': 'CLT0095', '학점': '3.0', '강의실': '자3-301', '개설학과': '물리학과', '강의타입': '일반과목', '분야':'기초과학'}, 
                {'': '80', '교과목': '광전자현장실습1', 'tel': '062-530-3351', '교과구분': '전선', '교과코드': 'PHY4018', '학점': '3.0', '강의실': '현장실습', '개설학과': '물리학과', '강의타입': '현장실습과목'}, 
                {'': '81', '교과목': '36.5도의물리학', 'tel': '062-530-3351', '교과구분': '교선', '교과코드': 'CLT0820', '학점': '3.0', '강의실': '이러닝', '개설학과': '물리학과', '강의타입': '이러닝과목', '분야':'기초과학'}, 
                {'': '82', '교과목': '일반물리2', 'tel': '062-530-3351', '교과구분': '교선', '교과코드': 'CLT0096', '학점': '3.0', '강의실': '이러닝', '개설학과': '물리학과', '강의타입': '이러닝과목', '분야':'기초과학'}, 
                {'': '83', '교과목': '일반생물2', 'tel': '062-530-3390', '교과구분': '교선', '교과코드': 'CLT0098', '학점': '3.0', '강의실': '자3-306', '개설학과': '생물학과', '강의타입': '일반과목', '분야':'기초과학'}, 
                {'': '84', '교과목': '수학1', 'tel': '062-530-3330', '교과구분': '교선', '교과코드': 'CLT0082', '학점': '3.0', '강의실': '자3-202', '개설학과': '수학과', '강의타입': '일반과목','분야':'수학'}, 
                {'': '85', '교과목': '수학1', 'tel': '062-530-3330', '교과구분': '교선', '교과코드': 'CLT0082', '학점': '3.0', '강의실': '자3-201', '개설학과': '수학과', '강의타입': '일반과목','분야':'수학'}, 
                {'': '86', '교과목': '수학2', 'tel': '062-530-3330', '교과구분': '교선', '교과코드': 'CLT0083', '학점': '3.0', '강의실': '자3-202', '개설학과': '수학과', '강의타입': '일반과목','분야':'수학'}, 
                {'': '87', '교과목': '기초통계학', 'tel': '062-530-3440', '교과구분': '교필', '교과코드': 'CLT0933', '학점': '3.0', '강의실': '자3-205', '개설학과': '통계학과', '강의타입': '일반과목','분야':'수학'}, 
                {'': '88', '교과목': '일반화학2', 'tel': '062-530-3370', '교과구분': '교선', '교과코드': 'CLT0085', '학점': '3.0', '강의실': '자3-101', '개설학과': '화학과', '강의타입': '일반과목', '분야':'기초과학'}, 
                {'': '89', '교과목': '5·18민주화운동과 세계의 항쟁', 'tel': '062-530-3916', '교과구분': '교선', '교과코드': 'CLT0952', '학점': '3.0', '강의실': '평생301', '개설학과': '518연구소', '강의타입': '일반과목', '분야':'역사'}, 
                {'': '90', '교과목': '성찰과소통을위한글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0888', '학점': '3.0', '강의실': '진리관103', '개설학과': '교육혁신본부', '강의타입': '일반과목', '분야':'말하기와쓰기'}, 
                {'': '91', '교과목': '성찰과소통을위한글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0888', '학점': '3.0', '강의실': '진리관103', '개설학과': '교육혁신본부', '강의타입': '일반과목', '분야':'말하기와쓰기'}, 
                {'': '92', '교과목': '과학기술글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0894', '학점': '3.0', '강의실': '진리관302', '개설학과': '교육혁신본부', '강의타입': '일반과목', '분야':'말하기와쓰기'}, 
                {'': '93', '교과목': '인문사회글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0893', '학점': '3.0', '강의실': '진리관202', '개설학과': '교육혁신본부', '강의타입': '일반과목', '분야':'말하기와쓰기'}, 
                {'': '94', '교과목': '효과적인말하기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0890', '학점': '3.0', '강의실': '진리관301', '개설학과': '교육혁신본부', '강의타입': '일반과목', '분야':'말하기와쓰기'}, 
                {'': '95', '교과목': '예술감성과미학', 'tel': '062-530-0355', '교과구분': '교선', '교과코드': 'CLT0828', '학점': '3.0', '강의실': '이러닝', '개설학과': '교육혁신본부', '강의타입': '이러닝과목', '분야':'철학'}, 
                {'': '96', '교과목': '국외현장실습1', 'tel': '062-530-1275', '교과구분': '일선', '교과코드': 'UNV5023', '학점': '2.0', '강의실': '국외현장실습', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '97', '교과목': '국외현장실습4', 'tel': '062-530-1275', '교과구분': '일선', '교과코드': 'UNV5010', '학점': '5.0', '강의실': '국외현장실습', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '98', '교과목': '국외현장실습6', 'tel': '062-530-1275', '교과구분': '일선', '교과코드': 'UNV5061', '학점': '1.0', '강의실': '국외현장실습', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '99', '교과목': '국외언어연수1', 'tel': '062-530-1275', '교과구분': '교양', '교과코드': 'CLT0875', '학점': '3.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '100', '교과목': '국외언어연수2', 'tel': '062-530-1275', '교과구분': '교선', '교과코드': 'CLT0587', '학점': '5.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '101', '교과목': '국외언어연수4', 'tel': '062-530-1275', '교과구분': '교선', '교과코드': 'CLT0783', '학점': '1.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '102', '교과목': '국외언어연수5', 'tel': '062-530-1275', '교과구분': '교선', '교과코드': 'CLT0877', '학점': '2.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '103', '교과목': '여수바다여행놀이', 'tel': '061-659-7026', '교과구분': '교선', '교과코드': 'CLT0954', '학점': '3.0', '강의실': '교407', '개설학과': '글로벌교육원', '강의타입': '일반과목', '분야':'기타'}, 
                {'': '104', '교과목': '생활영어1', 'tel': '062-530-3635', '교과구분': '교선', '교과코드': 'CLT0666', '학점': '3.0', '강의실': '본부지정', '개설학과': '언어교육원', '강의타입': '일반과목', '분야':'언어'}, 
                {'': '105', '교과목': '생활한국어1', 'tel': '062-530-3648', '교과구분': '교선', '교과코드': 'CLT0965', '학점': '3.0', '강의실': '진리관201', '개설학과': '언어교육원', '강의타입': '일반과목', '분야':'언어'}, 
                {'': '106', '교과목': '생활한국어2', 'tel': '062-530-3648', '교과구분': '교선', '교과코드': 'CLT0966', '학점': '3.0', '강의실': '진리관304', '개설학과': '언어교육원', '강의타입': '일반과목', '분야':'언어'}, 
                {'': '107', '교과목': '하계입영훈련', 'tel': '061-659-6523', '교과구분': '군사', '교과코드': 'ROTC010', '학점': '1.0', '강의실': '학군교', '개설학과': '학군단', '강의타입': '현장실습과목'}, 
                {'': '108', '교과목': '연구연수1', 'tel': '062-530-5918', '교과구분': '연구', '교과코드': 'GR23476', '학점': '3.0', '강의실': '국외연구/교육기관 연수', '개설학과': '일반대학원', '강의타입': '연구연수과목'}, 
                {'': '109', '교과목': '현장실습1', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4008', '학점': '2.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '110', '교과목': '현장실습7', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4011', '학점': '2.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '111', '교과목': '현장실습12', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4016', '학점': '2.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '112', '교과목': '현장실습13', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4017', '학점': '2.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '113', '교과목': '현장실습4', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4006', '학점': '5.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '114', '교과목': '현장실습5', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4007', '학점': '5.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '115', '교과목': '현장실습8', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4012', '학점': '5.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}, 
                {'': '116', '교과목': '현장실습9', 'tel': '062-530-0393', '교과구분': '일선', '교과코드': 'UNV4013', '학점': '5.0', '강의실': '기업체현장', '개설학과': '취업지원실', '강의타입': '현장실습'}
            ]
        )
        # 전공, 일선, 교양 구분
        if select_multi_species == "전공" :
            major_list = []
            for i in range(116):
                if df['개설학과'][i] == major :
                    major_list.append()

            df = df[df['교과구분'].isin(major_list)]
            tmp_df = df[df['분야'].isin(select_multi_species2)]
            tmp_df = tmp_df.loc[:,['교과목','tel', '교과코드', '학점', '강의실', '강의타입']]

        elif select_multi_species == "일선" :
            elective_list = []
            for i in range(116) :
                if ((df['교과구분'][i] == '전공' or df['교과구분'][i] == '전선' or df['교과구분'][i] == '전필') and df['개설학과'][i] != major) :
                    elective_list.append()
            df = df[df['교과구분'].isin(elective_list)]
            tmp_df = df[df['분야'].isin(select_multi_species2)]
            tmp_df = tmp_df.loc[:,['교과목','tel', '교과코드', '학점', '강의실', '강의타입']]

        else :
            df = df[df['교과구분'].isin(["교선", '교필','군사','교양'])]
            tmp_df = df[df['분야'].isin(select_multi_species2)]
            tmp_df = tmp_df.loc[:,['교과목','tel', '교과코드', '학점', '강의실', '강의타입']]

        # 데이터프레임 슬라이싱
        # df = df[df['교과구분'].isin(["교선", '교필','군사','교양'])]
        # tmp_df = df[df['분야'].isin(select_multi_species2)]
        # tmp_df = tmp_df.loc[:,['교과목','tel', '교과코드', '학점', '강의실', '강의타입']]
        # 필터링 결과 
        st.table(tmp_df)    

        st.write("전체 교과목")
        st.dataframe(df, use_container_width=True)

# 페이지: 전남대학교 스케쥴
def page_university_schedule():
    st.title("전남대학교 스케쥴")
    selected_date = st.date_input("날짜를 선택하세요.", datetime.date.today())

    if st.button("스케쥴 확인"):
        st.write(f"선택한 날짜: {selected_date}")

        df2 = pd.DataFrame([
                {'start': '2023-01-02', 'end': '2023-01-02', 'name': '제2학기 성적정정 마감'}, 
                {'start': '2023-01-03', 'end': '2023-01-03', 'name': '제2학기 성적제출 마감'}, 
                {'start': '2023-01-10', 'end': '2023-01-24', 'name': '제1학기 강의계획서 입력'}, 
                {'start': '2023-01-24', 'end': '2023-01-24', 'name': '동계 계절학기 성적제출 마감'}, 
                {'start': '2023-01-26', 'end': '2023-01-26', 'name': '2023년도 전기 일반대학원 종합시험'}, 
                {'start': '2023-01-27', 'end': '2023-01-27', 'name': '2023년도 전기 일반대학원 외국어시험'}, 
                {'start': '2023-02-01', 'end': '2023-02-14', 'name': '제1학기 대학원 수료후 등록생 신청'}, 
                {'start': '2023-02-07', 'end': '2023-02-07', 'name': '2022학년도 후기 석박사학위청구논문 제출 일정 공고'}, 
                {'start': '2023-02-09', 'end': '2023-02-10', 'name': '수강희망과목 예약'}, 
                {'start': '2023-02-13', 'end': '2023-03-03', 'name': '2023년도 전기 일반대학원 지도교수 배정'}, 
                {'start': '2023-02-14', 'end': '2023-02-14', 'name': '제1학기 수강신청(4학년)'}, 
                {'start': '2023-02-15', 'end': '2023-02-15', 'name': '제1학기 수강신청(3학년)'}, 
                {'start': '2023-02-16', 'end': '2023-02-16', 'name': '제1학기 수강신청(2학년)'}, 
                {'start': '2023-02-17', 'end': '2023-02-17', 'name': '제1학기 수강신청(1학년)'}, 
                {'start': '2023-02-20', 'end': '2023-02-23', 'name': '제1학기 등록 및 수료후 등록'}, 
                {'start': '2023-02-20', 'end': '2023-02-21', 'name': '제1학기 수강신청(전학년 공통)'}, 
                {'start': '2023-02-24', 'end': '2023-02-24', 'name': '2022학년도 전기 학위수여식'}, 
                {'start': '2023-03-02', 'end': '2023-03-08', 'name': '제1학기 수강신청 정정'}, 
                {'start': '2023-03-02', 'end': '2023-03-02', 'name': '제1학기 개강'}, 
                {'start': '2023-03-02', 'end': '2023-03-02', 'name': '2023학년도 입학식'}, 
                {'start': '2023-03-20', 'end': '2023-03-24', 'name': '2022학년도 후기 박사학위수여예정자 학위청구논문(심사용) 접수'}, 
                {'start': '2023-03-27', 'end': '2023-03-31', 'name': '2022학년도 후기 석사학위수여예정자 학위청구논문(심사용) 접수'}, 
                {'start': '2023-03-28', 'end': '2023-03-28', 'name': '제1학기 수업일수 1/4'}, 
                {'start': '2023-04-03', 'end': '2023-04-07', 'name': '2023학년도 전기 석·박사 학위수여예정자 학위청구논문 작성계획서 접수'}, 
                {'start': '2023-04-10', 'end': '2023-04-21', 'name': '제1학기 중간 수업평가'}, 
                {'start': '2023-04-17', 'end': '2023-04-21', 'name': '제1학기 중간고사'}, 
                {'start': '2023-04-24', 'end': '2023-04-24', 'name': '제1학기 수업일수 2/4'}, 
                {'start': '2023-05-01', 'end': '2023-05-01', 'name': '근로자의 날(휴업)'}, 
                {'start': '2023-05-23', 'end': '2023-05-23', 'name': '제1학기 수업일수 3/4'}, 
                {'start': '2023-06-08', 'end': '2023-06-08', 'name': '자체보강일'}, 
                {'start': '2023-06-09', 'end': '2023-06-09', 'name': '개교기념일(휴업)'}, 
                {'start': '2023-06-12', 'end': '2023-06-12', 'name': '5. 5.(금) 어린이날 보강 '}, 
                {'start': '2023-06-13', 'end': '2023-06-13', 'name': '6. 6.(화) 현충일 보강'}, 
                {'start': '2023-06-14', 'end': '2023-06-14', 'name': '5. 1.(월) 근로자의 날 보강'}, 
                {'start': '2023-06-15', 'end': '2023-06-15', 'name': '5. 29.(월) 부처님 오신 날 보강'}, 
                {'start': '2023-06-16', 'end': '2023-06-22', 'name': '제1학기 기말고사'}, 
                {'start': '2023-06-16', 'end': '2023-07-10', 'name': '제1학기 교수수업개선서(CQI) 입력'}, 
                {'start': '2023-06-16', 'end': '2023-07-03', 'name': '제1학기 최종 수업평가'}, 
                {'start': '2023-06-19', 'end': '2023-06-23', 'name': '2022학년도 후기 석·박사학위수여예정자 논문심사 결과 보고'}, 
                {'start': '2023-06-22', 'end': '2023-06-22', 'name': '제1학기 종강'}, 
                {'start': '2023-06-22', 'end': '2023-06-22', 'name': '제1학기 성적공고'}, 
                {'start': '2023-06-26', 'end': '2023-07-20', 'name': '하계 계절학기'}, 
                {'start': '2023-06-27', 'end': '2023-06-27', 'name': '제1학기 성적공고 마감'}, 
                {'start': '2023-06-30', 'end': '2023-06-30', 'name': '제1학기 성적정정 마감'}, 
                {'start': '2023-07-03', 'end': '2023-07-03', 'name': '제1학기 성적제출 마감'}, 
                {'start': '2023-07-10', 'end': '2023-07-24', 'name': '제2학기 수업계획서 입력'}, 
                {'start': '2023-07-26', 'end': '2023-07-26', 'name': '2023년도 후기 일반대학원 종합시험'}, 
                {'start': '2023-07-27', 'end': '2023-07-27', 'name': '하계 계절학기 성적제출 마감'}, 
                {'start': '2023-07-27', 'end': '2023-07-27', 'name': '2023년도 후기 일반대학원 외국어시험'}, 
                {'start': '2023-08-01', 'end': '2023-08-02', 'name': '수강희망과목 예약'}, 
                {'start': '2023-08-01', 'end': '2023-08-01', 'name': '2023학년도 전기 석·박사학위청구논문 제출 일정 공고'}, 
                {'start': '2023-08-02', 'end': '2023-08-16', 'name': '제2학기 대학원 수료후 등록생 신청'}, 
                {'start': '2023-08-04', 'end': '2023-08-04', 'name': '제2학기 수강신청(4학년)'}, 
                {'start': '2023-08-07', 'end': '2023-08-07', 'name': '제2학기 수강신청(3학년)'}, 
                {'start': '2023-08-08', 'end': '2023-08-08', 'name': '제2학기 수강신청(2학년)'}, 
                {'start': '2023-08-09', 'end': '2023-08-09', 'name': '제2학기 수강신청(1학년)'}, 
                {'start': '2023-08-10', 'end': '2023-08-11', 'name': '제2학기 수강신청(전학년 공통)'}, 
                {'start': '2023-08-16', 'end': '2023-09-01', 'name': '2023년도 후기 일반대학원 지도교수 배정'}, 
                {'start': '2023-08-22', 'end': '2023-08-25', 'name': '제2학기 등록 및 수료후 등록'}, 
                {'start': '2023-08-25', 'end': '2023-08-25', 'name': '2022학년도 후기 학위수여식'}, 
                {'start': '2023-09-01', 'end': '2023-09-07', 'name': '제2학기 수강신청 정정'}, 
                {'start': '2023-09-01', 'end': '2023-09-01', 'name': '제2학기 개강'}, 
                {'start': '2023-09-25', 'end': '2023-10-02', 'name': '2023학년도 전기 박사학위수여예정자 학위청구논문(심사용) 접수'}, 
                {'start': '2023-09-27', 'end': '2023-09-27', 'name': '제2학기 수업일수 1/4'}, 
                {'start': '2023-10-02', 'end': '2023-10-06', 'name': '2023학년도 전기 석사학위수여예정자 학위청구논문(심사용) 접수'}, 
                {'start': '2023-10-10', 'end': '2023-10-13', 'name': '2023학년도 후기 석·박사학위수여예정자 학위청구논문 작성계획서 접수'}, 
                {'start': '2023-10-16', 'end': '2023-10-27', 'name': '제2학기 중간 수업평가'}, 
                {'start': '2023-10-23', 'end': '2023-10-27', 'name': '제2학기 중간고사'}, 
                {'start': '2023-10-30', 'end': '2023-10-30', 'name': '제2학기 수업일수 2/4'}, 
                {'start': '2023-11-24', 'end': '2023-11-24', 'name': '제2학기 수업일수 3/4'}, 
                {'start': '2023-12-07', 'end': '2023-12-07', 'name': '9. 28.(목) 추석연휴 보강'}, 
                {'start': '2023-12-08', 'end': '2023-12-08', 'name': '9. 29.(금) 추석연휴 보강'}, 
                {'start': '2023-12-11', 'end': '2023-12-11', 'name': '자체보강일'}, 
                {'start': '2023-12-12', 'end': '2023-12-12', 'name': '10. 3.(화) 개천절 보강'}, 
                {'start': '2023-12-13', 'end': '2023-12-13', 'name': '10. 9.(월) 한글날 보강'}, 
                {'start': '2023-12-15', 'end': '2023-12-21', 'name': '제2학기 기말고사'}, 
                {'start': '2023-12-15', 'end': '2024-01-10', 'name': '제2학기 교수수업개선서(CQI) 입력'}, 
                {'start': '2023-12-15', 'end': '2024-01-03', 'name': '제2학기 최종 수업평가'}])
        
        for i in range(87):
            if str(df2['start'][i]) == str(selected_date) :
                st.write(f"{selected_date}, 일정입니다.")
                st.write(f"{df2['name'][i]}")
            
            
                
        

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
