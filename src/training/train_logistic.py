from sklearn.linear_model import LogisticRegression


def train_logistic(X_train, y_train):
    """
    Train Logistic Regression model.
    """

    model = LogisticRegression(
        random_state=42,
        max_iter=1000
    )

    model.fit(X_train, y_train)

    print("\n========== LOGISTIC REGRESSION ==========")
    print("Model trained successfully.")

    return model