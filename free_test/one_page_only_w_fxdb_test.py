import csv

from common.common_openapi import Openapi


def update_field():
    context = {
        "base_token": "VU2Gbh3f2aIfWks9tdIbYB98czb",
        "table_token": "tbliFx033k5gWJFc",
        "field_id": "fldFwPGF4b",
        "data": {"field_name":"ceshi", "type":1005}
    }
    cli.update_fields(context)


def delete_fields():
    context = {
        "base_token": "VU2Gbh3f2aIfWks9tdIbYB98czb",
        "table_token": "tbliFx033k5gWJFc"
    }


if __name__ == '__main__':
    domain = "https://open.feishu-boe.cn"
    app = {
        "appid":"cli_a43deefb6078d01c",
        "passcode":"We4QaoymSF5ZytRFv9k5vfqNQUih3nON"
    }
    session = "XN0YXJ0-0bai0bac-b9b6-4d4d-826a-de57815cbfin-WVuZA"
    cli = Openapi(domain,app["appid"],app["passcode"])
    cli.http_client.set_cookies({"session":session})
    cli.set_access_token_user().set_access_token_default("u")
    cli.http_client.set_headers({"x-tt-env":"boe_write_fxdb_direct_debug"})
