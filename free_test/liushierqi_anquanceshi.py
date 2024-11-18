from common.send_message_cs import EditTable

perf_headers = {
    "env": "pre_release",
    "x-tt-stress": "true"
}


def init_edit_table(table, rev):
    session = 'XN0YXJ0-96fo3706-aca6-435d-90a4-fbbcb6bc567f-WVuZA'
    domain = 'https://yalixw0asad.feishu.cn'
    base_token = 'ZfcAbLpRyaGYfhsoYKHcn5SQnze'
    table_token = table
    table_rev = rev
    handle = EditTable(session=session, token=table_token, rev=table_rev, parent_token=base_token, domain=domain)
    handle.HttpClient.set_headers(perf_headers)
    return handle


if __name__ == '__main__':
    table_5 = 'tbltRbLPlVsGigfU'
    record_id_5 = 'recBNUmy4j'
    rev = 112
    handle = init_edit_table(table_5, rev)
    context = {
        "field_id": "fldpKUpmaU",
        "data": {
            "type": 1,
            "value": [
                {
                    "type": "text",
                    "text": "测试越权编辑"
                }
            ]
        }
    }
    cellData = {
        "fldWKQg2jm": {
            "type": 1,
            "value": [
                {
                    "type": "text",
                    "text": "000"
                }
            ]
        }
    }
    handle.set_record_v2(record_id_5, context)
    # handle.add_record(is_fxdb_base=True)
    # handle.delete_record_v2(record_id)
    # handle.add_record(is_fxdb_base=True, cellData=cellData)
