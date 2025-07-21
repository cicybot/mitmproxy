
from mitmproxy.tools import main

'''

curl -v -x http://127.0.0.1:8080 https://www.baidu.com

'''
main.mitmweb(
    [
        "-v",
        "--listen-port",
        "10000",
        "--listen-host",
        "0.0.0.0",
        "--mode",
        "upstream:http://127.0.0.1:4445",
        "--upstream-auth","Account_10000:ssss"
    ]
)