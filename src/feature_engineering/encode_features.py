from sklearn.preprocessing import LabelEncoder


def encode_features(df):

    df = df.copy()

    gender_encoder = LabelEncoder()
    smoking_encoder = LabelEncoder()

    df["gender"] = gender_encoder.fit_transform(df["gender"])
    df["smoking_history"] = smoking_encoder.fit_transform(df["smoking_history"])

    print("\n========== FEATURE ENCODING ==========")
    print("Categorical features encoded successfully.")

    return df, gender_encoder, smoking_encoder