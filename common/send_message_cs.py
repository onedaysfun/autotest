import json
import random
import string

from common.base64_en_or_decode import base64encode, base64decode
from common.common_http import HttpClient
from loguru import logger

"""
cs层级：
operations:
    command/commands:
        action/actions:
            
"""


class set_record_context:
    def __init__(self, field_id, data):
        self.field_id = field_id
        self.data = data


def get_random_id(*params, **kwargs):
    """
    函数描述:随机生成recrod/option/field/view/table id
    type:string
    support:rec/fld/vew/tbl/opt/rol
    """
    id_type = params[0]
    if id_type == "tbl":
        return "tbl" + ''.join(random.sample(string.ascii_letters + string.digits, 13))
    elif id_type == "fld":
        return "fld" + ''.join(random.sample(string.ascii_letters + string.digits, 7))
    elif id_type == "vew":
        return "vew" + ''.join(random.sample(string.ascii_letters + string.digits, 7))
    elif id_type in ["rce", "rec"]:
        return "rec" + ''.join(random.sample(string.ascii_letters + string.digits, 7))
    elif id_type == "recV2":
        return "rec" + ''.join(random.sample(string.ascii_letters + string.digits, 11))
    elif id_type == "opt":
        return "opt" + ''.join(random.sample(string.ascii_letters + string.digits, 7))
    elif id_type == "rol":
        return "rol" + ''.join(random.sample(string.ascii_letters + string.digits, 7))
    else:
        print("输入错误")


def get_member_id():
    return random.randint(10000000000000, 99999999999999)


class EditBase:
    def __init__(self, session, token, rev, domain):
        self.cookies = {"session": session}
        self.token = token
        self.rev = rev
        self.domain = domain
        self.url = self.domain + "/space/api/rce/messages"
        self.HttpClient = HttpClient().set_headers({"referer": self.domain})
        self.base_content = {
            "type": "BITABLE_BASE",
            "req_id": random.randint(1, 1000),
            "version": 2,
            "data":
                {
                    "member_id": 56664990526289,
                    "type": "USER_CHANGES",
                    "token": self.token,
                    "lang": "zh",
                    "localRev": self.rev,
                    "operations": "",
                    "content_type": "gzip/base64"},

        }

    def root_request(self, operations):
        req_body = self.base_content
        req_body['data']['operations'] = base64encode(operations)
        member_id = get_member_id()
        req_body['data']['member_id'] = member_id
        try:
            resp = (self.HttpClient.set_url(self.url)
                    .set_method("post")
                    .set_data(json.dumps(req_body))
                    .set_cookies(self.cookies)
                    .set_params({"member_id": member_id})
                    .send_http()
                    )
            if resp.status_code == 200:
                self.rev += 1
                self.base_content['data']['localRev'] = self.rev
        except Exception as e:
            logger.error(f"add field  err:{e}")

    def update_meta(self, title: str):
        """base rename"""
        # 更新base名不增加rev
        header = {"referer": self.domain}
        title = title
        url = self.domain + "/space/api/bitable/update_meta/"
        form_data = {
            "token": self.token,
            "type": 8,
            "title": title
        }
        try:
            resp = (self.HttpClient
                    .set_url(url)
                    .set_method("post")
                    .set_data(form_data)
                    .set_cookies(self.cookies)
                    .set_headers(header)
                    .send_http()
                    )
            return resp
        except Exception as e:
            logger.error(f"update base title err:{e}")
            return None

    def update_table_name(self, name: str, table_id: str):
        """table rename"""
        member_id = get_member_id()
        new_name = name
        operations = [{
            "command": "SetTable",
            "type": 1,
            "actions": [
                {
                    "action": "base.setTable",
                    "type": 1,
                    "tableId": table_id,
                    "originName": "数据表",
                    "data": {
                        "name": new_name
                    }
                }
            ]}]
        req_body = self.base_content
        req_body['data']['operations'] = base64encode(operations)
        req_body['data']['member_id'] = member_id
        try:
            resp = (self.HttpClient.set_url(self.url)
                    .set_method("post")
                    .set_data(json.dumps(req_body))
                    .set_cookies(self.cookies)
                    .set_params({"member_id": member_id})
                    .send_http()
                    )
            if resp.status_code == 200:
                self.rev += 1
                self.base_content['data']['localRev'] = self.rev
        except Exception as e:
            logger.error(f"update table name err:{e}")


class EditTable:
    def __init__(self,domain,session,parent_token,token,rev):
        """
        :param session: 用户session
        :param token: 需要编辑的table token
        :param rev: 初始化类时的table revision
        :param parent_token: base token
        :param domain: 域名 like：https://www.bytedance.com
        """
        self.domain = domain
        self.cookies = {"session": session}
        self.parent_token = parent_token
        self.token = token
        self.rev = rev
        self.HttpClient = HttpClient().set_headers({"referer": self.domain})
        self.url = self.domain + "/space/api/rce/messages"
        self.table_content = {
            "type": "BITABLE_TABLE",
            "data":
                {"member_id": 56664990526289,
                 "type": "USER_CHANGES",
                 "token": self.token,
                 "lang": "zh",
                 "localRev": self.rev,
                 "operations": "",
                 "content_type": "gzip/base64",
                 "route_key": self.parent_token},
            "version": 2,
            "req_id": random.randint(1, 1000),
        }

    def root_request(self, operations):
        member_id = get_member_id()
        req_body = self.table_content
        req_body['data']['operations'] = base64encode(operations)
        req_body['data']['member_id'] = member_id
        try:
            resp = (self.HttpClient.set_url(self.url)
                    .set_method("post")
                    .set_data(json.dumps(req_body))
                    .set_cookies(self.cookies)
                    .set_params({"member_id": member_id})
                    .send_http()
                    )
            if resp.status_code == 200:
                self.rev += 1
                self.table_content['data']['localRev'] = self.rev
            return resp
        except Exception as e:
            logger.error(f"err:{e}")

    def batch_add_field(self, field_info: dict, field_name: str):
        """
        :param field_info:  {'Rating': 2},
                            {'MultiSelect': 4},
                            {'Currency': 2},
                            {'ModifiedUser': 1004},
                            {'Lookup': 19},
                            {'User': 11},
                            {'Stage': 24},
                            {'Text': 1},
                            {'SingleSelect': 3},
                            {'Button': 3001},
                            {'Email': 1},
                            {'Checkbox': 7},
                            {'Number': 2},
                            {'GroupChat': 23},
                            {'Attachment': 17},
                            {'Location': 22},
                            {'Barcode': 1},
                            {'DateTime': 5},
                            {'Phone': 13},
                            {'CreatedTime': 1001},
                            {'DuplexLink': 21},
                            {'AutoNumber': 1005},
                            {'CreatedUser': 1003},
                            {'Formula': 20},
                            {'SingleLink': 18},
                            {'ModifiedTime': 1002},
                            {'Progress': 2},
                            {'Url': 15}
        :param field_name name
        :return:
        """
        field_type = list(field_info.values())[0]
        field_ui_type = list(field_info.keys())[0]
        table_token = self.token
        operations = [{
            "command": "AddField",
            "actions": [{
                "action": "data.addField",
                "type": 2,
                "tableId": table_token,
                "fieldId": get_random_id("fld"),
                "data": {
                    "name": field_name,
                    "type": field_type,
                    "fieldUIType": field_ui_type,
                    "exInfo": {"fieldUIType": field_ui_type}
                }
            }]}]
        # 通用
        self.root_request(operations)

    def add_field_random(self, random_field_list: list, count: int):
        count = count
        operations = []
        for i in range(count):
            field_info = random.choice(random_field_list)
            field_type = list(field_info.values())[0]
            field_ui_type = list(field_info.keys())[0]
            table_token = self.token
            field_name = field_ui_type + "-" + str(random.randint(1, 1000))
            operation = {
                "command": "AddField",
                "actions": [{
                    "action": "data.addField",
                    "type": 2,
                    "tableId": table_token,
                    "fieldId": get_random_id("fld"),
                    "data": {
                        "name": field_name,
                        "type": field_type,
                        "fieldUIType": field_ui_type,
                        "exInfo": {"fieldUIType": field_ui_type}
                    }
                }]}
            operations.append(operation)
        self.root_request(operations)

    def add_record(self, is_fxdb_base: bool, cellData):
        """默认首行新增"""
        table_token = self.token
        member_id = get_member_id()
        if is_fxdb_base:
            operations = [{
                "command": "AddRecordsV2",
                "type": 2,
                "actions": [
                    {
                        "action": "data.addRecordV2",
                        "type": 2,
                        "tableId": table_token,
                        "recordId": get_random_id("recV2"),
                        "data": cellData
                    }
                ]
            }]
        else:
            operations = [{
                "command": "AddRecords",
                "type": 2,
                "actions": [
                    {
                        "action": "data.addRecord",
                        "type": 2,
                        "tableId": table_token,
                        "recordId": get_random_id("rec"),

                    }
                ]
            }]
        req_body = self.table_content
        req_body['data']['operations'] = base64encode(operations)
        req_body['data']['member_id'] = member_id
        try:
            resp = (self.HttpClient.set_url(self.url)
                    .set_method("post")
                    .set_data(json.dumps(req_body))
                    .set_cookies(self.cookies)
                    .set_params({"member_id": member_id})
                    .send_http()
                    )
            if resp.status_code == 200:
                self.rev += 1
                self.table_content['data']['localRev'] = self.rev
        except Exception as e:
            logger.error(f"add field  err:{e}")

    def add_view(self, field_list: list, is_fxdb_base: bool):
        field_list = field_list
        if is_fxdb_base:
            operations = [{
                "command": "AddViewV2",
                "type": 2,
                "actions": [
                    {
                        "action": "data.addViewV2",
                        "type": 2,
                        "tableId": "tblOGopU1rq4FJAx",
                        "viewId": "veweSGyrxx",
                        "data": {
                            "type": 1,
                            "index": 4,
                            "name": "表格 3",
                            "isPrivate": False,
                            "property": {
                                "rowHeightLevel": 1,
                                "fields": field_list,
                                "colInfos": {},
                                "filterInfo": None,
                                "sortInfo": [],
                                "frozenColCount": 1,
                                "group": [],
                                "autoSort": False,
                                "cardViewSetting": None
                            },
                            "owner": "7251926390889512979"
                        }
                    }
                ],
                "syncFlag": 0
            }]

    def add_field_sing_select_link(self, field_name: str, main_table: str, link_table: str):
        field_name = field_name
        main_table = main_table
        link_table = link_table
        field_id = get_random_id('fld')
        operations = [
            {
                'command': 'AddField',
                'type': 2,
                'actions': [
                    {
                        'action': 'data.addField',
                        'type': 2,
                        'tableId': main_table,
                        'fieldId': field_id,
                        'data': {
                            'name': field_name,
                            'type': 3,
                            'fieldUIType': 'SingleSelect',
                            'enumerable': True,
                            'exInfo': {'fieldUIType': 'SingleSelect'}, 'indexes': {'vewU0iOQTk': 2}}},
                    {
                        'action': 'data.setFieldAttr',
                        'type': 2,
                        'tableId': 'main_table',
                        'fieldId': field_id,
                        'data': {
                            'id': field_id,
                            'name': field_name,
                            'type': 3,
                            'fieldUIType': 'SingleSelect',
                            'enumerable': True,
                            'property':
                                {'optionsRule':
                                    {
                                        'conditions': [
                                            {'fieldType': 1, 'value': '', 'fieldId': 'fldfEf2CVu',
                                             'conditionId': 'conof7ydZq',
                                             'operator': 'isEmpty'},
                                            {'fieldType': 23, 'value': '', 'fieldId': 'fldTyr91ZT',
                                             'conditionId': 'conXwdwTY8',
                                             'operator': 'isEmpty'},
                                            {'fieldType': 11, 'value': '', 'fieldId': 'fld3MqJ86s',
                                             'conditionId': 'conX5hqRyD',
                                             'operator': 'isEmpty'},
                                            {'fieldType': 5, 'value': '', 'fieldId': 'fldr2uew0h',
                                             'conditionId': 'conPK4BagI',
                                             'operator': 'isEmpty'},
                                            {'fieldType': 17, 'value': '', 'fieldId': 'fldfFUqcWQ',
                                             'conditionId': 'conTuyZwLM',
                                             'operator': 'isEmpty'}],
                                        'conjunction': 'and',
                                        'targetField': 'fld7iL4fT4',
                                        'targetTable': link_table},
                                    'options': [],
                                    'optionsType': 1},
                            'exInfo': {'fieldUIType': 'SingleSelect'}}}],
                'syncFlag': 0}]

        # 通用
        member_id = get_member_id()
        req_body = self.table_content
        req_body['data']['operations'] = base64encode(operations)
        req_body['data']['member_id'] = member_id
        try:
            resp = (self.HttpClient.set_url(self.url)
                    .set_method("post")
                    .set_data(json.dumps(req_body))
                    .set_cookies(self.cookies)
                    .set_params({"member_id": member_id})
                    .send_http()
                    )
            if resp.status_code == 200:
                self.rev += 1
                self.table_content['data']['localRev'] = self.rev
        except Exception as e:
            logger.error(f"add field  err:{e}")

    def add_field_multi_select(self, field_name: str, main_table: str, link_table: str):
        field_name = field_name
        main_table = main_table
        link_table = link_table
        field_id = get_random_id('fld')
        operations = [
            {
                'command': 'AddField',
                'type': 2,
                'actions': [
                    {
                        'action': 'data.addField',
                        'type': 2,
                        'tableId': main_table,
                        'fieldId': field_id,
                        'data': {
                            'name': field_name,
                            'type': 4,
                            'fieldUIType': 'MultiSelect',
                            'enumerable': True,
                            'exInfo': {'fieldUIType': 'MultiSelect'},
                            'indexes': {'vewVBJTV72': 1}}
                    },
                    {
                        'action': 'data.setFieldAttr',
                        'type': 2,
                        'tableId': main_table,
                        'fieldId': field_id,
                        'data': {
                            'id': field_id,
                            'name': field_name,
                            'type': 4,
                            'fieldUIType': 'MultiSelect',
                            'enumerable': True,
                            'property': {
                                'optionsRule': {
                                    'conditions': [
                                        {'fieldType': 1, 'value': '', 'fieldId': 'fldRCzXazn',
                                         'conditionId': 'con5gH4irX',
                                         'operator': 'isEmpty'},
                                        {'fieldType': 23, 'value': '', 'fieldId': 'fldFAmqv4f',
                                         'conditionId': 'conDUroFgC',
                                         'operator': 'isEmpty'},
                                        {'fieldType': 11, 'value': '', 'fieldId': 'fldeY7BMDn',
                                         'conditionId': 'coniEGyr8o',
                                         'operator': 'isEmpty'},
                                        {'fieldType': 3, 'value': '', 'fieldId': 'fldkYvLcx4',
                                         'conditionId': 'conlsphKXR',
                                         'operator': 'isEmpty'},
                                        {'fieldType': 5, 'value': '', 'fieldId': 'fldcddN21v',
                                         'conditionId': 'conFrcopEs',
                                         'operator': 'isEmpty'}],
                                    'conjunction': 'and',
                                    'targetField': 'fldqLWW2x0',
                                    'targetTable': link_table},
                                'options': [], 'optionsType': 1},
                            'exInfo': {'fieldUIType': 'MultiSelect'}}}], 'syncFlag': 0}]
        self.root_request(operations)
        return self

    def set_record(self, table_token, record_id, field_map: list, opt_map: list):
        table_token = table_token
        field_map = field_map
        opt_map = opt_map
        record_id = record_id
        action_list = []
        # 合成action list
        for field_id in field_map:
            opt_id_list = []
            # 随机取多选项list opt_id_list
            opt_len = random.randint(1, len(opt_map))
            for index in range(0, opt_len):
                # 随机取选项
                opt_id = random.choice(opt_map)['id']
                if opt_id not in opt_id_list:
                    opt_id_list.append(opt_id)
            action = {
                'action': 'data.setRecord',
                'type': 2,
                'tableId': table_token,
                'recordId': record_id,
                'viewType': 1,
                'data':
                    {
                        field_id: {'value': opt_id_list, 'type': 4}}
            }
            action_list.append(action)
        operations = [
            {'command': 'SetRecord',
             'type': 2,
             'actions': action_list,
             'syncFlag': 0}]
        self.root_request(operations)

    def add_field_number_order_by(self, table, field_name):
        field_id = get_random_id('fld')
        operations = [
            {
                "command": "AddField",
                "type": 2,
                "actions": [
                    {
                        "action": "data.addField",
                        "type": 2,
                        "tableId": table,
                        "fieldId": field_id,
                        "data": {
                            "name": field_name,
                            "type": 2,
                            "fieldUIType": "Number",
                            "enumerable": False,
                            "exInfo": {
                                "fieldUIType": "Number"
                            }
                        }
                    },
                    {
                        "action": "data.setFieldAttr",
                        "type": 2,
                        "tableId": table,
                        "fieldId": field_id,
                        "data": {
                            "id": field_id,
                            "name": field_name,
                            "type": 2,
                            "fieldUIType": "Number",
                            "enumerable": False,
                            "property": {
                                "formatter": "0.0"
                            },
                            "exInfo": {
                                "fieldUIType": "Number"
                            }
                        }
                    }
                ],
                "syncFlag": 0
            }
        ]
        self.root_request(operations)

    def set_record_v2(self, record_id, context: dict):
        table_token = self.token
        record_id = record_id
        context = context
        field_id = context['field_id']
        data = context['data']
        action = {
            'action': 'data.setRecord',
            'type': 2,
            'tableId': table_token,
            'recordId': record_id,
            'viewType': 1,
            'data':
                {
                    field_id: data
                }
        }
        operations = [
            {'command': 'SetRecord',
             'type': 2,
             'actions': [action],
             'syncFlag': 0}]
        self.root_request(operations)

    def delete_record_v2(self, record_id):
        table_token = self.token
        record_id = record_id
        action = {
            "action": "data.deleteRecordV2",
            "type": 2,
            "tableId": table_token,
            "recordId": record_id
        }
        operations = [
            {'command': 'DeleteRecordsV2',
             'type': 2,
             'actions': [action],
             'syncFlag': 0}]
        self.root_request(operations)
