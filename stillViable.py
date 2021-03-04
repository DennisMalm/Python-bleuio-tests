tests = [{
    "commands": ["AT"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["ATE1", "ATE0"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["ATI"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVDATA=03:03:aa:fe 0d:16:aa:fe:10:00:03:67:6f:6f:67:6c:65:07", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVDATAI=5f2dd896-b886-4549-ae01-e41acd7a354a0203010400", "AT+ADVSTART", "AT+ADVSTOP"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+ADVRESP"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPCONNECT=[1]FD:37:13:D0:6D:02","AT+CANCELCONNECT"],
    "status": [],
    "restart": False,
    "pause": 0.5,
}, {

    "commands": ["AT+ENTERPASSKEY=123456"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+FINDSCANDATA=FF5"],
    "status": [],
    "restart": False,
    "pause": 5
}, {

    "commands": ["AT+GAPDISCONNECT"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPIOCAP"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPPAIR"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPUNPAIR"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GAPSCAN=5"],
    "status": [],
    "restart": False,
    "pause": 6.5
}, {

    "commands": ["AT+GAPSTATUS"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GATTCREAD=001B"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GATTCWRITE=001B HELLO"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+GETSERVICES"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+NUMCOMPA"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+SCANTARGET=00:00:00:00:00:01"],
    "status": [],
    "restart": False,
    "pause": 0.5,
    "expected": "ERROR"
}, {

    "commands": ["AT+SECLVL"],
    "status": [],
    "restart": False,
    "pause": 0.5
}, {

    "commands": ["AT+SETNOTI=0012"],
    "status": [],
    "restart": False,
    "pause": 0.5,
    "expected": "ERROR"
}, {

    "commands": ["AT+SETPASSKEY=123456"],
    "status": [],
    "restart": False,
    "pause": 0.5
}]
