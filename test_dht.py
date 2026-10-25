import time
import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT11(board.D4)

print("Reading DHT11 sensor... Press Ctrl+C to stop.")

while True:
  try:
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print(f"Temp: {temperature_c} C  /  Humidity: {humidity}%")
  except RuntimeError as error:
    print(f"Retrying... ({error.args[0]})")
  time.sleep(2.0)


