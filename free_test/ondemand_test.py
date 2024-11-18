import json
import random
import string

from common.common_ondemand import OndemandReq
from base64 import b64decode as base64decode


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


if __name__ == '__main__':
    domain = "https://internal-api-space.feishu-boe.net"
    cli = OndemandReq(domain)
    cli.http_client.set_cookies({"session": "XN0YXJ0-442o1bf7-ab2f-4a3a-ac1e-51c42c1056og-WVuZA"})
    cli.http_client.set_headers({"x-tt-env": "boe_ondemand_10w"})
    clientVars_context = {
        "base_token": "DvREbdCh1aEYGNslncdbuh3Scbb",
        "table_token": "tbljbb6OrM5sl2oK",
        "viewID": "vewGDvDwQe",
        "needBase": False,
        "recordLimit": 100,
        "viewLazyLoad": True,
        "ondemandLimit": 200,
        "ondemandVer": 2
    }
    # resp = cli.ondemand_client_vars(clientVars_context)
    groups_context = {
        "base_token": "DvREbdCh1aEYGNslncdbuh3Scbb",
        "table_token": "tbljbb6OrM5sl2oK",
        "viewID": "vewGDvDwQe",
        "groupList": None
    }
    groupList = [
        {"offset": 0, "limit": 1, "groupByList": []}
    ]
    groupByList = []
    groupByList.append({"fieldId": "fldkSYFaZz", "groupKey": [{"type": "text", "text": "1"}]})
    groupByList.append({"fieldId": "fldvJnOwVQ", "groupKey": [{"type": "text", "text": "1"}]})
    groupByList.append({"fieldId": "fldiLojhXI", "groupKey": [{"type": "text", "text": "1"}]})

    groupList[0]['groupByList'] = groupByList
    groups_context['groupList'] = json.dumps(groupList)
    cli.http_client.headers["referer"] = "https://bytedance.feishu-boe.net/base/DvREbdCh1aEYGNslncdbuh3Scbb"
    resp = cli.ondemand_groups(groups_context)
    print(json.loads(resp.json()['data']['groupInfoList']))