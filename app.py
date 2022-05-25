import streamlit as st
import numpy as np
import pandas as pd

TEAM_CHOICES = ["mavericks", "celtics", "warriors", "heat"]

st.title("2022 NBA Playoffs Statistics")
st.multiselect("Select team", TEAM_CHOICES)
