import streamlit as st
import pandas as pd
import datetime

# 페이지: 과목추천
def page_subject_recommendation():
    st.title("과목 추천")
    major = st.text_input("학과를 입력하세요.")
    name = st.text_input("이름을 입력하세요.")
    student_id = st.text_input("학번을 입력하세요.")
    remaining_credits = st.number_input("잔여학점을 입력하세요.", min_value=0)
    select_multi_species = st.multiselect(
        '원하는 분야를 고르세요',
        ['컴퓨터','경제','사회와지리', '심리', '역사', '언어', '수학', '기초과학', '철학', '정보', '교육','복지','국어와문학','의학','기타']

    )

    if st.button("추천 과목 확인"):
        st.write(f"학과: {major}")
        st.write(f"이름: {name}")
        st.write(f"학번: {student_id}")
        st.write(f"잔여학점: {remaining_credits}")


        # 추천과목 데이터

        df = pd.DataFrame(
            [
                {'': '1', '교과목': '공학을위한컴퓨터과학적사고', 'tel': '062-530-4206', '교과구분': '교선', '교과코드': 'CLT0797', '학점': '3.0', '강의실': 'AI융합-401', '개설학과': '인공지능학부', '강의타입': '일반과목'}, 
                {'': '2', '교과목': 'C프로그래밍및실습', 'tel': '062-530-4206', '교과구분': '전선', '교과코드': 'CIS9017', '학점': '3.0', '강의실': '공7-222', '개설학과': '인공지능학부', '강의타입': '실험실습과목'}, 
                {'': '3', '교과목': '인공지능기초', 'tel': '062-530-4206', '교과구분': '교선', '교과코드': 'CLT0961', '학점': '3.0', '강의실': '이러닝', '개설학과': '인공지능학부', '강의타입': '이러닝과목'}, 
                {'': '4', '교과목': '경영통계', 'tel': '062-530-1430', '교과구분': '전선', '교과코드': 'BUS2001', '학점': '3.0', '강의실': '경2-201', '개설학과': '경영학부', '강의타입': '일반과목'}, 
                {'': '5', '교과목': '재무관리', 'tel': '062-530-1430', '교과구분': '전필', '교과코드': 'BUS2017', '학점': '3.0', '강의실': '경1-210', '개설학과': '경영학부', '강의타입': '일반과목'}, 
                {'': '6', '교과목': '기업윤리', 'tel': '062-530-1430', '교과구분': '전선', '교과코드': 'BUS4028', '학점': '3.0', '강의실': '경2-301', '개설학과': '경영학부', '강의타입': '일반과목'},
                {'': '7', '교과목': '조직행동론', 'tel': '062-530-1430', '교과구분': '전필', '교과코드': 'BUS2012', '학점': '3.0', '강의실': '경1-210', '개설학과': '경영학부', '강의타입': '일반과목'}, 
                {'': '8', '교과목': '노사관계론', 'tel': '062-530-1430', '교과구분': '전선', '교과코드': 'BUS4003', '학점': '3.0', '강의실': '경2-302', '개설학과': '경영학부', '강의타입': '일반과목'}, 
                {'': '9', '교과목': '경제학개론', 'tel': '062-530-1540', '교과구분': '교선', '교과코드': 'CLT0763', '학점': '3.0', '강의실': '경1-150', '개설학과': '경제학과', '강의타입': '일반과목'}, 
                {'': '10', '교과목': '경제학개론', 'tel': '062-530-1541', '교과구분': '교선', '교과코드': 'CLT0764', '학점': '3.0', '강의실': '경1-150', '개설학과': '경제학과', '강의타입': '일반과목'}, 
                {'': '11', '교과목': '현장실습1', 'tel': '062-530-1660', '교과구분': '전선', '교과코드': 'MAE4081', '학점': '2.0', '강의실': '현장실습', '개설학과': '기계공학부', '강의타입': '현장실습과목'}, 
                {'': '12', '교과목': '현장실습2', 'tel': '062-530-1660', '교과구분': '전선', '교과코드': 'MAE4082', '학점': '3.0', '강의실': '현장실습', '개설학과': '기계공학부', '강의타입': '현장실습과목'}, 
                {'': '13', '교과목': '생활응용컴퓨터', 'tel': '062-530-3420', '교과구분': '교선', '교과코드': 'CLT0670', '학점': '3.0', '강의실': '이러닝', '개설학과': '소프트웨어공학과', '강의타입': '이러닝과목'}, 
                {'': '14', '교과목': '지능형ICT융합현장실습', 'tel': '062-530-1750', '교과구분': '전선', '교과코드': 'ECE9041', '학점': '2.0', '강의실': '(4주과정 현장실습)', '개설학과': '소프트웨어공학과', '강의타입': '현장실습과목'}, 
                {'': '15', '교과목': '공학을위한컴퓨터과학적사고', 'tel': '062-530-3420', '교과구분': '교선', '교과코드': 'CLT0868', '학점': '3.0', '강의실': '공7-222', '개설학과': '소프트웨어공학과', '강의타입': '일반과목'}, 
                {'': '16', '교과목': '실무소프트웨어프로젝트1', 'tel': '062-530-1750', '교과구분': '전선', '교과코드': 'SWE0001', '학점': '3.0', '강의실': '공7-217', '개설학과': '소프트웨어공학과', '강의타입': '일반과목'}, 
                {'': '17', '교과목': '현장실습', 'tel': '062-530-1700', '교과구분': '전선', '교과코드': 'MSE1006', '학점': '2.0', '강의실': '현장실습', '개설학과': '신소재공학부', '강의타입': '현장실습과목'}, 
                {'': '18', '교과목': '클라우드컴퓨팅', 'tel': '062-530-1751', '교과구분': '전선', '교과코드': 'ECE9054', '학점': '3.0', '강의실': '공7-118', '개설학과': '컴퓨터정보통신공학과', '강의타입': '일반과목'}, 
                {'': '19', '교과목': '지능형ICT융합현장실습', 'tel': '062-530-1751', '교과구분': '전선', '교과코드': 'ECE9041', '학점': '2.0', '강의실': '현장실습', '개설학과': '컴퓨터정보통신공학과', '강의타입': '현장실습과목'}, 
                {'': '20', '교과목': '어드벤쳐프로젝트', 'tel': '062-530-1751', '교과구분': '전선', '교과코드': 'ECE9053', '학점': '3.0', '강의실': '공7-118', '개설학과': '컴퓨터정보통신공학과', '강의타입': '일반과목'}, 
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
                {'': '40', '교과목': '교육심리', 'tel': '062-530-2340', '교과구분': '전공', '교과코드': 'EDU2062 ', '학점': '2.0', '강의실': '교육303', '개설학과': '교육학과', '강의타입': '일반과목'}, 
                {'': '41', '교과목': '교육평가', 'tel': '062-530-2340', '교과구분': '전공', '교과코드': 'EUD2057', '학점': '2.0', '강의실': '교육333', '개설학과': '교육학과', '강의타입': '일반과목'}, 
                {'': '42', '교과목': '영미문화교육', 'tel': '062-530-2430', '교과구분': '전공', '교과코드': 'EEL2007', '학점': '3.0', '강의실': '교육425', '개설학과': '영어교육과', '강의타입': '일반과목'}, 
                {'': '43', '교과목': '전문업무실습', 'tel': '062-530-2660', '교과구분': '전필', '교과코드': 'LIS4001', '학점': '3.0', '강의실': '현장실습', '개설학과': '문헌정보학과', '강의타입': '현장실습과목'}, 
                {'': '44', '교과목': '정보문화사', 'tel': '062-530-2660', '교과구분': '전선', '교과코드': 'LIS1003', '학점': '3.0', '강의실': '이러닝', '개설학과': '문헌정보학과', '강의타입': '이러닝과목'}, 
                {'': '45', '교과목': '현대사회의이해', 'tel': '062-530-2640', '교과구분': '교선', '교과코드': 'CLT0594', '학점': '3.0', '강의실': '사회274', '개설학과': '사회학과', '강의타입': '일반과목'}, 
                {'': '46', '교과목': '심리학개론', 'tel': '062-530-2650', '교과구분': '교선', '교과코드': 'CLT0046', '학점': '3.0', '강의실': '사회대별관11', '개설학과': '심리학과', '강의타입': '일반과목'}, 
                {'': '47', '교과목': '성격심리학', 'tel': '062-530-2650', '교과구분': '전선', '교과코드': 'PSY2006', '학점': '3.0', '강의실': '사회174', '개설학과': '심리학과', '강의타입': '일반과목'}, 
                {'': '48', '교과목': '조직심리학', 'tel': '062-530-2650', '교과구분': '전선', '교과코드': 'PSY3008', '학점': '3.0', '강의실': '사회177', '개설학과': '심리학과', '강의타입': '일반과목'}, 
                {'': '49', '교과목': '이상심리학', 'tel': '062-530-2650', '교과구분': '전선', '교과코드': 'PSY2003', '학점': '3.0', '강의실': '사회174', '개설학과': '심리학과', '강의타입': '일반과목'}, 
                {'': '50', '교과목': '관광여가지리학', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR2026', '학점': '3.0', '강의실': '사회대별관14', '개설학과': '지리학과', '강의타입': '일반과목'}, 
                {'': '51', '교과목': '지역개발의이해', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR4055', '학점': '3.0', '강의실': '사회428', '개설학과': '지리학과', '강의타입': '일반과목'}, 
                {'': '52', '교과목': '문화역사지리학', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR4035', '학점': '3.0', '강의실': '사회대별관14', '개설학과': '지리학과', '강의타입': '일반과목'}, 
                {'': '53', '교과목': 'The Environment and Human Life(환경과 인간생활)', 'tel': '062-530-2680', '교과구분': '전선', '교과코드': 'GGR3039', '학점': '3.0', '강의실': '사회428', '개설학과': '지리학과', '강의타입': '일반과목'}, 
                {'': '54', '교과목': '분쟁의세계지리', 'tel': '062-530-2680', '교과구분': '교선', '교과코드': 'CLT0833', '학점': '3.0', '강의실': '이러닝', '개설학과': '지리학과', '강의타입': '이러닝과목'}, 
                {'': '55', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교307', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '56', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교308', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '57', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교309', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '58', '교과목': '광고및마케팅커뮤니케이션', 'tel': '061-659-7370', '교과구분': '전공', '교과코드': 'GBA0010', '학점': '3.0', '강의실': '교310', '개설학과': '글로벌경영학과', '강의타입': '일반과목'}, 
                {'': '59', '교과목': '소비자학', 'tel': '062-530-1320', '교과구분': '전선', '교과코드': 'HMM3006', '학점': '3.0', '강의실': '이러닝', '개설학과': '생활복지학과', '강의타입': '이러닝과목'}, 
                {'': '60', '교과목': '노인복지', 'tel': '062-530-1320', '교과구분': '전선', '교과코드': 'HMM4029', '학점': '3.0', '강의실': '이러닝', '개설학과': '생활복지학과', '강의타입': '이러닝과목'}, 
                {'': '61', '교과목': '영양사현장실습', 'tel': '062-530-1330', '교과구분': '전선', '교과코드': 'FDN4019', '학점': '2.0', '강의실': '현장실습', '개설학과': '식품영양과학부', '강의타입': '현장실습과목'}, 
                {'': '62', '교과목': '수산해양교육론', 'tel': '061-659-7190', '교과구분': '전필', '교과코드': 'MIT0003', '학점': '3.0', '강의실': '이학관506호', '개설학과': '수산해양산업관광레저융합학과', '강의타입': '일반과목'}, 
                {'': '63', '교과목': '수산해양학 및 실습', 'tel': '061-659-7190', '교과구분': '전필', '교과코드': 'MIT0007', '학점': '3.0', '강의실': '수산해양대학813호', '개설학과': '수산해양산업관광레저융합학과', '강의타입': '일반과목'}, 
                {'': '64', '교과목': '레저스포츠관광론', 'tel': '061-659-7190', '교과구분': '전필', '교과코드': 'MIT0008', '학점': '3.0', '강의실': '이학관506호', '개설학과': '수산해양산업관광레저융합학과', '강의타입': '일반과목'}, 
                {'': '65', '교과목': '의학통계학', 'tel': '062-530-4191', '교과구분': '전선', '교과코드': 'MED4092', '학점': '3.0', '강의실': '진리관102', '개설학과': '의예과', '강의타입': '일반과목'}, 
                {'': '66', '교과목': '국어어문규범의이해', 'tel': '062-530-3130', '교과구분': '전필', '교과코드': 'KLL4024', '학점': '3.0', '강의실': '인1-108', '개설학과': '국어국문학과', '강의타입': '일반과목'}, 
                {'': '67', '교과목': '한국고전문학개론', 'tel': '062-530-3131', '교과구분': '전선', '교과코드': 'KLL1002', '학점': '3.0', '강의실': '인1-206', '개설학과': '국어국문학과', '강의타입': '일반과목'}, 
                {'': '68', '교과목': '한문', 'tel': '062-530-3132', '교과구분': '교선', '교과코드': 'CLT0002', '학점': '3.0', '강의실': '인1-206', '개설학과': '국어국문학과', '강의타입': '일반과목'}, 
                {'': '69', '교과목': '한국인의삶과문학', 'tel': '062-530-3133', '교과구분': '교선', '교과코드': 'CLT0829', '학점': '3.0', '강의실': '인1-108', '개설학과': '국어국문학과', '강의타입': '일반과목'}, 
                {'': '70', '교과목': '말하기의전략', 'tel': '062-530-3134', '교과구분': '교선', '교과코드': 'CLT0887', '학점': '3.0', '강의실': '인1-209', '개설학과': '국어국문학과', '강의타입': '일반과목'}, 
                {'': '71', '교과목': '서양의역사와문화', 'tel': '062-530-3240', '교과구분': '교선', '교과코드': 'CLT0836', '학점': '3.0', '강의실': '인3-301', '개설학과': '사학과', '강의타입': '일반과목'}, 
                {'': '72', '교과목': '문화유산의이해', 'tel': '062-530-3240', '교과구분': '전선', '교과코드': 'HIS1001', '학점': '3.0', '강의실': '인3-301', '개설학과': '사학과', '강의타입': '일반과목'}, 
                {'': '73', '교과목': '논리학', 'tel': '062-530-3220', '교과구분': '교선', '교과코드': 'CLT0591', '학점': '3.0', '강의실': '인1-106', '개설학과': '철학과', '강의타입': '일반과목'}, 
                {'': '74', '교과목': '호남의역사와문화', 'tel': '062-530-3240', '교과구분': '교선', '교과코드': 'CLT0566', '학점': '3.0', '강의실': '이러닝', '개설학과': '사학과', '강의타입': '이러닝과목'}, 
                {'': '75', '교과목': '동양고대사', 'tel': '062-530-3240', '교과구분': '전선', '교과코드': 'HIS2002', '학점': '3.0', '강의실': '이러닝', '개설학과': '사학과', '강의타입': '이러닝과목'}, 
                {'': '76', '교과목': '철학과 삶', 'tel': '062-530-3220', '교과구분': '교선', '교과코드': 'CLT0041', '학점': '3.0', '강의실': '이러닝', '개설학과': '철학과', '강의타입': '이러닝과목'}, 
                {'': '77', '교과목': '생명윤리', 'tel': '062-530-3220', '교과구분': '교선', '교과코드': 'CLT0863', '학점': '3.0', '강의실': '인3-306', '개설학과': '철학과', '강의타입': '일반과목'}, 
                {'': '78', '교과목': '긍정적학습동기유발전략세미나', 'tel': '062-530-2340', '교과구분': '전공', '교과코드': 'GR24575', '학점': '3.0', '강의실': '교육304', '개설학과': '교육학과', '강의타입': '일반과목'}, 
                {'': '79', '교과목': '일반물리1', 'tel': '062-530-3351', '교과구분': '교선', '교과코드': 'CLT0095', '학점': '3.0', '강의실': '자3-301', '개설학과': '물리학과', '강의타입': '일반과목'}, 
                {'': '80', '교과목': '광전자현장실습1', 'tel': '062-530-3351', '교과구분': '전선', '교과코드': 'PHY4018', '학점': '3.0', '강의실': '현장실습', '개설학과': '물리학과', '강의타입': '현장실습과목'}, 
                {'': '81', '교과목': '36.5도의물리학', 'tel': '062-530-3351', '교과구분': '교선', '교과코드': 'CLT0820', '학점': '3.0', '강의실': '이러닝', '개설학과': '물리학과', '강의타입': '이러닝과목'}, 
                {'': '82', '교과목': '일반물리2', 'tel': '062-530-3351', '교과구분': '교선', '교과코드': 'CLT0096', '학점': '3.0', '강의실': '이러닝', '개설학과': '물리학과', '강의타입': '이러닝과목'}, 
                {'': '83', '교과목': '일반생물2', 'tel': '062-530-3390', '교과구분': '교선', '교과코드': 'CLT0098', '학점': '3.0', '강의실': '자3-306', '개설학과': '생물학과', '강의타입': '일반과목'}, 
                {'': '84', '교과목': '수학1', 'tel': '062-530-3330', '교과구분': '교선', '교과코드': 'CLT0082', '학점': '3.0', '강의실': '자3-202', '개설학과': '수학과', '강의타입': '일반과목'}, 
                {'': '85', '교과목': '수학1', 'tel': '062-530-3330', '교과구분': '교선', '교과코드': 'CLT0082', '학점': '3.0', '강의실': '자3-201', '개설학과': '수학과', '강의타입': '일반과목'}, 
                {'': '86', '교과목': '수학2', 'tel': '062-530-3330', '교과구분': '교선', '교과코드': 'CLT0083', '학점': '3.0', '강의실': '자3-202', '개설학과': '수학과', '강의타입': '일반과목'}, 
                {'': '87', '교과목': '기초통계학', 'tel': '062-530-3440', '교과구분': '교필', '교과코드': 'CLT0933', '학점': '3.0', '강의실': '자3-205', '개설학과': '통계학과', '강의타입': '일반과목'}, 
                {'': '88', '교과목': '일반화학2', 'tel': '062-530-3370', '교과구분': '교선', '교과코드': 'CLT0085', '학점': '3.0', '강의실': '자3-101', '개설학과': '화학과', '강의타입': '일반과목'}, 
                {'': '89', '교과목': '5·18민주화운동과 세계의 항쟁', 'tel': '062-530-3916', '교과구분': '교선', '교과코드': 'CLT0952', '학점': '3.0', '강의실': '평생301', '개설학과': '518연구소', '강의타입': '일반과목'}, 
                {'': '90', '교과목': '성찰과소통을위한글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0888', '학점': '3.0', '강의실': '진리관103', '개설학과': '교육혁신본부', '강의타입': '일반과목'}, 
                {'': '91', '교과목': '성찰과소통을위한글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0888', '학점': '3.0', '강의실': '진리관103', '개설학과': '교육혁신본부', '강의타입': '일반과목'}, 
                {'': '92', '교과목': '과학기술글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0894', '학점': '3.0', '강의실': '진리관302', '개설학과': '교육혁신본부', '강의타입': '일반과목'}, 
                {'': '93', '교과목': '인문사회글쓰기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0893', '학점': '3.0', '강의실': '진리관202', '개설학과': '교육혁신본부', '강의타입': '일반과목'}, 
                {'': '94', '교과목': '효과적인말하기', 'tel': '062-530-0918', '교과구분': '교선', '교과코드': 'CLT0890', '학점': '3.0', '강의실': '진리관301', '개설학과': '교육혁신본부', '강의타입': '일반과목'}, 
                {'': '95', '교과목': '예술감성과미학', 'tel': '062-530-0355', '교과구분': '교선', '교과코드': 'CLT0828', '학점': '3.0', '강의실': '이러닝', '개설학과': '교육혁신본부', '강의타입': '이러닝과목'}, 
                {'': '96', '교과목': '국외현장실습1', 'tel': '062-530-1275', '교과구분': '일선', '교과코드': 'UNV5023', '학점': '2.0', '강의실': '국외현장실습', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '97', '교과목': '국외현장실습4', 'tel': '062-530-1275', '교과구분': '일선', '교과코드': 'UNV5010', '학점': '5.0', '강의실': '국외현장실습', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '98', '교과목': '국외현장실습6', 'tel': '062-530-1275', '교과구분': '일선', '교과코드': 'UNV5061', '학점': '1.0', '강의실': '국외현장실습', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '99', '교과목': '국외언어연수1', 'tel': '062-530-1275', '교과구분': '교양', '교과코드': 'CLT0875', '학점': '3.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '100', '교과목': '국외언어연수2', 'tel': '062-530-1275', '교과구분': '교선', '교과코드': 'CLT0587', '학점': '5.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '101', '교과목': '국외언어연수4', 'tel': '062-530-1275', '교과구분': '교선', '교과코드': 'CLT0783', '학점': '1.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '102', '교과목': '국외언어연수5', 'tel': '062-530-1275', '교과구분': '교선', '교과코드': 'CLT0877', '학점': '2.0', '강의실': '국외언어연수', '개설학과': '국제협력과', '강의타입': '현장실습과목'}, 
                {'': '103', '교과목': '여수바다여행놀이', 'tel': '061-659-7026', '교과구분': '교선', '교과코드': 'CLT0954', '학점': '3.0', '강의실': '교407', '개설학과': '글로벌교육원', '강의타입': '일반과목'}, 
                {'': '104', '교과목': '생활영어1', 'tel': '062-530-3635', '교과구분': '교선', '교과코드': 'CLT0666', '학점': '3.0', '강의실': '본부지정', '개설학과': '언어교육원', '강의타입': '일반과목'}, 
                {'': '105', '교과목': '생활한국어1', 'tel': '062-530-3648', '교과구분': '교선', '교과코드': 'CLT0965', '학점': '3.0', '강의실': '진리관201', '개설학과': '언어교육원', '강의타입': '일반과목'}, 
                {'': '106', '교과목': '생활한국어2', 'tel': '062-530-3648', '교과구분': '교선', '교과코드': 'CLT0966', '학점': '3.0', '강의실': '진리관304', '개설학과': '언어교육원', '강의타입': '일반과목'}, 
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

        st.dataframe(df, use_container_width=True)

        # tmp_df = df[df['분야'].isin(select_multi_species)]
        # # 선택한 종들의 결과표를 나타냅니다.  
        # st.table(tmp_df)    

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
    if st.button("과목추천"):
        page_subject_recommendation
    elif st.button("전남대학교 스케쥴"):
        page_university_schedule
    elif st.button("공지사항"):
        page_announcements
    # selected_page = st.sidebar.radio("페이지 선택", list(pages.keys()))


if __name__ == "__main__":
    main()

