import base64
import gzip
import json
import mg_user_json


def set_role_req_body_read(*params,**kwargs):
    """
    函数描述
    """
    import json
    table_json = params[0]
    role_id = params[1]
    table_id = table_json["meta"]["id"]
    schemaVersion = table_json["meta"]["schemaVersion"]
    return json.dumps({"baseRole":{"name":"可阅读","roleId":role_id,"members":[],"tableRoleMap":{table_id:{"tableId":table_id,"perm":1,"templateId":1,"schemaVersion":schemaVersion}}}})


def set_add_member_body_read(*params, **kwargs):
    """
    :param params:
    :param kwargs:
    :return:
    """
    import json
    table_json = params[0]
    role_id = params[1]
    account_info = params[2]
    table_id = table_json["meta"]["id"]
    schemaVersion = table_json["meta"]["schemaVersion"]
    user_id = account_info["user_id"]
    user_name = account_info["name"]
    user_memberAvatarUrl = account_info["avatarUrl"]
    format_body = {
        "needAddCollaborators": True,
        "baseRole": {
            "blockRoleMap": None,
            "roleId": role_id,
            "name": "可阅读",
            "members": [
                {
                    "memberId": str(user_id),
                    "memberType": 1,
                    "memberName": user_name,
                    "memberAvatarUrl": user_memberAvatarUrl,
                    "memberEnName": user_name,
                    "memberCrossTenant": True}]
                    }}
    return json.dumps(format_body)


def set_add_role_body(*params, **kwargs):
    """
    :param params:
    :param kwargs:
    :return:
    """
    table_json = params[0]
    role_id = params[1]
    account_info = params[2]
    table_id = table_json["meta"]["id"]
    schemaVersion = table_json["meta"]["schemaVersion"]
    user_id = account_info["user_id"]
    user_name = account_info["name"]
    user_memberAvatarUrl = account_info["avatarUrl"]
    format_body = {
        "needAddCollaborators": True,
        "baseRole": {
            "blockRoleMap": None,
            "roleId": role_id,
            "name": "无权限",
            "members": [
                {
                    "memberId": user_id,
                    "memberType": 1,
                    "memberName": user_name,
                    "memberAvatarUrl": user_memberAvatarUrl,
                    "memberEnName": user_name,
                    "memberCrossTenant": True}],
            "tableRoleMap": {
                table_id: {
                    "tableId": table_id,
                    "perm": 0,
                    "recRule": None,
                    "fieldPerm": None,
                    "templateId": 0,
                    "fieldPermV2": None,
                    "schemaVersion": schemaVersion}}}}
    return json.dumps(format_body)


def base64decode(*params):
    encoded = params[0]
    data = gzip.decompress(base64.b64decode(encoded))
    result = json.loads(data.decode("utf-8"))
    return result


def base64_encode(obj):
    data = gzip.compress(json.dumps(obj).encode())
    result = base64.b64encode(data).decode("utf-8")
    return result


def set_url(*params, **kwargs):
    """
    :param params:
    :param kwargs:
    :return:
    """
    domain = params[0]["tenant_url"]
    url_temp = {
        # create
        "create_base": "/space/api/explorer/v2/create/object/",
        # clientVars
        "client_var": "space/api/v1/bitable/{obj_token+}/clientvars?&needBase=true",
        # role
        "add_role": "/space/api/bitable/roles/{obj_token}/create",
        "update_role": "space/api/bitable/roles/{obj_token}/update",
        "list_role": "space/api/bitable/{obj_token}/roles"
    }

    if kwargs["method_mod"] == "role":
        url = url_temp[params[1]].format(obj_token=params[2])
        return "https://"+domain+url
    if kwargs["method_mod"] == "create":
        return "https://"+domain+url_temp["create_base"]
    if kwargs["method_mod"] == "clientVars":
        return "https://"+domain+url_temp["client_var"].format(obj_token=params[1])


def rec_messaage_data_add_record(*params,**kwargs):
    """
    函数描述
    """
    import json
    member_id = params[0]
    obj_token = params[1]
    table_json = params[2]
    record_id = params[3]
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


def rec_messaage_data_add_field(*params,**kwargs):
    """
    函数描述
    """
    import json
    member_id = params[0]
    obj_token = params[1]
    table_json = params[2]
    fieldId = params[3]
    tableId = table_json["meta"]["id"]
    viewId = table_json["views"][0]
    operation_uncode = [
  {
    "command": "AddField",
    "type": 2,
    "actions": [
      {
        "action": "data.addField",
        "type": 2,
        "tableId": tableId,
        "viewId": viewId,
        "fieldId": fieldId,
        "data": {
          "name": "sg用户02加到字段",
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
            viewId: 1
          }
        }
      }
    ],
    "syncFlag": 0
  }
]

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


def set_automation_send_massage_body(*params, **kwargs):
    """
    格式化请求体
    """
    import json
    import random
    import string
    ###获取/定义参数
    base_token = params[0]
    account_info = params[1]
    table_json = params[2]
    trigger_token = "tri" + "".join(random.sample(string.ascii_letters + string.digits, 9))
    action_token = "act" + "".join(random.sample(string.ascii_letters + string.digits, 9))
    ###参数变换
    user_id = account_info["user_id"]
    user_name = account_info["name"]
    user_department = "MG CN 测试租户(SG)"
    msg = "test"
    base_token = base_token
    base_token_use = f"\"{base_token}\""
    table_token = table_json["meta"]["id"]
    table_token_use = f"\"{table_token}\""
    trig_id = "trig_99d1ec"
    act_id = "act_361ac0"
    tabldFieldMap = {}
    for i in table_json["fieldMap"]:
          tabldFieldMap[i] = {"type": table_json["fieldMap"][i]["type"]}
    watch_field = list(table_json["fieldMap"].keys())[0]
    watch_field_use = {"fieldID": watch_field}
    flowSchema_parameters_ReceiverInfo = '{"ReceiverType":4,"Receivers":expr.flatten([{"UserType":4,"UserID":"user_id"}])}'
    flowSchema_parameters_ReceiverInfo_use = flowSchema_parameters_ReceiverInfo.replace("user_id", f"{user_id}")
    flowSchema_parameters_msg = '{"Header":{"title":{"content":expr.join(["massage_text"], ""),"tag":"plain_text"},"template":"purple"},"Elements":expr.flatten(expr.flatten([{"tag":"markdown","content":expr.join(expr.flatten(["massage_text"]), "")}]))}'
    flowSchema_parameters_msg_use = flowSchema_parameters_msg.replace("massage_text", f"{msg}")

    flowSchema = {"type": "standard",
                  "startAt": act_id,
                  "states": {
                      act_id: {
                          "type": "task",
                          "id": act_id,
                          "config": {
                              "type": "servicemanager",
                              "config": {"bizId": "bitable",
                                         "metaVersion": "v1",
                                         "metaName": "bitable",
                                         "domainName": "automation",
                                         "apiName": "notifyV2API"}},
                          "parameters": {
                              "ReceiverInfo": flowSchema_parameters_ReceiverInfo_use,
                              "Msg": flowSchema_parameters_msg_use
                          },
                          "end": True}},
                  "trigger": {
                      "type": "servicemanager",
                      "id": trig_id,
                      "parameters": {
                          "BaseToken": base_token_use,
                          "TableID": table_token_use,
                          "TriggerParam": f"{watch_field_use}"
                      },
                      "config": {
                          "domainName": "automation",
                          "eventName": "addRecordV2",
                          "bizId": "bitable",
                          "bizType": "",
                          "metaVersion": "v1.12",
                          "metaName": "bitable"}
                  }

                  }
    nodeSchema = {"triggerStepId": trigger_token,
                  "firstTaskStepId": action_token,
                  "relations": {trigger_token: [{"id": trig_id, "type": "servicemanager"}],
                                action_token: [{"id": act_id, "type": "task"}]}, "version": 1}
    draft = {
        "steps": [
            {
                "id": trigger_token,
                "type": "AddRecordTrigger",
                "data":
                    {
                        "tableId": f"ref_{table_token}",
                        "watchedFieldId": watch_field},
                "next": [{"ids": [action_token]}]},
            {
                "id": action_token,
                "type": "LarkMessageAction",
                "data": {
                    "notifyIdentity": "mixed",
                    "robotType": "bitable",
                    "persons": [
                        {
                            "type": "ref",
                            "id": f"{user_id}",
                            "value": f"{user_name}",
                            "tagType": "user",
                            "owner_type": 0,
                        }
                    ],
                    "groups": [
                        {
                            "type": "ref",
                            "id": f"{user_id}",
                            "value": f"{user_name}",
                            "tagType": "user",
                            "owner_type": 0,
                        }
                    ],
                    "title": [{"text": "test", "type": "text"}],
                    "titleTemplateColor": "purple",
                    "content": [{"text": "test", "type": "text"}],
                    "btnList": [
                        {
                            "btnKey": "message_btn_GgdtBm30",
                            "btnAction": "openLink",
                            "btnStyle": "primary",
                            "text": "查看记录详情",
                            "link": [
                                {
                                    "id": f"{trigger_token}-{table_token}-recordUrl11",
                                    "tagType": "stepLink",
                                    "stepId": trigger_token, "stepType": "AddRecordTrigger",
                                    "tableId": f"ref_{table_token}",
                                    "isShortcut": True, "fieldId": f"ref_{table_token}_", "viewId": "", "value": "",
                                    "stepNum": 1, "type": "ref"}]}], "needBtn": False, "needTopBase": True}, "next": []}
        ],
        "title": "发送消息",
        "tabldFieldMap": {
            table_token: tabldFieldMap
                }
    }
    extra = {
        "TableMap":
            {
                f"ref_{table_token}":
                    {
                        "TableID": table_token,
                        "FieldMap": {f"ref_{table_token}_": ""}}
            },
        "BlockMap": {}
    }
    automation_body = {
        "token": base_token,
        "draft": json.dumps(draft).replace(" ", ""),
        "extra": json.dumps(extra).replace(" ", ""),
        "triggerName": "addRecordV2",
        "status": 0,
        "flowSchema": json.dumps(flowSchema).replace(" ", ""),
        "nodeSchema": json.dumps(nodeSchema).replace(" ", ""),
        "source": "topbar_click_from_blank"
    }
    return json.dumps(automation_body).replace(" ", ""),draft


if __name__ == '__main__':
    account = mg_user_json.feishu01_cn
    table_json = {
        "meta": {
            "id": "tblQX35QvYoA5kWa",
            "rev": 0,
            "schemaVersion": 3
        }}
    role_id = "dasdasd"
    # print(set_add_role_body(table_json, role_id, account))
    encode = "H4sIAAAJbogA/2yQy2rzMBCF32XWXmTtbeD" \
             "/KW1KCCF7VTpup5U0ZiQlMSHvXuRLakp3Pp89PpcbBWRD7Y3YUUvUkOJM7aahZD8QzAmaWOJIFFbUpdcSRulxhh" \
             "+fHPpDvarnn8IxjyoW7xvC9Tj0oHZzb+jMuKTlRRU70y/SSgiIeUUUSYparFDH8G6lbVFFzCfGZQr/rlL6F0557fK" \
             "/wiV1tT2MRRYy1dpKiXlVczfOMtuYZI3DXuU6/PsVoRMNxZun2Eld0YqrZf+IarzdSug9Mks8cpg3md1+PlQTv6a" \
             "/zeaPxRwiw03hHzCbN489NFDbGZ/QUGCPlCWuh+uVg9HhGQO1RPfvAQBiuraB9gEAAA== "
    json01 = base64decode(encode)
    # print(json01)
    # for i in json01:
    #     # print(i)
    #     if "Map" in i:
    #         print(str(i)+'\t'+str(json01[i]))
    #     if "Num" in i:
    #         print(str(i)+'\t'+str(json01[i]))
    draft_str = "{\"steps\":[{\"id\":\"triZ6l4ksMGn\",\"type\":\"AddRecordTrigger\",\"data\":{\"tableId\":\"ref_tbl4JHKV6OTwNUzf\",\"watchedFieldId\":\"fld0brTMOq\"},\"next\":[{\"ids\":[\"actodhX9OZuL\"]}]},{\"id\":\"actodhX9OZuL\",\"type\":\"LarkMessageAction\",\"data\":{\"notifyIdentity\":\"mixed\",\"robotType\":\"bitable\",\"persons\":[{\"type\":\"ref\",\"id\":\"7288536971490623519\",\"value\":\"SG\\u5173\\u8054\\u79df\\u6237BASE-SG\",\"tagType\":\"user\",\"owner_type\":0}],\"groups\":[{\"type\":\"ref\",\"id\":\"7288536971490623519\",\"value\":\"SG\\u5173\\u8054\\u79df\\u6237BASE-SG\",\"tagType\":\"user\",\"owner_type\":0}],\"title\":[{\"text\":\"test\",\"type\":\"text\"}],\"titleTemplateColor\":\"purple\",\"content\":[{\"text\":\"test\",\"type\":\"text\"}],\"btnList\":[{\"btnKey\":\"message_btn_GgdtBm30\",\"btnAction\":\"openLink\",\"btnStyle\":\"primary\",\"text\":\"\\u67e5\\u770b\\u8bb0\\u5f55\\u8be6\\u60c5\",\"link\":[{\"id\":\"triZ6l4ksMGn-tbl4JHKV6OTwNUzf-recordUrl11\",\"tagType\":\"stepLink\",\"stepId\":\"triZ6l4ksMGn\",\"stepType\":\"AddRecordTrigger\",\"tableId\":\"ref_tbl4JHKV6OTwNUzf\",\"isShortcut\":true,\"fieldId\":\"ref_tbl4JHKV6OTwNUzf_\",\"viewId\":\"\",\"value\":\"\",\"stepNum\":1,\"type\":\"ref\"}]}],\"needBtn\":false,\"needTopBase\":true},\"next\":[]}],\"title\":\"\\u53d1\\u9001\\u6d88\\u606f\",\"tabldFieldMap\":{\"tbl4JHKV6OTwNUzf\":{\"fld0brTMOq\":{\"type\":3},\"fldw2dVTa1\":{\"type\":4},\"fldxxxq2aD\":{\"type\":5},\"fldAiVyx0r\":{\"type\":17},\"fld6Yk7HCB\":{\"type\":1},\"fldAIiovbg\":{\"type\":23},\"fldauqwTqx\":{\"type\":11}}}}"
    draft = json.loads(draft_str)
    print(draft)
    for i in draft["steps"]:
        print(i)