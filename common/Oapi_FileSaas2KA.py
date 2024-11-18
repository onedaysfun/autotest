import json
import time

from common import common_http
from common import common_openapi


class OpenapiSaas2KA:
    def __init__(self, access_token, domain):
        self.domain = domain
        self.access_token = access_token
        self.http_client = common_http.HttpClient().set_headers({"Authorization": "Bearer " + self.access_token})

    def creat_download_task(self, file_type, file_token):
        url = self.domain + "/open-apis/drive/v2/export_jobs"
        data = {
            "file_extension": "lark" + (file_type if file_type != "docx" else "doc"),
            "token": file_token,
            "type": file_type
        }
        resp = (self.http_client
                .set_url(url)
                .set_method("post")
                .set_data(data)
                .send_http())
        return resp

    def is_download_task_finish(self, ticket, file_token, file_type):
        url = self.domain + "/open-apis/drive/v2/export_jobs/" + str(ticket)
        resp = (self.http_client
                .set_url(url)
                .set_method("get")
                .set_params({"token": file_token, "type": file_type})
                .send_http()
                )
        return resp

    def save_file_in_local(self, file_token):
        self.http_client.params = {}
        self.http_client.data = {}
        url = self.domain + "/open-apis/drive/v1/export_tasks/file/" + file_token + "/download"
        resp = (self.http_client
                .set_url(url)
                .set_method("get")
                .send_http())
        return resp

    def creat_saas2ka_task(self, file_token, file_type, mount_key, file_name):
        """
        :param file_name:
        :param file_token: 云空间文件token
        :param file_type: sheet/docx/base
        :param mount_key: 空间目录token，空为根节点
        :return:
        """
        # self.http_client.set_headers({'Content-Type': 'application/json'})
        url = self.domain + "/open-apis/drive/v2/import_jobs"
        point = {
            "mount_type": 1,
            "mount_key": mount_key
        }
        data = {
            "file_extension": "lark" + (file_type if file_type != "docx" else "doc"),
            "file_token": file_token,
            "type": file_type,
            "file_name": file_name,
            "point": point
        }
        resp = (self.http_client
                .set_url(url)
                .set_method("post")
                .set_data(json.dumps(data))
                .send_http())
        return resp

    def get_saas2ka_task_status(self, ticket):
        url = self.domain + "/open-apis/drive/v2/import_jobs/" + str(ticket)
        resp = (self.http_client
                .set_url(url)
                .set_method("get")
                .send_http())
        return resp


if __name__ == '__main__':
    # 全局配置
    domain_boe = "https://open.feishu-boe.cn"
    domain = "https://open.feishu-pre.cn"
    ka_domain = "https://open.kaqa.statusfeishu.cn"

    domain_use = domain
    # app配置
    base_boe = {
        "app_id": "cli_a43deefb6078d01c",
        "app_secret": "We4QaoymSF5ZytRFv9k5vfqNQUih3nON"
    }
    bytedance_boe = {
        "app_id": "cli_a21752576078d01c",
        "app_secret": "P1831odz4WRKJlyROnmlKd4rseIba417"
    }
    mg_cn_online = {
        "app_id": "cli_a3e4bf1ec4fb500c",
        "app_secret": "7zIL6UhxJcmuWDSD6wkQegREvOzp0aSb"
    }
    ka_online = {
        "app_id": "cli_a5703c20c238d0a9",
        "app_secret": "7o8xJ2XnQKd0nXLCbZc8fekRRze5Au28"
    }
    Saas2KA_app = {
        "app_id": "cli_a688fe767448d00d",
        "app_secret": "vScL1kx4lRGDyaMKYvNnKWwOZC4GQq73"
    }
    #
    flag = int(input("请输入app_id："))
    # 填写导出的文件信息
    file_info = {
        "file_type": "sheet",
        "file_token": "T1kgsJoljhSlY5tMBsfcckSAn2f"
    }
    # 主流程
    if flag == 1:
        app = base_boe
    elif flag == 2:
        app = bytedance_boe
    elif flag == 3:
        app = mg_cn_online
    elif flag == 4:
        app = ka_online
    elif flag == 5:
        app = Saas2KA_app
    else:
        print("请输入正确的app_id")
        exit()
    app_id = app['app_id']
    app_secret = app['app_secret']
    if flag != 4:
        # openapi的accessToken初始化
        tools = common_openapi.Openapi(domain_use, app_id, app_secret).set_access_token_tenant()
        # Saas2KA类初始化
        test1 = OpenapiSaas2KA(tools.t_token, domain_use)
        # test1.http_client.set_headers({"x-tt-env": "boe_ka_migration_qa"})
        resp = test1.creat_download_task(file_info['file_type'], file_info['file_token'])
        ticket = resp.json()['data']['ticket']
    while 1 and flag != 4:
        resp = test1.is_download_task_finish(ticket, file_info['file_token'], file_info['file_type'])
        try:
            file_token = resp.json()['data']['result']['file_token']
            if file_token != '':
                print("创建完成～" + file_token + "\n")
                break
            else:
                time.sleep(2)
                print("创建文件中。。。\n")
                if resp.json()['data']['result']['job_status'] != 2:
                    break
        except Exception as e:
            time.sleep(1000)
            print("创建文件中。。。\n")
            if resp.json()['data']['result']['job_status'] != 2:
                break

    if flag != 4:
        resp = test1.save_file_in_local(file_token)
        file_type = file_info['file_type']
        file_name = "/Users/bytedance/downloads/Saas2KA_test.lark" + (file_type if file_type != 'docx' else 'doc')
        with open(file_name, "wb") as file:
            file.write(resp.content)
    # KA 导入
    if flag == 4:
        file_token = 'boxsfCJAPqZTuNL7ENVRYKVMiwc'
        mount_key = 'NfBCf3OcAlMfZedxjV6s9SGcfLg'
        file_type = 'sheet'
        tools2 = common_openapi.Openapi(ka_domain, app_id, app_secret).set_access_token_tenant()
        test2 = OpenapiSaas2KA(tools2.t_token, ka_domain)
        # test2.http_client.set_headers({"x-tt-env": "boe_ka_migration_qa"})
        resp = test2.creat_saas2ka_task(file_token, file_type, mount_key, "Saas2KA_test")
        ticket = resp.json()['data']['ticket']

    while 1:
        try:
            resp = test2.get_saas2ka_task_status(ticket)
            if resp.json()['data']['result']['job_status'] == 2:
                print("导入文件中～\n")
                continue
            else:
                break
        except Exception as e:
            time.sleep(1)
            continue
