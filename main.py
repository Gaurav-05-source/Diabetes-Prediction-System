from src.data.load_data import load_dataset
from src.data.inspect_data import inspect_dataset
from src.data.clean_data import clean_dataset

from src.eda.target_analysis import analyze_target
from src.eda.categorical_analysis import analyze_categorical_features
from src.eda.numerical_analysis import analyze_numerical_features

from src.feature_engineering.encode_features import encode_features
from src.feature_engineering.split_features import split_features
from src.feature_engineering.split_data import split_data
from src.feature_engineering.scale_features import scale_features

from src.training.train_logistic import train_logistic
from src.training.train_decision_tree import train_decision_tree
from src.training.train_random_forest import train_random_forest
from src.training.evaluate_model import evaluate_model
from src.training.compare_models import compare_models

from src.training.save_model import save_model


def main():

    # ===============================
    # Data Loading
    # ===============================
    df = load_dataset()

    # ===============================
    # Data Inspection
    # ===============================
    inspect_dataset(df)

    # ===============================
    # Data Cleaning
    # ===============================
    df = clean_dataset(df)

    # ===============================
    # Exploratory Data Analysis
    # ===============================
    analyze_target(df)
    analyze_categorical_features(df)
    analyze_numerical_features(df)

    # ===============================
    # Feature Engineering
    # ===============================
    df, gender_encoder, smoking_encoder = encode_features(df)

    X, y = split_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train, X_test, scaler = scale_features(X_train, X_test)

    # ===============================
    # Logistic Regression
    # ===============================
    logistic_model = train_logistic(X_train, y_train)

    logistic_result = evaluate_model(
        logistic_model,
        X_test,
        y_test
    )

    # ===============================
    # Decision Tree
    # ===============================
    decision_tree_model = train_decision_tree(
        X_train,
        y_train
    )

    decision_result = evaluate_model(
        decision_tree_model,
        X_test,
        y_test
    )

    # ===============================
    # Random Forest
    # ===============================
    random_forest_model = train_random_forest(
        X_train,
        y_train
    )

    random_result = evaluate_model(
        random_forest_model,
        X_test,
        y_test
    )

    # ===============================
    # Compare Models
    # ===============================
    results = [
        {
            "Model": "Logistic Regression",
            **logistic_result
        },
        {
            "Model": "Decision Tree",
            **decision_result
        },
        {
            "Model": "Random Forest",
            **random_result
        }
    ]

    compare_models(results)

    # ===============================
# Save Models
# ===============================

    save_model(logistic_model, "logistic_model.pkl")

    save_model(decision_tree_model, "decision_tree_model.pkl")

    save_model(random_forest_model, "random_forest_model.pkl")

    save_model(scaler, "scaler.pkl")

    save_model(smoking_encoder, "smoking_encoder.pkl")

    save_model(gender_encoder, "gender_encoder.pkl")



if __name__ == "__main__":
    main()