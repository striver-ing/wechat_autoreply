import requests
import re

def get_html(url):
    try:
        html = requests.get(url).text
    except Exception as e:
        print(e)
        return ''
    else:
        return html

_regexs = {}
# @log_function_time
def get_info(html, regexs, allow_repeat = False, fetch_one = False, split = None):
    regexs = isinstance(regexs, str) and [regexs] or regexs

    infos = []
    for regex in regexs:
        if regex == '':
                continue

        if regex not in _regexs.keys():
            _regexs[regex] = re.compile(regex, re.S)

        if fetch_one:
                infos = _regexs[regex].search(html)
                if infos:
                    infos = infos.groups()
                else:
                    continue
        else:
            infos = _regexs[regex].findall(str(html))

        if len(infos) > 0:
            # print(regex)
            break

    if fetch_one:
        infos = infos if infos else ('',)
        return infos if len(infos) > 1 else infos[0]
    else:
        infos = allow_repeat and infos or sorted(set(infos),key = infos.index)
        infos = split.join(infos) if split else infos
        return infos

################################################

duanzi_collection = set()

def spider_duanzi():
    url = 'http://www.neihanshequ.com/'
    html = get_html(url)

    regex = 'data-text="(.*?)"'
    datas = get_info(html, regex)

    for data in datas:
        if len(data) >= 30:
            duanzi_collection.add(data)

def get_duanzi():
    if not duanzi_collection:
        spider_duanzi()

    return duanzi_collection.pop()

if __name__ == '__main__':
    duanzi = get_duanzi()
    print(duanzi)
