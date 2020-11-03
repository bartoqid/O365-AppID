import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


def sharepoint_upload(firewall_ip, api_key, tenant):
    xpathvalue = '/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"]/application'
    elemetvalue = '<entry name="Sharepoint-upload-%s"><signature><entry name="Uploading">' \
                  '<and-condition><entry name="And Condition 1"><or-condition><entry name="Or Condition 1"><operator>' \
                  '<pattern-match><pattern>%s</pattern><context>http-req-host-header</context></pattern-match></operator>' \
                  '</entry></or-condition></entry><entry name="And Condition 2"><or-condition><entry name="Or Condition 1"><operator><pattern-match>' \
                  '<pattern>Scenario\: UploadFile</pattern><context>http-req-headers</context></pattern-match></operator></entry></or-condition></entry>' \
                  '</and-condition><scope>protocol-data-unit</scope><order-free>yes</order-free></entry>' \
                  '</signature><subcategory>auth-service</subcategory><category>business-systems</category><technology>browser-based</technology>' \
                  '<risk>1</risk><able-to-transfer-file>yes</able-to-transfer-file><tunnel-applications>yes</tunnel-applications></entry>' % (tenant, tenant)

    values = {'type': 'config', 'action': 'set', 'key': api_key, 'xpath': xpathvalue, 'element': elemetvalue}

    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    return response


def O365_domain(firewall_ip, api_key, tenant):
    xpathvalue = '/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"]/application'
    elemetvalue = '<entry name="Domain365-%s"><signature><entry name="O365-mydomain-login">' \
                  '<and-condition><entry name="And Condition 1"><or-condition><entry name="Or Condition 1"><operator><pattern-match>' \
                  '<pattern>%s</pattern><context>http-req-host-header</context></pattern-match></operator></entry></or-condition>' \
                  '</entry></and-condition><scope>protocol-data-unit</scope><order-free>no</order-free></entry></signature>' \
                  '<subcategory>social-business</subcategory><category>collaboration</category><technology>browser-based</technology><risk>1</risk>' \
                  '<able-to-transfer-file>yes</able-to-transfer-file><tunnel-applications>yes</tunnel-applications><pervasive-use>yes</pervasive-use></entry>' % (tenant, tenant)

    values = {'type': 'config', 'action': 'set', 'key': api_key, 'xpath': xpathvalue, 'element': elemetvalue}

    call = 'https://%s/api/' % (firewall_ip)

    response = requests.post(call, data=values, verify=False)

    return response