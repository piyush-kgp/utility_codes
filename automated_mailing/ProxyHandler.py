import requests
import re
import random
import json

class ProxyHandler:
    def __init__(self):
        pass
    def create_proxies(self):
        url = 'https://sslproxies.org/'
        source = str(requests.get(url).text)
        data = [list(filter(None, i))[0] for i in re.findall('<td class="hm">(.*?)</td>|<td>(.*?)</td>', source)]
        groupings = [dict(zip(['ip', 'port', 'code', 'using_anonymous'], data[i:i+4])) for i in range(0, len(data), 4)]
        json.dump(groupings, open('proxies.json', 'w'))
        return
    def get_proxy(self):
        groupings = json.load(open('proxies.json', 'r'))
        proxy_ = random.choice(groupings)
        while not str.isdigit(proxy_['port']):
            # dont know why but sometimes port is some random string so bypass those
            proxy_ = random.choice(groupings)
        return proxy_['ip'], int(proxy_['port'])
