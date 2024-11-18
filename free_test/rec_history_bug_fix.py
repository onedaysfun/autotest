from common.send_message_cs import EditTable
from common.base64_en_or_decode import base64encode, base64decode

if __name__ == '__main__':
    domain = "https://bytedance.feishu-boe.net/"
    session = ""
    session2 = ""
    token = "tbljz7aNPMuTJxWy"
    parent_token = "NQOmb6qCeabM3GsXZQCbJFo9cTg"
    table_rev = 3
    cli = EditTable(session2, token, table_rev, parent_token, domain)
    context = {
        "field_id": "fldvqS91NP",
        "data": {
            "type": 1,
            "value": [
                {
                    "type": "text",
                    "text": "1123"
                }
            ]
        }
    }
    cli.HttpClient.set_headers({"x-tt-env":"boe_es_merge"})
    cli.set_record_v2("recPDWRStz", context)