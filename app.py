from hoops_ref import HoopsRefClient
import streamlit as st
import matplotlib.pyplot as plt

cli = HoopsRefClient()

st.title("NBA Team Per Game Statistics")
st.subheader("Exploratory Data Analysis for Teams' Season Averages")
st.markdown("""
            Data source: [basketball-reference.com](https://www.basketball-reference.com)
            Author: Czar Yobero (open to work)
            Email: cyobero@gmail.com
""")

season = st.selectbox("Select season", options=[
                      year for year in reversed(range(1995, 2023))])
opponent = st.radio("Select offense or defense",
                    options=['Offense', 'Defense'])

df = cli.per_game_team(season, bool(opponent == 'Defense'))
df['Team'] = df['Team'].apply(lambda x: x.strip('*'))

teams = st.multiselect("Select team(s)", options=df.Team.unique(),
                       default=df.Team.unique())
col = st.selectbox("Select statistic", options=df.columns[4:])
asc = st.radio("Sort order", options=["Ascending", "Descending"])
df = df[['Team', col]][df.Team.isin(teams)].sort_values(
    by=col, ascending=bool(asc == "Ascending"))

fig, ax = plt.subplots()
ax.scatter(df[col], df.Team)
ax.title.set_text(f'{season} {opponent} {col} leaders')
ax.set_xlabel(f'{col}')
ax.grid()
st.pyplot(fig)
