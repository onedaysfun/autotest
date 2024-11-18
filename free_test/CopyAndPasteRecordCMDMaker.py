def get_cmd(**kwargs):
    base_token = kwargs["base_token"]
    table_token = kwargs["table_token"]
    session = kwargs["session"]
    record_num_all = kwargs["record_num_all"]
    cmd = ("./base perf run -n copy_paste_records --url "
           f"https://bytedance.feishu-boe.net/base/{base_token}\?table\={table_token} -s {session} -p "
           f"is_debug=true -p record_num_all={record_num_all} -p record_num_batch=2000  -p is_stress=false"
           f" -p is_random=true "
           f"-p is_pre_release=false  -p sleep_time=3")
    return cmd


if __name__ == '__main__':
    base_token = 'O8oNbUYSNaBZG4sxJYAbZYD1cjf'
    table_token = 'tblnvMReHFrY1EA2'
    session = 'XN0YXJ0-442o1bf7-ab2f-4a3a-ac1e-51c42c1056og-WVuZA'
    record_num_all = 100000
    cmd = get_cmd(base_token=base_token, table_token=table_token, session=session, record_num_all=record_num_all)
    print(cmd)

