from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from src.prediction.predict import predict_diabetes

app = Flask(__name__)

# Secret Key
app.secret_key = "diabetes_prediction_secret_key"


# ==================================
# Home Page
# ==================================

@app.route("/")
def home():

    data = session.pop("prediction_data", None)

    if data:
        return render_template("index.html", **data)

    return render_template("index.html")


# ==================================
# Prediction
# ==================================

@app.route("/predict", methods=["POST"])
def predict():

    gender = request.form["gender"]
    age = float(request.form["age"])
    hypertension = int(request.form["hypertension"])
    heart_disease = int(request.form["heart_disease"])
    smoking_history = request.form["smoking_history"]
    bmi = float(request.form["bmi"])
    hba1c = float(request.form["hba1c_level"])
    blood_glucose = float(request.form["blood_glucose_level"])

    prediction, probability = predict_diabetes(
        gender,
        age,
        hypertension,
        heart_disease,
        smoking_history,
        bmi,
        hba1c,
        blood_glucose
    )

    print("Prediction :", prediction)
    print("Probability:", probability)

    if prediction == 1:

        result = "High Risk of Diabetes"
        result_class = "danger"
        icon = "⚠️"
        recommendation = (
            "Please consult a healthcare professional "
            "for further evaluation."
        )

    else:

        result = "Low Risk of Diabetes"
        result_class = "success"
        icon = "✅"
        recommendation = (
            "Maintain a healthy lifestyle and regular "
            "health checkups."
        )

    # Store everything in session
    session["prediction_data"] = {

        "prediction": result,

        "confidence": probability * 100,

        "result_class": result_class,

        "icon": icon,

        "recommendation": recommendation,

        "gender": gender,

        "age": age,

        "hypertension": hypertension,

        "heart_disease": heart_disease,

        "smoking_history": smoking_history,

        "bmi": bmi,

        "hba1c_level": hba1c,

        "blood_glucose_level": blood_glucose
    }

    # Redirect to home page
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)