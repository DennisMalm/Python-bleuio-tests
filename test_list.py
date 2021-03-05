tests = [{
    "commands": ["AT"],
    "status": [],
    "restart": False,
    "pause": [0.5]
}, {

    "commands": ["ATE1", "ATE0"],
    "status": [],
    "restart": False,
    "pause": [0.5, 0.5]
}, {

    "commands": ["ATI"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": [],
    "restart": False,
    "pause": [0.5, 0.5, 0.5]
}, {

    "commands": ["AT+ADVDATAI=5f2dd896-b886-4549-ae01-e41acd7a354a0203010400", "AT+ADVSTART", "AT+ADVSTOP"],
    "result": [],
    "restart": False,
    "pause": [0.5, 0.5, 0.5]
}]
