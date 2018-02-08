import requests

APIKEY = 'd9f9bacfce194814b6a836946c7691c3'

def get_json(url, data):
    try:
        html = requests.post(url, data = data).json()
    except Exception as e:
        print(e)
        return ''
    else:
        return html

def get_replay(userid, text):
    data = {
        "key":APIKEY,
        "info":text,
        "userid":userid
    }
    replay = get_json('http://www.tuling123.com/openapi/api', data = data)
    return replay.get('text', '刚刚忙别的去了，你说什么？')

if __name__ == '__main__':
    replay = get_replay('21321', '北京')
    print(replay)
