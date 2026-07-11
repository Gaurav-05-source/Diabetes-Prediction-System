from sklearn.tree import DecisionTreeClassifier


def train_decision_tree(X_train, y_train):
    """
    Train Decision Tree model.
    """

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("\n========== DECISION TREE ==========")
    print("Model trained successfully.")

    return model