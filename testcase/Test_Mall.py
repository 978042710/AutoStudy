import requests
from utils.RequestsUtil import requests_get
from utils.RequestsUtil import requests_post
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml

def list():
    conf_y = ConfigYaml()
    url = conf_y.get_conf_url()
    r = requests_get(url)
    print(r)




def login():

    url = "https://www.moxinhuiyi.com/apis/course/api/course/category/list"
    # r = requests.post(url)
    # print(r.json())
    # print(r.status_code)
    request = Request()
    r = request.post(url)
    #r = requests_post(url)
    print(r)


if __name__ == '__main__':
    login()
    list()

