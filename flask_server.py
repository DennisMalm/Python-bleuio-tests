import time
import serial
import numpy as np
from flask import Flask, render_template, redirect, url_for, jsonify
from single_test_list import tests

# Flask
app = Flask(__name__)
test = np.random.rand()

# Dongle and port settings
connecting_to_dongle = 0
mode = " "
console = None
comport = "COM5"
tty_port = "/dev/tty.usbmodem4048FDE52EE01"

# Test vars
ctrl_c = "\x03"
fail_states = ["ERROR", "Invalid"]


# Methods
def connect_to_dongle():
    global connecting_to_dongle
    global console
    try:
        console = serial.Serial(
            port=comport,
            baudrate=57600,
            parity="N",
            stopbits=1,
            bytesize=8,
            timeout=0
        )
        if console.is_open.__bool__():
            connecting_to_dongle = 1
            print("Connected to dongle!")
            message = "Connected to dongle!"
    except:
        print("Dongle not connected. Please reconnect Dongle.")
        message = "Dongle not connected. Please reconnect Dongle."
    return message


def restart(obj="No object."):
    global con
    print(obj)
    print("Restarting.")
    con.write(str.encode("ATR"))
    con.write('\r'.encode())
    time.sleep(20)
    global connecting_to_dongle
    connecting_to_dongle = 0
    con = connect()


def switch_mode(mode_change):
    global mode
    print(f"Switching mode to {mode_change}")
    send_command(mode_change)
    mode = mode_change
    time.sleep(1)


def auto_test(test_list):
    global mode
    global con
    for test in tests:
        command_counter = 1
        pause_counter = 0
        if "mode" in test and test.get("mode") not in mode:
            switch_mode(test["mode"])
        for command in test["commands"]:
            print(f"\n------------------------\nNow testing: {command}")
            result = send_command(command)
            print(f"Pausing for {str(test['pause'][pause_counter])}")
            time.sleep(test["pause"][pause_counter])
            pause_counter += 1
            test["result"].append({command_counter: result})
            command_counter += 1
        if test["restart"]:
            restart(test)
        else:
            print(test)
        return test_list


def send_command(cmd):
    console.write(cmd.encode())
    console.write('\r'.encode())
    out = ' '
    time.sleep(0.5)
    while console.inWaiting() > 0:
        out += console.read(console.inWaiting()).decode()
    if not out.isspace():
        print(out)
    time.sleep(0.1)
    return "Fail" if any(ele in out for ele in fail_states) else "Pass"


completed_test = None


# Routes
@app.route('/')
def base():
    return render_template('index.html', connected=connecting_to_dongle)


@app.route('/update_page', methods=['POST', 'GET'])
def update_page():
    return jsonify('', render_template('test.html', result=completed_test))
    # return render_template('test.html', result=tests)


@app.route('/start', methods=['POST'])
def start():
    # global completed_test
    # completed_test = auto_test(tests)
    return render_template('result.html')


@app.route('/connect', methods=['POST', 'GET'])
def connect():
    global completed_test
    message = connect_to_dongle()
    completed_test = auto_test(tests)
    return render_template('result.html', message=message, result=completed_test)


if __name__ == "__main__":
    app.run(debug=True)
