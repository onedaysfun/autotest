import base64
import gzip
import json
import time

from Entity import base
from common import common_http
from loguru import logger
from common.base64_en_or_decode import base64encode, base64decode
from common.send_message_cs import EditBase, EditTable


class Edit:
    def __init__(self, url: str = None, session: str = None):
        self.is_fxdb_base = False
        self.base_info = base.Base()
        self.table_info = base.Table()
        self.base_info.token = url.split("/")[4]
        self.domain = "https://" + url.split("/")[2]
        self.cookies = {}
        if session:
            self.cookies["session"] = session
        self.httpClient = common_http.HttpClient()
        self.init_base_info()

    def init_base_info(self):
        domain = self.domain
        base_token = self.base_info.token
        self.table_info.parent_token = base_token
        try:
            resp = (self.httpClient.set_url(f"{domain}/space/api/v1/bitable/{base_token}/clientvars/?needBase=true")
                    .set_method("get")
                    .set_cookies(self.cookies)
                    .send_http()
                    )
            if resp.status_code == 200:
                try:
                    gzip_schema = resp.json()["data"]["oldSchema"]["gzipSchema"]
                    schema = base64decode(gzip_schema)
                    if schema:
                        self.base_info.id = schema['base']['id']
                        self.base_info.blocks = schema['base']['blocks']
                        self.base_info.version = schema['base']['rev']
                except Exception as a:
                    logger.info("no find oldSchema" + a.__str__())
                    gzip_schema = resp.json()["data"]["base"]
                    schema = base64decode(gzip_schema)
                    if schema:
                        self.base_info.id = schema['id']
                        self.base_info.blocks = schema['blocks']
                        self.base_info.version = schema['rev']
                    if schema["schemaVersion"] > 2:
                        self.is_fxdb_base = True
        except Exception as e:
            logger.error(e)

    def init_table_info(self, table_token):
        domain = self.domain
        base_token = self.base_info.token
        self.table_info.token = table_token
        try:
            resp = (self.httpClient.set_url(f"{domain}/space/api/v1/bitable/{base_token}/clientvars/")
                    .set_method("get")
                    .set_cookies(self.cookies)
                    .set_params({"tableID": table_token})
                    .send_http())
            if resp.status_code == 200:
                try:
                    gzip_schema = resp.json()["data"]["oldSchema"]["gzipSchema"]
                    schema = base64decode(gzip_schema)
                    if schema:
                        self.table_info.token = schema["data"]["table"]["meta"]["id"]
                        self.table_info.localRev = schema["data"]["table"]["meta"]["rev"]
                        self.table_info.field_map = schema["data"]["table"]["fieldMap"]
                except Exception as a:
                    logger.info("no find oldSchema" + a.__str__())
                    gzip_schema = resp.json()["data"]["table"]
                    schema = base64decode(gzip_schema)
                    if schema:
                        self.table_info.token = schema["meta"]["id"]
                        self.table_info.localRev = schema["meta"]["rev"]
                        self.table_info.field_map = schema["fieldMap"]

        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    url = "https://jvj3hlmfca.feishu-boe.cn/base/CoczboJNUasQrps3YrBb7dEVcbc"
    session = ""
    # 初始化base消息
    star = Edit(url, session)
    # 初始化需要操作的table信息 选择操作第一个table
    star.init_table_info(star.base_info.blocks[0])
    # testBaseClient = EditBase(session,
    #                           star.base_info.token,
    #                           star.base_info.version,
    #                           star.domain)
    # testtableClient = EditTable()
    # testBaseClient.update_meta("自动化修改")
    # testBaseClient.update_table_name("wogaide", star.table_info.token)
    # testBaseClient.update_table_name("888", star.table_info.token)
    testTableEditClient = EditTable(session,
                                    star.table_info.token,
                                    star.table_info.localRev,
                                    star.table_info.parent_token,
                                    star.domain)
    field_list_1 = [
        {'Rating': 2},
        {'Currency': 2},
        {'ModifiedUser': 1004},
        {'Lookup': 19},
        {'Stage': 24},
        {'Text': 1},
        {'Button': 3001},
        {'Email': 1},
        {'Checkbox': 7},
        {'Number': 2},
        {'Location': 22},
        {'Barcode': 1},
        {'Phone': 13},
        {'CreatedTime': 1001},
        {'DuplexLink': 21},
        {'CreatedUser': 1003},
        {'Formula': 20},
        {'SingleLink': 18},
        {'ModifiedTime': 1002},
        {'Progress': 2},
        {'Url': 15}]
    for i in field_list_1:
        testTableEditClient.add_field(i, list(i.keys())[0])
        time.sleep(1)
