import random
import serial
import time
from test_list import tests


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
local_tests = [{
    "commands": ["AT"],
    "result": [],
    "restart": False,
    "pause": [0.5]
}, {

    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "result": [],
    "restart": False,
    "pause": [5, 0.5, 0.5]
}]


def connect():
    global connecting_to_dongle
    global console
    while connecting_to_dongle == 0:
        print("\nConnecting to dongle...")
        try:
            console = serial.Serial(
                port='COM4',
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
    print(f"\nConnected to Dongle.\n")


def menu():
    print("\nTest suite starting!\n")
    while True:
        choice = input(
            "\n1. ATI\n2. TEST_DICT LENGTH\n3. RANDOM FROM TEST_DICT LENGTH\n4. PERIPHERAL\n5. CENTRAL \n6. Print completed tests\n7. AUTO TEST\n")
        if choice == "1":
            send_command("ATI")
        elif choice == "2":
            # send_command("AT+PERIPHERAL")
            print(len(tests))
        elif choice == "3":
            auto_test(random.choice(tests))
        elif choice == "4":
            send_command("AT+PERIPHERAL")
        elif choice == "5":
            send_command("AT+CENTRAL")
        elif choice == "6":
            print_completed_tests()
        elif choice == "7":
            for test_object in tests:
                auto_test(test_object)
            print_completed_tests()
        else:
            print("Not valid input, try again.")


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
    for test_object in tests:
        print("\n\n[Commands Run]")
        print(test_object["commands"])
        print("[Result]")
        print(test_object["result"])


def auto_test(test_object):
    global con
    out = ' '
    command_counter = 1
    pause_counter = 0
    for command in test_object["commands"]:
        print(f"\nNow testing: {command}\n-----------------")
        con.write(str.encode(command))
        con.write('\r'.encode())
        time.sleep(1)

        while con.inWaiting() > 0:
            out += con.read(con.inWaiting()).decode()
        time.sleep(0.2)
        if not out.isspace():
            print(">>" + out)
        print("pausing " + str(test_object["pause"][pause_counter]))
        time.sleep(test_object["pause"][pause_counter])
        pause_counter += 1
        if test_object.get("expected") in fail_states and test_object.get("expected") in out:
            pass_or_fail = "Pass"
        else:
            pass_or_fail = "Fail" if "ERROR" in out or "Invalid" in out else "Pass"
        test_object["result"].append({command_counter: pass_or_fail})
        out = ' '
        command_counter += 1
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
con = connect()
menu()
