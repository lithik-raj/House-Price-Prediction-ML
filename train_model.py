# train_model.py

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("house_data.csv")

print("\nDataset Preview:")
print(df.head())

# ==========================
# HANDLE MISSING VALUES
# ==========================

df = df.dropna()

# ==========================
# ENCODE LOCATION TYPE
# ==========================

encoder = LabelEncoder()

df["location_type"] = encoder.fit_transform(df["location_type"])

# Urban = 2 (example)
# Suburban = 1
# Rural = 0
# Actual mapping depends on data order

# ==========================
# FEATURES & TARGET
# ==========================

X = df[
    [
        "area",
        "bedrooms",
        "bathrooms",
        "floors",
        "parking",
        "house_age",
        "location_type"
    ]
]

y = df["price"]

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# MODEL
# ==========================

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=15,
    random_state=42
)

# ==========================
# TRAIN
# ==========================

model.fit(X_train, y_train)

# ==========================
# TEST
# ==========================

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("\nModel Performance")
print("----------------------")
print("R2 Score :", round(r2, 4))
print("MAE      :", round(mae, 2))

# ==========================
# SAVE MODEL
# ==========================

with open("house_model.pkl", "wb") as file:
    pickle.dump(model, file)

# ==========================
# SAVE ENCODER
# ==========================

with open("location_encoder.pkl", "wb") as file:
    pickle.dump(encoder, file)

print("\nModel Saved Successfully!")
print("house_model.pkl created")
print("location_encoder.pkl created")