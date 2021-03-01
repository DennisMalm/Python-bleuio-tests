import serial
import time

connecting_to_dongle = 0
console = None
comport = "COM4"

adv_data = "03:03:aa:fe"
ibeacon = "5f2dd896-b886-4549-ae01-e41acd7a354a0203010400"
eddystone_hex = "0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07"
completed_tests = []
test_to_run = ["AT+ADVSTART", "AT+ADVSTOP"]
test_dict = [{
    "type": "Advertising",
    "commands": ["AT+ADVSTART", "AT+ADVSTOP"],
    "status": "none",
    "restart": False
}, {
    "type": "ibeacon",
    "commands": ["AT+ADVDATAI=5f2dd896-b886-4549-ae01-e41acd7a354a0203010400", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": "none",
    "restart": False
}, {
    "type": "eddystone",
    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": "none",
    "restart": False
}, {
    "type": "scan",
    "commands": ["AT+CENTRAL", "AT+GAPSCAN=4"],
    "status": "none",
    "restart": False,
    "pause": 10
}, {
    "type": "Find and scan",
    "commands": ["AT+FINDSCANDATA=FF5", "\x03"],
    "status": "none",
    "restart": False,
}, {
    "type": "Info",
    "commands": ["ATI"],
    "status": "none",
    "restart": False
}, {
    "type": "Advertise response",
    "commands": ["AT+ADVRESP"],
    "status": "none",
    "restart": False
}, {
    "type": "Echo",
    "commands": ["ATE1", "ATE0"],
    "status": "none",
    "restart": False,
    "pause": 5
}]


def connect():
    global connecting_to_dongle
    global console
    while connecting_to_dongle == 0:
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
                return console
        except:
            print("Dongle not connected. Please reconnect Dongle.")
            time.sleep(5)


def print_completed_tests():
    for test_status in test_dict:
        print(f"{test_status}")


def auto_test():
    global con
    for test_object in test_dict:
        fail_counter = 0
        for command in test_object["commands"]:
            con.write(str.encode(command))
            con.write('\r'.encode())
            time.sleep(1)
            out = ' '
            time.sleep(1)
            while con.inWaiting() > 0:
                out += con.read(con.inWaiting()).decode()
            if not out.isspace():
                print(">>" + out)
            if "ERROR" in out:
                fail_counter += 1
            # completed_tests.append({"COMPLETED": {False if "ERROR" in out else True}, "TEST": command})
        test_object["status"] = "Pass" if fail_counter == 0 else f"{fail_counter} fails"
        if "pause" in test_object:
            time.sleep(test_object["pause"])
        else:
            time.sleep(3)
        if test_object["restart"]:
            print(test_object)
            print("Restarting.")
            con.write(str.encode("ATR"))
            con.write('\r'.encode())
            time.sleep(20)
            global connecting_to_dongle
            connecting_to_dongle = 0
            con = connect()
        else:
            print(test_object)
            print("Restart is false.")


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
print(f"\nConnected to Dongle at port {comport}.\n")
print("\nTest suite starting!\n")

while True:
    choice = input("\n1. ATI\n2. PERIPHERAL\n3. ADVSTOP\n4. TEST CASE\n5. Print completed tests\n6. AUTO TEST\n")
    if choice == "1":
        send_command("ATI")
    elif choice == "2":
        send_command("AT+PERIPHERAL")
    elif choice == "3":
        send_command("AT+ADVSTOP")
    elif choice == "4":
        send_command("AT+CENTRAL", "AT+GAPSCAN=5", True)
    elif choice == "5":
        print_completed_tests()
    elif choice == "6":
        auto_test()
        print_completed_tests()
    else:
        print("Not valid input, try again.")
