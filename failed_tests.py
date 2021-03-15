# Failed tests, problem not in program
tests = [{

    "commands": ["AT+GAPCONNECT=[1]FD:00:00:D0:0D:02", "AT+CANCELCONNECT"],
    "mode": "AT+CENTRAL",
    "result": [],
    "restart": False,
    "pause": [10, 1]
}]