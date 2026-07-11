import pandas as pd


def analyze_target(df: pd.DataFrame):
    """
    Analyze the target variable (diabetes).
    """

    print("\n========== TARGET VARIABLE ANALYSIS ==========")

    target_counts = df["diabetes"].value_counts()

    print("\nDiabetes Distribution:")

    print(target_counts)

    print("\nPercentage Distribution:")

    percentage = round(
        df["diabetes"].value_counts(normalize=True) * 100,
        2
    )

    print(percentage)