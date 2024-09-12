import streamlit as st

st.title("3단계: 소셜 활동 입력")

if 'social' not in st.session_state:
    st.session_state['social'] = {
        "만난 사람": "가족",
        "활동 유형": "경조사"
    }

# 만난 사람 및 활동 유형 입력
st.write("개인적으로 만난 사람을 체크해줘!")
met_with_options = ["가족", "친구", "애인", "직장동료", "대외활동 멤버", "지인", "기타"]
met_with = st.selectbox("만난 사람", ["가족", "친구", "애인", "직장동료", "대외활동 멤버", "지인", "기타"], met_with_options.index(st.session_state['social'].get('만난 사람')))
st.text("")

activity_type_options = ["경조사", "액티비티", "근황토크", "식사 및 술", "온라인", "기타"]
activity_type = st.selectbox("활동 유형", ["경조사", "액티비티", "근황토크", "식사 및 술", "온라인", "기타"], activity_type_options.index(st.session_state['social'].get('활동 유형')))

col1, col2, col3 = st.columns([1, 5, 1])

with col1:
    if st.button("이전"):
        st.session_state['social'] = {
            "만난 사람": met_with,
            "활동 유형": activity_type
        }
        st.switch_page("pages/page2_routine.py")
with col3:
    if st.button("다음"):
        st.session_state['social'] = {
            "만난 사람": met_with,
            "활동 유형": activity_type
        }
        st.switch_page("pages/page4_work.py")