from flask import Flask, render_template

app = Flask(__name__)

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = float(f.read()) / 1000.0
        return round(temp, 1)
    except:
        return 42.5 # Mock temp if tested off-pi

@app.route('/')
def index():
    temp = get_cpu_temp()
    fan_status = "ACTIVE (Cooling)" if temp > 50.0 else "STANDBY (Normal)"
    return render_template('index.html', temp=temp, fan_status=fan_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

