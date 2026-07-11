import pandas as pd


def analyze_numerical_features(df: pd.DataFrame):
    """
    Analyze numerical features.
    """

    print("\n========== NUMERICAL FEATURE ANALYSIS ==========")

    numerical_columns = [
        "age",
        "bmi",
        "HbA1c_level",
        "blood_glucose_level"
    ]

    for column in numerical_columns:

        print(f"\n{column.upper()}")

        print(df[column].describe())