import time

from common import send_message_cs

domain = "https://y5vna3awkt.larksuite-boe.com"
session = "XN0YXJ0-072l64e9-7b21-4068-9804-0764588f7i63-WVuZA"
token = "tblyAXv1zzAJSzVz"
parent_token = "SVVAbJqpPahLWosrprybLO56v7f"
table_rev = 0


def add_record(count=None, times=None):
    if count == None:
        count = 1
    if times == None:
        times = 1
    for i in range(count):
        cli.add_record(is_fxdb_base=True)
        time.sleep(times)


if __name__ == '__main__':
    cli = send_message_cs.EditTable(session, token, table_rev, parent_token, domain)
    add_record(100,1)