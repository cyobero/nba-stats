import numpy as np
import pandas as pd


def _clean(df=pd.DataFrame):
    """Cleans DataFrame by filtering and renaming some columns"""
    df["Venue"] = df["Unnamed: 5"].apply(lambda x: 'H' if x is np.nan else 'A')
    df = df[["Date", "Opponent", "Tm", "Opp", "Venue"]]
    return df


def load_df(team, year, season='regular_season'):
    """Loads cleaned data for given NBA team during a given year. Valid values for
    `season` are 'regular_season' (default) and 'playoffs'."""
    path = "./data/team/{team}/{year}/{season}.csv".format(team=team, year=year,
                                                           season=season)
    df = pd.read_csv(path, index_col="G")

    return _clean(df)
