from threading import Thread

from common.interface.history import History

doc_list = [
    {
        "token": "JpMrbrTKnaLNlwsFJ7PjBjTcpxd",
        "major0": {
            "version_id": "7428109038353252386",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428531597573226529",
            "major_version": 252
        },
    },
    {
        "token": "Q3rkbukg5aUjM0sovlFjrIRhpbf",
        "major0": {
            "version_id": "7428127008306561058",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428531499739889697",
            "major_version": 246
        },
    },
    {
        "token": "OXk1bM9ckaPtCFsk5SZj7ehfpTd",
        "major30w": {
            "version_id": "7428536025164890145",
            "major_version": 252
        },
        "major0": {
            "version_id": "7428115580379611170",
            "major_version": 0
        },
    },
    {
        "token": "RaUsbT7a3anb41sH4q8jWhDTpxf",
        "major0": {
            "version_id": "7428136893979672610",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428536386680782881",
            "major_version": 249
        }
    },
    {
        "token": "FddwbX7DtamTJysxsHEj9eqgp0g",
        "major0": {
            "version_id": "7428136927998165026",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428537016092704801",
            "major_version": 249
        }
    },
    {
        "token": "OSRkbrZGlaVwxCsmR97jz2ZLpbb",
        "major0": {
            "version_id": "7428146605045137442",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428537426196054049",
            "major_version": 249
        }
    },
    {
        "token": "MNl7bOBYhavyAksGjEPjlX9CpUI",
        "major0": {
            "version_id": "7428146628106207266",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428540298217226273",
            "major_version": 237
        }
    },
    {
        "token": "RmFVbj0ZiaFM30sB580j7pWkpQf",
        "major0": {
            "version_id": "7428158285860519970",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428570774190309409",
            "major_version": 249
        }
    },
    {
        "token": "BICpbUvRoajOWdsmNc5jbn9mpff",
        "major0": {
            "version_id": "7428158306897788962",
            "major_version": 0
        },
        "major30w": {
            "version_id": "7428571295511478305",
            "major_version": 248
        }
    }
]


doc_list_100w = [
    {
        "token": "RAQMbCSCva1rPXsBt2ycAZjJn5b",
        "major0": {
            "version_id": "7430103439933718556",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431207224711184387",
            "major_version": 1113
        },
        "major_max": {
            "version_id": "7431200964776837122",
            "major_version": 1065
        }
    },
    {
        "token": "DodNbyMa6ap0XzsgYgwc5LKKnAD",
        "major0": {
            "version_id": "7430107446856810500",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431208217249988612",
            "major_version": 1055
        },
        "major_max": {
            "version_id": "7431148596194820099",
            "major_version": 1052
        }
    },
    {
        "token": "I8kLbbjTNagymTsWe92cXqOInUd",
        "major0": {
            "version_id": "7430107677677682691",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431208612929634307",
            "major_version": 1045
        },
        "major_max": {
            "version_id": "7431208612929634307",
            "major_version": 1039
        }
    },
    {
        "token": "COeWbSYBfackDmsu0YccGQwfnBe",
        "major0": {
            "version_id": "7430108247071096834",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431209366431563804",
            "major_version": 1185
        },
        "major_max": {
            "version_id": "7431209366431563804",
            "major_version": 1179
        }
    },
    {
        "token": "DMysblhbcalzxZsuv8vcuAm4nzf",
        "major0": {
            "version_id": "7430108488501493763",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431114354478743580",
            "major_version": 1044
        },
        "major_max": {
            "version_id": "7431114354478743580",
            "major_version": 1038
        }
    },
    {
        "token": "My0vbmuQFaTk5QsWYxnct8kMnue",
        "major0": {
            "version_id": "7430108653030424579",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431114429888905217",
            "major_version": 1044
        },
        "major_max": {
            "version_id": "7431114429888905217",
            "major_version": 1040
        }
    },
    {
        "token": "Coadbt7xtamhoIsr7Abcy7wbnse",
        "major0": {
            "version_id": "7430108895283003420",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431114668201279492",
            "major_version": 1043
        },
        "major_max": {
            "version_id": "7431114668201279492",
            "major_version": 1039
        }
    },
    {
        "token": "RtZSbqz39a09Hvs06AHcCYjlnmc",
        "major0": {
            "version_id": "7430109054555373596",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431114742494576643",
            "major_version": 1044
        },
        "major_max": {
            "version_id": "7431114742494576643",
            "major_version": 1042
        }
    },
    {
        "token": "VRc0bsTh3a7aTAsEXgrcUboVnTl",
        "major0": {
            "version_id": "7430109204809924610",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431114807578001411",
            "major_version": 1043
        },
        "major_max": {
            "version_id": "7431114807578001411",
            "major_version": 1037
        }
    },
    {
        "token": "B4N6buKgoa9gQ5sMbyYcGLsDnSF",
        "major0": {
            "version_id": "7430109441996816386",
            "major_version": 0
        },
        "major100w": {
            "version_id": "7431114882299756545",
            "major_version": 1054
        },
        "major_max": {
            "version_id": "7431114882299756545",
            "major_version": 1048
        }
    }
]


def task(i, recover_0, is_max):
    if recover_0:
        key = "major0"
    else:
        key = "major100w"
    if is_max:
        key = "major_max"
    token = doc_list_100w[i]["token"]
    version_id = doc_list_100w[i][key]["version_id"]
    major_id = doc_list_100w[i][key]["major_version"]
    Cli.time_machine_recover(token, version_id, major_id)


if __name__ == '__main__':
    domain = "https://yalixw0asad.feishu.cn"
    cookies = {"session": "XN0YXJ0-6bbgaa77-4277-4e9d-bcc0-0af9e54e7200-WVuZA"}
    headers = {"x-tt-stress": "true", "env": "pre_release"}
    Cli = History(domain, cookies)
    Cli.httpClient.set_headers(headers)
    # 是否还原到0版本
    recover_0 = False
    # 是否还原到max版本
    is_max = False
    # 起始文档数组的下标
    # 0，2，5
    start = 0
    # 文档数组的长度
    # 2，3，5
    length = 5
    thread_list = []
    for i in range(start, start + length):
        t = Thread(target=task(i, recover_0, is_max))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()