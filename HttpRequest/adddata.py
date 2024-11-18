b = {"type": "BITABLE_TABLE", "data": {"member_id": 23052941239901,
                                       "user_ticket": "cZLcr4v1DxB7f9YSIJamQ6zX3VbEo9rycku1HCpA430SsDv4AHkIzJmVH0pU5hzPKsuTVeeWRAGXMX+aXZ06WUUysfYMDc/LkPTZ6Gmnp0HlCL6rzN5H6/pd+Dt1JkYw7Ou4oQ3sVKHlC81d3NGR3A==",
                                       "type": "USER_CHANGES", "token": "tblQLHxjTRIGWAby", "lang": "zh", "localRev": 0,
                                       "operations": "H4sIAAAAAAACA1WNsQ6CMBRF/+XNjWnQENONRW3iIMToQBgebWPQUhBqgRD+3YI6uN3cd+556QiiKks0EhhEUiZKVI1sLwEQsEOtgAUEUNiiMi2wdPxmD0u0uMLf4n9gMdeKz0qb6/h46O/nhO+vUT54yhWqW25OdX1Ud+vTy7fNoll6H3VoBY+57+c3wMaPMkHz8EBBKQ23T7eBacoItIMRO403YHTK3haEU7vRAAAA",
                                       "signature": "8e7c5d1d-b9a6-42b9-b1ff-66f84728d234",
                                       "content_type": "gzip/base64", "route_key": "Jd6wbcMXxa26vrsIz7ocIrvun1c"},
     "version": 2, "req_id": 53,
     "context": {"os": "mac", "app_version": "1.0.12.3341", "os_version": "10.15.7", "platform": "web",
                 "request_id": "4agqec1A1H0T-5df88c5a3c85af53312496e917a5fb7d682c8275"}}


operations = [
  {
    "command": "AddRecordsV2",
    "type": 2,
    "actions": [
      {
        "action": "data.addRecordV2",
        "type": 2,
        "tableId": "tblQLHxjTRIGWAby",
        "viewId": "vewxApw3Pu",
        "recordId": "recl6tcIQI",
        "data": {
          "tableRank": "i00068qv4"
        }
      }
    ],
    "syncFlag": 0
  }
]


def set_rce_message_data02(*parmas,**kwargs):
    """
    函数描述
    """
    import json
    member_id = parmas[0]
    obj_token = parmas[1]
    table_json = parmas[2]
    record_id = parmas[3]
    tableId = table_json["meta"]["id"]
    viewId = table_json["views"][0]
    operation_uncode = [
  {
    "command": "AddRecordsV2",
    "type": 2,
    "actions": [
      {
        "action": "data.addRecordV2",
        "type": 2,
        "tableId": tableId,
        "viewId": viewId,
        "recordId": record_id,
        "data": {
          "tableRank": "i00068qv4"
        }
      }
    ],
    "syncFlag": 0
  }
]
    def base64_encode(obj):
        import gzip
        import base64
        import json
        data = gzip.compress(json.dumps(obj).encode())
        result = base64.b64encode(data).decode("utf-8")
        return result

    obj_data=base64_encode(operation_uncode)
    data1={
    "type": "BITABLE_TABLE",
    "data": {
        "member_id": member_id,
        "type": "USER_CHANGES",
        "token": tableId,
        "lang": "zh",
        "localRev": table_json["meta"]["rev"],
        "operations": obj_data,
        "content_type": "gzip/base64",
        "route_key": obj_token
    }
}
    data=json.dumps(data1)
    return data