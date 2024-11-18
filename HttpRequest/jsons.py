import json
from json import JSONDecodeError

automation = {
        "token": "HYPsbirpVaaMGfstA5rcsIiBnMv",
        "draft": "{\"steps\":[{\"id\":\"trigGBvqXnnu\",\"type\":\"AddRecordTrigger\",\"data\":{\"tableId\":\"ref_tblEmu33m6pkb4dz\",\"watchedFieldId\":\"fldprFJtLk\"},\"next\":[{\"ids\":[\"actbdEWdyju\"]}]},{\"id\":\"actbdEWdyju\",\"type\":\"LarkMessageAction\",\"data\":{\"notifyIdentity\":\"mixed\",\"robotType\":\"bitable\",\"persons\":[{\"type\":\"ref\",\"avatarUrl\":\"https://s3-imfile.feishucdn.com/static-resource/v1/v2_3b91dfe0-5de4-4998-a49d-7c58ca2a4c8g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp\",\"id\":\"7288536971490623519\",\"value\":\"SG关联租户BASE-SG\",\"tagType\":\"user\",\"owner_type\":0,\"department\":\"MG CN 测试租户(SG)\"}],\"groups\":[{\"type\":\"ref\",\"avatarUrl\":\"https://s3-imfile.feishucdn.com/static-resource/v1/v2_3b91dfe0-5de4-4998-a49d-7c58ca2a4c8g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp\",\"id\":\"7288536971490623519\",\"value\":\"SG关联租户BASE-SG\",\"tagType\":\"user\",\"owner_type\":0,\"department\":\"MG CN 测试租户(SG)\"}],\"title\":[{\"text\":\"test\",\"type\":\"text\"}],\"titleTemplateColor\":\"purple\",\"content\":[{\"text\":\"test\",\"type\":\"text\"}],\"btnList\":[{\"btnKey\":\"message_btn_GgdtBm30\",\"btnAction\":\"openLink\",\"btnStyle\":\"primary\",\"text\":\"查看记录详情\",\"link\":[{\"id\":\"trigGBvqXnnu-tblEmu33m6pkb4dz-recordUrl11\",\"tagType\":\"stepLink\",\"stepId\":\"trigGBvqXnnu\",\"stepType\":\"AddRecordTrigger\",\"tableId\":\"ref_tblEmu33m6pkb4dz\",\"isShortcut\":true,\"fieldId\":\"ref_tblEmu33m6pkb4dz_\",\"viewId\":\"\",\"value\":\"\",\"stepNum\":1,\"type\":\"ref\"}]}],\"needBtn\":false,\"needTopBase\":true},\"next\":[]}],\"title\":\"流程 2\",\"tabldFieldMap\":{\"tblEmu33m6pkb4dz\":{\"fldH30eYhG\":{\"type\":17},\"fldprFJtLk\":{\"type\":1},\"fldrPHLVkC\":{\"type\":1},\"fldkOelH9n\":{\"type\":23},\"fldKusu1Ky\":{\"type\":11},\"fldvLVbNzg\":{\"type\":3},\"fldRtpq1lj\":{\"type\":4},\"fldQN11CyB\":{\"type\":5}}}}",
        "extra": "{\"TableMap\":{\"ref_tblEmu33m6pkb4dz\":{\"TableID\":\"tblEmu33m6pkb4dz\",\"FieldMap\":{\"ref_tblEmu33m6pkb4dz_\":\"\"}}},\"BlockMap\":{}}",
        "triggerName": "addRecordV2",
        "status": 1,
        "flowSchema": "{\"type\":\"standard\",\"startAt\":\"act_361ac0\",\"states\":{\"act_361ac0\":{\"type\":\"task\",\"id\":\"act_361ac0\",\"config\":{\"type\":\"servicemanager\",\"config\":{\"bizId\":\"bitable\",\"metaVersion\":\"v1\",\"metaName\":\"bitable\",\"domainName\":\"automation\",\"apiName\":\"notifyV2API\"}},\"parameters\":{\"ReceiverInfo\":\"{\\\"ReceiverType\\\":4,\\\"Receivers\\\":expr.flatten([{\\\"UserType\\\":4,\\\"UserID\\\":\\\"7288536971490623519\\\"}])}\",\"Msg\":\"{\\\"Header\\\":{\\\"title\\\":{\\\"content\\\":expr.join([\\\"test\\\"], \\\"\\\"),\\\"tag\\\":\\\"plain_text\\\"},\\\"template\\\":\\\"purple\\\"},\\\"Elements\\\":expr.flatten(expr.flatten([{\\\"tag\\\":\\\"markdown\\\",\\\"content\\\":expr.join(expr.flatten([\\\"test\\\"]), \\\"\\\")}]))}\"},\"end\":true}},\"trigger\":{\"type\":\"servicemanager\",\"id\":\"trig_99d1ec\",\"parameters\":{\"BaseToken\":\"\\\"HYPsbirpVaaMGfstA5rcsIiBnMv\\\"\",\"TableID\":\"\\\"tblEmu33m6pkb4dz\\\"\",\"TriggerParam\":\"{\\\"fieldID\\\":\\\"fldprFJtLk\\\"}\"},\"config\":{\"domainName\":\"automation\",\"eventName\":\"addRecordV2\",\"bizId\":\"bitable\",\"bizType\":\"\",\"metaVersion\":\"v1.12\",\"metaName\":\"bitable\"}}}",
        "nodeSchema": "{\"triggerStepId\":\"trigGBvqXnnu\",\"firstTaskStepId\":\"actbdEWdyju\",\"relations\":{\"trigGBvqXnnu\":[{\"id\":\"trig_99d1ec\",\"type\":\"servicemanager\"}],\"actbdEWdyju\":[{\"id\":\"act_361ac0\",\"type\":\"task\"}]},\"version\":1}",
        "source": "topbar_click_from_blank"
    }


def set_automation_send_massage_body():

    user_id = 7288536971490623519
    user_name = "SG关联租户BASE-SG"
    user_department = "MG CN 测试租户(SG)"
    msg = "test"
    base_token = "HYPsbirpVaaMGfstA5rcsIiBnMv"
    base_token_use = f"\"{base_token}\""
    table_token = "tblEmu33m6pkb4dz"
    table_token_use = f"\"{table_token}\""
    trig_id = "trig_99d1ec"
    trigger_token = "trigGBvqXnnu"
    action_token = "actbdEWdyju"
    act_id = "act_361ac0"
    watch_field = "fldprFJtLk"
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
                            "avatarUrl": "https://s3-imfile.feishucdn.com/static-resource/v1/v2_3b91dfe0-5de4-4998-a49d-7c58ca2a4c8g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
                            "id": f"{user_id}",
                            "value": f"{user_name}",
                            "tagType": "user",
                            "owner_type": 0,
                            "department": user_department
                        }
                    ],
                    "groups": [
                        {
                            "type": "ref",
                            "avatarUrl": "https://s3-imfile.feishucdn.com/static-resource/v1/v2_3b91dfe0-5de4-4998-a49d-7c58ca2a4c8g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
                            "id": f"{user_id}",
                            "value": f"{user_name}",
                            "tagType": "user",
                            "owner_type": 0,
                            "department": user_department
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
            table_token: {"fldH30eYhG": {"type": 17}, "fldprFJtLk": {"type": 1}, "fldrPHLVkC": {"type": 1},
                                 "fldkOelH9n": {"type": 23}, "fldKusu1Ky": {"type": 11}, "fldvLVbNzg": {"type": 3},
                                 "fldRtpq1lj": {"type": 4}, "fldQN11CyB": {"type": 5}}}
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
    return json.dumps(automation_body).replace(" ", "")


if __name__ == "__main__":
    # for i in automation:
    #     try:
    #         print(i.__str__() + " = " + str(json.loads(automation[i])))
    #     except Exception as e:
    #         print(e.__str__())
    #         continue
    # print("\"asdad\"")
    # print(flowSchema_parameters_ReceiverInfo_use)
    # print(flowSchema_parameters_msg_use)

    # print(x)
    # print(json.dumps(json.dumps(flowSchema)).replace(" ", ""))
    print(set_automation_send_massage_body())
    print(json.dumps(automation).replace(" ", ""))
    # if automation["draft"] != json.dumps(json.dumps(draft)).replace(" ", ""):
    #     print("YES")
