import requests



#1.get封装
def requests_get(url,headers=None):
    r = requests.get(url,headers = headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

    res = dict()
    res["code"] = code
    res["body"] = body
    return res

#2.post封装
def requests_post(url,json=None):
    r = requests.post(url,json=json)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

    res = dict()
    res["code"] = code
    res["body"] = body
    return res

#重构
class Request:
    def requests_api(self,url,json=None,headers=None,method='get'):
        if method == 'get':
            r = requests_get(url,headers=headers)
        elif method == 'post':
            r = requests_post(url,json=json)

        # code = r.status_code
        # try:
        #     body = r.json()
        # except Exception as e:
        #     body = r.text
        #
        # res = dict()
        # res["code"] = code
        # res["body"] = body
        return r

#重构get请求
    def get(self,url,**kwargs):
        return self.requests_api(url,method='get',**kwargs)


#重构post请求
    def post(self,url,**kwargs):
        return self.requests_api(url,method='post', **kwargs)