import streamlit as st

# 카테고리 및 세부 내용 입력
st.title("오늘 어떤 경험(일)을 했어?")

if 'work' not in st.session_state:
    st.session_state['work'] = {
        "experience_type": "일(업무)",
        "feeling": "긍정적",
        "detail_type": "선택",
        "story": "",
        "insight": ""
    }

experience_type_options = ["일(업무)", "경험", "취미"]
# 1. 경험 선택
experience_type = st.radio("경험 유형", ["일(업무)", "경험", "취미"],experience_type_options.index(st.session_state['work']['experience_type']))

# 공백 추가
st.text("")

# 2. 해당 일에 대한 느낌
experience_feeling_options = ["긍정적", "부정적"]
experience_feeling = st.radio("해당 일은 어땠어?", ["긍정적", "부정적"], experience_feeling_options.index(st.session_state['work']['feeling']))

# 공백 추가
st.text("")

task_list = []
# 3. 구체적으로 어떤 일이야?
match experience_type:
    case "일(업무)":
        task_list = ["선택", "회사일", "취업 준비", "아르바이트, 프리랜서", "인턴", "봉사활동", "대외활동 및 공모전", "학교", "그외"]
    case "경험":
        task_list = ["선택", "여행간 경험", "실패한 경험", "새로운 경험", "사소한 경험", "소중한 경험", "도전적인 경험", "성장한 경험", "그외"]
    case "취미":
        task_list = ["선택", "영상 시청", "음악", "요리", "독서", "스포츠", "온라인 게임", "미술", "그외"]
 
specific_task = st.selectbox(
        "구체적으로 어떤 일이야?", 
        task_list,
        task_list.index(st.session_state['work']['detail_type'])
)



# 결과 출력
# st.write(f"경험: {experience_type}, 느낌: {experience_feeling}, 구체적인 일: {specific_task}")

question_label = "무슨일 있었는데?"

match experience_type:
    case "일(업무)":
        question_label = "무슨일 있었는데?"
    case "경험":
        question_label = "그 경험은 어땠어?"
    case "취미":
        question_label = "그 취미활동에 대해 리뷰해줘"

story = st.text_area(question_label, value=st.session_state['work']['story'])


if experience_feeling == "긍정적":
    insight = st.text_area("내가 얻은 구체적인 성과(요령, 인사이트)가 있어?", value=st.session_state['work']['insight'])
else:
    insight = st.text_area("어떻게 잘 해결될 수 있을 것 같아?", value=st.session_state['work']['insight'])


# 버튼을 2개의 컬럼으로 나눔
col1, col2, col3 = st.columns([1, 5, 1])
error_message = ""  # 에러 메시지 변수

with col1:
    if st.button("이전"):
        print(specific_task)
        if specific_task == "선택":
            error_message= "구체적인 일이 무엇이였는지 선택해주세요"
        else:
            st.session_state['work'] = {
                "experience_type": experience_type,
                "feeling": experience_feeling,
                "detail_type": specific_task,
                "story": story,
                "insight": insight
            }
            st.switch_page("pages/page3_social.py")

with col3:
    if st.button("다음"):
        print(specific_task)
        if specific_task == "선택":
            error_message= "구체적인 일이 무엇이였는지 선택해주세요"
        else:
            st.session_state['work'] = {
                "experience_type": experience_type,
                "feeling": experience_feeling,
                "detail_type": specific_task,
                "story": story,
                "insight": insight
            }
            st.switch_page("pages/page5_emotion.py")
if error_message:
    st.error(error_message)