import joblib


def load_objects():

    model = joblib.load("models/random_forest_model.pkl")

    scaler = joblib.load("models/scaler.pkl")

    gender_encoder = joblib.load("models/gender_encoder.pkl")

    smoking_encoder = joblib.load("models/smoking_encoder.pkl")

    print("\n========== OBJECTS LOADED ==========")
    print("Model, scaler and encoders loaded successfully.")

    return model, scaler, gender_encoder, smoking_encoder