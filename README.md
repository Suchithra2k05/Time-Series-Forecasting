# Time-Series-Forecasting

📈 Time-Series Forecasting – ARIMA & Prophet
This project showcases time-series forecasting using two popular techniques:

ARIMA – A statistical modeling approach for stationary data.

Prophet – A forecasting tool from Meta (Facebook) designed for capturing trends, seasonality, and holiday effects with minimal tuning.

The dataset here is simulated monthly sales data for demonstration purposes.

📌 Why Time-Series Forecasting Matters
Forecasting future values is essential in many industries:

📊 Business & Sales – Demand forecasting, inventory planning

📈 Finance – Stock prices, exchange rates

🌦 Weather – Temperature, rainfall prediction

🏭 Manufacturing – Production scheduling

🚛 Logistics – Shipment demand estimation

Accurate forecasting helps in strategic decision-making and resource optimization.

📊 Project Summary
Data: Simulated monthly sales data from Jan 2020 to Dec 2024.

Models Used:

ARIMA (2, 1, 2) – Captures autocorrelation and moving averages.

Prophet – Handles trend, seasonality, and noise automatically.

Forecast Horizon: 12 months ahead.

Goal: Compare the forecasting styles and outputs of ARIMA vs Prophet.

⚙️ Step-by-Step Workflow

1. Data Simulation
Generated 60 months of sales data with:

Poisson-distributed base demand

Upward trend over time

Random noise

2. Data Visualization
Initial plot to understand the historical trend.

3. ARIMA Modeling
ARIMA(p, d, q) = (2, 1, 2)

p: Auto-regressive terms

d: Differencing to make the series stationary

q: Moving average terms

Forecasted 12 months into the future.

4. Prophet Modeling
Reformatted data to Prophet format (ds = date, y = value).

Prophet automatically detects:

Yearly seasonality

Trend changes

Uncertainty intervals

Forecasted the same 12-month horizon.

5. Model Comparison
Overlaid ARIMA and Prophet forecasts on the same chart.

Dashed vertical line marks the start of forecast period.

📊 Sample Output Visualization

The resulting chart shows:

Black Line → Original Sales Data

Red Line → ARIMA Forecast

Blue Line → Prophet Forecast

Dashed Gray Line → Forecast Start

This visualization helps compare:

How ARIMA tends to follow recent trends closely.

How Prophet smooths forecasts with seasonality/trend adjustments.


💡 Key Takeaways

ARIMA is great for short-term forecasting when patterns are stable and well-defined.

Prophet is excellent for longer-term forecasting and when seasonality/trend shifts exist.

Visualization is key to understanding and comparing forecasts.

Data preparation (stationarity, missing values) heavily impacts forecast accuracy.

🛠 How to Run

# Clone repository
git clone https://github.com/yourusername/time-series-forecasting.git
cd time-series-forecasting

# Install dependencies
pip install pandas numpy matplotlib statsmodels prophet

# Run script

python forecasting.py

🔮 Possible Extensions
Use real datasets (stock market, weather, retail sales).

Perform ARIMA parameter tuning with pmdarima.auto_arima.

Add seasonality & holiday effects in Prophet.

Evaluate accuracy with:

RMSE (Root Mean Squared Error)

MAPE (Mean Absolute Percentage Error)

Deploy as an API for real-time forecasts.
