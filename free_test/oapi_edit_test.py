import random
import string
from threading import Lock, Thread
import common.common_openapi
from loguru import logger

list_info = []


def task():
    cli = random.choice([cli1, cli2, cli3, cli4])
    record = random.choice(record_list)
    context = {
        'base_token': 'IUfybqdF7aBnxgs5P9jc6E15n5d',
        'table_token': 'tblBOI99CQ85gBUL',
        'record': record,
        'data': {
            'fields': {
                'text': "测试:" + cli.session + str(random.randint(1, 1000))
            }
        }
    }
    message = record + ":" + cli.session
    list_info.append(message)
    cli.set_record(context)


if __name__ == '__main__':
    domain = 'https://open.feishu-pre.cn'
    app_id = 'cli_a3e4bf1ec4fb500c'
    app_secret = '7zIL6UhxJcmuWDSD6wkQegREvOzp0aSb'
    session_1 = 'XN0YXJ0-b57m4c7a-22db-4e4e-8e14-bf9691313c02-WVuZA'
    session_2 = 'XN0YXJ0-b57m4c7a-22db-4e4e-8e14-bf9691313c02-WVuZA'
    session_3 = 'XN0YXJ0-f06ube27-0793-4a01-ae3b-b53392391947-WVuZA'
    session_4 = 'XN0YXJ0-d46hf6ff-eed2-490b-a027-b2d8d74157d1-WVuZA'

    cli1 = common.common_openapi.Openapi(domain, app_id, app_secret)
    cli1.session = session_1
    cli1.open_id = ''
    cli1.set_access_token_user().set_access_token_default("u")

    cli2 = common.common_openapi.Openapi(domain, app_id, app_secret)
    cli2.session = session_2
    cli2.open_id = ''
    cli2.set_access_token_user().set_access_token_default("u")

    cli3 = common.common_openapi.Openapi(domain, app_id, app_secret)
    cli3.session = session_3
    cli3.open_id = ''
    cli3.set_access_token_user().set_access_token_default("u")

    cli4 = common.common_openapi.Openapi(domain, app_id, app_secret)
    cli4.session = session_4
    cli4.open_id = ''
    cli4.set_access_token_user().set_access_token_default("u")

    record_list = [
        'recd8QFe0f', 'recDWeo6zI', 'recJDbMFxo', 'recKj8gFeS', 'recpf2oyVF', 'recuX7TY63', 'recT3Y0ZJm',
        'recLpykg5U', 'rechW9xes7', 'rec22vWajD', 'recu8GyZrEIm8z', 'recu8GyZrEvuvR', 'recu8GyZrEqWWy',
        'recu8GyZrEQS6K', 'recu8GyZrEDYxk', 'recu8GyZrEsTqH', 'recu8GyZrEuxrE', 'recu8GyZrE1ysT',
        'recu8GyZrEF6ih', 'recu8GyZrEhT4G', 'recu8GyZrEWxFU', 'recu8GyZrEvhPn', 'recu8GyZrEy6es',
        'recu8GyZrEq7R6', 'recu8GyZrEzzeT', 'recu8GyZrEKJUp', 'recu8GyZrEKKT9', 'recu8GyZrEvaUa',
        'recu8GyZrEzpoS', 'recu8GyZrENukF', 'recu8GyZrElwlY', 'recu8GyZrELDvE', 'recu8GyZrElBwr',
        'recu8GyZrE7MBv', 'recu8GyZrEKQsg', 'recu8GyZrETRQh', 'recu8GyZrEDTPz', 'recu8GyZrEYBe7',
        'recu8GyZrE6jwz', 'recu8GyZrEPCNa', 'recu8GyZrEbfPS', 'recu8GyZrEUsp5', 'recu8GyZrE9uGi',
        'recu8GyZrE9cmq', 'recu8GyZrELcOh', 'recu8GyZrEWa8t', 'recu8GyZrEqlY2', 'recu8GyZrE1lDz',
        'recu8GyZrEbAYZ', 'recu8GyZrEc8QS', 'recu8GyZrEBkMI', 'recu8GyZrEO2SL', 'recu8GyZrEmrBE',
        'recu8GyZrElvUO', 'recu8GyZrENKyc', 'recu8GyZrE7hvv', 'recu8GyZrEkZe9', 'recu8GyZrENokM',
        'recu8GyZrEjkev', 'recu8GyZrEPfM1', 'recu8GyZrEMGGM', 'recu8GyZrEbTsK', 'recu8GyZrEcFmc',
        'recu8GyZrEqhqh', 'recu8GyZrE1Ged', 'recu8GyZrENQ4z', 'recu8GyZrEsVMF', 'recu8GyZrEeyd9',
        'recu8GyZrESfte', 'recu8GyZrE0Ln2', 'recu8GyZrEZCbA', 'recu8GyZrEipps', 'recu8GyZrEVGUE',
        'recu8GyZrEg2xF', 'recu8GyZrEyrZS', 'recu8GyZrEXyGJ', 'recu8GyZrEZI6q', 'recu8GyZrEzCZ0',
        'recu8GyZrE4Fpa', 'recu8GyZrECagm', 'recu8GyZrE7T15', 'recu8GyZrEsGaf', 'recu8GyZrEuVba',
        'recu8GyZrEUDVo', 'recu8GyZrE9cQ2', 'recu8GyZrEAg7v', 'recu8GyZrEvwc4', 'recu8GyZrEAZIb',
        'recu8GyZrEUMif', 'recu8GyZrEE1oM', 'recu8GyZrEBmaA', 'recu8GyZrEutit', 'recu8GyZrESdGY',
        'recu8GyZrEggJ6', 'recu8GyZrEH2Gr', 'recu8GyZrEN0xt', 'recu8GyZrEnhQx', 'recu8GyZrEAZBm',
        'recu8GyZrEQdeU', 'recu8GyRTGZfOW']

    lock = Lock()
    threads = []
    for i in range(10):
        t = Thread(target=task)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    logger.info(str(list_info))

# t = []
