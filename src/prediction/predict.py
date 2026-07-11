from src.prediction.load_objects import load_objects
from src.prediction.preprocess_input import preprocess_input


def predict_diabetes(
    gender,
    age,
    hypertension,
    heart_disease,
    smoking_history,
    bmi,
    hba1c_level,
    blood_glucose_level
):

    model, scaler, gender_encoder, smoking_encoder = load_objects()

    input_data = preprocess_input(
        gender,
        age,
        hypertension,
        heart_disease,
        smoking_history,
        bmi,
        hba1c_level,
        blood_glucose_level,
        scaler,
        gender_encoder,
        smoking_encoder
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    return prediction, probability