from sklearn.preprocessing import StandardScaler


def scale_features(X_train, X_test):

    scaler = StandardScaler()

    numerical_columns = [
        "age",
        "bmi",
        "HbA1c_level",
        "blood_glucose_level"
    ]

    X_train = X_train.copy()
    X_test = X_test.copy()

    X_train[numerical_columns] = scaler.fit_transform(
        X_train[numerical_columns]
    )

    X_test[numerical_columns] = scaler.transform(
        X_test[numerical_columns]
    )

    print("\n========== FEATURE SCALING ==========")
    print("Numerical features scaled successfully.")

    return X_train, X_test, scaler