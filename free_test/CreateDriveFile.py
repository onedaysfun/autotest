# -*- coding: utf-8 -*-
import base64
import gzip
import json
import time
import os
import requests
# from requests_toolbelt.multipart.encoder import MultipartEncoder
from urllib.parse import quote, urlencode
# import tool
import pandas as pd

LocalPathPre = "/Users/bytedance/Desktop/mgdata/"
LocalImagePath = "/Users/bytedance/Desktop/mgdata/images/"
LocalPDFPath = "/Users/bytedance/Desktop/mgdata/pdfs/"


TestFilePath = "/Users/bytedance/Downloads/"

AccountConfig = {
    "cn_space": "XN0YXJ0-108l0ee3-37dc-44b8-b335-afc9c21dca1e-WVuZA",
    "sg_space": "XN0YXJ0-f94v8057-0802-42f9-8024-3404fd6d1c80-WVuZA",
    "va_space": "XN0YXJ0-938ua8ed-d355-4ff9-9a8e-377ca4c73cf1-WVuZA"
}


def create_image():
    scene_config = ["cn_space", "va_space", "sg_space", "cn_doc", "va_doc", "sg_doc"]
    for scene in scene_config:
        for i in range(98):
            url = "http://box-filegen.byted.org/image"
            params = {
                "width": 800,
                "height": 800,
                "ext": ".jpg",
            }
            rsp = requests.get(url, params=params)
            image_name = int(time.time())
            image_path = LocalImagePath + scene + "/" + str(i) + str(image_name) + ".jpg"
            print(i, rsp.status_code)
            if rsp.status_code == 200:
                with open(image_path, 'wb') as f:
                    for chunk in rsp.iter_content(chunk_size=4096):
                        if chunk:
                            f.write(chunk)
    time.sleep(5)


def create_pdf():
    scene_config = ["cn_space", "va_space", "sg_space"]
    for scene in scene_config:
        for i in range(48):
            url = "http://box-filegen.byted.org/pdf"
            params = {
                "paragraphs": 5,
                "para_length": 1000,
                "ext": ".pdf",
            }
            rsp = requests.get(url, params=params)
            pdf_name = int(time.time())
            pdf_path = LocalPDFPath + scene + "/" + str(i) + str(pdf_name) + ".pdf"
            print(i, rsp.status_code)
            if rsp.status_code == 200:
                with open(pdf_path, 'wb') as f:
                    for chunk in rsp.iter_content(chunk_size=4096):
                        if chunk:
                            f.write(chunk)
        time.sleep(5)


def create_one_pdf():
    for i in range(2):
        url = "http://box-filegen.byted.org/pdf"
        params = {
            "paragraphs": 19,
            "para_length": 1500,
            "ext": ".pdf",
        }
        rsp = requests.get(url, params=params)
        pdf_name = int(time.time())
        pdf_path = LocalPDFPath + "" + str(i) + str(pdf_name) + ".pdf"
        print(i, rsp.status_code)
        if rsp.status_code == 200:
            with open(pdf_path, 'wb') as f:
                for chunk in rsp.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)


def upload_image_to_space_boe():
    upload_all_url_pre = "https://bytedance.feishu-boe.cn/space/api/box/stream/upload/all/"
    file_path = "/Users/bytedance/Desktop/mgdata/images/cn_space/01649838467.jpg"
    file_name = "01649838467.jpg"
    data_dic = {
        "name": file_name,
        "size": os.path.getsize(file_path),
        "mount_point": "explorer",
        "push_open_history_record": 1,
        "mount_node_token": ""
    }
    header = {
        "X-Tt-Stress": "true",
        "cookie": "session=XN0YXJ0-260j40e4-c8f5-44dc-b2d8-f80bb08c7fpv-WVuZA",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryUUimaWnbK0l0IC32"
    }
    boundary = "----WebKitFormBoundaryUUimaWnbK0l0IC32"

    multipart_encoder = MultipartEncoder(
        fields={
            "type": "application/octet-stream",
            "filename": file_name,
            "Content-Type": "application/octet-stream",
            "file": (
                file_name, open(file_path, 'rb'), 'application/octet-stream')
        },
        boundary=boundary
    )
    url = upload_all_url_pre + "?" + urlencode(data_dic)
    response = requests.post(url=url, headers=header, data=multipart_encoder)
    print(response.status_code)
    print(response.content)
    print(response.headers)


def upload_image_to_space_online(type_name, result_file_name):
    upload_all_url_pre = "https://www.feishu.cn/space/api/box/stream/upload/all/"
    dir_path = LocalImagePath + type_name + "/"
    file_names = tool.get_file_names_by_dir_path(dir_path)
    result_token = []
    for file_name in file_names:
        print(file_name)
        file_path = dir_path + file_name
        data_dic = {
            "name": file_name,
            "size": os.path.getsize(file_path),
            "mount_point": "explorer",
            "push_open_history_record": 1,
            "mount_node_token": ""
        }
        header = {
            # "X-Tt-Stress": "true",
            "env": "Pre_release",
            "cookie": "session=" + AccountConfig[type_name],
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryUUimaWnbK0l0IC32"
        }

        boundary = "----WebKitFormBoundaryUUimaWnbK0l0IC32"

        multipart_encoder = MultipartEncoder(
            fields={
                "type": "application/octet-stream",
                "filename": file_name,
                "Content-Type": "application/octet-stream",
                "file": (
                    file_name, open(file_path, 'rb'), 'application/octet-stream')
            },
            boundary=boundary
        )
        url = upload_all_url_pre + "?" + urlencode(data_dic)
        response = requests.post(url=url, headers=header, data=multipart_encoder)
        print(response.status_code)
        print(response.content)
        print(response.headers)
        rsp_content = json.loads(response.content)
        file_token = rsp_content["data"]["file_token"]
        result_token.append(file_token)
        time.sleep(1)
    result_csv = dir_path + result_file_name
    df = {
        "token": result_token,
    }
    data = pd.DataFrame(df)
    data.to_csv(result_csv, index=False)


def upload_file_to_space_online(file_type, type_name, result_file_name):
    upload_all_url_pre = "https://pqjfabd1vo.feishu.cn/space/api/box/stream/upload/all/"
    dir_path = LocalPathPre + file_type + "/" + type_name + "/"
    file_names = tool.get_file_names_by_dir_path(dir_path)
    result_token = []
    for file_name in file_names:
        print(file_name)
        file_path = dir_path + file_name
        data_dic = {
            "name": file_name,
            "size": os.path.getsize(file_path),
            "mount_point": "explorer",
            "push_open_history_record": 1,
            "mount_node_token": ""
        }
        header = {
            # "X-Tt-Stress": "true",
            # "env": "Pre_release",
            "cookie": "session=" + AccountConfig[type_name],
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryUUimaWnbK0l0IC32",
            "x-tt-trace": "1"
        }

        boundary = "----WebKitFormBoundaryUUimaWnbK0l0IC32"

        multipart_encoder = MultipartEncoder(
            fields={
                "type": "application/octet-stream",
                "filename": file_name,
                "Content-Type": "application/octet-stream",
                "file": (
                    file_name, open(file_path, 'rb'), 'application/octet-stream')
            },
            boundary=boundary
        )
        url = upload_all_url_pre + "?" + urlencode(data_dic)
        response = requests.post(url=url, headers=header, data=multipart_encoder)
        print(response.status_code)
        print(response.content)
        print(response.headers)
        rsp_content = json.loads(response.content)
        file_token = rsp_content["data"]["file_token"]
        result_token.append(file_token)
        time.sleep(3)
    result_csv = dir_path + result_file_name
    df = {
        "token": result_token,
    }
    data = pd.DataFrame(df)
    data.to_csv(result_csv, index=False)



def get_file_info_pre():
    url = "https://www.feishu.cn/space/api/box/file/info/"
    data_dic = {
        "caller": "explorer",
        "file_token": "boxcnKDgPdHBpbES7AwKL12jbFb",
        "mount_point": "explorer",
        "option_params": ["preview_meta", "check_cipher"]
    }
    header = {
        # "X-Tt-Stress": "true",
        # "env": "pre_release",
        "content-type": "application/json",
        "cookie": "session=XN0YXJ0-73btcfb7-1db0-456d-a024-1fa3a9232aa1-WVuZA",
    }

    response = requests.post(url=url, headers=header, data=json.dumps(data_dic))
    print(response.status_code)
    print(response.content)
    print(response.headers)


def create_doc():
    url = "https://www.feishu.cn/space/api/explorer/v2/create/object/"
    data_dic = {
        "type": 2,
        "name": "test",
        "source": 0,
    }
    header = {
        # "X-Tt-Stress": "true",
        # "env": "pre_release",
        "content-type": "application/json",
        "cookie": "session=XN0YXJ0-73btcfb7-1db0-456d-a024-1fa3a9232aa1-WVuZA",
        "referer": "https://www.feishu.cn/drive/home"
    }

    response = requests.post(url=url, headers=header, data=json.dumps(data_dic))
    print(response.status_code)
    print(response.content)
    print(response.headers)


def upload_image_to_doc():
    prepare_url = "https://api3-eeft-docs.larkoffice.com/space/api/box/upload/prepare/"
    file_path = "/Users/bytedance/Desktop/mgdata/images/cn_space/01649838467.jpg"
    file_name = "01649838467.jpg"
    data_dic = {
        "name": file_name,
        "size": os.path.getsize(file_path),
        "mount_point": "bitable_image",
        "mount_node_token": "BBMBb87yna6fxesaDeal2g2jgdd",
        "size_checker": False
    }
    header = {
        # "X-Tt-Stress": "true",
        # "env": "pre_release",
        "cookie": "session=XN0YXJ0-a99k63fc-ae98-4a92-9715-4324dd16ddd1-WVuZA",
        "referer": "https://www.feishu.cn/docs/doccn2MHx9qYAMwrIk9UBj4Wovd",
        "content-type": "application/json"
    }
    prepare_rsp = requests.post(prepare_url, headers=header, data=json.dumps(data_dic))
    print("prepare", prepare_rsp.status_code)
    prepare_data = json.loads(prepare_rsp.content)
    upload_id = prepare_data["data"]["upload_id"]
    block_size = prepare_data["data"]["block_size"]

    merge_block_url = "https://internal-api-drive-stream.feishu.cn/space/api/box/stream/upload/merge_block/?"
    merge_block_url += "upload_id=" + upload_id + "&mount_point=doc_image"
    merge_block_header = {
        "cookie": "session=XN0YXJ0-a99k63fc-ae98-4a92-9715-4324dd16ddd1-WVuZA",
        "x-block-origin-size": str(block_size),
        "x-seq-list": "0",
        "x-block-list-checksum": get_checksum(file_path),
        "referer": "https://www.feishu.cn/",
        "content-type": "application/json"
    }
    with open(file_path, "rb") as f:
        merge_block_data = f.read()
    merge_block_rsp = requests.post(merge_block_url, headers=merge_block_header, data=merge_block_data)
    print("merge_block", merge_block_rsp.status_code)

    finish_url = "https://www.feishu.cn/space/api/box/upload/finish/"
    finish_data = {
        "mount_point": "doc_image",
        "num_blocks": 1,
        "push_open_history_record": 0,
        "upload_id": upload_id,
    }
    finish_header = {
        "cookie": "session=XN0YXJ0-73btcfb7-1db0-456d-a024-1fa3a9232aa1-WVuZA",
        "referer": "https://www.feishu.cn/docs/doccn2MHx9qYAMwrIk9UBj4Wovd"
    }
    finish_rsp = requests.post(finish_url, headers=finish_header, data=json.dumps(finish_data))
    print("finish", finish_rsp.status_code)
    finish_content = json.loads(finish_rsp.content)
    print(finish_content["code"])
    print(finish_content["data"]["file_token"])



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


if __name__ == '__main__':
    # upload_file_to_space_online("pdfs", "va_space", "va_space_pdfs_token.csv")
    # url = "https://bytedance.feishu.cn/space/api/box/invoke/create/"
    # headers = {
    #     "cookie": "session=XN0YXJ0-de1o9847-720b-4c74-8777-f4599edc84e0-WVuZA",
    #     "referer": "https://bytedance.feishu.cn/drive/home/"
    # }
    # list_data = [{"token":"boxlg0RWJEdcEHUpxsUi0xtTshb","type":12,"name":"71.jpeg"},{"token":"boxlgkmI8VwPgE244MigrIFYGkf","type":12,"name":"pexels-photo-9024609.jpg"}]
    # # 折中方案，参数按如下方式组织，也是模拟multipart/form-data的核心
    # params = {"invoke_data": json.dumps(list_data)}
    #
    # res = requests.post(url, files=params, headers=headers)
    # # 查看请求体是否符合要求，有具体接口可以直接用具体接口，成功则符合要求，此处主要是演示用
    # print(res.request.body)
    # # 查看请求头
    # print(res.request.headers)
    # print(res.content)
    checksum = get_checksum(TestFilePath + "单行1KB.csv")
    print(checksum)


def get_upload_all_url(params):
    import os
    from urllib.parse import urlencode
    g_url = params[0]
    file_name = params[1]
    file_path =  "/tmp/blocks-app-download/" + file_name
    pre_url = g_url + "space/api/box/stream/upload/all/"
    folder_token = params[2]
    if folder_token == "''":
        folder_token = ""
    data_dic = {
        "name":file_name,
        "size": os.path.getsize(file_path),
        "mount_point": "explorer",
        "push_open_history_record":1,
        "mount_node_token":folder_token
    }
    url = pre_url + "?"+urlencode(data_dic)+"&ext%5Bextra%5D=&size_checker=true"
    return url


cs = [
    {
        "command": "SetRecord",
        "type": 2,
        "actions": [
            {
                "action": "data.setRecord",
                "type": 2,
                "tableId": "tblIwPvEQXMJKaW4",
                "viewId": "vewOpbv4DJ",
                "recordId": "rectZrrjKwwbnx",
                "viewType": 1,
                "data": {
                    "fldYlTe8T9": {
                        "type": 17,
                        "value": [
                            {
                                "id": "A6aAbDLyCoOYxNxnWdPbTdSQcih",
                                "attachmentToken": "A6aAbDLyCoOYxNxnWdPbTdSQcih",
                                "name": "单行1KB.csv",
                                "mimeType": "text/csv",
                                "size": 1092,
                                "timeStamp": 1703227401473
                            }
                        ]
                    }
                }
            }
        ],
        "syncFlag": 0
    }
]
def base64_encode(obj):
    data = gzip.compress(json.dumps(obj).encode())
    result = base64.b64encode(data).decode("utf-8")
    return result

print(base64_encode(cs))