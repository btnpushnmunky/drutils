import pandas as pd


def split_date_column(df, date_column):
    """
    Split the `date_column` of DataFrame `df` into month, day and year columns.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame containing a date column to be split.
    date_column: str
        Name of the column to split

    Returns
    -------
    df: pd.DataFrame
        Original DataFrame with month, day and year columns added.
    """
    if df[date_column].dtypes is not "datetime64[ns]":
        df[date_column] = pd.to_datetime(df[date_column])
    else:
        pass
    df.loc[:, "month"] = df["Date"].dt.month
    df.loc[:, "day"] = df["Date"].dt.day
    df.loc[:, "year"] = df["Date"].dt.year
    return df