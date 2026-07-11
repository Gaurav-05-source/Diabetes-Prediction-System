import pandas as pd


def preprocess_input(
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
):

    gender = gender_encoder.transform([gender])[0]

    smoking_history = smoking_encoder.transform([smoking_history])[0]

    input_df = pd.DataFrame({

        "gender": [gender],

        "age": [age],

        "hypertension": [hypertension],

        "heart_disease": [heart_disease],

        "smoking_history": [smoking_history],

        "bmi": [bmi],

        "HbA1c_level": [hba1c_level],

        "blood_glucose_level": [blood_glucose_level]

    })

    numerical_columns = [
        "age",
        "bmi",
        "HbA1c_level",
        "blood_glucose_level"
    ]

    input_df[numerical_columns] = scaler.transform(
        input_df[numerical_columns]
    )

    return input_df