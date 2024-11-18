import csv
import random
import time

from common.send_message_cs import EditTable

# if __name__ == '__main__':
#     main_table = "tbl2ajk8p2i0gBCV"
#     tables = [
#         "tbleT4IfhoBCIRek",
#         "tblmu8x4uKEnlGxZ",
#         "tblrEAyPxoR0qu09",
#         "tblcuPr0Q2WgCdXE",
#         "tblk9H5YZN6NINBC",
#         "tbl5h7AFH0kLyWGD",
#         "tblfc9gSUmsPyFBF",
#         "tblYK105LpBdSggf",
#         "tbls91iCC9U19zLB",
#         "tbl6xUNBuR26HFWm",
#         "tbl7ngRjLzpzYNZC",
#         "tbl2FQtmb0qQ2auQ",
#         "tblWKo9bqQfK0Iwh",
#         "tbl4yGTFyroHcpq3",
#         "tbl8BEJuBP60Kay2",
#         "tblynYquLM1LIHs6",
#         "tbl0of3mcpLziu6e",
#         "tblXibCBlUJrpBIv",
#         "tblrzqBrSk1hQs5f",
#         "tbl65x4Nn0TXbq01",
#         "tblfCYKCBakmuzZU",
#         "tbleL1ay9IaR5j1c",
#         "tbl3PsDc5XGjIXIM",
#         "tbljjrB38zWNHUBD",
#         "tbl0nTBshmQIbAFb",
#         "tblJQhlCRnrzGdMx",
#         "tbl9BFH47nRWz3qp",
#         "tblkOZUh0sLah445",
#         "tblzm5KZtEBLEbe4",
#         "tblxje0vdwfGQEMx",
#         "tblXIKLBXUKgm1S0"
#     ]
#
#     # table config
#     session = 'XN0YXJ0-dd5ic30d-5c00-4ae6-a2d5-3ec04d9844pj-WVuZA'
#     token = main_table
#     rev = 86
#     parent_token = 'YvS7bUBM1abEMMsqXz8bs3hrcdH'
#     domain = 'https://bytedance.feishu-boe.net'
#     # todo：add table
#
#     # add link fields
#     cli = EditTable(session, token, rev, parent_token, domain)
#     # for link_table in tables:
#     #     field_name = 'multipleSelect-' + link_table
#     #     cli.add_field_multi_select(field_name, main_table, link_table)
#     #     time.sleep(1)
#     # set records with singleSelect
#     options = [
#         {
#             "id": "optpd8wNYP",
#             "name": "1",
#             "color": 0
#         },
#         {
#             "id": "optpfYE91S",
#             "name": "2",
#             "color": 1
#         },
#         {
#             "id": "optStE69Ed",
#             "name": "3",
#             "color": 2
#         },
#         {
#             "id": "optKdO71Wh",
#             "name": "4",
#             "color": 3
#         },
#         {
#             "id": "optm0HX3bf",
#             "name": "5",
#             "color": 4
#         },
#         {
#             "id": "opt9CfvFYJ",
#             "name": "6",
#             "color": 5
#         },
#         {
#             "id": "opt3fejCFb",
#             "name": "296",
#             "color": 6
#         },
#         {
#             "id": "optpJBAyTG",
#             "name": "298",
#             "color": 7
#         },
#         {
#             "id": "optFyOa16S",
#             "name": "299",
#             "color": 8
#         },
#         {
#             "id": "optsIxeQPn",
#             "name": "300",
#             "color": 9
#         },
#         {
#             "id": "opt9ygpZ8m",
#             "name": "297",
#             "color": 0
#         },
#         {
#             "id": "opt1lYM5pw",
#             "name": "7",
#             "color": 1
#         },
#         {
#             "id": "optNwqZGbh",
#             "name": "8",
#             "color": 2
#         },
#         {
#             "id": "optMolkeWr",
#             "name": "9",
#             "color": 3
#         },
#         {
#             "id": "opt9VjSSWR",
#             "name": "10",
#             "color": 4
#         },
#         {
#             "id": "opth4EaqAx",
#             "name": "11",
#             "color": 5
#         },
#         {
#             "id": "optYh9AY3n",
#             "name": "12",
#             "color": 6
#         },
#         {
#             "id": "optBWrO4Hc",
#             "name": "13",
#             "color": 7
#         },
#         {
#             "id": "optRLrqJgx",
#             "name": "14",
#             "color": 8
#         },
#         {
#             "id": "optdoExO2E",
#             "name": "15",
#             "color": 9
#         },
#         {
#             "id": "opt2hEUUtH",
#             "name": "16",
#             "color": 0
#         },
#         {
#             "id": "optQCfDzfi",
#             "name": "17",
#             "color": 1
#         },
#         {
#             "id": "optgFiAh1e",
#             "name": "18",
#             "color": 2
#         },
#         {
#             "id": "optDft3fEz",
#             "name": "19",
#             "color": 3
#         },
#         {
#             "id": "optQuwH97s",
#             "name": "20",
#             "color": 4
#         },
#         {
#             "id": "opttzMVNhe",
#             "name": "21",
#             "color": 5
#         },
#         {
#             "id": "opteUeHIKz",
#             "name": "22",
#             "color": 6
#         },
#         {
#             "id": "optNityaWR",
#             "name": "23",
#             "color": 7
#         },
#         {
#             "id": "optuZ7F5a1",
#             "name": "24",
#             "color": 8
#         },
#         {
#             "id": "opt1vBcVe8",
#             "name": "25",
#             "color": 9
#         },
#         {
#             "id": "optOHHtBCL",
#             "name": "26",
#             "color": 0
#         },
#         {
#             "id": "optd2NhLTW",
#             "name": "27",
#             "color": 1
#         },
#         {
#             "id": "optR1yPBV7",
#             "name": "28",
#             "color": 2
#         },
#         {
#             "id": "optZoQPsDD",
#             "name": "29",
#             "color": 3
#         },
#         {
#             "id": "optf7X8aRX",
#             "name": "30",
#             "color": 4
#         },
#         {
#             "id": "optC7zgpks",
#             "name": "31",
#             "color": 5
#         },
#         {
#             "id": "optHHa0tC5",
#             "name": "32",
#             "color": 6
#         },
#         {
#             "id": "optyp6RlaC",
#             "name": "33",
#             "color": 7
#         },
#         {
#             "id": "optZEqBRjH",
#             "name": "34",
#             "color": 8
#         },
#         {
#             "id": "optrRDPOji",
#             "name": "35",
#             "color": 9
#         },
#         {
#             "id": "opt2HPPOeo",
#             "name": "36",
#             "color": 0
#         },
#         {
#             "id": "optttCQlPE",
#             "name": "37",
#             "color": 1
#         },
#         {
#             "id": "optLUgea0X",
#             "name": "38",
#             "color": 2
#         },
#         {
#             "id": "optt5JMeqM",
#             "name": "39",
#             "color": 3
#         },
#         {
#             "id": "optlTb9ksj",
#             "name": "40",
#             "color": 4
#         },
#         {
#             "id": "optPggJrqk",
#             "name": "41",
#             "color": 5
#         },
#         {
#             "id": "optk0YYvtQ",
#             "name": "42",
#             "color": 6
#         },
#         {
#             "id": "optiGOsZ6e",
#             "name": "43",
#             "color": 7
#         },
#         {
#             "id": "opt1f49zaH",
#             "name": "44",
#             "color": 8
#         },
#         {
#             "id": "optfLNsEoo",
#             "name": "45",
#             "color": 9
#         },
#         {
#             "id": "optRp52xcu",
#             "name": "46",
#             "color": 0
#         },
#         {
#             "id": "optVbThO81",
#             "name": "47",
#             "color": 1
#         },
#         {
#             "id": "opt1Idp5VJ",
#             "name": "48",
#             "color": 2
#         },
#         {
#             "id": "optRbMqJza",
#             "name": "49",
#             "color": 3
#         },
#         {
#             "id": "optnPj5yuW",
#             "name": "50",
#             "color": 4
#         },
#         {
#             "id": "optXnwioV2",
#             "name": "51",
#             "color": 5
#         },
#         {
#             "id": "optWaD4xj6",
#             "name": "52",
#             "color": 6
#         },
#         {
#             "id": "optNRCMtcT",
#             "name": "53",
#             "color": 7
#         },
#         {
#             "id": "opt43i5tRA",
#             "name": "54",
#             "color": 8
#         },
#         {
#             "id": "optI3U9zwJ",
#             "name": "55",
#             "color": 9
#         },
#         {
#             "id": "opt971DyJ2",
#             "name": "56",
#             "color": 0
#         },
#         {
#             "id": "opt5B8ewZw",
#             "name": "57",
#             "color": 1
#         },
#         {
#             "id": "opt285ii7E",
#             "name": "58",
#             "color": 2
#         },
#         {
#             "id": "optM1BiN4u",
#             "name": "59",
#             "color": 3
#         },
#         {
#             "id": "optDJLzBsA",
#             "name": "60",
#             "color": 4
#         },
#         {
#             "id": "optZO8Ou5n",
#             "name": "61",
#             "color": 5
#         },
#         {
#             "id": "optkGq7sgW",
#             "name": "62",
#             "color": 6
#         },
#         {
#             "id": "optA0eoQpb",
#             "name": "63",
#             "color": 7
#         },
#         {
#             "id": "optYBrUOC4",
#             "name": "64",
#             "color": 8
#         },
#         {
#             "id": "opthxS2uT8",
#             "name": "65",
#             "color": 9
#         },
#         {
#             "id": "optOmbvta7",
#             "name": "66",
#             "color": 0
#         },
#         {
#             "id": "opthWx0aMv",
#             "name": "67",
#             "color": 1
#         },
#         {
#             "id": "optxkyosjF",
#             "name": "68",
#             "color": 2
#         },
#         {
#             "id": "optQc7vpuS",
#             "name": "69",
#             "color": 3
#         },
#         {
#             "id": "opta1k40dF",
#             "name": "70",
#             "color": 4
#         },
#         {
#             "id": "optxKDzeHd",
#             "name": "71",
#             "color": 5
#         },
#         {
#             "id": "opt1xwWHYy",
#             "name": "72",
#             "color": 6
#         },
#         {
#             "id": "optGxrl3S3",
#             "name": "73",
#             "color": 7
#         },
#         {
#             "id": "optlzp3sCU",
#             "name": "74",
#             "color": 8
#         },
#         {
#             "id": "optrpLKdcM",
#             "name": "75",
#             "color": 9
#         },
#         {
#             "id": "optgqxVVIG",
#             "name": "76",
#             "color": 0
#         },
#         {
#             "id": "optmfoaRJ7",
#             "name": "77",
#             "color": 1
#         },
#         {
#             "id": "opthsUcajA",
#             "name": "78",
#             "color": 2
#         },
#         {
#             "id": "optYRqBFuT",
#             "name": "79",
#             "color": 3
#         },
#         {
#             "id": "optcGuTeoZ",
#             "name": "80",
#             "color": 4
#         },
#         {
#             "id": "opt56aZZan",
#             "name": "81",
#             "color": 5
#         },
#         {
#             "id": "optH0C18N6",
#             "name": "82",
#             "color": 6
#         },
#         {
#             "id": "optUw7HyOp",
#             "name": "83",
#             "color": 7
#         },
#         {
#             "id": "optFma2T8Q",
#             "name": "84",
#             "color": 8
#         },
#         {
#             "id": "optKJyDTkd",
#             "name": "85",
#             "color": 9
#         },
#         {
#             "id": "opt3VVfwng",
#             "name": "86",
#             "color": 0
#         },
#         {
#             "id": "optOh3a9Ny",
#             "name": "87",
#             "color": 1
#         },
#         {
#             "id": "optKR6HuuQ",
#             "name": "88",
#             "color": 2
#         },
#         {
#             "id": "optahsQweW",
#             "name": "89",
#             "color": 3
#         },
#         {
#             "id": "optuX8nR17",
#             "name": "90",
#             "color": 4
#         },
#         {
#             "id": "optNLcVEPf",
#             "name": "91",
#             "color": 5
#         },
#         {
#             "id": "optABIsQBq",
#             "name": "92",
#             "color": 6
#         },
#         {
#             "id": "opt8fPj0Zs",
#             "name": "93",
#             "color": 7
#         },
#         {
#             "id": "opt7ZcekiR",
#             "name": "283",
#             "color": 8
#         },
#         {
#             "id": "optIEkdcZG",
#             "name": "284",
#             "color": 9
#         },
#         {
#             "id": "optghPJk51",
#             "name": "285",
#             "color": 0
#         },
#         {
#             "id": "optUsITHQE",
#             "name": "286",
#             "color": 1
#         },
#         {
#             "id": "optRPrerBe",
#             "name": "287",
#             "color": 2
#         },
#         {
#             "id": "optlasFty7",
#             "name": "288",
#             "color": 3
#         },
#         {
#             "id": "optE4wPOwc",
#             "name": "289",
#             "color": 4
#         },
#         {
#             "id": "optpLH8iXj",
#             "name": "290",
#             "color": 5
#         },
#         {
#             "id": "opt8Ln5JpP",
#             "name": "291",
#             "color": 6
#         },
#         {
#             "id": "optaD8nw3n",
#             "name": "292",
#             "color": 7
#         },
#         {
#             "id": "opt9aVxdOl",
#             "name": "293",
#             "color": 8
#         },
#         {
#             "id": "optiVzN7H5",
#             "name": "294",
#             "color": 9
#         },
#         {
#             "id": "optXlDVkX3",
#             "name": "295",
#             "color": 0
#         },
#         {
#             "id": "optF7Q2PaP",
#             "name": "94",
#             "color": 1
#         },
#         {
#             "id": "optTZXpW0e",
#             "name": "95",
#             "color": 2
#         },
#         {
#             "id": "optNXmjj1t",
#             "name": "96",
#             "color": 3
#         },
#         {
#             "id": "optZ01HQE4",
#             "name": "97",
#             "color": 4
#         },
#         {
#             "id": "opt5p1TlqG",
#             "name": "98",
#             "color": 5
#         },
#         {
#             "id": "opte7ostxn",
#             "name": "99",
#             "color": 6
#         },
#         {
#             "id": "opt4tVn5Qe",
#             "name": "100",
#             "color": 7
#         },
#         {
#             "id": "optWEQdTIP",
#             "name": "101",
#             "color": 8
#         },
#         {
#             "id": "optNXgbXTj",
#             "name": "102",
#             "color": 9
#         },
#         {
#             "id": "optXcO9czn",
#             "name": "103",
#             "color": 0
#         },
#         {
#             "id": "optTnsvGMQ",
#             "name": "104",
#             "color": 1
#         },
#         {
#             "id": "optMne9ruy",
#             "name": "105",
#             "color": 2
#         },
#         {
#             "id": "optgTvfKD3",
#             "name": "106",
#             "color": 3
#         },
#         {
#             "id": "optGMc4w3H",
#             "name": "107",
#             "color": 4
#         },
#         {
#             "id": "optTItwy71",
#             "name": "108",
#             "color": 5
#         },
#         {
#             "id": "optKkbHpQI",
#             "name": "109",
#             "color": 6
#         },
#         {
#             "id": "optmKYwBx8",
#             "name": "110",
#             "color": 7
#         },
#         {
#             "id": "optrtnzZb2",
#             "name": "111",
#             "color": 8
#         },
#         {
#             "id": "opt9W8Vx5E",
#             "name": "112",
#             "color": 9
#         },
#         {
#             "id": "opt887bey2",
#             "name": "113",
#             "color": 0
#         },
#         {
#             "id": "optF2EzWNb",
#             "name": "114",
#             "color": 1
#         },
#         {
#             "id": "opt1I68uI4",
#             "name": "115",
#             "color": 2
#         },
#         {
#             "id": "optTmiI7xP",
#             "name": "116",
#             "color": 3
#         },
#         {
#             "id": "optsWS0PzV",
#             "name": "117",
#             "color": 4
#         },
#         {
#             "id": "optQVUxrOh",
#             "name": "118",
#             "color": 5
#         },
#         {
#             "id": "optMGO1v0b",
#             "name": "119",
#             "color": 6
#         },
#         {
#             "id": "optlxmAMpl",
#             "name": "120",
#             "color": 7
#         },
#         {
#             "id": "optupgT6nD",
#             "name": "121",
#             "color": 8
#         },
#         {
#             "id": "optrLHxG0m",
#             "name": "122",
#             "color": 9
#         },
#         {
#             "id": "optBBFhUJg",
#             "name": "123",
#             "color": 0
#         },
#         {
#             "id": "optqx7B05a",
#             "name": "124",
#             "color": 1
#         },
#         {
#             "id": "optQD4r86I",
#             "name": "125",
#             "color": 2
#         },
#         {
#             "id": "optZ2OOY0Y",
#             "name": "126",
#             "color": 3
#         },
#         {
#             "id": "optFdqxW59",
#             "name": "127",
#             "color": 4
#         },
#         {
#             "id": "optlnGJrKm",
#             "name": "128",
#             "color": 5
#         },
#         {
#             "id": "optQBbHVOX",
#             "name": "129",
#             "color": 6
#         },
#         {
#             "id": "opt0XEo07p",
#             "name": "130",
#             "color": 7
#         },
#         {
#             "id": "optcJpQiBp",
#             "name": "131",
#             "color": 8
#         },
#         {
#             "id": "optrb1x5ne",
#             "name": "132",
#             "color": 9
#         },
#         {
#             "id": "optqa7ZYfv",
#             "name": "133",
#             "color": 0
#         },
#         {
#             "id": "opt5q5SlMo",
#             "name": "134",
#             "color": 1
#         },
#         {
#             "id": "optu7LzUaL",
#             "name": "135",
#             "color": 2
#         },
#         {
#             "id": "optrt1J3RT",
#             "name": "136",
#             "color": 3
#         },
#         {
#             "id": "opt1cJOmh9",
#             "name": "137",
#             "color": 4
#         },
#         {
#             "id": "optPtpXo3v",
#             "name": "138",
#             "color": 5
#         },
#         {
#             "id": "optE0Ab0VE",
#             "name": "139",
#             "color": 6
#         },
#         {
#             "id": "optCHyRDMT",
#             "name": "140",
#             "color": 7
#         },
#         {
#             "id": "optX08Vds7",
#             "name": "141",
#             "color": 8
#         },
#         {
#             "id": "optzhgg6xJ",
#             "name": "142",
#             "color": 9
#         },
#         {
#             "id": "optCyeyV8H",
#             "name": "143",
#             "color": 0
#         },
#         {
#             "id": "opt0Z8jJz2",
#             "name": "144",
#             "color": 1
#         },
#         {
#             "id": "opto3dYPAm",
#             "name": "145",
#             "color": 2
#         },
#         {
#             "id": "optQB3FtUk",
#             "name": "146",
#             "color": 3
#         },
#         {
#             "id": "optIXnYksy",
#             "name": "147",
#             "color": 4
#         },
#         {
#             "id": "optJRfi5uM",
#             "name": "148",
#             "color": 5
#         },
#         {
#             "id": "optgBhYJdK",
#             "name": "149",
#             "color": 6
#         },
#         {
#             "id": "optKkew81w",
#             "name": "150",
#             "color": 7
#         },
#         {
#             "id": "optMTe8yyX",
#             "name": "151",
#             "color": 8
#         },
#         {
#             "id": "optu5rsB57",
#             "name": "152",
#             "color": 9
#         },
#         {
#             "id": "optefWrxOk",
#             "name": "153",
#             "color": 0
#         },
#         {
#             "id": "opt3mwqDHd",
#             "name": "154",
#             "color": 1
#         },
#         {
#             "id": "optPBCwLh6",
#             "name": "155",
#             "color": 2
#         },
#         {
#             "id": "optHLBGX8Q",
#             "name": "156",
#             "color": 3
#         },
#         {
#             "id": "optNsxftZP",
#             "name": "157",
#             "color": 4
#         },
#         {
#             "id": "optIuFagjN",
#             "name": "158",
#             "color": 5
#         },
#         {
#             "id": "optikjAVXu",
#             "name": "159",
#             "color": 6
#         },
#         {
#             "id": "optpm06mIj",
#             "name": "160",
#             "color": 7
#         },
#         {
#             "id": "optLlK1UfA",
#             "name": "161",
#             "color": 8
#         },
#         {
#             "id": "optPdgV71g",
#             "name": "162",
#             "color": 9
#         },
#         {
#             "id": "optU9ZpwH2",
#             "name": "163",
#             "color": 0
#         },
#         {
#             "id": "optHA8rTRT",
#             "name": "164",
#             "color": 1
#         },
#         {
#             "id": "optC01UbK3",
#             "name": "165",
#             "color": 2
#         },
#         {
#             "id": "optYKzWBa3",
#             "name": "166",
#             "color": 3
#         },
#         {
#             "id": "optb0Ql9NB",
#             "name": "167",
#             "color": 4
#         },
#         {
#             "id": "optJirYXux",
#             "name": "168",
#             "color": 5
#         },
#         {
#             "id": "optICX8noN",
#             "name": "169",
#             "color": 6
#         },
#         {
#             "id": "optnBQEGre",
#             "name": "170",
#             "color": 7
#         },
#         {
#             "id": "optpzuxKwN",
#             "name": "171",
#             "color": 8
#         },
#         {
#             "id": "optI0tyhKL",
#             "name": "172",
#             "color": 9
#         },
#         {
#             "id": "optdEsYLf9",
#             "name": "173",
#             "color": 0
#         },
#         {
#             "id": "optRlzMePK",
#             "name": "174",
#             "color": 1
#         },
#         {
#             "id": "optk1eQMgG",
#             "name": "175",
#             "color": 2
#         },
#         {
#             "id": "optyDAsY5e",
#             "name": "176",
#             "color": 3
#         },
#         {
#             "id": "opt0E3idII",
#             "name": "177",
#             "color": 4
#         },
#         {
#             "id": "optfQ61qof",
#             "name": "178",
#             "color": 5
#         },
#         {
#             "id": "optf9lwQoW",
#             "name": "179",
#             "color": 6
#         },
#         {
#             "id": "optWUYTeny",
#             "name": "180",
#             "color": 7
#         },
#         {
#             "id": "optFeF00Ct",
#             "name": "181",
#             "color": 8
#         },
#         {
#             "id": "optdfSOX6j",
#             "name": "182",
#             "color": 9
#         },
#         {
#             "id": "optfzsi70e",
#             "name": "272",
#             "color": 0
#         },
#         {
#             "id": "optoT3b6YW",
#             "name": "273",
#             "color": 1
#         },
#         {
#             "id": "optpZ4OrfE",
#             "name": "274",
#             "color": 2
#         },
#         {
#             "id": "optn9HFb1y",
#             "name": "275",
#             "color": 3
#         },
#         {
#             "id": "optETsi7qm",
#             "name": "276",
#             "color": 4
#         },
#         {
#             "id": "optnhBZOnm",
#             "name": "277",
#             "color": 5
#         },
#         {
#             "id": "optZ3PyApJ",
#             "name": "278",
#             "color": 6
#         },
#         {
#             "id": "optK833fwh",
#             "name": "279",
#             "color": 7
#         },
#         {
#             "id": "opthEVyPbL",
#             "name": "280",
#             "color": 8
#         },
#         {
#             "id": "opt8qPiUxj",
#             "name": "281",
#             "color": 9
#         },
#         {
#             "id": "optgfeWSas",
#             "name": "282",
#             "color": 0
#         },
#         {
#             "id": "opt8SNpYiJ",
#             "name": "183",
#             "color": 1
#         },
#         {
#             "id": "optWArGij1",
#             "name": "184",
#             "color": 2
#         },
#         {
#             "id": "opt9WWChZE",
#             "name": "185",
#             "color": 3
#         },
#         {
#             "id": "optpElj47O",
#             "name": "186",
#             "color": 4
#         },
#         {
#             "id": "optjt578mE",
#             "name": "187",
#             "color": 5
#         },
#         {
#             "id": "opt4NR57sm",
#             "name": "188",
#             "color": 6
#         },
#         {
#             "id": "optDuoburY",
#             "name": "189",
#             "color": 7
#         },
#         {
#             "id": "optPRztzrC",
#             "name": "190",
#             "color": 8
#         },
#         {
#             "id": "optFCTpDK2",
#             "name": "191",
#             "color": 9
#         },
#         {
#             "id": "optKSc7QZE",
#             "name": "192",
#             "color": 0
#         },
#         {
#             "id": "opt24Wgp9E",
#             "name": "193",
#             "color": 1
#         },
#         {
#             "id": "optrJKZcIg",
#             "name": "194",
#             "color": 2
#         },
#         {
#             "id": "optzsfteLS",
#             "name": "195",
#             "color": 3
#         },
#         {
#             "id": "opt8GizMzY",
#             "name": "196",
#             "color": 4
#         },
#         {
#             "id": "opt91XSiob",
#             "name": "197",
#             "color": 5
#         },
#         {
#             "id": "optl3xh2Cy",
#             "name": "198",
#             "color": 6
#         },
#         {
#             "id": "optND8zFcv",
#             "name": "199",
#             "color": 7
#         },
#         {
#             "id": "optqhtRyVH",
#             "name": "200",
#             "color": 8
#         },
#         {
#             "id": "optt4DX1tx",
#             "name": "201",
#             "color": 9
#         },
#         {
#             "id": "optBrecDXo",
#             "name": "202",
#             "color": 0
#         },
#         {
#             "id": "optlNyIxV5",
#             "name": "203",
#             "color": 1
#         },
#         {
#             "id": "opt5UkD1BF",
#             "name": "204",
#             "color": 2
#         },
#         {
#             "id": "opt9nlxWzT",
#             "name": "205",
#             "color": 3
#         },
#         {
#             "id": "optcJXhm8p",
#             "name": "206",
#             "color": 4
#         },
#         {
#             "id": "optSgPD8Mn",
#             "name": "207",
#             "color": 5
#         },
#         {
#             "id": "opt7jhqlWs",
#             "name": "208",
#             "color": 6
#         },
#         {
#             "id": "optvhXSgzE",
#             "name": "209",
#             "color": 7
#         },
#         {
#             "id": "opt7X1GvGc",
#             "name": "210",
#             "color": 8
#         },
#         {
#             "id": "opt6ajGEb7",
#             "name": "211",
#             "color": 9
#         },
#         {
#             "id": "opt0fzjL7j",
#             "name": "212",
#             "color": 0
#         },
#         {
#             "id": "opthT0EeCM",
#             "name": "213",
#             "color": 1
#         },
#         {
#             "id": "optoLFVpiB",
#             "name": "214",
#             "color": 2
#         },
#         {
#             "id": "opt1RElRRp",
#             "name": "215",
#             "color": 3
#         },
#         {
#             "id": "opt4auk2Ye",
#             "name": "216",
#             "color": 4
#         },
#         {
#             "id": "optI4tJUNH",
#             "name": "217",
#             "color": 5
#         },
#         {
#             "id": "optomGU6Ss",
#             "name": "218",
#             "color": 6
#         },
#         {
#             "id": "optKrbFPr4",
#             "name": "219",
#             "color": 7
#         },
#         {
#             "id": "optRUL21WQ",
#             "name": "220",
#             "color": 8
#         },
#         {
#             "id": "optkgJZDPl",
#             "name": "221",
#             "color": 9
#         },
#         {
#             "id": "optUbP9f3U",
#             "name": "222",
#             "color": 0
#         },
#         {
#             "id": "optzMzaZvG",
#             "name": "223",
#             "color": 1
#         },
#         {
#             "id": "optUXVJAGc",
#             "name": "224",
#             "color": 2
#         },
#         {
#             "id": "optqL3Ru6Z",
#             "name": "225",
#             "color": 3
#         },
#         {
#             "id": "optdme6obh",
#             "name": "226",
#             "color": 4
#         },
#         {
#             "id": "optl5pZKF8",
#             "name": "227",
#             "color": 5
#         },
#         {
#             "id": "optXyIpZAZ",
#             "name": "228",
#             "color": 6
#         },
#         {
#             "id": "optBW0QZ0v",
#             "name": "229",
#             "color": 7
#         },
#         {
#             "id": "optXGafqtu",
#             "name": "230",
#             "color": 8
#         },
#         {
#             "id": "optkDc0eYD",
#             "name": "231",
#             "color": 9
#         },
#         {
#             "id": "optgZJcjgO",
#             "name": "232",
#             "color": 0
#         },
#         {
#             "id": "optjtFhPsU",
#             "name": "233",
#             "color": 1
#         },
#         {
#             "id": "optrMl78ZP",
#             "name": "234",
#             "color": 2
#         },
#         {
#             "id": "optEGB3OPB",
#             "name": "235",
#             "color": 3
#         },
#         {
#             "id": "optGInZ2dj",
#             "name": "236",
#             "color": 4
#         },
#         {
#             "id": "optjzpAQFl",
#             "name": "237",
#             "color": 5
#         },
#         {
#             "id": "optqFJm0lz",
#             "name": "238",
#             "color": 6
#         },
#         {
#             "id": "optDBOiObt",
#             "name": "239",
#             "color": 7
#         },
#         {
#             "id": "optTfNJbG6",
#             "name": "240",
#             "color": 8
#         },
#         {
#             "id": "optbPNoDa2",
#             "name": "241",
#             "color": 9
#         },
#         {
#             "id": "optTWwjudf",
#             "name": "242",
#             "color": 0
#         },
#         {
#             "id": "opt72u70uj",
#             "name": "243",
#             "color": 1
#         },
#         {
#             "id": "optd8lTQdP",
#             "name": "244",
#             "color": 2
#         },
#         {
#             "id": "optL54xusP",
#             "name": "245",
#             "color": 3
#         },
#         {
#             "id": "optN84AuHx",
#             "name": "246",
#             "color": 4
#         },
#         {
#             "id": "opt9FUKTy3",
#             "name": "247",
#             "color": 5
#         },
#         {
#             "id": "optIrlfwL2",
#             "name": "248",
#             "color": 6
#         },
#         {
#             "id": "opt6mZFv7x",
#             "name": "249",
#             "color": 7
#         },
#         {
#             "id": "opt6IivApU",
#             "name": "250",
#             "color": 8
#         },
#         {
#             "id": "optZOHsjiv",
#             "name": "251",
#             "color": 9
#         },
#         {
#             "id": "opttNHeoPC",
#             "name": "252",
#             "color": 0
#         },
#         {
#             "id": "optFgqfNhH",
#             "name": "253",
#             "color": 1
#         },
#         {
#             "id": "optWCEFlUa",
#             "name": "254",
#             "color": 2
#         },
#         {
#             "id": "opt6kTt791",
#             "name": "255",
#             "color": 3
#         },
#         {
#             "id": "opt9Tv9cXs",
#             "name": "256",
#             "color": 4
#         },
#         {
#             "id": "optprP9DuJ",
#             "name": "257",
#             "color": 5
#         },
#         {
#             "id": "opto9Mcgv8",
#             "name": "258",
#             "color": 6
#         },
#         {
#             "id": "optpGBuXHj",
#             "name": "259",
#             "color": 7
#         },
#         {
#             "id": "optkyPNVJY",
#             "name": "260",
#             "color": 8
#         },
#         {
#             "id": "optH6EqYGK",
#             "name": "261",
#             "color": 9
#         },
#         {
#             "id": "opt3HYefdH",
#             "name": "262",
#             "color": 0
#         },
#         {
#             "id": "optur1W9oB",
#             "name": "263",
#             "color": 1
#         },
#         {
#             "id": "optZeYS9Gb",
#             "name": "264",
#             "color": 2
#         },
#         {
#             "id": "optOmyYEVm",
#             "name": "265",
#             "color": 3
#         },
#         {
#             "id": "opttBXA3L1",
#             "name": "266",
#             "color": 4
#         },
#         {
#             "id": "opt76TFp36",
#             "name": "267",
#             "color": 5
#         },
#         {
#             "id": "opt9QY5oZB",
#             "name": "268",
#             "color": 6
#         },
#         {
#             "id": "optGnOYZSZ",
#             "name": "269",
#             "color": 7
#         },
#         {
#             "id": "optQVzgsKQ",
#             "name": "270",
#             "color": 8
#         },
#         {
#             "id": "optfhyt7co",
#             "name": "271",
#             "color": 9
#         }
#     ]
#     fields = [
#         "fldpej7U4c",
#         "fldLpG7dJv",
#         "fld1Z2yHFC",
#         "fld6CLcx7D",
#         "fldu7Rao9v",
#         "flditNoRQ4",
#         "fldUvDmxCd",
#         "fldsDM2UTB",
#         "fldKI7SOg9",
#         "fldea7HZEB",
#         "fldzDTEPCJ",
#         "fld3XyW0zC",
#         "fldy2JpPu8",
#         "fldYjb8FSx",
#         "flds0A2yde",
#         "fldtOZEyXF",
#         "fldb5DRU3n",
#         "fld38AXTbB",
#         "fldCKweuRa",
#         "fldhmr7dWJ",
#         "flddZuHSzo",
#         "fldpsGT9yd",
#         "fld7yodp3K",
#         "fldzDru42f",
#         "fldAF4kKhB",
#         "fldDgPRQXk",
#         "fld6Mq8BZ2",
#         "fldwAiVyKG",
#         "fldx0AvVc9",
#         "fldGbhSeyE",
#         "fldougHKxU"
#     ]
#     records2_json = {
#         "recCOpuJ9v": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recjC4wzYp": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recrkjFVWr": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recNlChw6i": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recOlJa4kp": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recTzwiZVo": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "rec3Yr8LMU": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recsYuzqP6": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recRXQ7NuA": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recwfvMW4L": {
#             "recMeta": {
#                 "rev": 5,
#                 "createdTime": 1711616912,
#                 "createdUser": "7091186056053129235",
#                 "historyLevel": 0,
#                 "modifiedTime": 1711618444,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DICfF": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DrigW": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DIZsK": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DIEZZ": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DLm7b": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dnxrs": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DkWkR": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DlV4x": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DA8bg": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DhZYb": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DEnyA": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DaKI4": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DCp9b": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2De2Wb": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DmNRJ": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DeiPG": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DhMxO": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DbdBA": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DkrDE": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D6VVm": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dtzh9": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DWlDk": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DbkAC": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DWCcF": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DAMDu": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DgEOd": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DrmaW": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DYo1a": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DKwrd": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DUwT1": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DkRnc": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DGfNN": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DpjsK": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dh5G4": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DJOL1": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DPMle": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DmCjA": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Ddhcl": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DAizc": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dn6U4": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D00xv": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DLKr2": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DZtMd": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D8Xhq": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DX5me": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DmcZl": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DcUIi": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DkvST": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DKVFZ": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DSRmc": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dws7u": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DWze3": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DKhPy": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DEtXN": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DE4vc": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D3LVi": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D970g": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DyNDR": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DspDS": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DmDH3": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DAmoK": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D2qgb": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DaNza": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dq6ss": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DyjMs": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D8NpN": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DjyvM": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DScSt": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D3Jt8": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DefhA": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DzGtY": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DsZ2Y": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D5uVQ": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DqYPc": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Do6gt": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Du3u5": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DvAyF": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DZeFg": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DeVfg": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DKUiJ": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DyE2L": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DYAZp": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DaNvF": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D1R8B": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2D8XpM": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DzbNg": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2Dwn0U": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DVquS": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DavS0": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         },
#         "recu8jcU2DpytL": {
#             "recMeta": {
#                 "rev": 0,
#                 "historyLevel": 0,
#                 "createdTime": 1711619957,
#                 "createdUser": "7091186056053129235",
#                 "modifiedTime": 1711619957,
#                 "modifiedUser": "7091186056053129235"
#             }
#         }
#     }
#     records2 = list(records2_json.keys())
#     for record in records2:
#         cli.set_record(main_table, record, fields, options)
#         time.sleep(2)

# group by order by
if __name__ == '__main__':
    table = 'tblZAbvdPRHUtPBJ'
    parent_token = 'K3JlbLqBTacYCssUptDbzfl1cMb'
    table_rev = 2444
    base_rev = 0
    domain = 'https://bytedance.feishu-boe.net'
    session = 'XN0YXJ0-dd5ic30d-5c00-4ae6-a2d5-3ec04d9844pj-WVuZA'

    # init table edit class
    cli = EditTable(session, table, table_rev, parent_token, domain)
    # for i in range(0, 100):
    #     cli.add_field_number_order_by(table, "OrderByNum-" + str(i))
    #     time.sleep(1)

    singleSelectList = ['fldB2dBalV', 'fldYA8AZRm', 'fldxiYAPDt']
    optionList = [
        {
            "id": "optpNgohQ7",
            "name": "1",
            "color": 0
        },
        {
            "id": "optsobIQMm",
            "name": "3",
            "color": 1
        },
        {
            "id": "optFBLUkEr",
            "name": "5",
            "color": 2
        },
        {
            "id": "optURYULRp",
            "name": "10",
            "color": 3
        },
        {
            "id": "optAYzFJVi",
            "name": "2",
            "color": 4
        },
        {
            "id": "optOVwO020",
            "name": "4",
            "color": 5
        },
        {
            "id": "optPiKNJ6z",
            "name": "6",
            "color": 6
        },
        {
            "id": "optR3g928F",
            "name": "7",
            "color": 7
        },
        {
            "id": "opthxJEjr1",
            "name": "8",
            "color": 8
        },
        {
            "id": "optupVngtI",
            "name": "9",
            "color": 9
        }
    ]
    numberFieldMap = {
        "fldDB50nOf": {
            "id": "fldDB50nOf",
            "name": "OrderByNum-0",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldITqorAg": {
            "id": "fldITqorAg",
            "name": "OrderByNum-1",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldqA9WZOl": {
            "id": "fldqA9WZOl",
            "name": "OrderByNum-2",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldLuKBxHw": {
            "id": "fldLuKBxHw",
            "name": "OrderByNum-3",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldnzOLx8v": {
            "id": "fldnzOLx8v",
            "name": "OrderByNum-4",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldcyFPE5h": {
            "id": "fldcyFPE5h",
            "name": "OrderByNum-5",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldEw3VuPl": {
            "id": "fldEw3VuPl",
            "name": "OrderByNum-6",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldxMalKY9": {
            "id": "fldxMalKY9",
            "name": "OrderByNum-7",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldJ8mh5a6": {
            "id": "fldJ8mh5a6",
            "name": "OrderByNum-8",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld02dC6Xz": {
            "id": "fld02dC6Xz",
            "name": "OrderByNum-9",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld4dQfYak": {
            "id": "fld4dQfYak",
            "name": "OrderByNum-10",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldoD3zAGU": {
            "id": "fldoD3zAGU",
            "name": "OrderByNum-11",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld9sAve8t": {
            "id": "fld9sAve8t",
            "name": "OrderByNum-12",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld28upPqf": {
            "id": "fld28upPqf",
            "name": "OrderByNum-13",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldgeMO5Ro": {
            "id": "fldgeMO5Ro",
            "name": "OrderByNum-14",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldMfF94GH": {
            "id": "fldMfF94GH",
            "name": "OrderByNum-15",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldbAhgo3e": {
            "id": "fldbAhgo3e",
            "name": "OrderByNum-16",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldb12rH4U": {
            "id": "fldb12rH4U",
            "name": "OrderByNum-17",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldIfM0nW6": {
            "id": "fldIfM0nW6",
            "name": "OrderByNum-18",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldZn6vBR3": {
            "id": "fldZn6vBR3",
            "name": "OrderByNum-19",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldtVwbcZK": {
            "id": "fldtVwbcZK",
            "name": "OrderByNum-20",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldxcuzvwD": {
            "id": "fldxcuzvwD",
            "name": "OrderByNum-21",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld1sCd3z7": {
            "id": "fld1sCd3z7",
            "name": "OrderByNum-22",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flduzPe1ZB": {
            "id": "flduzPe1ZB",
            "name": "OrderByNum-23",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldor05a1w": {
            "id": "fldor05a1w",
            "name": "OrderByNum-24",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldH3IKk4r": {
            "id": "fldH3IKk4r",
            "name": "OrderByNum-25",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldNBxwYEl": {
            "id": "fldNBxwYEl",
            "name": "OrderByNum-26",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldvj5Bha9": {
            "id": "fldvj5Bha9",
            "name": "OrderByNum-27",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldyLmMRhi": {
            "id": "fldyLmMRhi",
            "name": "OrderByNum-28",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldHVRa16h": {
            "id": "fldHVRa16h",
            "name": "OrderByNum-29",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldqHGawSU": {
            "id": "fldqHGawSU",
            "name": "OrderByNum-30",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldniAe870": {
            "id": "fldniAe870",
            "name": "OrderByNum-31",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld58Oma2f": {
            "id": "fld58Oma2f",
            "name": "OrderByNum-32",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldm37kORj": {
            "id": "fldm37kORj",
            "name": "OrderByNum-33",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldf3gNqnh": {
            "id": "fldf3gNqnh",
            "name": "OrderByNum-34",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld9K16lpJ": {
            "id": "fld9K16lpJ",
            "name": "OrderByNum-35",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flddL178sK": {
            "id": "flddL178sK",
            "name": "OrderByNum-36",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldOq1GetS": {
            "id": "fldOq1GetS",
            "name": "OrderByNum-37",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldjNL5HYW": {
            "id": "fldjNL5HYW",
            "name": "OrderByNum-38",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldDxKikoW": {
            "id": "fldDxKikoW",
            "name": "OrderByNum-39",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldP2mvHFn": {
            "id": "fldP2mvHFn",
            "name": "OrderByNum-40",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldl2xH8ZN": {
            "id": "fldl2xH8ZN",
            "name": "OrderByNum-41",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldDBN8c6o": {
            "id": "fldDBN8c6o",
            "name": "OrderByNum-42",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldcw2k0C6": {
            "id": "fldcw2k0C6",
            "name": "OrderByNum-43",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldvkHMYSx": {
            "id": "fldvkHMYSx",
            "name": "OrderByNum-44",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldQ6pin2M": {
            "id": "fldQ6pin2M",
            "name": "OrderByNum-45",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldN9qOK0y": {
            "id": "fldN9qOK0y",
            "name": "OrderByNum-46",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld7KesQWZ": {
            "id": "fld7KesQWZ",
            "name": "OrderByNum-47",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldQYEgzsC": {
            "id": "fldQYEgzsC",
            "name": "OrderByNum-48",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldhBVqJ2G": {
            "id": "fldhBVqJ2G",
            "name": "OrderByNum-49",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldGqdBFJa": {
            "id": "fldGqdBFJa",
            "name": "OrderByNum-50",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldEwGSOQc": {
            "id": "fldEwGSOQc",
            "name": "OrderByNum-51",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld3ktCIdR": {
            "id": "fld3ktCIdR",
            "name": "OrderByNum-52",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldBaH1oWh": {
            "id": "fldBaH1oWh",
            "name": "OrderByNum-53",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldIb8NcDR": {
            "id": "fldIb8NcDR",
            "name": "OrderByNum-54",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldRh9aESJ": {
            "id": "fldRh9aESJ",
            "name": "OrderByNum-55",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldMKW8ZE7": {
            "id": "fldMKW8ZE7",
            "name": "OrderByNum-56",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldcbX2BvZ": {
            "id": "fldcbX2BvZ",
            "name": "OrderByNum-57",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldzMmYEgF": {
            "id": "fldzMmYEgF",
            "name": "OrderByNum-58",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld976JiNY": {
            "id": "fld976JiNY",
            "name": "OrderByNum-59",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldfgq3HRB": {
            "id": "fldfgq3HRB",
            "name": "OrderByNum-60",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldZIS5UWm": {
            "id": "fldZIS5UWm",
            "name": "OrderByNum-61",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld3QybeOH": {
            "id": "fld3QybeOH",
            "name": "OrderByNum-62",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldolcOrzA": {
            "id": "fldolcOrzA",
            "name": "OrderByNum-63",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flduBxIDVw": {
            "id": "flduBxIDVw",
            "name": "OrderByNum-64",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld2VrlomD": {
            "id": "fld2VrlomD",
            "name": "OrderByNum-65",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldoUBv2RN": {
            "id": "fldoUBv2RN",
            "name": "OrderByNum-66",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldLkBfD5v": {
            "id": "fldLkBfD5v",
            "name": "OrderByNum-67",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldHybOir0": {
            "id": "fldHybOir0",
            "name": "OrderByNum-68",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld73iSgtU": {
            "id": "fld73iSgtU",
            "name": "OrderByNum-69",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldnSQuIsP": {
            "id": "fldnSQuIsP",
            "name": "OrderByNum-70",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldDya9QZo": {
            "id": "fldDya9QZo",
            "name": "OrderByNum-71",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldP0viUuj": {
            "id": "fldP0viUuj",
            "name": "OrderByNum-72",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldlp2wZ6j": {
            "id": "fldlp2wZ6j",
            "name": "OrderByNum-73",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldwf2jaGI": {
            "id": "fldwf2jaGI",
            "name": "OrderByNum-74",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld23Ng16V": {
            "id": "fld23Ng16V",
            "name": "OrderByNum-75",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld5yf2qpO": {
            "id": "fld5yf2qpO",
            "name": "OrderByNum-76",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldZAjuU7d": {
            "id": "fldZAjuU7d",
            "name": "OrderByNum-77",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldkMt3GHd": {
            "id": "fldkMt3GHd",
            "name": "OrderByNum-78",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldPRfBIvV": {
            "id": "fldPRfBIvV",
            "name": "OrderByNum-79",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld4LiPmR2": {
            "id": "fld4LiPmR2",
            "name": "OrderByNum-80",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldosuw2hm": {
            "id": "fldosuw2hm",
            "name": "OrderByNum-81",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldSWG4uBQ": {
            "id": "fldSWG4uBQ",
            "name": "OrderByNum-82",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldXMjFHY2": {
            "id": "fldXMjFHY2",
            "name": "OrderByNum-83",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldgpB6CMl": {
            "id": "fldgpB6CMl",
            "name": "OrderByNum-84",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldSrHob5k": {
            "id": "fldSrHob5k",
            "name": "OrderByNum-85",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flddk1A29p": {
            "id": "flddk1A29p",
            "name": "OrderByNum-86",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldnWPOAZ4": {
            "id": "fldnWPOAZ4",
            "name": "OrderByNum-87",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldo6c3Eet": {
            "id": "fldo6c3Eet",
            "name": "OrderByNum-88",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldUVZnkP1": {
            "id": "fldUVZnkP1",
            "name": "OrderByNum-89",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldEwp6gRo": {
            "id": "fldEwp6gRo",
            "name": "OrderByNum-90",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fld2pMTLF6": {
            "id": "fld2pMTLF6",
            "name": "OrderByNum-91",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldv69dj5x": {
            "id": "fldv69dj5x",
            "name": "OrderByNum-92",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldJKDzANO": {
            "id": "fldJKDzANO",
            "name": "OrderByNum-93",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flddPyJsE8": {
            "id": "flddPyJsE8",
            "name": "OrderByNum-94",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldOIKlGJL": {
            "id": "fldOIKlGJL",
            "name": "OrderByNum-95",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldQTCMPve": {
            "id": "fldQTCMPve",
            "name": "OrderByNum-96",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldtvWOLAV": {
            "id": "fldtvWOLAV",
            "name": "OrderByNum-97",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "fldlnzUiry": {
            "id": "fldlnzUiry",
            "name": "OrderByNum-98",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        },
        "flda3jMcDk": {
            "id": "flda3jMcDk",
            "name": "OrderByNum-99",
            "type": 2,
            "property": {
                "formatter": "0.0"
            },
            "fieldUIType": "Number",
            "exInfo": {
                "fieldUIType": "Number"
            }
        }
    }
    numberFieldList = list(numberFieldMap.keys())
    new_recordList = []
    with open("test.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            new_recordList.append(row[0])
    operations = []
    for record_id in new_recordList:
        # actions
        actions = []
        # 写入单选
        for field_id in singleSelectList:
            opt_id = random.choice(optionList)['id']
            action = {
                "action": "data.setRecord",
                "type": 2,
                "tableId": table,
                "recordId": record_id,
                "viewType": 1,
                "data": {
                    field_id: {
                        "value": opt_id,
                        "type": 3
                    }
                }
            }
            actions.append(action)
        # 写入数字字段
        for field_id in numberFieldList:
            value = random.randint(-5000, 5000)
            action = {
                "action": "data.setRecord",
                "type": 2,
                "tableId": table,
                "recordId": record_id,
                "viewType": 1,
                "data": {
                    field_id: {
                        "type": 2,
                        "value": value
                    }
                }
            }
            actions.append(action)
        operation = {
            'command': 'SetRecord',
            'type': 2,
            'actions': actions,
            'syncFlag': 0}
        operations.append(operation)
        if len(operations) == 100:
            cli.root_request(operations)
            time.sleep(0.5)
            operations = []



    # sortInfos = []
    # for field_id in numberFieldList:
    #     sortInfo = {"fieldId": field_id, "desc": False}
    #     sortInfos.append(sortInfo)
    # actions = [{
    #     "action": "view.sortRecordsV2",
    #     "type": 2,
    #     "tableId": table,
    #     "viewId": "vewFS7dbKF",
    #     "data": {
    #         "sortInfo": sortInfos,
    #         "autoSort": True
    #     }
    # }]
    # operations = [
    #     {
    #         "command": "SortRecordV2",
    #         "type": 2,
    #         "actions": actions,
    #         "syncFlag": 1
    #     }
    # ]
    # cli.root_request(operations)
