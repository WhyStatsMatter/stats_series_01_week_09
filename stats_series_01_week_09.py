# Snippet 1: Introduction to Time Series Analysis
import pandas as pd
import matplotlib.pyplot as plt

time_series = pd.Series([1, 2, 3, 4, 5, 6, 7])
time_series.plot()
plt.show()

# Snippet 2: Stationarity and Differencing
from statsmodels.tsa.stattools import adfuller

result = adfuller(time_series) # ADF test
time_series_diff = time_series.diff().dropna() # Differencing

# Snippet 3: ARIMA Model
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(time_series, order=(1, 1, 1))
fit_model = model.fit()
forecast = fit_model.forecast(steps=1) # Forecasting

# Snippet 4: Forecasting and Validation
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(time_series[1:], time_series_diff)
