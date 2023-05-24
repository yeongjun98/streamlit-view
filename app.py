import streamlit as st
import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    return data

# 웹 페이지 타이틀 설정
st.title("날씨 정보")

# 도시 선택
city = st.selectbox("도시를 선택하세요.", ["서울", "뉴욕", "런던"])

# 도시 선택 후 처리
if st.button("날씨 확인"):
    weather_data = get_weather(city)
    
    if weather_data["cod"] != "404":
        main_weather = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        temp = round(temp - 273.15, 2)  # 온도를 섭씨로 변환
        
        st.write(f"도시: {city}")
        st.write(f"날씨: {main_weather} - {description}")
        st.write(f"온도: {temp}°C")
    else:
        st.write("날씨 정보를 가져올 수 없습니다.")
