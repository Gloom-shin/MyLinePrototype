import streamlit as st

st.set_page_config(page_title="다섯 단계 일기 작성", page_icon="📄")

st.title("다섯 단계 일기 작성")
st.write("왼쪽의 사이드바에서 단계를 선택하여 일기를 작성하세요.")

# 페이지 초기 상태 설정
if 'page' not in st.session_state:
    st.session_state.page = "page1_person_info"


info = st.Page( "pages/page1_person_info.py", title="info", icon=":material/dashboard:")
routin = st.Page("pages/page2_routine.py", title="routin", icon=":material/bug_report:")
social = st.Page("pages/page3_social.py", title="social", icon=":material/bug_report:")
work = st.Page("pages/page4_work.py", title="work", icon=":material/bug_report:")
emotion = st.Page("pages/page5_emotion.py", title="emotion", icon=":material/bug_report:")


pg = st.navigation(
    {
        "diary": [info, routin, social, work, emotion],
    }
)

pg.run()
