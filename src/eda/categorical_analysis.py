import pandas as pd


def analyze_categorical_features(df: pd.DataFrame):
    """
    Analyze categorical features.
    """

    print("\n========== CATEGORICAL FEATURE ANALYSIS ==========")

    categorical_columns = [
        "gender",
        "smoking_history"
    ]

    for column in categorical_columns:

        print(f"\n{column.upper()}")

        print(df[column].value_counts())

        print("\nPercentage")

        percentage = round(
            df[column].value_counts(normalize=True) * 100,
            2
        )

        print(percentage)