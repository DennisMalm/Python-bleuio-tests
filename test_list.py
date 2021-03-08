tests = [{
    "commands": ["AT"],
    "result": [],
    "restart": False,
    "pause": [0.5]
}, {

    "commands": ["ATE1", "ATE0"],
    "result": [],
    "restart": False,
    "pause": [0.5, 0.5]
}, {

    "commands": ["ATI"],
    "result": [],
    "restart": False,
    "pause": [0.5]
}, {

    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "mode": "AT+PERIPHERAL",
    "result": [],
    "restart": False,
    "pause": [1, 1, 1]
}, {

    "commands": ["AT+ADVDATAI=5f2dd896-b886-4549-ae01-e41acd7a354a0203010400", "AT+ADVSTART", "AT+ADVSTOP"],
    "mode": "AT+PERIPHERAL",
    "result": [],
    "restart": False,
    "pause": [1, 1, 1]
}, {

    "commands": ["AT+GAPCONNECT=[0]FD:37:13:D0:6D:02", "AT+CANCELCONNECT", "AT+CANCELCONNECT"],
    "mode": "AT+CENTRAL",
    "result": [],
    "restart": False,
    "pause": [3, 1, 1]
}]
