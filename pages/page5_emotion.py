import streamlit as st

st.title("5단계: 감정 입력")

# 좋았던 일, 아쉬웠던 일 입력
good = st.text_area("오늘 좋았던 점", "오늘 좋았던 점을 작성하세요.")
bad = st.text_area("오늘 아쉬웠던 점", "오늘 아쉬웠던 점을 작성하세요.")

if st.button("제출"):
    st.session_state['emotion'] = {
        "좋았던 점": good,
        "아쉬웠던 점": bad
    }
    
    # 모든 세션 상태를 보여줌
    st.write("전체 일기 정보:")
    st.json(st.session_state)