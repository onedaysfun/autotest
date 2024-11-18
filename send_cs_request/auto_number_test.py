from common import common_http, base64_en_or_decode, send_message_cs

if __name__ == '__main__':
    domain = "https://bitable-test.feishu-boe.cn"
    session = ""
    base_token = "SH94bEPjxauzRasdcCWb8LO5c2f"
    table_token = "tbllSswmHN0GHPLE"
    field_id = "fldToMUy5Q"
    table_rev = 36
    env = {"x-tt-env": "boe_canjie_test"}
    action_deleteFields = {
        'command': 'DeleteFields',
        'type': 2,
        'actions': [{
            'action': 'data.deleteField',
            'type': 2,
            'tableId': table_token,
            'fieldId': field_id,
            'name': '自动编号',
            'data': {'indexes': {}}
        }],
        'syncFlag': 0}
    action_SetFieldAttr = {
        'command': 'SetFieldAttr',
        'type': 2,
        'actions': [{
            'action': 'data.setFieldAttr',
            'type': 2,
            'tableId': table_token,
            'fieldId': field_id,
            'originData': {
                'name': '自动编号',
                'type': 1005,
                'property': {
                    'isAdvancedRules': False,
                    'reformatExistingRecord': True,
                    'ruleFieldOptions': [{'value': '3', 'type': 1}]},
                'description': {},
                'fieldUIType': 'AutoNumber',
                'exInfo': {'fieldUIType': 'AutoNumber'}},
            'data': {
                'name': '自动编号',
                'type': 1005,
                'property': {
                    'isAdvancedRules': True,
                    'reformatExistingRecord': True,
                    'ruleFieldOptions': [{'value': '3', 'type': 1}]},
                'description': {},
                'fieldUIType': 'AutoNumber',
                'exInfo': {'fieldUIType': 'AutoNumber'}}
        }],
        'syncFlag': 0}
    handle = send_message_cs.EditTable(session, table_token, table_rev, base_token, domain)
    handle.HttpClient.set_headers(env)
    operations = [action_deleteFields, action_SetFieldAttr]
    handle.root_request(operations=operations)

