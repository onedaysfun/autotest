import json

from loguru import logger

from common import common_http


class OndemandReq:
    def __init__(self, domain: str):
        self.domain = domain
        self.http_client = common_http.HttpClient()

    def ondemand_client_vars(self, context: dict):
        """
        :param context: dict 请求参数
            {
            base_token: str, 必填
            table_token: str, 必填
            viewID: str,
            needBase: bool,
            recordLimit: int,
            viewLazyLoad: bool,
            ondemandLimit: int,
            ondemandVer: int
            }
        :return: http resp
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        query_params = {
            "tableID": table_token
        }
        if "viewID" in list(context.keys()):
            view_token = context["viewID"]
            query_params["viewID"] = view_token
        if "needBase" in list(context.keys()):
            need_base = context["needBase"]
            query_params["needBase"] = need_base
        if "recordLimit" in list(context.keys()):
            record_limit = context["recordLimit"]
            query_params["recordLimit"] = record_limit
        if "viewLazyLoad" in list(context.keys()):
            view_lazy_load = context["viewLazyLoad"]
            query_params["viewLazyLoad"] = view_lazy_load
        if "ondemandLimit" in list(context.keys()):
            ondemand_limit = context["ondemandLimit"]
            query_params["ondemandLimit"] = ondemand_limit
        if "ondemandVer" in list(context.keys()):
            ondemand_ver = context["ondemandVer"]
            query_params["ondemandVer"] = ondemand_ver

        url = self.domain + "/space/api/v1/bitable/" + base_token + "/clientvars"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("get")
                    .set_params(query_params)
                    .send_http())
            if resp.status_code == 200:
                return resp
        except Exception as e:
            logger.warning(str(e))

    def ondemand_records(self, context: dict):
        """
        :param context: dict 请求参数
            {
            base_token: str,
            table_token: str,
            viewID: str,
            tableRev: int,
            jointRev: int,
            groupByInfoList: str like json.dumps(list)
            ondemandVer: int
            }
        :return: http resp
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        url = self.domain + "/space/api/v1/bitable/" + base_token + "/ondemand/records"
        query_params = {
            "tableID": table_token
        }
        if "viewID" in list(context.keys()):
            view_token = context["viewID"]
            query_params["viewID"] = view_token
        if "tableRev" in list(context.keys()):
            table_rev = context["tableRev"]
            query_params["tableRev"] = table_rev
        if "jointRev" in list(context.keys()):
            joint_rev = context["jointRev"]
            query_params["jointRev"] = joint_rev
        data = {}
        if "groupByInfoList" in list(context.keys()):
            group_by_info_list = context["groupByInfoList"]
            data["groupByInfoList"] = group_by_info_list
        if "ondemandVer" in list(context.keys()):
            ondemand_ver = context["ondemandVer"]
            data["ondemandVer"] = ondemand_ver
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_params(query_params)
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return resp
        except Exception as e:
            logger.warning(str(e))

    def ondemand_groups(self, context: dict):
        """
        :param context: dict 请求参数
            {
            base_token: str,
            table_token: str,
            viewID: str,
            tableRev: int,
            jointRev: int,
            groupList: str like json.dumps(list)
            }
        :return: http resp
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        url = self.domain + "/space/api/v1/bitable/" + base_token + "/groups"
        data = {
            "tableID": table_token
        }
        if "viewID" in list(context.keys()):
            view_token = context["viewID"]
            data["viewID"] = view_token
        if "tableRev" in list(context.keys()):
            table_rev = context["tableRev"]
            data["tableRev"] = table_rev
        if "jointRev" in list(context.keys()):
            joint_rev = context["jointRev"]
            data["jointRev"] = joint_rev
        if "groupList" in list(context.keys()):
            group_list = context["groupList"]
            data["groupList"] = group_list
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return resp
        except Exception as e:
            logger.warning(str(e))

    # todo: 按需的统计接口，看看啥时候有空写吧
    def ondemand_stats(self, context: dict):
        """
        :param context:
        {
            "tableID":"tblStwkc4IrX8eVS",
            "tableRev":5,
            "jointRev":5,
            "viewID":"vewykhGLSu",
            "groupList":"[{\"groupByList\":[]}]",
            "fieldList":[{"fieldID":"fldlReBCiN","statType":1}]
        }
        :return:
        """
        base_token = context["base_token"]
        table_token = context["table_token"]
        url = self.domain + "/space/api/v1/bitable/" + base_token + "/ondemand/group/stats"
        data = {
            "tableID": table_token
        }
        if "viewID" in list(context.keys()):
            view_token = context["viewID"]
            data["viewID"] = view_token
        if "tableRev" in list(context.keys()):
            table_rev = context["tableRev"]
            data["tableRev"] = table_rev
        if "jointRev" in list(context.keys()):
            joint_rev = context["jointRev"]
            data["jointRev"] = joint_rev
        if "groupList" in list(context.keys()):
            group_list = context["groupList"]
            data["groupList"] = group_list
        if "fieldList" in list(context.keys()):
            field_list = context["fieldList"]
            data["fieldList"] = field_list
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return resp
        except Exception as e:
            logger.warning(str(e))

    def ondemand_search_record(self, context: dict):
        """
        context:{"tableID":"tblStwkc4IrX8eVS","tableRev":8,"jointRev":8,"keyword":"","offset":0,"recordIDList":[],"limit":101,"queryType":"range"}
        """
        base_token = context["base_token"]
        tableID = context["tableID"]
        data = {
            "tableID": tableID
        }
        if "recordIDList" in list(context.keys()):
            recordIDList = context["recordIDList"]
            data["recordIDList"] = recordIDList
        if "queryType" in list(context.keys()):
            queryType = context["queryType"]
            data["queryType"] = queryType
        if "keyword" in list(context.keys()):
            keyword = context["keyword"]
            data["keyword"] = keyword
        if "limit" in list(context.keys()):
            limit = context["limit"]
            data["limit"] = limit
        if "offset" in list(context.keys()):
            offset = context["offset"]
            data["offset"] = offset
        if "tableRev" in list(context.keys()):
            tableRev = context["tableRev"]
            data["tableRev"] = tableRev
        if "jointRev" in list(context.keys()):
            jointRev = context["jointRev"]
            data["jointRev"] = jointRev
        url = self.domain + "/space/api/v1/bitable/" + base_token + "/search-records"
        try:
            resp = (self.http_client
                    .set_url(url)
                    .set_method("post")
                    .set_data(json.dumps(data))
                    .send_http())
            if resp.status_code == 200:
                return resp
        except Exception as e:
            logger.warning(str(e))


