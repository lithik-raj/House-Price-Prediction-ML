# 🏠 AI House Price Prediction & Real Estate Valuation System

<p align="center">
  <strong>End-to-End Machine Learning Web Application for Real Estate Price Forecasting powered by Random Forest Regression and Flask.</strong>
</p>

<p align="center">
  <a href="https://github.com/lithik-raj/House-Price-Prediction-ML"><img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repo" /></a>
  <a href="https://vercel.com/new/clone?repository-url=https://github.com/lithik-raj/House-Price-Prediction-ML"><img src="https://img.shields.io/badge/Deploy%20with-Vercel-black?style=for-the-badge&logo=vercel" alt="Deploy on Vercel" /></a>
  <a href="https://house-price-prediction-ml-lithik-raj.vercel.app"><img src="https://img.shields.io/badge/Live%20Demo-Vercel%20Production-00ffc8?style=for-the-badge&logo=vercel" alt="Live Demo" /></a>
  <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License: MIT" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-1.24%2B-013243?style=flat-square&logo=numpy&logoColor=white" />
</p>

---

## 📌 Live Deployments & Quick Links

| Resource | Direct Link | Description |
|---|---|---|
| 🐙 **GitHub Repository** | [github.com/lithik-raj/House-Price-Prediction-ML](https://github.com/lithik-raj/House-Price-Prediction-ML) | Source code, dataset, and trained weights |
| ⚡ **Vercel 1-Click Deploy** | [Deploy to Vercel](https://vercel.com/new/clone?repository-url=https://github.com/lithik-raj/House-Price-Prediction-ML) | Zero-config serverless cloud deployment |
| 🌐 **Vercel Live Application** | [house-price-prediction-ml-lithik-raj.vercel.app](https://house-price-prediction-ml-lithik-raj.vercel.app) | Live interactive house price forecasting |

---

## 📖 Project Overview

Valuing residential real estate accurately is critical for buyers, sellers, lenders, and real estate developers. Traditional property valuation relies on manual appraisals that are often subjective and slow.

**AI House Price Prediction** delivers an automated, high-precision valuation engine. Built using **Scikit-Learn's Random Forest Regressor** and packaged into an interactive **Flask Web Application**, the model evaluates core structural and spatial factors (carpet area, bedroom & bathroom counts, floor elevation, parking capacity, building age, and regional locality classifications) to forecast fair market property valuations instantly.

---

## ✨ Features & Architecture

- **Random Forest Regression Ensemble**: High-variance resistance and non-linear feature interaction mapping.
- **Categorical Feature Encoding**: LabelEncoder pipeline preserving spatial locality categorization (`Urban`, `Suburban`, `Rural`).
- **Interactive Glassmorphism UI**: Dynamic property valuation calculator with real-time currency formatting.
- **Vercel Serverless Ready**: Packaged for zero-maintenance Python serverless deployment via `@vercel/python`.

---

## 📊 Model Input Features

| Feature Name | Type | Range / Options | Description |
|---|---|---|---|
| `Area` | Numeric (sq ft) | 500 – 10,000+ | Total built-up carpet area |
| `Bedrooms` | Integer | 1 – 10 | Total bedroom count |
| `Bathrooms` | Integer | 1 – 8 | Total bathroom count |
| `Floors` | Integer | 1 – 5 | Number of building floors |
| `Parking` | Integer | 0 – 5 | Dedicated vehicle parking spaces |
| `House Age` | Integer (years) | 0 – 50 | Age of the property structure |
| `Location Type` | Categorical | `Urban`, `Suburban`, `Rural` | Geographic density classification |

---

## 🚀 Local Installation & Setup

```bash
# 1. Clone repository
git clone https://github.com/lithik-raj/House-Price-Prediction-ML.git
cd House-Price-Prediction-ML

# 2. Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start web application
python app.py
# Open: http://localhost:5000
```

---

## ☁️ Deploy to Vercel

1. Push this repository to GitHub: `https://github.com/lithik-raj/House-Price-Prediction-ML`
2. Open **[vercel.com/new](https://vercel.com/new)**
3. Select `House-Price-Prediction-ML` and click **Deploy**.
4. Vercel automatically detects `vercel.json` and spins up the Python serverless environment.

---

## 📄 License & Author

- **Author**: [Lithik Raj](https://github.com/lithik-raj)
- **License**: [MIT](LICENSE)
