
import re
import smtplib
import datetime
import pytz
import socks
from ProxyHandler import ProxyHandler
import os

LOGGER_INFO = "logger.INFO"
LOGGER_WARNING = "logger.WARNING"
LOGGER_ERROR = "logger.ERROR"


def is_valid_email(email):
    if len(email) > 7:
        return bool(re.match( "^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
    return False

def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

def is_valid_port(port):
    try:
        int(port)
        return True
    except:
        return False

def get_domain_from_email(email):
    if is_valid_email(email):
        return email.split('@')[-1]
    else:
        print("Invalid Email: %s" %(email))

def get_domain_name_from_smtp_host(smtp_host):
    return '.'.join(smtp_host.split('.')[-2:])

def send_email(sender, password, receiver, smtp_host, smtp_port, content):
    while True:
        try:
            proxy_handler = ProxyHandler()
            if not os.path.isfile('proxies.json'):
                proxy_handler.create_proxies()
            proxy_host, proxy_port = proxy_handler.get_proxy() # Returns free proxy server IPs
            print('TRYING WITH PROXY %s %s' %(proxy_host, proxy_port))
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, proxy_host, proxy_port)
            socks.wrapmodule(smtplib)
            server = smtplib.SMTP(host=smtp_host, port=smtp_port)
            server.login(sender,password)
            return server.sendmail(sender,receiver, content)
        except:
            continue


def get_today_in_epoch():
    return int(datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.utc).timestamp())
