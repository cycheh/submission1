import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title(":wave: About this App")

st.write("This School Navigator Streamlit App integrates key information within a user-friendly platform to simplify and facilitate the school selection process for parents and students.")

st.write("The app is able to answer queries on subjects and CCAs offered, location and nearby public transport options pertaining to the specific schools that users are considering :heart:")

with st.expander(":earth_asia: Scope of Project"):
    st.write("This app aims to help parents and their school-going children with the process of choosing a MOE school (including primary, secondary and pre-university), by consolidating a variety of relevant information such as school location; nearest public transportation; subjects offered by the school as well as co-curricular activities offered by the school.")
    st.write("Users can use natural language to interact with the platform and make queries. In response, the platform then uses LLM + RAG methodology to retrieve the relevant data from the consolidated database.")
    st.write("The coverage of the schools in the database includes all MOE schools across Singapore, encompassing key decision points such as subjects and CCAs offered, location and nearby public transport options.")

with st.expander(":rocket: Objectives"):
    st.write("The objective of this project is to provide a unified platform that consolidates important data for exploring MOE schools in one place.")
    st.write("This eliminates the need for parents and students to navigate multiple sources to gather essential information—such as school locations, transport accessibility, subject offerings, and co-curricular activities—often leading to decisions made without considering all major aspects, or based on incomplete data.")
    st.write("In addition to the significant time savings, this simplifies the journey from something that could be fragmented and overwhelming to an enjoyable and interactive experience with the app.")

with st.expander(":rainbow: Features"):
    st.write("1. The app provides insights into general information and location of schools, specifically contact details, postal code, address and nearby MRT stations.")
    st.write("2. The app is able to compare subject offerings across schools, e.g. 'Does School A or School B offer Geography as a subject?' due to its access to the database of subjects offered by each school.")
    st.write("3. The app can tell users what CCAs are offered in each school, e.g. sports, arts, music societies etc., due to its access to the database of all schools' CCAs.")

with st.expander(":star: Data Sources"):
    st.write("Data is consolidated from 3 MOE datasets on data.gov.sg, namely:")
    st.write("1. General information of schools --> link: https://data.gov.sg/datasets?topics=education&resultId=d_688b934f82c1059ed0a6993d2a829089&page=1")
    st.write("2. Subjects offered by schools --> link: https://data.gov.sg/datasets?topics=education&resultId=d_f1d144e423570c9d84dbc5102c2e664d&page=1")
    st.write("3. CCAs offered by schools --> link: https://data.gov.sg/datasets?topics=education&resultId=d_9aba12b5527843afb0b2e8e4ed6ac6bd&page=1")
