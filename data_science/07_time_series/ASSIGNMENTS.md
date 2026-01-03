# Time Series Assignments

## Objective
Predict the future using the past.

## Prerequisites
- `pip install statsmodels`

## Practical Assignments

### Assignment 1: Decomposition
**Goal:** Understand the data.
1.  Load the **AirPassengers** dataset (classic 1950s data).
2.  Use `statsmodels.tsa.seasonal.seasonal_decompose`.
3.  Plot Trend, Seasonality, and Residuals separately.
4.  *Question*: Is the trend linear or exponential?

### Assignment 2: ARIMA Forecasting
**Goal:** Statistical prediction.
1.  Check for Stationarity (Visual inspection or Augmented Dickey-Fuller test).
2.  If not stationary, apply Differencing (`df.diff()`).
3.  Train an `ARIMA(p=1, d=1, q=1)` model on the data.
4.  Forecast the next 12 months.

### Assignment 3: LSTM Stock Predictor
**Goal:** Deep Learning on Sequences.
1.  Download a Stock CSV (e.g., AAPL).
2.  Preprocess: Normalize data to (0, 1) using MinMaxScaler.
3.  Create sequences:
    *   Input: Days 1-60.
    *   Target: Day 61.
4.  Train an LSTM model.
5.  Plot Actual vs Predicted price.

## Conceptual Quiz
1.  What is "Lag"?
2.  Why is "Look-ahead Bias" dangerous in Time Series backtesting?
3.  What happens if you try to fit ARIMA on a stock price that constantly grows (Non-Stationary)?
