import time
import lgpio

PIN1 = 22
PIN2 = 23

# Temperature threshold in Celsius 
# (Set to 50°C for easy testing; you can raise it to 60°C or 65°C later)
TEMP_THRESHOLD = 50.0

def get_cpu_temp():
    """Reads the Raspberry Pi's built-in CPU temperature."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_str = f.read().strip()
            return float(temp_str) / 1000.0
    except Exception:
        return 0.0

print("--- Server Room Guardian: Smart Thermal Monitor ---")
h = lgpio.gpiochip_open(0)

try:
    lgpio.gpio_claim_output(h, PIN1)
    lgpio.gpio_claim_output(h, PIN2)

    fan_is_on = False

    while True:
        current_temp = get_cpu_temp()
        print(f"Current Pi CPU Temperature: {current_temp:.1f}°C")

        if current_temp >= TEMP_THRESHOLD and not fan_is_on:
            print("--> Temperature threshold reached! Turning fan ON...")
            lgpio.gpio_write(h, PIN1, 1)
            lgpio.gpio_write(h, PIN2, 1)
            fan_is_on = True
        elif current_temp < (TEMP_THRESHOLD - 3) and fan_is_on:
            print("--> Temperature is normal. Turning fan OFF...")
            lgpio.gpio_write(h, PIN1, 0)
            lgpio.gpio_write(h, PIN2, 0)
            fan_is_on = False

        time.sleep(5)  # Check every 5 seconds

except KeyboardInterrupt:
    print("\nManual stop detected.")

finally:
    # Safety shutdown
    lgpio.gpio_write(h, PIN1, 0)
    lgpio.gpio_write(h, PIN2, 0)
    lgpio.gpiochip_close(h)
    print("Guardian offline. GPIO closed safely.")

