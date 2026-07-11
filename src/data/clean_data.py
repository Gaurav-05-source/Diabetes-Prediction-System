import pandas as pd


def clean_dataset(df: pd.DataFrame):
    """
    Clean the diabetes dataset.
    """

    print("\n========== DATA CLEANING ==========")

    print(f"\nInitial Shape : {df.shape}")

    duplicate_rows = df.duplicated().sum()

    print(f"Duplicate Rows : {duplicate_rows}")

    df = df.drop_duplicates()

    print(f"Final Shape : {df.shape}")

    print(f"Rows Removed : {duplicate_rows}")

    return df