# need params: table_id,view_id,field_id(NEW)
# member_id = params[0]
# obj_token = params[1]
# table_json = params[2]
# fieldId = params[3]
add_field_operation = [
    {
        "command": "AddField",
        "type": 2,
        "actions": [
            {
                "action": "data.addField",
                "type": 2,
                "tableId": "tblhMvhMMBBaeH2A",
                "viewId": "vewWvlFXXy",
                "fieldId": "fldKGtsbxm",
                "data": {
                    "name": "文本 2",
                    "type": 1,
                    "fieldUIType": "Text",
                    "enumerable": False,
                    "allowedEditModes": {
                        "manual": True,
                        "scan": False
                    },
                    "exInfo": {
                        "fieldUIType": "Text"
                    },
                    "indexes": {
                        "vewWvlFXXy": 1
                    }
                }
            }
        ],
        "syncFlag": 0
    }
]
