import json

groupList = "[{\"condition\":{\"fieldID\":\"fldhdu4T3G\",\"groupKey\":\"optxeUCvTK\"},\"count\":10,\"children\":[{\"condition\":{\"fieldID\":\"fldr72DBCa\",\"groupKey\":\"optgbdbiLA\"},\"count\":9,\"children\":null}]}]"
print(groupList)
a = [
    {"groupByList":
        [
            {"fieldID": "fldyuqYn3m", "groupKey": [{"text": "1", "type": "text"}]},
            {"fieldID": "fldO2HZN46", "groupKey": [{"text": "1", "type": "text"}]},
            {"fieldID": "fldMTKalwI", "groupKey": [{"text": "1", "type": "text"}]}
        ]
    }
]
# print(json.dumps(a).replace(' ', ''))
account = {
    "owner": {
        "user_id": 7091186056053129235,
        "session": "XN0YXJ0-442o1bf7-ab2f-4a3a-ac1e-51c42c1056og-WVuZA",
        "name": "朱贵兵",
        "tenantID": 1,
        "tenant_url": "https://bytedance.feishu-boe.net/",
        "api_domain": "https://internal-api-space.feishu-boe.net"
    },
    "editor": {
        "user_id": 7218013830545145876,
        "session": "XN0YXJ0-043lccd0-ee4b-4d6e-9697-a79e016ee1gs-WVuZA",
        "name": "朱贵兵2",
        "tenantID": 1,
        "tenant_url": "https://bytedance.feishu-boe.net/",
        "api_domain": "https://internal-api-space.feishu-boe.net"
    }
}

test_data_sv6 = {
    "no_perm": {
        "sv6": {
            "2k": {
                "base": "UOcWbaa5faruxsspgdkbXjtBced",
                "table": "tbl9eNTVpVsP6szF",
                "view": "vew1fN3i1v"
            },
            "2w": {
                "base": "F45Nbhuq1alUlUseL55bVa5vcBc",
                "table": "tbl7Vh0MsZYfh7e4",
                "view": "vew1fN3i1v"
            }
        },
        "sv5": {
            "2k": {
                "base": "PkPVbJ04haP4EosCsQ3bBrF6cvg",
                "table": "tbl9Y2QvMvOV60Wi",
                "view": "vewVC4VbJU"
            },
            "2w": {
                "base": "CXRcbNNrLa1DWBsC9sQbtrKxcuh",
                "table": "tbl2wceLXvFS2bpX",
                "view": "vew4CX9yFW"
            }
        },
        "sv3": {
            "2k": {
                "base": "K59LbnNz4a1Mf7sVkSSbjYnjcDd",
                "table": "tblp6jHh7WtdP4tP",
                "view": "vewWcmc7tZ"
            },
            "2w": {
                "base": "MQN4bSGbeaqheas1fDubb6DIcHc",
                "table": "tblueOcguntg5iPb",
                "view": "vewctTK9Az"
            }
        },
        "sv2": {
            "2k": {
                "base": "RIa5bxwWPap3igs8Ha7bMN2Wcwg",
                "table": "tblfREYR1Y7tCTkb",
                "view": "vewH4B3p7b"
            },
            "2w": {
                "base": "AlQNbT8WmaD2IwsGg9sbwzaIcYb",
                "table": "tblmiGRUv7j1F1J1",
                "view": "vewmECoBWE"
            }
        },
        "viewInfoMap": {
            "base": "KeTxbZ9e1a9q1PsEn2PbayDJcDe",
            "table": "tblo9IhJL05YhhSz",
            "view": "vewXGjPnwq",
            "view_2": "vewFq3iNB6"
        },
        "getGroupsInfos": {
            "base": "CuaCbUEcPakpIksem8SbrUZScFg",
            "table": "tbl9cBtLAZf3rFJI",
            "view_group": "vewUNAjelb",
            "view_no_group": "vewCJ6demf",
            "groupConf": [
                {"fieldId": "fldkSYFaZz", "groupKey": [{"type": "text", "text": "1"}]},
            ]
        },
        "getStatsInfo": {
            "base": "DvREbdCh1aEYGNslncdbuh3Scbb",
            "table": "tblYBGdEOLAZtXpF",
            "view": "vewHQoCjPg",
            "field_id": ["fldyuqYn3m", "fldO2HZN46", "fldMTKalwI"]
        },
        "searchRecord": {
            "base": "X2FQb9MbTaNrvfsgKiQbDXQZc9e",
            "table": "tblJm3jVFzdDVLU0",
            "view": "vewQFEF6HY",
            "commentIdList": ["1712656621930001907"],
            "mentionIdList": ["1712720288660615210"],
        },
        "miniClientVars": {
            "base": "LAdEbSMtXaQ0IAs0Trkbofxncpg",
            "table": "tblxh7a1ByfRafhd",
            "view": "vewGDvDwQe"
        },
        "clientVars": {
            "base": "ALwVbrwVTaux05s6YgdbB9lRcEe",
            "table": "tbl3RJsHWzefsWSD",
            "view": "vewGDvDwQe"
        },
        "ondemandRecords": {
            "base": "RSjwbGEPJab6ODs2TtcbxDjScxe",
            "table": "tblneeuMhD7m6cNq",
            "view": "vewCJ6demf"
        }
    },
    "perm": {}
}
groups = json.loads(
    "[{\"offset\":0,\"limit\":1,\"groupByList\":[{\"fieldID\":\"fld0hY9RVO\",\"groupKey\":null},{\"fieldID\":\"fldNl5BJwc\",\"groupKey\":null}]}]")
print(groups)

# fld0hY9RVO
# fldNl5BJwc
# fldKqgQ0eP
# flden2KRbb
# fldq0rTCzb
# fldw6eYrxN
# fldLM4gKLK
# fldvpjtrBi
# fld0lWf0Ok
# fldeE9QEZt
# fldWX9z6pu
groups = [
    {
        'offset': 0,
        'limit': 1,
        'groupByList': [
            {'fieldID': 'fld0hY9RVO', 'groupKey': None},
            {'fieldID': 'fldNl5BJwc', 'groupKey': None},
            {'fieldID': 'fldKqgQ0eP', 'groupKey': None},
            {'fieldID': 'flden2KRbb', 'groupKey': None},
            {'fieldID': 'fldq0rTCzb', 'groupKey': None},
            {'fieldID': 'fldw6eYrxN', 'groupKey': None},
            {'fieldID': 'fldLM4gKLK', 'groupKey': None},
            {'fieldID': 'fldvpjtrBi', 'groupKey': None},
            {'fieldID': 'fld0lWf0Ok', 'groupKey': None},
            {'fieldID': 'fldeE9QEZt', 'groupKey': None},
            {'fieldID': 'fldWX9z6pu', 'groupKey': None}
        ]
    }
]
print(json.dumps(groups).replace('"', '\\"'))
