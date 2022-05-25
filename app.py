import streamlit as st
from utils import load_df

TEAM_CHOICES = ["mavericks", "celtics", "warriors", "heat"]

st.title("2022 NBA Playoffs Statistics")
team_select = st.multiselect("Select team", TEAM_CHOICES)
grouped_by = st.radio("Group data by", ["Opponent", "Venue"])

for team in team_select:
    df = load_df(team, '2021-2022', 'playoffs')
    st.write(df.groupby(grouped_by).mean())
