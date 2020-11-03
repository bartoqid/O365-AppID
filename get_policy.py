import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


def get_policy(firewall_ip, api_key):
    xpathvalue = '/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"]/rulebase/security'

    values = {'type': 'config', 'action': 'get', 'key': api_key, 'xpath': xpathvalue}

    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    return response