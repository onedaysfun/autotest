if __name__ == '__main__':
    tableTokens = [
        'tblAOt05O12F2mg3',
        'tbleabQ6h3c1xiaE',
        'tblmnVQKLPZrSasS',
        'tblaIAZjCnCFLZIl',
        'tbl32uaQ4hTLIkDK',
        'tblm1xLi2EB0uMXt',
        'tblp6rxi5KVMDkyZ',
        'tblbFNW479mNfQip',
        'tblCl51vxCzho9xD',
        'tblUSJQFsruuXKmJ',
    ]
    session = ''
    for tableToekn in tableTokens:
        cmd = ("./base perf run -n copy_paste_records --url "
               f"https://yalixw0asad.feishu.cn/base/E7rDbSPOoa4Zl3sVqWFcvRjJnfh\?table\={tableToekn} -s {session} -p "
               "is_debug=true -p record_num_all=1000000 -p record_num_batch=2000  -p is_stress=true -p is_random=true -p "
               "env_name=ppe_lark_base_dashboard_mpp -p is_pre_release=true -p header.x-use-ppe=1 -p sleep_time=10")
        print(cmd)
    session2 = 'XN0YXJ0-789h8f43-472c-48cc-811f-cd4785aaddks-WVuZA'
    tableToken = 'tblLJXR6CtE0KoCO'
    cmd2 = ("./base perf run -n copy_paste_records --url "
            f"https://bytedance.feishu-boe.net/base/NzuobLC5YajmTts6A7Ib6GWxcEJ\?table\={tableToken} -s {session2} -p "
            "is_debug=true -p record_num_all=50000 -p record_num_batch=2000  -p is_stress=true -p is_random=true -p "
            "env_name=boe_migrate_field_activities -p is_pre_release=false  -p sleep_time=10")
    print(cmd2)
