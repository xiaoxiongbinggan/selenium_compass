import requests


def login_in():
    url = 'https://test-gateway.tking.com/catfish-flowers/catfish/client/loginByWorkNum'
    data = {
        'channelType': 'CATFISH_PC',
        'loginType': 'DING',
        'workNum': '108983'
    }
    response = requests.get(url, data)
    return response.json()['data']['token']


if __name__ == '__main__':
    print(login_in())
