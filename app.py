from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# ==========================
# LOAD MODEL
# ==========================

with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("location_encoder.pkl", "rb") as file:
    encoder = pickle.load(file)


# ==========================
# HOME PAGE
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# PREDICTION
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        area = float(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        floors = int(request.form["floors"])
        parking = int(request.form["parking"])
        house_age = int(request.form["house_age"])
        location_type = request.form["location_type"]

        # Encode Location
        location_encoded = encoder.transform([location_type])[0]

        features = np.array([
            [
                area,
                bedrooms,
                bathrooms,
                floors,
                parking,
                house_age,
                location_encoded
            ]
        ])

        prediction = model.predict(features)[0]

        predicted_price = f"₹ {prediction:,.0f}"

        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price: {predicted_price}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )