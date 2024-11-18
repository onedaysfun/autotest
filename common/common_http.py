import logging
import json
import time

import requests
from loguru import logger
LOG_FORMAT = "%(asctime)s.%(msecs)04d - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
need_req_log = True
need_resp_log = True
Text: str


class HttpClient:
    def __init__(self):
        self.method: str = "get"
        self.headers: dict = {}
        self.time_out: int = 60
        self.url: str = "none"
        self.data: dict = {}
        self.params: dict = {}
        self.cookies: dict = {}

    def send_http(self):
        method = self.method
        url = self.url
        time_out = self.time_out
        headers = self.headers
        cookies = self.cookies
        data = self.data
        params = self.params
        Req = requests.request(
            method=method,
            headers=headers,
            url=url,
            timeout=time_out,
            cookies=cookies,
            data=data,
            params=params
        )
        if need_req_log:
            json_cookies = json.dumps(cookies, sort_keys=True, indent=4).__str__()
            try:
                json_data = json.dumps(data, sort_keys=True, indent=4).__str__()
            except Exception as e:
                json_data = str(e)
            LOG_Req_BODY = f"<HttpRequest>: [{method.upper()}] {url}\ntime_out:{time_out}\nheaders:{headers}\ncookies:{json_cookies}\ndata:{json_data}\nparams:{params}\n"
            logger.info(LOG_Req_BODY)
        if need_resp_log:
            try:
                reqJson = Req.json()
                resp_header = Req.headers
                json_body = json.dumps(reqJson, sort_keys=True, indent=4).__str__()
                LOG_RESP_BODY = f"<HttpResponse>: [{method.upper()}] {url}\nstatus_code:{Req.status_code}\ncontent:{json_body}\n"
                if "X-Tt-Logid" in Req.headers.keys():
                    LOG_RESP_BODY = f"<HttpResponse>: [{method.upper()}] {url}\nstatus_code:{Req.status_code}\nlogid:{resp_header['x-tt-logid']}\ncontent:{json_body}\n"
                logger.info(LOG_RESP_BODY)
            except Exception as e:
                logger.warning(Req.content)
                logging.warning(e)
        return Req

    def set_method(self, method: str, **kwargs):
        """
        :param method: choices one ["get","post","put","delete"]
        :param kwargs: method = ["get","post","put","delete"]
        :return:
        """
        if method:
            self.method = method
        elif kwargs["method"]:
            self.method = kwargs["method"]
        return self

    def set_url(self, url: str, **kwargs):
        """
        :param url: str
        :param kwargs:
        :return:
        """
        if url:
            self.url = url
        elif kwargs["url"]:
            self.url = kwargs["url"]
        return self

    def set_cookies(self, cookies: dict, **kwargs):
        """
        :param cookies: dict()
        :param kwargs:
        :return:
        """
        if cookies:
            self.cookies.update(cookies)
        elif kwargs["cookies"]:
            self.cookies = kwargs["cookies"]
        return self

    def set_data(self, data: dict, **kwargs):
        if data:
            self.data = data
        elif kwargs["data"]:
            self.data = kwargs["data"]
        return self

    def set_params(self, params: dict, **kwargs):
        if params:
            self.params = params
        elif kwargs["params"]:
            self.params = kwargs["params"]
        return self

    def set_headers(self, headers: dict, **kwargs):
        if headers:
            self.headers.update(headers)
        elif kwargs["headers"]:
            self.headers.update(headers)
        return self


if __name__ == '__main__':
    ht = HttpClient()
    ht.cookies = {"1": 1}
    cookies = {"2":2,"3":3}
    ht.set_cookies(cookies)
    print(ht.cookies)



    print(int(time.time()))