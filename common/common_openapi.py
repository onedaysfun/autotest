import json

from loguru import logger

from common.common_http import HttpClient


class Openapi:
    def __init__(self, domain: str, app_id: str, app_secret: str):
        self.pass_code = None
        self.domain = domain
        self.app_id = app_id
        self.app_secret = app_secret
        self.session = ""
        self.open_id = ""
        # app_access_token
        self.t_token = ""
        # user_access_token
        self.u_token = ""
        self.access_token_use = ""
        self.http_client = HttpClient()

    def set_access_token_tenant(self):
        if self.t_token != "":
            self.access_token_use = self.t_token
            return self
        url = self.domain + "/open-apis/auth/v3/tenant_access_token/internal/"
        data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                self.t_token = resp.json()['tenant_access_token']
        except Exception as e:
            logger.warning(str(e))
        return self

    def set_access_token_user(self):
        if self.u_token != "":
            self.access_token_use = self.u_token
            return self
        # session2code
        url = self.domain + "/open-apis/mina/v2/login"
        data = {
            "appid": self.app_id,
            "sessionid": self.session
        }
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(data)
                    .send_http())
            if resp.status_code == 200:
                self.pass_code = resp.json()['data']['code']
        except Exception as e:
            logger.warning(str(e))
        # code2token
        url2 = self.domain + "/open-apis/mina/loginValidate"
        data2 = {
            "appid": self.app_id,
            "secret": self.app_secret,
            "code": self.pass_code
        }
        try:
            resp = (self.http_client
                    .set_url(url2)
                    .set_method("post")
                    .set_data(data2)
                    .send_http())
            if resp.status_code == 200:
                self.u_token = resp.json()['access_token']
        except Exception as e:
            logger.warning(str(e))
        return self

    def set_access_token_default(self, token_type):
        """
        :param token_type: [t/u]
        :return:
        """
        if token_type == "t":
            self.access_token_use = self.t_token
        elif token_type == "u":
            self.access_token_use = self.u_token
        if self.access_token_use != "":
            self.http_client.set_headers({"Authorization": "Bearer " + self.access_token_use})
        else:
            logger.error("access_token_use is nil!")

    def create_base(self, name, folder_token):
        url = self.domain + "/open-apis/bitable/v1/apps"
        data = {"name": name, "folder_token": folder_token}
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(data)
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))
        return self

    def create_sheet(self, title, folder_token):
        url = self.domain + "/open-apis/sheets/v3/spreadsheets"
        data = {"title": title, "folder_token": folder_token}
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(data)
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))
        return self

    def create_docx(self, title, folder_token):
        url = self.domain + "/open-apis/docx/v1/documents"
        data = {"title": title, "folder_token": folder_token}
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(data)
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))
        return self

    def create_nodes_wiki(self, space_id, obj_type, title, parent_node_token):
        """
        :param space_id:
        :param obj_type: [doc,docx,sheet,bitable,file]
        :param title:
        :param parent_node_token:
        :return:
        """
        url = self.domain + f"/open-apis/wiki/v2/spaces/{str(space_id)}/nodes"
        data = {
            "obj_type": obj_type,
            "title": title,
            "node_type": "origin",
            "parent_node_token": parent_node_token
        }
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(data)
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))

    def set_record(self, context):
        base_token = context["base_token"]
        table_token = context["table_token"]
        record = context["record"]
        data = context["data"]
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/tables/{table_token}/records/{record}"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("put")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))

    def batch_create_records(self, context):
        """
        help doc: https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_create
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        data = context["data"]
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/tables/{table_token}/records/batch_create"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))

    def batch_delete_records(self, context):
        """
        help doc: https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_delete
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        data = context["data"]
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/tables/{table_token}/records/batch_delete"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))

    def batch_update_records(self, context):
        """
        help doc: https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/batch_update
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        data = context["data"]
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/tables/{table_token}/records/batch_update"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return self
        except Exception as e:
            logger.warning(str(e))

    def copy_base(self, context: dict):
        """
        help doc: https://open.feishu.cn/document/server-docs/docs/bitable-v1/app/copy
        """
        base_token = context["base_token"]
        data = {}
        if "name" in list(context.keys()):
            data["name"] = context["name"]
        if "folder_token" in list(context.keys()):
            data["folder_token"] = context["folder_token"]
        if "without_content" in list(context.keys()):
            data["without_content"] = context["without_content"]
        if "time_zone" in list(context.keys()):
            data["time_zone"] = context["time_zone"]
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/copy"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            return resp
        except Exception as e:
            logger.warning(str(e))

    def transfer_owner(self, context):
        """
        help doc:https://open.feishu.cn/document/server-docs/docs/permission/permission-member/transfer_owner
        """
        file_token = context["token"]
        file_type = context["type"]
        data = {
            "member_type": context["member_type"],
            "member_id": context["member_id"]
        }
        url = self.domain + f"/open-apis/drive/v1/permissions/{file_token}/members/transfer_owner"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_params({"type": file_type})
                    .set_data(json.dumps(data))
                    .send_http())
            return resp
        except Exception as e:
            logger.warning(str(e))

    def create_fields(self, context: dict):
        """
        help doc:https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/create
        """
        base_token = context['base_token']
        table_token = context['table_token']
        data = {
            "field_name": context['field_name'],
            "type": context['type']
        }
        if "property" in list(context.keys()):
            data['property'] = context['property']
        if "description" in list(context.keys()):
            data['description'] = context['description']
        if "ui_type" in list(context.keys()):
            data['ui_type'] = context['ui_type']
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/tables/{table_token}/fields"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            return resp
        except Exception as e:
            logger.warning(str(e))

    def update_fields(self, context: dict):
        """
        help doc:https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/update
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        field_id = context["field_id"]
        data = context["data"]
        url = self.domain + f"/open-apis/bitable/v1/apps/{base_token}/tables/{table_token}/fields/{field_id}"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("put")
                    .set_data(json.dumps(data))
                    .send_http())
            return resp
        except Exception as e:
            logger.warning(str(e))

    def delete_field(self, context):
        """
        help doc:https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-field/delete
        """
        base_token = context["base_token"]

    def subscribe_base(self, context:dict):
        """
        help doc:https://open.feishu-pre.cn/document/server-docs/docs/drive-v1/event/subscribe
        """
        base_token = context["token"]
        base_type = context["type"]
        url = self.domain + f"/open-apis/drive/v1/files/{base_token}/subscribe"
        params = {
            "file_type": base_type
        }
        self.http_client.data = {}
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_params(params)
                    .send_http())
            return resp
        except Exception as e:
            logger.warning(str(e))

    def subscribe_base_get(self, context: dict):
        """
        help doc:URL_ADDRESS
        """
        base_token = context["token"]
        base_type = context["type"]
        url = self.domain + f"/open-apis/drive/v1/files/{base_token}/get_subscribe"
        params = {
            "file_type": base_type
        }
        self.http_client.data = {}
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("get")
                    .set_params(params)
                    .send_http())
            return resp
        except Exception as e:
            logger.warning(str(e))


if __name__ == '__main__':
    domain = "https://open.feishu-boe.cn"
    base_boe = {
        "app_id": "cli_a43deefb6078d01c",
        "app_secret": "We4QaoymSF5ZytRFv9k5vfqNQUih3nON"
    }
    bytedance_boe = {
        "app_id": "cli_a21752576078d01c",
        "app_secret": "P1831odz4WRKJlyROnmlKd4rseIba417"
    }
    session = ""
    cli = Openapi(domain,base_boe['app_id'], base_boe['app_secret'])
    cli.session = session
    # cli.http_client.set_headers({"x-tt-env":"boe_copy_mq_point_kill"})
    cli.set_access_token_user().set_access_token_default("u")
    context_copy = {
        "base_token": "UT95bg3KwaSICUsEGfTbhCYIcmI"
    }
    resp = cli.copy_base(context_copy)
    app_token = resp.json()["data"]["app"]["app_token"]
    context_transfer = {
        "token": app_token,
        "type": "bitable",
        "member_type": "openid",
        "member_id": "ou_76c98d78303bf9f7c374cdc462ac0bba"
    }
    cli.transfer_owner(context_transfer)