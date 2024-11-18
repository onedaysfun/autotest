from common.send_message_cs import EditTable

table_token_list =[
    "tblkNrdZshSWPOAW",
    "tblxhAzQjud3eDWi",
    "tblg86tvCagcj0BA",
    "tblMQnZju9LXbj7d",
    "tblr8pWR8YzqTplt",
    "tblh8dtUa5xcsFWm",
    "tblVWk7EvBUc5Moj",
    "tblurEXEqWPlI3fq",
    "tblPL4cSGowNgO0V",
    "tbluEUXk69HEg4ox",
    "tblsz7ve7GKsoJAB",
    "tblDrey3z4rZuvWh",
    "tblnxQb8dbJCxfIv",
    "tblW4YY13mhOUNuM",
    "tblTU7q9TgxQCJvX",
    "tblH6OkZ771LaKTI",
    "tblzrLrzjzCcbfpL",
    "tbleXSYMMStWPp7K",
    "tblrADiNKJzFMv4w",
    "tblfbBljvIQEFVzd",
    "tblGk6AvytCX0hw9",
    "tbl6h3fE21d35gdW",
    "tblbREb3lr9mHqyi",
    "tblFi70KLcq36wz0",
    "tblRX3BMZ0tXXKE3",
    "tblLx0j07dbynGgR",
    "tbl0AHTIDSh4tSK6",
    "tbloTPeT96nwqrmt",
    "tblWpXPuQ8TloMIw",
    "tblWvJE6dzhnyVOb",
    "tblWn4HtKwRCI1iF",
    "tblDNlY51MaN7RRU",
    "tblYStZG7HAGiAKY",
    "tblWCOlVCCNPev3t",
    "tblz46cYV04yJsUy",
    "tbl6uPHtIsd2XMyh",
    "tbltVcsrzjiJx1u8",
    "tblKuIsh9xIVzETt",
    "tblLvOuGmltNkskF",
    "tbl1jRq2KN3dRZ4K",
    "tblGc67lP97TWK1k",
    "tblFKkEoOHSWZURF",
    "tblhyAwYhchnoi0v",
    "tbl1XqlGy0MSOVoI",
    "tblnAh5KaErtsJLV",
    "tblAbWoSSH7Z9wI3",
    "tblOoc3KZ68q2L1n",
    "tblQWH19ZaG5SXms",
    "tblYwu2FebRhP8J9",
    "tblOgnmRUjrB1Z5d"
]

if __name__ == '__main__':
    domain_jp = "https://yalixw0asad.feishu.cn/"
    session = ""
    headers = {"x-tt-stress": "true", "env": "pre_release"}
    parent_token = "BICpbUvRoajOWdsmNc5jbn9mpff"
    for table_token in table_token_list:
        cli = EditTable(domain_jp, session, parent_token, table_token, 0)
        cli.HttpClient.set_headers(headers)
        cli.add_record(True,{})
