from get_api_key import get_key
from create_appid import sharepoint_upload
from create_appid import O365_domain
from get_policy import get_policy
import getpass

# Enter firewall IP
firewall_ip = input("Please Enter firewall IP: ")
# Enter firewall admin
firewall_admin = input("Please Enter firewall username: ")
# Enter password for firewall
firewall_password = getpass.getpass("Please enter firewall password: ")

tenant = input("Please Enter tenant name: ")

key = get_key(firewall_ip, firewall_admin, firewall_password)

policy = get_policy(firewall_ip, key)

sharepoint_result = sharepoint_upload(firewall_ip, key, tenant)

O365_domain_result = O365_domain(firewall_ip, key, tenant)

#print(result.text)
#print(result1.text)