# AI-Powered Energy Consumption Forecasting System

A beginner-friendly Python machine-learning project that simulates hourly electricity consumption, trains a forecasting model, evaluates predictions, and saves charts and results.

> **Important:** The included data is synthetic and created for education. It is not measured electricity data and results should not be treated as real-world performance claims.

## Project goal
Forecast energy consumption from time-based patterns to demonstrate how smart buildings, utilities, and energy teams could plan demand.

## Workflow
1. Generate an hourly demo dataset.
2. Clean missing readings and engineer time/lag features.
3. Split chronologically into training and test data.
4. Train a scaled Multi-Layer Perceptron (MLP) regressor.
5. Evaluate using MAE, RMSE, and R².
6. Save the model, predictions, metrics, and visualizations.

## Folder structure
```text
AI-Energy-Forecasting/
├── data/                 # generated energy.csv
├── src/                  # reusable forecasting pipeline
├── models/               # saved trained model
├── outputs/              # predictions and evaluation metrics
├── images/               # charts
├── docs/                 # project notes
├── notebooks/            # optional experiments
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements
Python 3.10 or newer recommended. No GPU is required.

### Windows (PowerShell or Command Prompt)
```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

## Expected outputs
- `data/energy.csv`
- `models/energy_forecast_model.pkl`
- `outputs/evaluation_metrics.json`
- `outputs/predictions.csv`
- `images/actual_vs_predicted.png`
- `images/hourly_consumption.png`

Metrics vary slightly by installed library version. MAE and RMSE are errors in kWh; lower is generally better. R² compares model fit against a baseline and can be negative if predictions are poor.

## Dataset
The program generates 180 days of hourly simulated consumption with daily peaks, weekday/weekend variation, a seasonal component, noise, and a few missing values for the cleaning step.



## Limitations and future improvements
- Uses simulated rather than real meter data.
- The demonstration model is a baseline; production forecasting needs domain review, real data, seasonality checks, and monitoring.
- Possible extensions: public energy datasets, weather/calendar features, forecast horizons, Flask API, and a dashboard.
<img width="1505" height="752" alt="Screenshot 2026-10-14 194212" src="https://github.com/user-attachments/assets/4762ce7e-c594-420e-b187-587e5cfe6864" />
<img width="1795" height="781" alt="Screenshot 2026-10-14 194147" src="https://github.com/user-attachments/assets/39c96aaa-9962-4de8-a57c-acfbe150b534" />
