import time
import lgpio

PIN1 = 22
PIN2 = 23

print("--- Server Room Guardian: Fan Controller ---")
h = lgpio.gpiochip_open(0)

try:
    lgpio.gpio_claim_output(h, PIN1)
    lgpio.gpio_claim_output(h, PIN2)

    print("--> Turning cooling fan ON...")
    lgpio.gpio_write(h, PIN1, 1)
    lgpio.gpio_write(h, PIN2, 1)

    time.sleep(10)

    print("--> Turning cooling fan OFF...")
    lgpio.gpio_write(h, PIN1, 0)
    lgpio.gpio_write(h, PIN2, 0)

except KeyboardInterrupt:
    print("\nManual interrupt detected.")

finally:
    lgpio.gpio_write(h, PIN1, 0)
    lgpio.gpio_write(h, PIN2, 0)
    lgpio.gpiochip_close(h)
    print("Guardian standby mode. GPIO closed safely.")

