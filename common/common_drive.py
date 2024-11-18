import json
import os

from loguru import logger

from common_http import HttpClient


def get_checksum(file_path):
    import zlib
    import os
    is_exist_file = os.path.exists(file_path)
    if not is_exist_file:
        return None
    with open(file_path, 'rb') as file:
        data = file.read()
        check_sum = zlib.adler32(data) & 0xffffffff
    return str(check_sum)


class Upload:
    def __init__(self, file_path: str, domain: str, mount_token: str, mount_point: str, session: str):
        self.file_token: str = ""
        self.upload_id: int = 0
        self.file_path = file_path
        self.domain = domain
        self.mount_token = mount_token
        self.mount_point = mount_point
        self.block_size: int = 0
        self.cookies = {"session": session}
        self.headers = {"referer": self.domain + "/base/" + self.mount_token}
        self.http_client = HttpClient().set_cookies(self.cookies).set_headers(self.headers)

    def prepare(self):
        """挂载容器 预处理"""
        name = self.file_path.split("/")[-1]
        data = {
            "mount_node_token": self.mount_token,
            "mount_point": self.mount_point,
            "name": name,
            "size": os.path.getsize(self.file_path),
            "size_checker": False
        }
        # print(len(data))
        # print(len(json.dumps(data)))
        url = self.domain + "/space/api/box/upload/prepare/"
        try:
            resp = (self.http_client
                    .set_method("post")
                    .set_url(url)
                    .set_data(json.dumps(data))
                    .send_http()
                    )
            if resp.status_code == 200:
                self.block_size = resp.json()['data']['block_size']
                self.upload_id = resp.json()['data']['upload_id']
        except Exception as e:
            logger.warning(str(e))

        return self

    def merge_block(self):
        """上传文件"""
        url = self.domain + "/space/api/box/stream/upload/merge_block/"
        headers = {
            "x-block-origin-size": str(self.block_size),
            "x-seq-list": "0",
            "x-block-list-checksum": get_checksum(self.file_path)
        }
        params = {
            "upload_id": self.upload_id,
            "mount_point": self.mount_point
        }
        with open(self.file_path, "rb") as f:
            data = f.read()
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_headers(headers)
                    .set_params(params)
                    .set_data(data)
                    .send_http())
            if resp.status_code == 200:
                logger.info("success upload req")
        except Exception as e:
            logger.warning(str(e))
        """上传文件"""
        return self

    def finsh(self):
        url = self.domain + "/space/api/box/upload/finish/"
        data = {
            "mount_point": self.mount_point,
            "upload_id": str(self.upload_id),
            "num_blocks": 1,
            "push_open_history_record": 0
        }
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                self.file_token = resp.json()['data']['file_token']
        except Exception as e:
            logger.warning(str(e))
        """任务状态轮训"""
        return self


class Download:
    def __init__(self, file_token: str, domain: str, session: str):
        self.file_token = file_token
        self.domain = domain
        self.cookies = {"session": session}
        self.headers = {"referer": self.domain + "/base/" + self.file_token}


if __name__ == '__main__':
    path = "/Users/bytedance/downloads/6位小数.xlsx"
    domain = "https://e5test1655436560.larkoffice.com"
    mount_token = "Rx9vbCNvWaFwRnsdxqjcIy5Lnig"
    mount_point = "bitable"
    session = "XN0YXJ0-4a3laaf7-ed84-45ad-941f-6ef8a8a5ae55-WVuZA"
    upload_task = Upload(path, domain, mount_token, mount_point, session)
    # print(os.path.getsize(path))
    upload_task.prepare().merge_block().finsh()
    print(upload_task.file_token)
    """D7kKbSm71ozUFyx7uxqbQrXHcLb"""
    '''V2Kjbkso7oFPvMx4YvxbDL83cFe'''
    """P2oEbZRCboiY7MxqMNFbzMWDcxh"""
