import streamlit as st

st.title("2단계: 루틴 입력")

if 'routines' not in st.session_state:
    st.session_state['routines'] = {}

# 루틴 체크박스
health = st.checkbox("운동" , value=st.session_state['routines'].get('운동', False))
stretching = st.checkbox("스트레칭" , value=st.session_state['routines'].get('스트레칭', False))
skincare = st.checkbox("스킨케어" , value=st.session_state['routines'].get('스킨케어', False))
learning = st.checkbox("학습" , value=st.session_state['routines'].get('학습', False))
vitamins = st.checkbox("비타민 섭취" , value=st.session_state['routines'].get('비타민 섭취', False))

routines = {
    "운동": health,
    "스트레칭": stretching,
    "스킨케어": skincare,
    "학습": learning,
    "비타민 섭취": vitamins
}
col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    if st.button("이전"):
        st.session_state['routines'] = routines
        st.session_state.page = "page1_person_info"
        st.switch_page("pages/page1_person_info.py")

with col3:
    if st.button("다음"):
        st.session_state['routines'] = routines
        st.session_state.page = "page1_person_info"
        st.switch_page("pages/page3_social.py")