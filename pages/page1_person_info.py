import datetime
import streamlit as st

st.title("1단계: 기본 정보 입력")

# 사람이름 입력
if 'name' not in st.session_state:
    st.session_state['name'] = ""
if 'date' not in st.session_state:
    st.session_state['date'] = str(datetime.datetime.now().date())
if 'day_rating' not in st.session_state:
    st.session_state['day_rating'] = 5
if 'weather' not in st.session_state:
    st.session_state['weather'] = "맑음"

name = st.text_input(value=st.session_state['name'],label="이름을 입력하세요")
# 날짜 입력
date = st.date_input("오늘 날짜를 입력하세요", value=datetime.datetime.strptime(st.session_state['date'], '%Y-%m-%d').date())
# 오늘 하루 점수
day_rating = st.slider("오늘 하루 점수 (1-10)", 1, 10,  value=st.session_state['day_rating'])

# 날씨 선택
weather_options = ["맑음", "흐림", "비", "눈", "바람", "기타"]
selected_weather = st.selectbox("오늘 날씨는?", ["맑음", "흐림", "비", "눈", "바람", "기타"], weather_options.index(st.session_state['weather']))

routin = st.Page("pages/page2_routine.py", title="routin", icon=":material/bug_report:")

col1, col2, col3 = st.columns([1, 5, 1])

with col3:

    if st.button("다음"):
        st.session_state['name'] = name
        st.session_state['date'] = str(date)
        st.session_state['day_rating'] = day_rating
        st.session_state['weather'] = selected_weather
        st.switch_page(routin)
