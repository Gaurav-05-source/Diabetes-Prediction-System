def split_features(df):

    X = df.drop("diabetes", axis=1)

    y = df["diabetes"]

    print("\n========== FEATURE SELECTION ==========")
    print(f"Features Shape : {X.shape}")
    print(f"Target Shape   : {y.shape}")

    return X, y