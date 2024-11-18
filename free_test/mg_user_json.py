import json

a = {"user_01": {"tenant_id": "7071097893049909276",
                 "tenant_domain": "e5test1655436560",
                 "root_domain": ".feishu.cn",
                 "tenant_url": "e5test1655436560.feishu.cn",
                 "name": "bitable-feishu-cn-online05卡点",
                 "enname": "bitable-feishu-cn-online05卡点",
                 "user_id": 7144998225501634562,
                 "avatarUrl": "",
                 "session": "XN0YXJ0-63fl35c7-6890-4cdd-95cf-bb073a869f73-WVuZA"},
     "user_02": {"tenant_id": "7071097893049909276",
                 "tenant_domain": "e5test1655436560",
                 "root_domain": ".feishu.cn",
                 "tenant_url": "e5test1655436560.feishu.cn",
                 "name": "bitable-feishu-cn-online06卡点",
                 "enname": "bitable-feishu-cn-online06卡点",
                 "user_id": 7161306251832442908,
                 "avatarUrl": "",
                 "session": "XN0YXJ0-f7ete9ef-d324-4f2b-a6a2-90017d7fdaef-WVuZA"},
     "user_03": {"tenant_id": "7071097893049909276",
                 "tenant_domain": "e5test1655436560",
                 "root_domain": ".feishu.cn",
                 "tenant_url": "e5test1655436560.feishu.cn",
                 "user_id": 7144997712834314241,
                 "session": "XN0YXJ0-de5ob881-00c3-464b-9f56-6c6974a67678-WVuZA"}}

feishu01_cn = {
    "tenant_id": "7248912367147728898",
    "tenant_domain": "yq4fc040c3v",
    "root_domain": ".feishu.cn",
    "tenant_url": "yq4fc040c3v.feishu.cn",
    "name": "主租户BASE-CN",
    "enname": "主租户BASE-CN",
    "user_id": 7269396164267474947,
    "avatarUrl": "https://s16-imfile-sg.feishucdn.com/static-resource/avatar/v2_eb0c09ce-01a4-44bc-911e-85b5ff83894g_320.webp",
    "session": "XN0YXJ0-4d5pf5dd-0a44-4847-bb49-fdda9d97c5aa-WVuZA",
    "test_file_folder": "V6KbfaLjDlnzstdEU6vcH5ZSnbc"
}
feishu01_sg = {
    "tenant_id": "7248912367147728898",
    "tenant_domain": "yq4fc040c3v",
    "root_domain": ".feishu.cn",
    "tenant_url": "yq4fc040c3v.feishu.cn",
    "name": "主租户BASE-SG",
    "enname": "",
    "user_id": 7268957031548076064,
    "avatarUrl": "",
    "session": "XN0YXJ0-3aet5a46-67b1-4d32-bc8e-f61c65ua9ar1-WVuZA",
    "test_file_folder": ""
}
feishu02_sg = {
    "tenant_id": "7031501951141445633",
    "tenant_domain": "qi55yo5o2e",
    "root_domain": ".feishu.cn",
    "tenant_url": "qi55yo5o2e.feishu.cn",
    "name": "SG关联租户BASE-SG",
    "enname": "",
    "user_id": 7288536971490623519,
    "avatarUrl": "",
    "session": "XN0YXJ0-700t9c24-e356-4e1f-99ef-0cfa68o408p5-WVuZA",
    "test_file_folder": "LGObffUAilmEhrdE6facfZuJnBf"
}
feishu03_jp = {
    "tenant_id": "7071097893049909276",
    "tenant_domain": "e5test1655436560",
    "root_domain": ".feishu.cn",
    "tenant_url": "e5test1655436560.feishu.cn",
    "name": "JP关联租户BASE-JP",
    "enname": "",
    "user_id": 7288587976194392098,
    "avatarUrl": "",
    "session": "XN0YXJ0-463g358c-e740-46ae-8ff8-496468gvv81m-WVuZA",
    "test_file_folder": "KO8cfPY7glqhymdHF0ZctgAInae"
}
user_list = {
    "feishu01_cn": feishu01_cn,
    "feishu01_sg": feishu01_sg,
    "feishu02_sg": feishu02_sg,
    "feishu03_jp": feishu03_jp
}
account_mg = {
    "feishu01": {
        "cn": [feishu01_cn],
        "sg": [feishu01_sg]
    },
    "feishu02": {
        "sg": [feishu02_sg]
    },
    "feishu03": {
        "jp": [feishu03_jp]
    }
}
# print(json.dumps(account_mg))
table_json = {
  "meta": {
    "id": "tbl53cX3AwcxmhKW",
    "rev": 2,
    "schemaVersion": 3,
    "recordsNum": 11,
    "level": 0,
    "depRev": "",
    "jointRev": -1,
    "exType": 0
  },
  "views": [
    "vewiTtwFi8"
  ],
  "viewMap": {
    "vewiTtwFi8": {
      "id": "vewiTtwFi8",
      "name": "表格",
      "isPrivate": False,
      "type": 1,
      "owner": "7269396164267474947",
      "publicLevel": 0,
      "privateViewOwner": None,
      "property": {
        "records": [],
        "fields": [
          "fldfWFTQmx",
          "fldeHd4ZAF",
          "fldYlWIoA7",
          "fldOtUyrdk",
          "fldHajdLAo",
          "fldnvjpk19",
          "fldGCaKPSU",
          "fldQ8Aex8C"
        ],
        "sortInfo": [],
        "group": [],
        "filterInfo": None,
        "colInfos": {},
        "rowHeightLevel": 1,
        "frozenColCount": 1,
        "cardViewSetting": None,
        "hierarchyConfig": None
      }
    }
  },
  "commentMap": {},
  "resourceMap": {},
  "fieldMap": {
    "fldHajdLAo": {
      "name": "单选",
      "isPrimary": False,
      "type": 3,
      "property": {
        "optionsType": 0,
        "optionsRule": None,
        "options": []
      },
      "description": {},
      "fieldUIType": "SingleSelect"
    },
    "fldnvjpk19": {
      "name": "多选",
      "isPrimary": False,
      "type": 4,
      "property": {
        "optionsType": 0,
        "optionsRule": None,
        "options": []
      },
      "description": {},
      "fieldUIType": "MultiSelect"
    },
    "fldGCaKPSU": {
      "name": "日期",
      "isPrimary": False,
      "type": 5,
      "property": {
        "dateFormat": "yyyy/MM/dd",
        "timeFormat": "",
        "displayTimeZone": False,
        "autoFill": False
      },
      "description": {},
      "fieldUIType": "DateTime"
    },
    "fldQ8Aex8C": {
      "name": "附件",
      "isPrimary": False,
      "type": 17,
      "property": {
        "capture": []
      },
      "description": {},
      "fieldUIType": "Attachment"
    },
    "fldfWFTQmx": {
      "name": "文本",
      "isPrimary": False,
      "type": 1,
      "description": {},
      "fieldUIType": "Text",
      "allowedEditModes": {
        "manual": True,
        "scan": False
      }
    },
    "fldYlWIoA7": {
      "name": "讨论群",
      "isPrimary": False,
      "type": 23,
      "property": {
        "multiple": False
      },
      "description": {},
      "fieldUIType": "GroupChat"
    },
    "fldeHd4ZAF": {
      "name": "文本 2",
      "isPrimary": False,
      "type": 1,
      "description": {},
      "fieldUIType": "Text",
      "allowedEditModes": {
        "scan": False,
        "manual": True
      },
      "exInfo": {
        "fieldUIType": "Text"
      }
    },
    "fldOtUyrdk": {
      "name": "人员",
      "isPrimary": False,
      "type": 11,
      "property": {
        "multiple": False
      },
      "description": {},
      "fieldUIType": "User"
    }
  },
  "currentView": "vewiTtwFi8",
  "groupList": [
    {
      "by": None,
      "recordIDList": [
        "rechjDeJOB",
        "recutpz2N3",
        "recY1vBWwe",
        "recrk9jsMg",
        "recPjYPnv4",
        "recuymCc56",
        "recztPEHsE",
        "rec1h47d61",
        "recven7W9v",
        "rec7hDjZXn",
        "rec8MI7YvR"
      ],
      "firstRecordOffset": 0,
      "groupRecordNum": 0
    }
  ],
  "viewGroupNum": 0,
  "viewRecordNum": 0,
  "recordCount": 11,
  "recordMeta": {
    "recztPEHsE": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "rechjDeJOB": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recY1vBWwe": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recrk9jsMg": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "rec1h47d61": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "rec7hDjZXn": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "rec8MI7YvR": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698820801,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recPjYPnv4": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recuymCc56": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recutpz2N3": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recven7W9v": {
      "recMeta": {
        "rev": 0,
        "createdTime": 1698809233,
        "createdUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "modifiedUser": "7269396164267474947"
      }
    }
  },
  "cascadeProxyFieldMap": None,
  "formulaInfo": {
    "code": 0,
    "fieldMap": None,
    "calcCompletionTime": 0
  },
  "recordMap": {
    "recY1vBWwe": {
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "recPjYPnv4": {
      "fldGCaKPSU": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldnvjpk19": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      }
    },
    "recuymCc56": {
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedTime": 1698809233,
        "value": None,
        "modifiedUser": "7269396164267474947"
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldOtUyrdk": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "recztPEHsE": {
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldYlWIoA7": {
        "modifiedTime": 1698809233,
        "value": None,
        "modifiedUser": "7269396164267474947"
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "rec1h47d61": {
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedTime": 1698809233,
        "value": None,
        "modifiedUser": "7269396164267474947"
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "rec8MI7YvR": {
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedTime": 1698820801,
        "value": None,
        "modifiedUser": "7269396164267474947"
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698820801,
        "value": None
      }
    },
    "rechjDeJOB": {
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "recutpz2N3": {
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedTime": 1698809233,
        "value": None,
        "modifiedUser": "7269396164267474947"
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "rec7hDjZXn": {
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldHajdLAo": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    },
    "recrk9jsMg": {
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldGCaKPSU": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "value": None,
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233
      },
      "fldHajdLAo": {
        "modifiedTime": 1698809233,
        "value": None,
        "modifiedUser": "7269396164267474947"
      }
    },
    "recven7W9v": {
      "fldGCaKPSU": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldQ8Aex8C": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldfWFTQmx": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldYlWIoA7": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldeHd4ZAF": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldOtUyrdk": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      },
      "fldHajdLAo": {
        "modifiedTime": 1698809233,
        "value": None,
        "modifiedUser": "7269396164267474947"
      },
      "fldnvjpk19": {
        "modifiedUser": "7269396164267474947",
        "modifiedTime": 1698809233,
        "value": None
      }
    }
  },
  "rankInfo": {
    "nextRank": "i0006v7y8",
    "rankMap": {
      "rec7hDjZXn": "i0005m9s0",
      "recrk9jsMg": "i0001vf9c",
      "rechjDeJOB": "i00000000",
      "recutpz2N3": "i0000mh34",
      "recuymCc56": "i00034dfk",
      "recztPEHsE": "i0003quio",
      "recY1vBWwe": "i00018y68",
      "recven7W9v": "i0004zsow",
      "rec1h47d61": "i0004dbls",
      "recPjYPnv4": "i0002hwcg",
      "rec8MI7YvR": "i00068qv4"
    },
    "viewRankMap": {
      "vewiTtwFi8": {}
    }
  },
  "cs": [],
  "deniedRecords": None,
  "tablePerm": True,
  "milestoneMap": {},
  "schemaVersion": 3,
  "userMap": {
    "7269396164267474947": {
      "name": "主租户BASE-CN",
      "enName": "主租户BASE-CN",
      "avatarUrl": "https://s1-imfile.feishucdn.com/static-resource/v1/v2_eb0c09ce-01a4-44bc-911e-85b5ff83894g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp"
    }
  },
  "primaryKey": "fldfWFTQmx"
}

if __name__ == '__main__':
    print(table_json["fieldMap"].__len__())
    tabldFieldMap = {}
    for i in table_json["fieldMap"]:
          tabldFieldMap[i] = {"type": table_json["fieldMap"][i]["type"]}
    print(tabldFieldMap)
    print(list(table_json["fieldMap"].keys())[0])
    if "fldOtUyrdk" not in table_json["fieldMap"].keys():
        print("dasdasdsa")