import pandas as pd


def load_dataset():
    """
    Load the diabetes prediction dataset.
    """

    file_path = "data/raw/diabetes_prediction_dataset.csv"

    df = pd.read_csv(file_path)

    print("\n========== DATA LOADED ==========")
    print(f"Dataset Shape : {df.shape}")

    return df