import random
import string

from common.base64_en_or_decode import base64encode,base64decode


def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))


name = generate_random_string(4001)


operator = [
    {
        "command": "ConvertField",
        "type": 2,
        "actions": [
            {
                "action": "data.setFieldAttr",
                "type": 2,
                "tableId": "tblsrMHNOw8SQOK8",
                "viewId": "vewMUWhTXI",
                "fieldId": "fldFTx7JTB",
                "originData": {
                    "name": "ddddd",
                    "type": 1,
                    "description": {},
                    "fieldUIType": "Text",
                    "allowedEditModes": {
                        "manual": True,
                        "scan": False
                    }
                },
                "data": {
                    "name": name,
                    "type": 1,
                    "description": {},
                    "fieldUIType": "Text",
                    "allowedEditModes": {
                        "manual": True,
                        "scan": False
                    }
                }
            }
        ],
        "syncFlag": 0
    }
]

operator2 = [
    {
        "command": "ConvertField",
        "type": 2,
        "actions": [
            {
                "action": "data.setFieldAttr",
                "type": 2,
                "tableId": "tblsrMHNOw8SQOK8",
                "viewId": "vewMUWhTXI",
                "fieldId": "fldFTx7JTB",
                "originData": {
                    "name": "ddddd",
                    "type": 1,
                    "description": {
                        "content": [
                            {
                                "type": "text",
                                "text": "112222"
                            }
                        ],
                        "disableSync": False
                    },
                    "fieldUIType": "Text",
                    "allowedEditModes": {
                        "manual": True,
                        "scan": False
                    }
                },
                "data": {
                    "name": "ddddd",
                    "type": 1,
                    "description": {
                        "content": [
                            {
                                "type": "text",
                                "text": name
                            }
                        ],
                        "disableSync": False
                    },
                    "fieldUIType": "Text",
                    "allowedEditModes": {
                        "manual": True,
                        "scan": False
                    }
                }
            }
        ],
        "syncFlag": 0
    }
]
print(base64encode(operator2))