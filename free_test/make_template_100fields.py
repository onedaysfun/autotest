import csv
import random
import time

from common.send_message_cs import EditTable

if __name__ == '__main__':
    table = 'tblyG17wxhfhUlkL'
    parent_token = 'OGmAbx7MdavBWQsSLGmbIgBKcff'
    table_rev = 48
    base_rev = 0
    domain = 'https://bytedance.feishu-boe.net'
    session = 'XN0YXJ0-dd5ic30d-5c00-4ae6-a2d5-3ec04d9844pj-WVuZA'

    # init table edit class
    cli = EditTable(session, table, table_rev, parent_token, domain)
    random_field_list = [
        {'Currency': 2},
        {'Text': 1},
        {'Email': 1},
        {'Checkbox': 7},
        {'Number': 2},
        {'Barcode': 1},
        {'DateTime': 5},
        {'Phone': 13},
        {'AutoNumber': 1005},
        {'Progress': 2},
        {'Url': 15}
    ]
    # for i in range(29):
    #     cli.add_field_random(random_field_list, 10)
    #     time.sleep(1)
    # cli.add_field_random(random_field_list, 5)
    fieldMap = {
        "fldeLHwZaQ": {
            "id": "fldeLHwZaQ",
            "name": "人员",
            "type": 11,
            "property": {
                "multiple": False
            },
            "description": {},
            "fieldUIType": "User"
        },
        "fldLAbT0Du": {
            "id": "fldLAbT0Du",
            "name": "单选",
            "type": 3,
            "property": {
                "options": [],
                "optionsType": 0,
                "optionsRule": None
            },
            "description": {},
            "fieldUIType": "SingleSelect"
        },
        "fldK7lbFEv": {
            "id": "fldK7lbFEv",
            "name": "多选",
            "type": 4,
            "property": {
                "optionsRule": None,
                "options": [],
                "optionsType": 0
            },
            "description": {},
            "fieldUIType": "MultiSelect"
        },
        "fldxecuAgX": {
            "id": "fldxecuAgX",
            "name": "文本",
            "type": 1,
            "description": {},
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            }
        },
        "fld1gwR1xC": {
            "id": "fld1gwR1xC",
            "name": "讨论群",
            "type": 23,
            "property": {
                "multiple": False
            },
            "description": {},
            "fieldUIType": "GroupChat"
        },
        "fldz4QRrwP": {
            "id": "fldz4QRrwP",
            "name": "Email-88",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldtCePqdc": {
            "id": "fldtCePqdc",
            "name": "DateTime-231",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fld4XL0PuQ": {
            "id": "fld4XL0PuQ",
            "name": "Url-237",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldDZzacMj": {
            "id": "fldDZzacMj",
            "name": "Text-984",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldXYIge0p": {
            "id": "fldXYIge0p",
            "name": "Progress-512",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldlxLR7jU": {
            "id": "fldlxLR7jU",
            "name": "Barcode-415",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldZgazD9i": {
            "id": "fldZgazD9i",
            "name": "Currency-307",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldWcXqNRE": {
            "id": "fldWcXqNRE",
            "name": "DateTime-52",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldViDojaJ": {
            "id": "fldViDojaJ",
            "name": "Progress-593",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldPpw41J2": {
            "id": "fldPpw41J2",
            "name": "Email-999",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fld0ZVN2gW": {
            "id": "fld0ZVN2gW",
            "name": "Text-320",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldwl75yUx": {
            "id": "fldwl75yUx",
            "name": "Phone-849",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldpHDK604": {
            "id": "fldpHDK604",
            "name": "Url-951",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld8uX3W7F": {
            "id": "fld8uX3W7F",
            "name": "DateTime-404",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldNYTOXKa": {
            "id": "fldNYTOXKa",
            "name": "Url-189",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldjnGechk": {
            "id": "fldjnGechk",
            "name": "Barcode-151",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldBo7hvd6": {
            "id": "fldBo7hvd6",
            "name": "Progress-732",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldGRjpcWd": {
            "id": "fldGRjpcWd",
            "name": "Checkbox-569",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldj7Fl4R0": {
            "id": "fldj7Fl4R0",
            "name": "Progress-62",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldBmL4eZQ": {
            "id": "fldBmL4eZQ",
            "name": "DateTime-745",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldDXfCBJy": {
            "id": "fldDXfCBJy",
            "name": "Email-73",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "flddCZNbQE": {
            "id": "flddCZNbQE",
            "name": "Currency-961",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldNWLS5fg": {
            "id": "fldNWLS5fg",
            "name": "Email-9",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldsUBYJib": {
            "id": "fldsUBYJib",
            "name": "DateTime-682",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldDLN5uKC": {
            "id": "fldDLN5uKC",
            "name": "Email-854",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldcqxrkb5": {
            "id": "fldcqxrkb5",
            "name": "Number-273",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldzJfvHEL": {
            "id": "fldzJfvHEL",
            "name": "Number-60",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld407iNIJ": {
            "id": "fld407iNIJ",
            "name": "Url-490",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldYinFD9t": {
            "id": "fldYinFD9t",
            "name": "Url-559",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldY65Z7LR": {
            "id": "fldY65Z7LR",
            "name": "Phone-360",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldQEboTOI": {
            "id": "fldQEboTOI",
            "name": "Checkbox-27",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldFPYozE5": {
            "id": "fldFPYozE5",
            "name": "AutoNumber-448",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldk0tYaiZ": {
            "id": "fldk0tYaiZ",
            "name": "Url-705",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld4guzfq0": {
            "id": "fld4guzfq0",
            "name": "Currency-473",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldZcD03yi": {
            "id": "fldZcD03yi",
            "name": "Phone-351",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldhfDtyPS": {
            "id": "fldhfDtyPS",
            "name": "Number-199",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldspPDdR0": {
            "id": "fldspPDdR0",
            "name": "Url-284",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldM6UOzDl": {
            "id": "fldM6UOzDl",
            "name": "Currency-944",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fld6w9alJd": {
            "id": "fld6w9alJd",
            "name": "AutoNumber-481",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "flddHQfMuN": {
            "id": "flddHQfMuN",
            "name": "Number-500",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldAPWp27q": {
            "id": "fldAPWp27q",
            "name": "DateTime-608",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldl132T0G": {
            "id": "fldl132T0G",
            "name": "Text-884",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldtZJrGhf": {
            "id": "fldtZJrGhf",
            "name": "Currency-114",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fld9iEp3ah": {
            "id": "fld9iEp3ah",
            "name": "Barcode-386",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldpA3gUqG": {
            "id": "fldpA3gUqG",
            "name": "Barcode-795",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldH9V5Da6": {
            "id": "fldH9V5Da6",
            "name": "Currency-180",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fld4iUP7Ij": {
            "id": "fld4iUP7Ij",
            "name": "Checkbox-404",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldGUplvzY": {
            "id": "fldGUplvzY",
            "name": "Text-141",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldngAPDbu": {
            "id": "fldngAPDbu",
            "name": "DateTime-988",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fld8NtXLEs": {
            "id": "fld8NtXLEs",
            "name": "Phone-645",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldxjlf4UT": {
            "id": "fldxjlf4UT",
            "name": "Text-416",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldN4wDSVA": {
            "id": "fldN4wDSVA",
            "name": "AutoNumber-97",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldmursihX": {
            "id": "fldmursihX",
            "name": "Checkbox-866",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldRloWEjH": {
            "id": "fldRloWEjH",
            "name": "Currency-776",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldiTjvMGa": {
            "id": "fldiTjvMGa",
            "name": "Url-924",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldzmGO0To": {
            "id": "fldzmGO0To",
            "name": "Email-870",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldW7Dq1t3": {
            "id": "fldW7Dq1t3",
            "name": "Currency-368",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldE3aKWSG": {
            "id": "fldE3aKWSG",
            "name": "Number-143",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldwVeIhCd": {
            "id": "fldwVeIhCd",
            "name": "AutoNumber-316",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldplT9Hze": {
            "id": "fldplT9Hze",
            "name": "Email-909",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldU4YZwhP": {
            "id": "fldU4YZwhP",
            "name": "AutoNumber-711",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldzeYpCX7": {
            "id": "fldzeYpCX7",
            "name": "Barcode-17",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldgUnyDmv": {
            "id": "fldgUnyDmv",
            "name": "Url-758",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldY7eaRvz": {
            "id": "fldY7eaRvz",
            "name": "Url-725",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldywBpYgm": {
            "id": "fldywBpYgm",
            "name": "Text-880",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldKq36tln": {
            "id": "fldKq36tln",
            "name": "Email-32",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldtIBZYSL": {
            "id": "fldtIBZYSL",
            "name": "Phone-746",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldH9tcSwY": {
            "id": "fldH9tcSwY",
            "name": "Phone-503",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldZvFwhjs": {
            "id": "fldZvFwhjs",
            "name": "DateTime-225",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldEWpoux9": {
            "id": "fldEWpoux9",
            "name": "Number-165",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldVx0659R": {
            "id": "fldVx0659R",
            "name": "Barcode-81",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldBiQ72Zx": {
            "id": "fldBiQ72Zx",
            "name": "Barcode-96",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldywhgUD3": {
            "id": "fldywhgUD3",
            "name": "AutoNumber-514",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldEuijgC3": {
            "id": "fldEuijgC3",
            "name": "Text-945",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldK2roaOG": {
            "id": "fldK2roaOG",
            "name": "Text-805",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "flddRCW2El": {
            "id": "flddRCW2El",
            "name": "Email-326",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldkhGgzXe": {
            "id": "fldkhGgzXe",
            "name": "Checkbox-353",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldwy4t35z": {
            "id": "fldwy4t35z",
            "name": "Email-325",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldmoWnXL4": {
            "id": "fldmoWnXL4",
            "name": "AutoNumber-133",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "flddBJ850m": {
            "id": "flddBJ850m",
            "name": "Checkbox-860",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fld1SKl5Jb": {
            "id": "fld1SKl5Jb",
            "name": "Url-522",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldxtaqVgM": {
            "id": "fldxtaqVgM",
            "name": "Url-910",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldNnmWrG7": {
            "id": "fldNnmWrG7",
            "name": "Currency-131",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fld95Ztp21": {
            "id": "fld95Ztp21",
            "name": "Text-882",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldcQ60mvM": {
            "id": "fldcQ60mvM",
            "name": "Text-598",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldhH5ETYF": {
            "id": "fldhH5ETYF",
            "name": "Phone-342",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldFqlZ192": {
            "id": "fldFqlZ192",
            "name": "Email-762",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldgPubdK0": {
            "id": "fldgPubdK0",
            "name": "Barcode-615",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldpUlOVdf": {
            "id": "fldpUlOVdf",
            "name": "Barcode-483",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldnK1uC8y": {
            "id": "fldnK1uC8y",
            "name": "Text-667",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldMs0STwv": {
            "id": "fldMs0STwv",
            "name": "Currency-685",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldm57Skls": {
            "id": "fldm57Skls",
            "name": "Text-268",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fld0VW9atS": {
            "id": "fld0VW9atS",
            "name": "DateTime-779",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldz2RLmY3": {
            "id": "fldz2RLmY3",
            "name": "Progress-642",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldBXmAqTI": {
            "id": "fldBXmAqTI",
            "name": "Progress-25",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "flduB8hgk3": {
            "id": "flduB8hgk3",
            "name": "Barcode-211",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldazUF5HL": {
            "id": "fldazUF5HL",
            "name": "Barcode-638",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldTlxzLBA": {
            "id": "fldTlxzLBA",
            "name": "Checkbox-758",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldDAYdQgy": {
            "id": "fldDAYdQgy",
            "name": "Progress-394",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldKpvQfoE": {
            "id": "fldKpvQfoE",
            "name": "Phone-743",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fld2k9DZv8": {
            "id": "fld2k9DZv8",
            "name": "Email-424",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldh98KLtV": {
            "id": "fldh98KLtV",
            "name": "Text-625",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldE5PG4FK": {
            "id": "fldE5PG4FK",
            "name": "Progress-687",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldQdCTNMA": {
            "id": "fldQdCTNMA",
            "name": "AutoNumber-249",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldlm8J3yT": {
            "id": "fldlm8J3yT",
            "name": "Number-981",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldES52H6s": {
            "id": "fldES52H6s",
            "name": "Progress-246",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldx7tPQj0": {
            "id": "fldx7tPQj0",
            "name": "Url-692",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld4MsgXJK": {
            "id": "fld4MsgXJK",
            "name": "Phone-349",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldGLAYyvt": {
            "id": "fldGLAYyvt",
            "name": "Url-866",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld8ZSNLqn": {
            "id": "fld8ZSNLqn",
            "name": "Barcode-425",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldxvWbCDR": {
            "id": "fldxvWbCDR",
            "name": "Number-430",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldRciq4N9": {
            "id": "fldRciq4N9",
            "name": "Phone-966",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldWAvxqnX": {
            "id": "fldWAvxqnX",
            "name": "AutoNumber-639",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldTG2J6BN": {
            "id": "fldTG2J6BN",
            "name": "Checkbox-515",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fld5o0Mtsb": {
            "id": "fld5o0Mtsb",
            "name": "Url-921",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldk8Yy1qx": {
            "id": "fldk8Yy1qx",
            "name": "Url-120",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldNgeKlh7": {
            "id": "fldNgeKlh7",
            "name": "Progress-198",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fld9eQG2hr": {
            "id": "fld9eQG2hr",
            "name": "Url-47",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldMP7eLIB": {
            "id": "fldMP7eLIB",
            "name": "Currency-15",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldseATq9a": {
            "id": "fldseATq9a",
            "name": "AutoNumber-210",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fld1bYufs8": {
            "id": "fld1bYufs8",
            "name": "Barcode-950",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldnfzMHd3": {
            "id": "fldnfzMHd3",
            "name": "Text-755",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldjI9PDiK": {
            "id": "fldjI9PDiK",
            "name": "Number-937",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld6FjVpXc": {
            "id": "fld6FjVpXc",
            "name": "Number-436",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldvqQKo0u": {
            "id": "fldvqQKo0u",
            "name": "AutoNumber-488",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldZrq9Nx6": {
            "id": "fldZrq9Nx6",
            "name": "DateTime-786",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldkCSDo0R": {
            "id": "fldkCSDo0R",
            "name": "Barcode-228",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldhyotrA3": {
            "id": "fldhyotrA3",
            "name": "Barcode-192",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldwVyQiDG": {
            "id": "fldwVyQiDG",
            "name": "Phone-3",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldmeq6HoJ": {
            "id": "fldmeq6HoJ",
            "name": "Number-885",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld7iuxHzo": {
            "id": "fld7iuxHzo",
            "name": "Number-677",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldJRI3uNK": {
            "id": "fldJRI3uNK",
            "name": "Number-919",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld8SfyQbW": {
            "id": "fld8SfyQbW",
            "name": "DateTime-904",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldg0MOInJ": {
            "id": "fldg0MOInJ",
            "name": "Phone-892",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fld60vMdRz": {
            "id": "fld60vMdRz",
            "name": "Text-701",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fld3Sx7dAi": {
            "id": "fld3Sx7dAi",
            "name": "Number-958",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flde7PhCML": {
            "id": "flde7PhCML",
            "name": "AutoNumber-729",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldEGHRjYU": {
            "id": "fldEGHRjYU",
            "name": "Text-788",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldNBOqP6C": {
            "id": "fldNBOqP6C",
            "name": "Barcode-898",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldNdqpehG": {
            "id": "fldNdqpehG",
            "name": "Url-125",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldY2S54GF": {
            "id": "fldY2S54GF",
            "name": "Number-900",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldIycitSq": {
            "id": "fldIycitSq",
            "name": "Currency-90",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldBOhJyua": {
            "id": "fldBOhJyua",
            "name": "Phone-217",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldqltbxRA": {
            "id": "fldqltbxRA",
            "name": "Barcode-603",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fld9YH8eGw": {
            "id": "fld9YH8eGw",
            "name": "Number-250",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldf4MgZRN": {
            "id": "fldf4MgZRN",
            "name": "Url-198",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "flde71J4ju": {
            "id": "flde71J4ju",
            "name": "Checkbox-390",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldS0GWiDq": {
            "id": "fldS0GWiDq",
            "name": "Number-119",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldR5i6QwL": {
            "id": "fldR5i6QwL",
            "name": "Number-230",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldLjiZMa4": {
            "id": "fldLjiZMa4",
            "name": "Number-168",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldflgGMjH": {
            "id": "fldflgGMjH",
            "name": "Email-507",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldlni15Hs": {
            "id": "fldlni15Hs",
            "name": "Currency-652",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldlJsnE9T": {
            "id": "fldlJsnE9T",
            "name": "Url-53",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld2cWILae": {
            "id": "fld2cWILae",
            "name": "Url-439",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldStMPjYg": {
            "id": "fldStMPjYg",
            "name": "Email-322",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldm2NF7Id": {
            "id": "fldm2NF7Id",
            "name": "Progress-612",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldb5HNYPf": {
            "id": "fldb5HNYPf",
            "name": "DateTime-989",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fld5nztwxN": {
            "id": "fld5nztwxN",
            "name": "Email-661",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldjBSeZ32": {
            "id": "fldjBSeZ32",
            "name": "Url-688",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld4G8FuiV": {
            "id": "fld4G8FuiV",
            "name": "DateTime-96",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldOsVWMwn": {
            "id": "fldOsVWMwn",
            "name": "Progress-216",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldl1kH9zp": {
            "id": "fldl1kH9zp",
            "name": "Progress-234",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldTd604lw": {
            "id": "fldTd604lw",
            "name": "Url-933",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld4ecNkgD": {
            "id": "fld4ecNkgD",
            "name": "AutoNumber-112",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldTYDeNxm": {
            "id": "fldTYDeNxm",
            "name": "Checkbox-53",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldXnUfGr9": {
            "id": "fldXnUfGr9",
            "name": "AutoNumber-458",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldnhQWtgO": {
            "id": "fldnhQWtgO",
            "name": "Currency-561",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldaoCOIq3": {
            "id": "fldaoCOIq3",
            "name": "Url-190",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld2btxMIl": {
            "id": "fld2btxMIl",
            "name": "Text-165",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldoLzBF3j": {
            "id": "fldoLzBF3j",
            "name": "Checkbox-387",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldDA63QR9": {
            "id": "fldDA63QR9",
            "name": "Barcode-590",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldfL0l1aX": {
            "id": "fldfL0l1aX",
            "name": "DateTime-342",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldayEtnJM": {
            "id": "fldayEtnJM",
            "name": "Url-74",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldwiB6cpg": {
            "id": "fldwiB6cpg",
            "name": "Barcode-675",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldLmQTFo3": {
            "id": "fldLmQTFo3",
            "name": "Progress-685",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldgSE2wQd": {
            "id": "fldgSE2wQd",
            "name": "Phone-507",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldjmTF9lV": {
            "id": "fldjmTF9lV",
            "name": "AutoNumber-238",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldPpN829u": {
            "id": "fldPpN829u",
            "name": "AutoNumber-900",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldKHtq3nZ": {
            "id": "fldKHtq3nZ",
            "name": "Text-525",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldy3eAsdQ": {
            "id": "fldy3eAsdQ",
            "name": "Url-267",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldQVGgvSY": {
            "id": "fldQVGgvSY",
            "name": "Email-85",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldQkger1P": {
            "id": "fldQkger1P",
            "name": "Checkbox-911",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldQUgYoCw": {
            "id": "fldQUgYoCw",
            "name": "Text-575",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldgSX7yzG": {
            "id": "fldgSX7yzG",
            "name": "Text-475",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldsjVCOAR": {
            "id": "fldsjVCOAR",
            "name": "Checkbox-325",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fld2uy8d0f": {
            "id": "fld2uy8d0f",
            "name": "Number-292",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldDzQv7PH": {
            "id": "fldDzQv7PH",
            "name": "Barcode-295",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldfGWLUbg": {
            "id": "fldfGWLUbg",
            "name": "Phone-47",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldRnEXKHN": {
            "id": "fldRnEXKHN",
            "name": "AutoNumber-352",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldIgl37qU": {
            "id": "fldIgl37qU",
            "name": "AutoNumber-899",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldWZKAjk7": {
            "id": "fldWZKAjk7",
            "name": "Phone-615",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldZfKuV0j": {
            "id": "fldZfKuV0j",
            "name": "Progress-888",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldnKDeUHB": {
            "id": "fldnKDeUHB",
            "name": "Checkbox-526",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldvhVot5G": {
            "id": "fldvhVot5G",
            "name": "Progress-951",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldCLpKimX": {
            "id": "fldCLpKimX",
            "name": "Progress-413",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldxB6wUrk": {
            "id": "fldxB6wUrk",
            "name": "AutoNumber-535",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fld5MeRzD3": {
            "id": "fld5MeRzD3",
            "name": "DateTime-150",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldd4F3fcg": {
            "id": "fldd4F3fcg",
            "name": "Phone-315",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldgt7jT2I": {
            "id": "fldgt7jT2I",
            "name": "Url-832",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldpMj698f": {
            "id": "fldpMj698f",
            "name": "Text-477",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldsMinUrY": {
            "id": "fldsMinUrY",
            "name": "Phone-605",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fld9fkX0Da": {
            "id": "fld9fkX0Da",
            "name": "Url-522",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldwT73bM0": {
            "id": "fldwT73bM0",
            "name": "Text-708",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fld3i4wXdI": {
            "id": "fld3i4wXdI",
            "name": "Number-974",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldp8tvwjK": {
            "id": "fldp8tvwjK",
            "name": "AutoNumber-186",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldr1vMcFR": {
            "id": "fldr1vMcFR",
            "name": "Currency-346",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldHfcy2S3": {
            "id": "fldHfcy2S3",
            "name": "Email-563",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldyNPbIDO": {
            "id": "fldyNPbIDO",
            "name": "Email-886",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fld92lRKNf": {
            "id": "fld92lRKNf",
            "name": "AutoNumber-616",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldbyszTDh": {
            "id": "fldbyszTDh",
            "name": "Checkbox-184",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldRg4S8Gh": {
            "id": "fldRg4S8Gh",
            "name": "Url-722",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "flddi9TcSt": {
            "id": "flddi9TcSt",
            "name": "Number-535",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldwDZrPGE": {
            "id": "fldwDZrPGE",
            "name": "Barcode-215",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldvesgJbI": {
            "id": "fldvesgJbI",
            "name": "Currency-700",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fld7MDvVHl": {
            "id": "fld7MDvVHl",
            "name": "Currency-785",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldgaMNIoz": {
            "id": "fldgaMNIoz",
            "name": "Text-831",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldQSe0M3i": {
            "id": "fldQSe0M3i",
            "name": "Phone-929",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldq6n25JU": {
            "id": "fldq6n25JU",
            "name": "Number-951",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldRTkiuB0": {
            "id": "fldRTkiuB0",
            "name": "Text-96",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fld1MRsLcj": {
            "id": "fld1MRsLcj",
            "name": "Number-555",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldahkQ8yU": {
            "id": "fldahkQ8yU",
            "name": "Email-794",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldhqeKLtV": {
            "id": "fldhqeKLtV",
            "name": "Number-443",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldAEc2CHz": {
            "id": "fldAEc2CHz",
            "name": "Barcode-47",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fld4pzaIt1": {
            "id": "fld4pzaIt1",
            "name": "Email-869",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldn3YIKXj": {
            "id": "fldn3YIKXj",
            "name": "Currency-792",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldZE3U8HS": {
            "id": "fldZE3U8HS",
            "name": "Number-20",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldqVbFtwf": {
            "id": "fldqVbFtwf",
            "name": "Barcode-1",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldnFypSwv": {
            "id": "fldnFypSwv",
            "name": "Url-197",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldRnA0UNm": {
            "id": "fldRnA0UNm",
            "name": "Email-521",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldMCimHcV": {
            "id": "fldMCimHcV",
            "name": "Checkbox-630",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fld6CjYora": {
            "id": "fld6CjYora",
            "name": "Phone-716",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldMxrBhs1": {
            "id": "fldMxrBhs1",
            "name": "Barcode-524",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldYGcsFDX": {
            "id": "fldYGcsFDX",
            "name": "DateTime-837",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldt26uTlm": {
            "id": "fldt26uTlm",
            "name": "Phone-396",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldYje5LEi": {
            "id": "fldYje5LEi",
            "name": "Currency-192",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldgB1mMGK": {
            "id": "fldgB1mMGK",
            "name": "Url-124",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fld7KXdD3c": {
            "id": "fld7KXdD3c",
            "name": "AutoNumber-393",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldywbgAo9": {
            "id": "fldywbgAo9",
            "name": "Currency-583",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldTg8Ew9l": {
            "id": "fldTg8Ew9l",
            "name": "Currency-746",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fld8a4kfnG": {
            "id": "fld8a4kfnG",
            "name": "Barcode-250",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldD2f7uJ0": {
            "id": "fldD2f7uJ0",
            "name": "Checkbox-860",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fld5ZHIC9r": {
            "id": "fld5ZHIC9r",
            "name": "AutoNumber-505",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldZhgGT2S": {
            "id": "fldZhgGT2S",
            "name": "Currency-595",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldRLhxDIq": {
            "id": "fldRLhxDIq",
            "name": "Progress-776",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fld2d0PQam": {
            "id": "fld2d0PQam",
            "name": "Text-616",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldj6JoQhn": {
            "id": "fldj6JoQhn",
            "name": "Url-670",
            "type": 15,
            "property": {
                "extractExternalUrl": False
            },
            "fieldUIType": "Url",
            "exInfo": {
                "fieldUIType": "Url"
            }
        },
        "fldPLpRSgO": {
            "id": "fldPLpRSgO",
            "name": "Currency-969",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldalGwDx6": {
            "id": "fldalGwDx6",
            "name": "AutoNumber-940",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldvgRHObx": {
            "id": "fldvgRHObx",
            "name": "DateTime-54",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldC4Ywhgc": {
            "id": "fldC4Ywhgc",
            "name": "Progress-177",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldFHoUMh2": {
            "id": "fldFHoUMh2",
            "name": "Checkbox-307",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldZxWtngr": {
            "id": "fldZxWtngr",
            "name": "Currency-243",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldC9LJBjb": {
            "id": "fldC9LJBjb",
            "name": "Barcode-663",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldrL3dnP0": {
            "id": "fldrL3dnP0",
            "name": "Checkbox-983",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldZwNmTJt": {
            "id": "fldZwNmTJt",
            "name": "Number-215",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldYfoM4ZJ": {
            "id": "fldYfoM4ZJ",
            "name": "Progress-982",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldWFYEh4q": {
            "id": "fldWFYEh4q",
            "name": "DateTime-217",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldOhSRYLc": {
            "id": "fldOhSRYLc",
            "name": "Progress-293",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldzDRLHU9": {
            "id": "fldzDRLHU9",
            "name": "Currency-986",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldxTQVSN0": {
            "id": "fldxTQVSN0",
            "name": "Currency-711",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldfLMaEoU": {
            "id": "fldfLMaEoU",
            "name": "Checkbox-208",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldmyklp8a": {
            "id": "fldmyklp8a",
            "name": "Barcode-582",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldQaAy1Dd": {
            "id": "fldQaAy1Dd",
            "name": "Barcode-914",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldm2zJO7A": {
            "id": "fldm2zJO7A",
            "name": "DateTime-373",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldT4Y5JQq": {
            "id": "fldT4Y5JQq",
            "name": "Phone-332",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldzI8F4rf": {
            "id": "fldzI8F4rf",
            "name": "Text-783",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldChoYUwd": {
            "id": "fldChoYUwd",
            "name": "Checkbox-948",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldZmCEIU6": {
            "id": "fldZmCEIU6",
            "name": "Barcode-996",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldaWE1ArP": {
            "id": "fldaWE1ArP",
            "name": "DateTime-748",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldhqiAMf6": {
            "id": "fldhqiAMf6",
            "name": "Number-410",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldRsMJmn1": {
            "id": "fldRsMJmn1",
            "name": "Barcode-78",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldo8GWP3d": {
            "id": "fldo8GWP3d",
            "name": "Checkbox-677",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldPi4amdx": {
            "id": "fldPi4amdx",
            "name": "Text-336",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldLj7lhdq": {
            "id": "fldLj7lhdq",
            "name": "AutoNumber-944",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldfyMrIeS": {
            "id": "fldfyMrIeS",
            "name": "Progress-94",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fld4ex9O7v": {
            "id": "fld4ex9O7v",
            "name": "Email-660",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldguGorc4": {
            "id": "fldguGorc4",
            "name": "Phone-407",
            "type": 13,
            "property": None,
            "fieldUIType": "Phone",
            "exInfo": {
                "fieldUIType": "Phone"
            }
        },
        "fldXc8WNiB": {
            "id": "fldXc8WNiB",
            "name": "Barcode-392",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldacY4gLZ": {
            "id": "fldacY4gLZ",
            "name": "Text-555",
            "type": 1,
            "property": None,
            "fieldUIType": "Text",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Text"
            }
        },
        "fldhJGTISs": {
            "id": "fldhJGTISs",
            "name": "Progress-467",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fld7jWHTwK": {
            "id": "fld7jWHTwK",
            "name": "AutoNumber-865",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldKFkUtTZ": {
            "id": "fldKFkUtTZ",
            "name": "Progress-5",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldRhHY3j7": {
            "id": "fldRhHY3j7",
            "name": "Barcode-119",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldCNYUgQR": {
            "id": "fldCNYUgQR",
            "name": "Checkbox-454",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldvEzkt7D": {
            "id": "fldvEzkt7D",
            "name": "Barcode-497",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldw6qjzyD": {
            "id": "fldw6qjzyD",
            "name": "DateTime-443",
            "type": 5,
            "property": {
                "dateFormat": "yyyy/MM/dd",
                "timeFormat": "",
                "autoFill": False
            },
            "fieldUIType": "DateTime",
            "exInfo": {
                "fieldUIType": "DateTime"
            }
        },
        "fldPizvIln": {
            "id": "fldPizvIln",
            "name": "Progress-333",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldSWKQMxp": {
            "id": "fldSWKQMxp",
            "name": "Currency-600",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Currency",
            "exInfo": {
                "fieldUIType": "Currency"
            }
        },
        "fldckIjdi8": {
            "id": "fldckIjdi8",
            "name": "Checkbox-498",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fldMlw8oya": {
            "id": "fldMlw8oya",
            "name": "Progress-941",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Progress",
            "exInfo": {
                "fieldUIType": "Progress"
            }
        },
        "fldjaCOQUh": {
            "id": "fldjaCOQUh",
            "name": "AutoNumber-177",
            "type": 1005,
            "property": {
                "ruleFieldOptions": [
                    {
                        "value": "3",
                        "type": 1
                    }
                ],
                "isAdvancedRules": False,
                "reformatExistingRecord": True
            },
            "fieldUIType": "AutoNumber",
            "exInfo": {
                "fieldUIType": "AutoNumber"
            }
        },
        "fldnPz4lVL": {
            "id": "fldnPz4lVL",
            "name": "Checkbox-967",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        },
        "fld9uWL6oG": {
            "id": "fld9uWL6oG",
            "name": "Barcode-130",
            "type": 1,
            "property": None,
            "fieldUIType": "Barcode",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Barcode"
            }
        },
        "fldQVvjxRF": {
            "id": "fldQVvjxRF",
            "name": "Email-394",
            "type": 1,
            "property": None,
            "fieldUIType": "Email",
            "allowedEditModes": {
                "manual": True,
                "scan": False
            },
            "exInfo": {
                "fieldUIType": "Email"
            }
        },
        "fldbsakAHF": {
            "id": "fldbsakAHF",
            "name": "Checkbox-189",
            "type": 7,
            "property": {
                "styleId": "0"
            },
            "fieldUIType": "Checkbox",
            "exInfo": {
                "fieldUIType": "Checkbox"
            }
        }
    }
    field_id_list = list(fieldMap.keys())
    record_list = []
    with open("test.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            record_list.append(row[0])
    # 遍历记录
    for record in record_list:
        # 遍历字段
        actions = []
        for field_id in field_id_list:
            data = None
            field_info = fieldMap[field_id]
            if field_info['fieldUIType'] in ['Text', 'Barcode']:
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": [
                            {
                                "type": "text",
                                "text": "text" + str(random.randint(0,1000))
                            }
                        ]
                    }}
            elif field_info['fieldUIType'] == 'Email':
                email = str(random.randint(1,100000)) + "@" + str(random.randint(1,100000)) + "." + str(random.randint(1,100000))
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": [
                            {
                                "type": "url",
                                "text": email,
                                "link": "mailto:" + email
                            }
                        ]
                    }
                }
            elif field_info['fieldUIType'] == 'Url':
                urlList = ['www.baidu.com','www.bilibili.com','github.com','bytedance.com','google.com']
                url = random.choice(urlList)
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": [
                            {
                                "type": "url",
                                "text": url,
                                "link": "https://" + url
                            }
                        ]
                    }
                }
            elif field_info['fieldUIType'] == 'Phone':
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": {
                            "fullPhoneNum": "+" + str(random.randint(1, 100000000))
                        }
                    }
                }
            elif field_info['fieldUIType'] == 'Checkbox':
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": random.choice([False, True])
                    }
                }
            elif field_info['fieldUIType'] in ['Currency', 'Number']:
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": random.randint(-10000, 10000)
                    }
                }
            elif field_info['fieldUIType'] == 'DateTime':
                data = {
                    field_id: {
                        "type": field_info['type'],
                        "value": int(time.time() * 1000) ,
                        "reminder": None
                    }
                }
            else:
                continue
            action = {
                "action": "data.setRecord",
                "type": 2,
                "tableId": table,
                "recordId": record,
                "data": data
            }
            actions.append(action)
        operations = [
            {
                "command": "SetRecord",
                "type": 2,
                "actions": actions,
                "syncFlag": 0
            }
        ]
        cli.root_request(operations)
        time.sleep(0.5)
