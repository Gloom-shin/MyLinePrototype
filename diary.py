import streamlit as st
import json

st.title('일기 Form')

# Date input
date = st.date_input("오늘 날짜", value=None)

# Day rating input
day_rating = st.slider("하루 점수(1-10)", min_value=1, max_value=10, value=6)

# Weather input
weather = st.selectbox("날씨", ["맑음", "흐림", "비", "눈", "바람", "기타"], index=1)

# Routine checkboxes
st.write("루틴:")
health = st.checkbox("Health", value=False)
stretching = st.checkbox("Stretching", value=True)
skincare = st.checkbox("Skincare", value=True)
learning = st.checkbox("Learning", value=True)
vitamins = st.checkbox("Vitamins", value=False)

routines = {
    "health": health,
    "stretching": stretching,
    "skincare": skincare,
    "learning": learning,
    "vitamins": vitamins
}

# Social activities input
st.write("Social 활동:")
met_with = st.text_input("만난 사람", "없음")
activity_type = st.text_input("활동 유형", "없음")


social_activities = {
    "met_with": met_with,
    "activity_type": activity_type
}

# Work or experience input
st.write("Work or Experience:")
category = st.selectbox("Category", ["Work", "Experience", "Study", "Other"], index=0)
subcategory = st.text_input("Subcategory", "Job Preparation")
details = st.text_area("Details", 
    "Today, I focused on interview preparation. I spent a lot of time organizing expected questions and creating my own answers.")

work_or_experience = {
    "category": category,
    "subcategory": subcategory,
    "details": details
}

# Emotions input
st.write("Emotions:")
HowAreYouToday = st.text_input("How are you feeling today?", "I feel better now that the rain has stopped.")
good = st.text_area("What was good today?", 
    "While preparing, I felt like I was growing more. The more I prepare, the more confident I feel.")
bad = st.text_area("What was bad today?", 
    "But there's still a lingering fear of 'what if I fail again?' I need to ensure this doesn't hinder my preparation.")

emotions = {
    "HowAreYouToday": HowAreYouToday,
    "good": good,
    "bad": bad
}

# Future plans input
future_plan = st.text_area("Future Plan", 
    "Tomorrow, I plan to finalize my interview materials and practice answering the expected questions.")

# When the user submits the form, display the result
if st.button("Submit"):
    journal_entry = {
        "date": str(date),
        "day_rating": day_rating,
        "weather": weather,
        "routines": routines,
        "social_activities": social_activities,
        "work_or_experience": work_or_experience,
        "emotions": emotions,
        "future_plan": future_plan
    }

    st.write("Journal Entry:")
    st.json(journal_entry)

    # Convert to JSON and display
    json_result = json.dumps(journal_entry, indent=4, ensure_ascii=False)
    st.code(json_result, language="json")