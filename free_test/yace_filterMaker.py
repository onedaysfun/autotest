import json
import random
import string

str = "{\"conjunction\":\"and\",\"conditions\":[{\"fieldId\":\"fldTpOsHMN\",\"fieldType\":11,\"operator\":\"is\",\"value\":[{\"userId\":\"6921583492111269907\"}],\"conditionId\":\"conKY91azm\"}]}"
filter_json = {
    "conjunction": "and",
    "conditions": [
        {
            "fieldId": "fldTpOsHMN",
            "fieldType": 11,
            "operator": "is",
            "value": [
                {"userId": "6921583492111269907"}
            ],
            "conditionId": "conKY91azm"
        }
    ]}

operators = ["is", "isNot"]
fileID = {
    "10w": {
        "文本": {
            "id": "fldUdZyY1L",
            "type": 1
        },
        "多选": {
            "id": "fld3Dfrgu4",
            "type": 4,
            "exist_value": "opt0pE4lRH"
        },
        "人员": {
            "id": "fldXOLRVmh",
            "type": 11,
            "exist_value": "8750608427116858506"
        },
        "数字": {
            "id": "fldEcCj9bJ",
            "type": 2
        }
    },
    "20w": {
        "文本": {
            "id": "fldjJs1D2O",
            "type": 1
        },
        "多选": {
            "id": "fld3EtJLKX",
            "type": 4,
            "exist_value": "optfkEByHK"
        },
        "人员": {
            "id": "fldieGpif6",
            "type": 11,
            "exist_value": "4826044552829031283"
        },
        "数字": {
            "id": "fldKAzx3Lr",
            "type": 2
        }
    },
    "100w": {
        "文本": {
            "id": "",
            "type": 1
        },
        "多选": {
            "id": "",
            "type": 4,
            "exist_value": ""
        },
        "人员": {
            "id": "",
            "type": 11,
            "exist_value": ""
        },
        "数字": {
            "id": "",
            "type": 2
        }
    }

}


def get_id_type(*params, doc_use="10w"):
    field = params[0]
    filed_id = fileID[doc_use][field]['id']
    filed_type = fileID[doc_use][field]['type']
    return filed_id, filed_type


def get_exist_value(*params, doc_use="10w"):
    field = params[0]
    if field not in ["人员", "多选"]:
        return None
    filed_value = fileID[doc_use][field]['exist_value']
    return filed_value


def get_value(*params):
    field = params[0]
    value = None
    if field == '文本':
        value = ["$$random:num:10$$"]
    if field == '人员':
        value = [{"userId": "$$random:text:16$$"}]
    if field == '数字':
        value = ["$$random:num:5$$"]
    if field == '多选':
        value = ["opt$$random:string:7$$"]
    return value


def get_operator(*params):
    operator = params[0]
    condition = None
    if operator == "等于":
        condition = "is"
    if operator == "不等于":
        condition = "isNot"
    if operator == "包含":
        condition = "contains"
    if operator == "不包含":
        condition = "doesNotContain"
    if operator == "大于":
        condition = "isGreater"
    return condition


# 联合查询使用
def create_conditions_(conjunction="and", flag=True, doc_use="10w"):
    """
    :param doc_use:
    :param flag:
    :param conjunction:
    :return:
    """
    filter_info = {
        "conjunction": conjunction,
        "conditions": []
    }
    if flag:
        list = [
            ["人员", "包含"],
            ["多选", "包含"]
        ]
    else:
        list = [
            ["人员", "不等于"],
            ["多选", "不包含"]
        ]
    for i in list:
        field_id, field_type = get_id_type(i[0], doc_use=doc_use)
        value = get_value(i[0])
        if flag:
            use_value = get_exist_value(i[0], doc_use=doc_use)
            if i[0] == "人员":
                value = [{"userId": "$$random:num:16$$"}, {"userId": use_value}]
            if i[0] == "多选":
                value = ["opt$$random:string:7$$", use_value]
        operator = get_operator(i[1])
        conditionId = "con" + ''.join(random.sample(string.ascii_letters + string.digits, 7))
        condition = {
            "fieldId": field_id,
            "fieldType": field_type,
            "operator": operator,
            "value": value,
            "conditionId": conditionId
        }
        filter_info['conditions'].append(condition)
    return filter_info


# 单个查询使用
def output_filter_info(*params, doc_use="10w"):
    """
    :param
    params[0]: 文本、人员、数字、多选
    params[1]: 等于，不等于，大于，小于，包含，不包含，为空，不为空
    :return:
    """
    field = params[0]
    operator = params[1]

    filed_id = fileID[doc_use][field]['id']
    filed_type = fileID[doc_use][field]['type']
    if field == '文本':
        value = ["$$random:text:10$$"]
    if field == '人员':
        use_value = get_exist_value(field, doc_use=doc_use)
        if operator == '包含':
            value = [{"userId": "$$random:num:16$$"}, {"userId": use_value}]
        else:
            value = [{"userId": "$$random:num:16$$"}]
    if field == '数字':
        value = ["$$random:num:5$$"]
    if field == '多选':
        use_value = get_exist_value(field, doc_use=doc_use)
        if operator == '包含':
            value = ["opt$$random:string:7$$", use_value]
        else:
            value = ["opt$$random:string:7$$"]
    filter_json['conditions'][0]['value'] = value
    if operator == "等于":
        filter_json['conditions'][0]['operator'] = "is"
    if operator == "不等于":
        filter_json['conditions'][0]['operator'] = "isNot"
    if operator == "包含":
        filter_json['conditions'][0]['operator'] = "contains"
    if operator == "不包含":
        filter_json['conditions'][0]['operator'] = "doesNotContain"
    filter_json['conditions'][0]['fieldId'] = filed_id
    filter_json['conditions'][0]['fieldType'] = filed_type
    return filter_json


if __name__ == '__main__':
    info_list = []
    cj_list = [
        ["人员", "等于"],
        ["人员", "不等于"],
        ["多选", "包含"],
        ["多选", "不包含"],
        ["人员", "包含"],
        ["文本", "包含"]
    ]
    # for i in cj_list:
    #     s = output_filter_info(i[0], i[1], doc_use="20w")
    #     info_list.append(s)
    #     print(json.dumps(s).replace(" ", ""))
    member_select_hit_index = create_conditions_()
    # member_select_hit_index_or = create_conditions_("or")
    member_select_no_index = create_conditions_(flag=False)
    # member_select_no_index_or = create_conditions_("or", flag=False)
    print(json.dumps(member_select_hit_index).replace(" ", ""))
    # print(json.dumps(member_select_hit_index_or).replace(" ", ""))
    print(json.dumps(member_select_no_index).replace(" ", ""))
    # print(json.dumps(member_select_no_index_or).replace(" ", ""))
    member_select_hit_index_20w = create_conditions_(doc_use="20w")
    member_select_no_index_20w = create_conditions_(flag=False, doc_use="20w")
    print(json.dumps(member_select_no_index_20w).replace(" ", ""))
    print(json.dumps(member_select_hit_index_20w).replace(" ", ""))
