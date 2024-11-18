import json
import time

from common_http import HttpClient


class SpaceApi:
    def __init__(self):
        self.client = HttpClient()
        self.domain = "https://bytedance.feishu-boe.net"

    def root_req(self):
        return self.client.send_http()

    def get_folders(self, length=50):
        """
        get folders from space root
        """
        query_params = {
            "length": length
        }

        url = self.domain + "/space/api/explorer/v3/my_space/folder/"
        resp = (self.client.set_method("get")
                .set_params(query_params)
                .set_url(url)
                .send_http())
        return resp

    def get_objs(self, length=50):
        """
        get objects from space root
        """
        query_params = {
            "length": length
        }
        url = self.domain + "/space/api/explorer/v3/my_space/obj/"
        resp = (self.client.set_method("get")
                .set_params(query_params)
                .set_url(url)
                .set_headers({"referer": self.domain})
                .send_http())
        return resp

    def list_folder(self, length=50, token=""):
        query_params = {
            "length": length,
            "token": token,
            "acs": 1
        }
        url = self.domain + "/space/api/explorer/v3/children/list/"
        resp = (self.client.set_method("get")
                .set_params(query_params)
                .set_url(url)
                .set_headers({"referer": self.domain})
                .send_http())
        return resp

    def remove_folders(self, tokens, apply=1):
        req_data = {
            "tokens": tokens,
            "apply": apply
        }
        url = self.domain + "/space/api/explorer/v3/remove/"
        resp = (self.client.set_method("post")
                .set_data(json.dumps(req_data))
                .set_url(url)
                .set_headers({"referer": self.domain})
                .send_http())
        return resp


if __name__ == '__main__':
    cli = SpaceApi()

    cookies = {
        "session": "XN0YXJ0-955p82b7-400b-4230-87ad-4edbaa644bgh-WVuZA"
    }
    cli.domain = "https://bytedance.feishu-boe.net"
    cli.client.set_cookies(cookies)

    node_list = cli.get_folders(length=50).json()["data"]["node_list"]
    # node_list = cli.get_objs(length=50).json()["data"]["node_list"]

    cli.remove_folders(node_list)
    # cli.list_folder(token="V0REfhYRklibxOd8V5gbot2jc7I")

