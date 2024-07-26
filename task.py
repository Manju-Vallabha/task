import streamlit as st
import pandas as pd
import lightgbm as lgb
import time

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('updated_skills_courses.csv')

data = load_data()

data['skill_list'] = data['Skills'].apply(lambda x: x.split('|'))

st.title('Job Portal: Candidate Ranking System')
st.markdown("### Search for candidates based on skills")

st.write("Skills in the database be like - 'Python,  Java,  C++,  JavaScript")
st.write("After entering the skill hit enter")

search_skill = st.text_input('Enter the skill to search for:', '')

if search_skill:

    bar = st.progress(0)
    time.sleep(1)
    bar.progress(50)
    time.sleep(2)
    bar.progress(100)
    
    def count_courses_with_exact_skill(courses, search_skill):
        return sum(search_skill.lower() in course.lower().split() for course in courses.split('|'))

    data['num_courses_with_skill'] = data.apply(lambda row: count_courses_with_exact_skill(row['Courses'], search_skill), axis=1)

    data['has_skill'] = data['skill_list'].apply(lambda x: search_skill in x)
    filtered_data = data[data['has_skill']]

    if not filtered_data.empty:
        # Prepare data for LightGBM
        X = filtered_data[['num_courses_with_skill', 'Experience']]
        y = filtered_data['num_courses_with_skill']  
        group = [len(filtered_data)]  

        dtrain_lgb = lgb.Dataset(X, label=y, group=group)
        params_lgb = {
            'objective': 'lambdarank',
            'eval_metric': 'ndcg'
        }
        model_lgb = lgb.train(params_lgb, dtrain_lgb, num_boost_round=10)
        preds_lgb = model_lgb.predict(X)

        filtered_data['predicted_rank_lgb'] = preds_lgb

        ranked_candidates_lgb = filtered_data.sort_values(by='predicted_rank_lgb', ascending=False).head(5)

        st.markdown("### Top 5 Candidates According to LambdaMART")
        for _, row in ranked_candidates_lgb.iterrows():
            experience_years = str(row['Experience'])  # Ensure experience is converted to string
            with st.expander(f"Candidate: {row['Name']}"):
                st.write(f"**Courses with Skill:** {row['num_courses_with_skill']}")
                st.write(f"**Experience:** {experience_years} years")
    else:
        st.write("No candidates found with the specified skill.")
else:
    st.write("Please enter a skill to search.")
