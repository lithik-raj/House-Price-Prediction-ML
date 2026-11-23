import os
import pickle
import numpy as np
from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

# ==========================
# LOAD MODEL & ENCODER
# ==========================
model_path = os.path.join(BASE_DIR, "house_model.pkl")
encoder_path = os.path.join(BASE_DIR, "location_encoder.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

with open(encoder_path, "rb") as file:
    encoder = pickle.load(file)


# ==========================
# ROUTES
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


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
                location_encoded,
            ]
        ])

        prediction = model.predict(features)[0]
        predicted_price = f"₹ {prediction:,.0f}"

        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price: {predicted_price}",
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
