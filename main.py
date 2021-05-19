# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from woocommerce import API

wcapi = API(
    url="https://gaat.fashion",
    consumer_key="ck_53c400a337b5de4f927565e848c6dbe63c72fe25",
    consumer_secret="cs_b64df74d7c0b1f884ba617b0e03d3bc38ba47a56",
    version="wc/v3",
)


def print_hi():
    print(wcapi.get("productss", params={'slug': ''}).json())

    pass


if __name__ == '__main__':
    print_hi()
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
