from pdutils.pandasutils import split_date_column
import pandas as pd
import os

TEST_DIR = os.path.dirname(__file__)


def test_split_date_column():
    df = pd.read_csv(os.path.join(TEST_DIR, "date_data.csv"))
    split_df = split_date_column(df, "Date")
    columns = list(split_df.columns)
    assert columns == ["Name", "Color", "Date", "month", "day", "year"]