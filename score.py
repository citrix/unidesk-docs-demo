import sys
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
base_url = 'http://61.160.184.184:8080/'
post_url = base_url+'getKnowledgeFilenames.do'
cookies  = dict(JSESSIONID = '8ACFAE3E4109BA9E8CD508B95B414DFC',sitech_userCode = 'chs',sitech_sysCode = 'skms', sitech_usercitysid = '11')

def geturl(id):
    response = requests.post(post_url, data = {'docid':id}, cookies = cookies)
    file_raw = response.text.split('$$')[1]
    soup = BeautifulSoup(file_raw,"html.parser")
    file_name = ''
    for tablerow in soup.find_all(id="checkAll"):
        file_name = file_name + tablerow.get('value') + ','
    downloadurl = base_url + 'downloadDocFiles.do?docid='+ str(id) + '&fileids=' + file_name
    download(downloadurl)

def download(downloadurl):
    session = requests.Session()
    session.get(downloadurl, cookies = cookies)

with open('ids.txt', 'r') as f:
    for line in f:
        print line
        geturl(int(line))







