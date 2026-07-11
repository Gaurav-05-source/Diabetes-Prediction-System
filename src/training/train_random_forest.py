from sklearn.ensemble import RandomForestClassifier


def train_random_forest(X_train, y_train):
    """
    Train Random Forest model.
    """

    model = RandomForestClassifier(
        n_estimators=100,
        criterion="gini",
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    print("\n========== RANDOM FOREST ==========")
    print("Model trained successfully.")

    return model