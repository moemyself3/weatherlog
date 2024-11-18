# 🌤 weatherlog.py ⛈
This python script connects to weather station via `ssh` using `paramiko` and reads the output to a `.csv` file in a loop.

## usage
```
python -m weatherlog 
```

## suggestion on reading log real-time
Users can monitor the .csv file real-time using `tail`
```
tail -f log_weather_*.csv
```
