# Snippet 1: Introduction to Time Series Analysis
time_series <- ts(c(1, 2, 3, 4, 5, 6, 7))
plot(time_series)

# Snippet 2: Stationarity and Differencing
library(tseries)

adf.test(time_series) # ADF test
time_series_diff <- diff(time_series) # Differencing

# Snippet 3: ARIMA Model
model <- arima(time_series, order=c(1, 1, 1))
forecast <- predict(model, n.ahead = 1)$pred # Forecasting

# Snippet 4: Forecasting and Validation
mse <- mean((time_series[2:7] - time_series_diff)^2)
