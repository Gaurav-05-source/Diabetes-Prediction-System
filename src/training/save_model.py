import joblib
import os


def save_model(model, filename):
    """
    Save a trained model or preprocessing object.
    """

    os.makedirs("models", exist_ok=True)

    file_path = os.path.join("models", filename)

    joblib.dump(model, file_path)

    print(f"Saved: {file_path}")