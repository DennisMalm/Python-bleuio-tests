import random
import serial
import time
# from test_list import tests
from alpha_tests import tests

# Dongle and port settings
connecting_to_dongle = 0
mode = "AT+PERIPHERAL"
console = None
comport = "COM4"
tty_port = "/dev/tty.usbmodem4048FDE52D2C1"

# Test vars
ctrl_c = "\x03"
fail_states = ["ERROR", "Invalid"]

# Test objects
completed_tests = []
test_to_run = []


def connect():
    global connecting_to_dongle
    global console
    while connecting_to_dongle == 0:
        print("\nConnecting to dongle...")
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
    print(f"\nConnected to Dongle.\n")


def menu():
    print("\nTest suite starting!\n")
    while True:
        choice = input(
            "\n1. ATI\n2. WRITE COMMAND\n3. RANDOM FROM TEST_DICT LENGTH\n4. PERIPHERAL\n5. CENTRAL \n6. Print completed tests\n7. AUTO TEST\n")
        if choice == "1":
            send_command("ATI")
        elif choice == "2":
            send_command(input("Write command to send: "))
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
            send_command("AT+PERIPHERAL")
        else:
            print("Not valid input, try again.")


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


def print_completed_tests():
    for test_object in tests:
        print("\n\n[Commands Run]")
        print(test_object["commands"])
        print("[Result]")
        print(test_object["result"])


def auto_test(test_object):
    global mode
    global con
    out = ' '
    command_counter = 1
    pause_counter = 0
    if "mode" in test_object:
        if test_object.get("mode") not in mode:
            print("Switching mode to " + test_object["mode"])
            send_command(test_object["mode"])
            mode = test_object["mode"]
            time.sleep(2)
    for command in test_object["commands"]:
        print(f"\n------------------------\nNow testing: {command}")
        con.write(str.encode(command))
        con.write('\r'.encode())
        time.sleep(1)

        while con.inWaiting() > 0:
            out += con.read(con.inWaiting()).decode()
        time.sleep(0.2)
        if not out.isspace():
            print(">> " + out)
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

    con.write(cmd_one.encode())
    con.write('\r'.encode())
    time.sleep(0.5)
    if dual:
        con.write(cmd_two.encode())
        con.write('\r'.encode())
    out = ' '
    time.sleep(0.5)
    while con.inWaiting() > 0:
        out += con.read(con.inWaiting()).decode()
    if not out.isspace():
        print(f">> {out} {cmd_one}")
    time.sleep(0.1)


# Start of program
if __name__ == "__main__":
    con = connect()
    menu()
