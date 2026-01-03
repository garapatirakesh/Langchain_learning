# Time Series Analysis Concepts

## 1. What is Time Series?
Data indexed by time. Sequence matters.
*   *Examples*: Stock Prices, Weather, Server Load, Sales.

## 2. Components of TS
Any chart can be decomposed into:
1.  **Trend**: Long-term direction (Up/Down).
2.  **Seasonality**: Repeating patterns (e.g., Ice cream sales go up every July).
3.  **Noise (Residuals)**: Randomness.

## 3. Stationarity (Critical Concept)
Most statistical models (ARIMA) assume the data is **Stationary**.
*   **Stationary means**: Mean and Variance do not change over time.
*   **Why?**: You can't predict the future if the rules of physics keep changing.
*   **The Fix**: Differencing. Instead of predicting "Price", predict "Price Today - Price Yesterday".

## 4. Models
### A. ARIMA (AutoRegressive Integrated Moving Average)
*   **AR (AutoRegressive)**: Predicting today based on yesterday. ($Y_t = \alpha Y_{t-1}$)
*   **I (Integrated)**: The Differencing step (to make it stationary).
*   **MA (Moving Average)**: Predicting based on past *errors*.

### B. Prophet (by Facebook)
*   Designed for business forecasting. Handles holidays and missing data remarkably well.

### C. LSTMs for Time Series
*   Using Deep Learning to look back at a "Window" (e.g., last 30 days) to predict Day 31.
*   Better at capturing complex non-linear patterns than ARIMA.
