import common.common_openapi as common_openapi


if __name__ == '__main__':
    domain = "https://open.feishu-boe.net"
    context = {
        "token": "ISDdbzyKbaZ89RsV1hbb3UZrcBb",
        "type": "bitable"
    }
    id = "cli_a21752576078d01c"
    password = "P1831odz4WRKJlyROnmlKd4rseIba417"
    session = "XN0YXJ0-907u0825-9e65-434f-b945-33117ae17cmo-WVuZA"
    cli = common_openapi.Openapi(domain, id, password)
    cli.session = session
    cli.set_access_token_user().set_access_token_default("u")
    cli.subscribe_base_get(context)
    # cli.subscribe_base(context)


