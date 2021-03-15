tests = [{
    "commands": ["AT+GAPCONNECT=[0]40:48:FD:E5:2E:E0", "AT+GAPPAIR", "AT+GAPUNPAIR"],
    "mode": "AT+CENTRAL",
    "result": [],
    "restart": False,
    "pause": [5, 2, 2]
}, {
    "commands": ["AT+GAPCONNECT=[0]40:48:FD:E5:2E:E0",
                 "AT+GATTCREAD=001B",
                 "AT+GATTCWRITE=001B HELLO",
                 "AT+GATTCWRITEB=001B 0101",
                 "AT+GETSERVICES",
                 "AT+SPSSEND=HEJ",
                 "AT+GAPDISCONNECT"],
    "mode": "AT+CENTRAL",
    "result": [],
    "restart": False,
    "pause": [5, 2, 2, 2, 2, 2, 2]
}]
