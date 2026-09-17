"""Application entry point for Cricbuzz LiveStats."""

import streamlit as st

from utils.db_connection import execute_query, initialize_database


st.set_page_config(
    page_title="Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide",
)

initialize_database()

st.title("Cricbuzz LiveStats")
st.subheader("Real-Time Cricket Insights & SQL-Based Analytics")
st.write(
    "Use the navigation links below to explore live cricket data, player "
    "performance, SQL analytics, and player records."
)

st.divider()

st.header("Explore the Project")
nav_columns = st.columns(5)
page_links = [
    ("Home", "pages/1_Home.py"),
    ("Live Matches", "pages/2_Live_Matches.py"),
    ("Player Stats", "pages/3_Player_Stats.py"),
    ("SQL Analytics", "pages/4_SQL_Analytics.py"),
    ("CRUD Operations", "pages/5_CRUD_Operations.py"),
]
for column, (label, page_path) in zip(nav_columns, page_links):
    with column:
        st.page_link(page_path, label=label, icon="🏏")

st.header("Database Snapshot")
counts = execute_query(
    """
    SELECT
        (SELECT COUNT(*) FROM teams) AS teams,
        (SELECT COUNT(*) FROM players) AS players,
        (SELECT COUNT(*) FROM matches) AS matches,
        (SELECT COUNT(*) FROM batting_stats) AS batting_records,
        (SELECT COUNT(*) FROM bowling_stats) AS bowling_records
    """
)[0]

metric_columns = st.columns(5)
for column, label in zip(
    metric_columns,
    ["Teams", "Players", "Matches", "Batting records", "Bowling records"],
):
    key = label.lower().replace(" ", "_")
    column.metric(label, counts[key])
