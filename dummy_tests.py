tests = [{
    "commands": ["AT"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["ATE1", "ATE0"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["ATI"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVDATAI=5f2dd896-b886-4549-ae01-e41acd7a354a0203010400", "AT+ADVSTART", "AT+ADVSTOP"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVRESP"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPCONNECT=[1]FD:37:13:D0:6D:02", "AT+CANCELCONNECT", "AT+CANCELCONNECT"],
    "result": [],
    "restart": False,
    "pause": 0.5,
}, {

    "commands": ["AT+ENTERPASSKEY=123456"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+FINDSCANDATA=FF5"],
    "result": [],
    "restart": False,
    "pause": 5
}, {

    "commands": ["AT+GAPDISCONNECT"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPIOCAP"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPPAIR"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPUNPAIR"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPSCAN=5"],
    "result": [],
    "restart": False,
    "pause": 6.5
}, {

    "commands": ["AT+GAPresult"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GATTCREAD=001B"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GATTCWRITE=001B HELLO"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GETSERVICES"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+NUMCOMPA"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+SCANTARGET=00:00:00:00:00:01"],
    "result": [],
    "restart": False,
    "pause": 0.5,
    "expected": "ERROR"
}, {

    "commands": ["AT+SECLVL"],
    "result": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+SETNOTI=0012"],
    "result": [],
    "restart": False,
    "pause": 0.5,
    "expected": "ERROR"
}, {

    "commands": ["AT+SETPASSKEY=123456"],
    "result": [],
    "restart": False,
    "pause": 0.5
}]
