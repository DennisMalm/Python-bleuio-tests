import random
import serial
import time
from commandList import tests as testOne
from stillViable import tests as testTwo

# Dongle and port settings
connecting_to_dongle = 0
console = None
comport = "COM4"
tty_port = "/dev/tty.usbmodem4048FDE52D231"

ctrl_c = "\x03"
adv_data = "03:03:aa:fe"
ibeacon = "5f2dd896-b886-4549-ae01-e41acd7a354a0203010400"
eddystone_hex = "0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07"
fail_states = ["ERROR", "Invalid"]

# Test objects
completed_tests = []
test_to_run = ["AT+ADVSTART", "AT+ADVSTOP"]
test_dict = [{
    "type": "Advertising",
    "commands": ["ATI"],
    "status": [],
    "restart": False
}, {
    "type": "ibeacon",
    "commands": ["AT+ADVDATAI=5f2dd896-b886-4549-ae01-e41acd7a354a0203010400", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": [],
    "restart": False
}, {
    "type": "eddystone",
    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": [],
    "restart": False}]

tanke_object = {
    "type": "Echo",
    "commands": ["ATE1", "ATE0"],
    "status": "none",
    "restart": False,
    "pause": 5
}


def connect():
    global connecting_to_dongle
    global console
    while connecting_to_dongle == 0:
        try:
            console = serial.Serial(
                port=tty_port,
                baudrate=57600,
                parity="N",
                stopbits=1,
                bytesize=8,
                timeout=0
            )
            if console.is_open.__bool__():
                connecting_to_dongle = 1
                return console
        except:
            print("Dongle not connected. Please reconnect Dongle.")
            time.sleep(5)


def restart(restart):
    global con
    print(restart)
    print("Restarting.")
    con.write(str.encode("ATR"))
    con.write('\r'.encode())
    time.sleep(20)
    global connecting_to_dongle
    connecting_to_dongle = 0
    con = connect()


def print_completed_tests():
    for test_status in test_dict:
        print(f"{test_status}")


def auto_test(test_object):
    global con
    out = ' '
    # i = 0
    # i += 1

    for command in test_object["commands"]:
        print(f"Now testing: {command}\n-----------------")
        con.write(str.encode(command))
        con.write('\r'.encode())
        time.sleep(1)

        while con.inWaiting() > 0:
            out += con.read(con.inWaiting()).decode()
        time.sleep(0.2)
        if not out.isspace():
            print(">>" + out)
        time.sleep(0.2)
        if test_object.get("expected") in fail_states and test_object.get("expected") in out:
            pass_or_fail = "Pass"
        else:
            pass_or_fail = "Fail" if "ERROR" in out or "Invalid" in out else "Pass"
        test_object["status"].append({command: pass_or_fail})
        out = ' '
    if "pause" in test_object:
        time.sleep(test_object["pause"])
    else:
        time.sleep(3)
    if test_object["restart"]:
        restart(test_object)
    else:
        print(test_object)


def send_command(cmd_one, cmd_two="ATI", dual=False):
    con.write(str.encode(cmd_one))
    con.write('\r'.encode())
    time.sleep(1)
    if dual:
        con.write(str.encode(cmd_two))
        con.write('\r'.encode())
    out = ' '
    time.sleep(1)
    while con.inWaiting() > 0:
        out += con.read(con.inWaiting()).decode()

    if not out.isspace():
        print(">>" + out)
    completed_tests.append({"COMPLETED": {False if "ERROR" in out else True}, "TEST": cmd_one})
    time.sleep(0.1)


# Start of program
print("\nConnecting to dongle...")
con = connect()
print(f"\nConnected to Dongle.\n")
print("\nTest suite starting!\n")

while True:
    choice = input(
        "\n1. ATI\n2. TEST_DICT LENGTH\n3. RANDOM FROM TEST_DICT LENGTH\n4. PERIPHERAL\n5. CENTRAL \n6. Print completed tests\n7. AUTO TEST\n")
    if choice == "1":
        send_command("ATI")
    elif choice == "2":
        # send_command("AT+PERIPHERAL")
        print(len(test_dict))
    elif choice == "3":
        auto_test(random.choice(testOne))
    elif choice == "4":
        send_command("AT+PERIPHERAL")
    elif choice == "5":
        send_command("AT+CENTRAL")
    elif choice == "6":
        print_completed_tests()
    elif choice == "7":
        for test_object in testTwo:
            auto_test(test_object)
        print_completed_tests()
    else:
        print("Not valid input, try again.")
