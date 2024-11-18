import json
import random

from common import common_http


class History:
    def __init__(self, domain, cookies):
        self.domain = domain
        self.cookies = cookies
        self.headers = {"referer": self.domain}
        self.httpClient = common_http.HttpClient().set_headers(self.headers)

    def get_history_list(self, base_token, table_token, page_size=20, page_token=""):
        # todo:AI填的，需要改
        resp = (self.httpClient.set_url(f"{self.domain}/space/api/v1/bitable/history/list")
                .set_method("get")
                .set_cookies(self.cookies)
                .set_params({"baseToken": base_token, "tableToken": table_token, "pageSize": page_size, "pageToken": page_token})
                .send_http())
        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    def get_history_list_with_filter(self, base_token, table_token, page_size=20, page_token="", filter=""):
        # todo:AI填的，需要改
        resp = (self.httpClient.set_url(f"{self.domain}/space/api/v1/bitable/history/list")
                .set_method("get")
                .set_cookies(self.cookies)
                .set_params({"baseToken": base_token, "tableToken": table_token, "pageSize": page_size, "pageToken": page_token, "filter": filter})
                .send_http())
        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    def get_history_detail(self, base_token, table_token, history_id):
        # todo:AI填的，需要改
        resp = (self.httpClient.set_url(f"{self.domain}/space/api/v1/bitable/history/detail")
                .set_method("get")
                .set_cookies(self.cookies)
                .set_params({"baseToken": base_token, "tableToken": table_token, "historyID": history_id})
                .send_http())

        if resp.status_code == 200:
            return resp.json()
        else:
            return None

    def time_machine_recover(self, base_token, version_id: str, major_id: int):
        data = {
            "token": base_token,
            "versionId": version_id,
            "majorVersion": major_id,
            "memberId": random.randint(10000000000000, 99999999999999)
        }
        resp = (self.httpClient.set_url(f"{self.domain}/space/api/bitable/history/{base_token}/recover")
                .set_method("post")
                .set_cookies(self.cookies)
                .set_data(json.dumps(data))
                .send_http())
        if resp.status_code == 200:
            return resp.json()
        else:
            return None


if __name__ == '__main__':
    # 全局配置
    domain_jp = "https://njpwk6t510h2.jp.larksuite.com"
    domain_boe = "https://bytedance.feishu-boe.net"
    cookies_jp = {"session": "XN0YXJ0-1d4v7a86-ae2b-4a9e-9fd1-b9f998mih61j-WVuZA"}
    cookies_boe = {"session": "XN0YXJ0-955p82b7-400b-4230-87ad-4edbaa644bgh-WVuZA"}
    headers = {"x-tt-stress": "true", "env": "pre_release"}

    client = History(domain_boe, cookies_boe)
    client.time_machine_recover("UOOcbFrXYa7hbusuoTDbhbqZcdh", "7428488926013079572", 0)

