import random
import serial
import time
from single_test_list import tests as single_tests
from pair_test_list import tests as pair_tests
from check_dongle_code import tests as alpha_tests

# Dongle and port settings
connecting_to_dongle = 0
mode = " "
console = None
comport = "COM5"
tty_port = "/dev/tty.usbmodem4048FDE52D231"
target_dongle_address = "Placeholder"

# Test vars
ctrl_c = "\x03"
fail_states = ["ERROR", "error", "Invalid"]

# Test objects
completed_tests = []


# test_to_run = []

def dongle_settings():
    global comport
    global target_dongle_address
    user_port = input("Port id: ")
    print(user_port)
    if user_port:
        comport = user_port
    print(comport)
    user_target = input("Target address: ")
    print(user_target)
    if user_target:
        target_dongle_address = user_target
    print(target_dongle_address)


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
            "\n1. ATI\n2. WRITE COMMAND\n3. RANDOM FROM TEST_DICT LENGTH\n4. PERIPHERAL\n5. CENTRAL \n6. Restart\n7. "
            "AUTO TEST\n8. PAIRINGS\n9. WRITE TO FILE\n10. Set Port and Target\n")
        if choice == "1":
            send_command("ATI")
        elif choice == "2":
            send_command(input("Write command to send: "))
        elif choice == "3":
            auto_test(random.choice(single_tests))
        elif choice == "4":
            send_command("AT+PERIPHERAL")
        elif choice == "5":
            send_command("AT+CENTRAL")
        elif choice == "6":
            restart()
        elif choice == "7":
            auto_test(single_tests)
            print_completed_tests()
            switch_mode("AT+PERIPHERAL")
        elif choice == "8":
            auto_test(pair_tests)
            print_completed_tests()
            switch_mode("AT+PERIPHERAL")
        elif choice == "9":
            file = open('test_run.txt', 'w')
            file.write('writing something...')
            file.close()
        elif choice == "10":
            dongle_settings()
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
    run_counter = 1
    for test_run in completed_tests:
        print(f"-------------\nTest run: {run_counter}\n-------------")
        for test in test_run:
            print("\n[Commands Run]")
            print(test["commands"])
            print("[Result]")
            print(test["result"])
        run_counter += 1


def switch_mode(mode_change):
    global mode
    print(f"Switching mode to {mode_change}")
    send_command(mode_change)
    mode = mode_change
    time.sleep(1)


def auto_test(test_list_template):
    global mode
    global con
    test_list = test_list_template
    for test in test_list:
        command_counter = 1
        pause_counter = 0
        if "mode" in test and test.get("mode") != mode:
            print("before mode change --------")
            switch_mode(test["mode"])
            print("after mode change ---------")
        for command in test["commands"]:
            print(f"\n------------------------\nNow testing: {command}")
            result = send_command(command)
            print(f"Pausing for {str(test['pause'][pause_counter])}")
            time.sleep(test["pause"][pause_counter])
            pause_counter += 1
            test["result"].append({"Test: " + str(command_counter): result})
            command_counter += 1
        if test["restart"]:
            restart(test)
        else:
            print(test)
    completed_tests.append(test_list)


def send_command(cmd):
    con.write(cmd.encode())
    con.write('\r'.encode())
    out = ' '
    time.sleep(0.5)
    while con.inWaiting() > 0:
        out += con.read(con.inWaiting()).decode()
    if not out.isspace():
        print(out)
    time.sleep(0.1)
    return "Fail" if any(ele in out for ele in fail_states) else "Pass"


# Start of program
if __name__ == "__main__":
    dongle_settings()
    con = connect()
    menu()
