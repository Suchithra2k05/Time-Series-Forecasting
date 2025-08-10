import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

# Step 1: Simulate Monthly Sales Data
np.random.seed(42)
dates = pd.date_range(start='2020-01-01', periods=60, freq='M')
sales = np.random.poisson(lam=200, size=60) + np.linspace(0, 50, 60)
df = pd.DataFrame({'Date': dates, 'Sales': sales})
df.set_index('Date', inplace=True)

# Plot original data
plt.figure(figsize=(10, 4))
plt.plot(df['Sales'], label='Original Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# Step 2: ARIMA Forecast
arima_model = ARIMA(df['Sales'], order=(2, 1, 2))  # Adjust (p,d,q) as needed
arima_fit = arima_model.fit()
arima_forecast = arima_fit.forecast(steps=12)
arima_forecast_dates = pd.date_range(start=df.index[-1] + pd.offsets.MonthBegin(), periods=12, freq='M')
arima_forecast_series = pd.Series(arima_forecast, index=arima_forecast_dates)

# Step 3: Prophet Forecast
df_prophet = df.reset_index().rename(columns={'Date': 'ds', 'Sales': 'y'})
prophet_model = Prophet()
prophet_model.fit(df_prophet)

future = prophet_model.make_future_dataframe(periods=12, freq='M')
prophet_forecast = prophet_model.predict(future)

# Step 4: Plot Both Forecasts
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Sales'], label='Original Sales', color='black')
plt.plot(arima_forecast_series.index, arima_forecast_series.values, label='ARIMA Forecast', color='red')
plt.plot(prophet_forecast['ds'], prophet_forecast['yhat'], label='Prophet Forecast', color='blue', alpha=0.6)
plt.axvline(df.index[-1], color='gray', linestyle='--', label='Forecast Start')
plt.title('Sales Forecast using ARIMA and Prophet')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
