import argparse
import json
import random
import string
import webbrowser
import requests
# username= 'contextbi\jatin'
# password='delhi$123'
userDirectory, userId = "PALAASH-LT-010","jatin.anand"
# userDirectory = 'contextbi'
# userId = 'vikram.kumar'
CloudURL = 'contextbi-qs.contextbi.net' 
VirtualProxy = 'webticket'
CertificatePath = 'C:\\ProgramData\\Qlik\\Sense\\Repository\\Exported Certificates\\PALAASH-LT-010\\'
# CertificatePath = 'C:\\ProgramData\\Qlik\\Sense\\Repository\\Exported Certificates\\contextbi-qs.contextbi.net\\'
# url1='https://contextbi-qs.contextbi.net/hub'
# url2='https://contextbi-qs.contextbi.net/adfs/hub'

# privateKeyPath = "C:\\ProgramData\\Qlik\\Sense\\Repository\\Exported Certificates\\PALAASH-LT-010\\"
parser = argparse.ArgumentParser()
parser.add_argument('--server', help='Qlik Sense Server to connect to')
parser.add_argument('--certs', help='Location of certificates')
parser.add_argument('--virtualproxy', help='Qlik Sense Virtual Proxy')
parser.add_argument('--user', help='user')
parser.add_argument('--userdirectory', help='directory to append')

args = parser.parse_args()

requests.packages.urllib3.disable_warnings()

def set_xrf(): 
    """
    Create XRF key used to prevent cross site request forgery
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, 16))

xrf = set_xrf()
certificate=(CertificatePath+'/client.pfx', CertificatePath+'/server.pfx')
root = root=CertificatePath+'root.cer'
headers = {
    'content-type': 'application/json',
    'X-Qlik-Xrfkey': xrf,
}

def get_ticket():
    """
    Post arguments to the Qlik Sense Virtual Proxy
    :return: Ticket
    """
    payload = {'UserDirectory': userDirectory, 'UserId': userId}
    json_payload = json.dumps(payload)
    url = 'https://{0}:4243/qps/ticket?Xrfkey={1}'.format(args.server, xrf)
    if args.virtualproxy is not None:
        url = 'https://{0}:4243/qps/{1}/ticket?Xrfkey={2}'.format(CloudURL, VirtualProxy, xrf)
    response = requests.post(url, data=json_payload, headers=headers, verify=root, cert=certificate)
    return response.json().get('Ticket')

def create_url():
    """
    Construct the URL with the Qlik Sense Ticket
    """
    url = 'https://{0}/hub/?qlikTicket={1}'.format(CloudURL, get_ticket())
    if args.virtualproxy is not None:
        url = 'https://{0}/{1}/hub/?qlikTicket={2}'.format(CloudURL, VirtualProxy, get_ticket())
    return url

if __name__ == '__main__':
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(create_url()) 