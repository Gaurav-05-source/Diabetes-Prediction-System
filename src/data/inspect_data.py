import pandas as pd


def inspect_dataset(df: pd.DataFrame):
    """
    Display basic information about the dataset.
    """

    print("\n========== DATASET INSPECTION ==========")

    print(f"\nShape : {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nStatistical Summary:")
    print(df.describe())