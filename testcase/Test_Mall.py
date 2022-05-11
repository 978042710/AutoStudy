import requests


def login():
    url = "https://www.moxinhuiyi.com/apis/course/api/course/category/list"
    r = requests.post(url)
    print(r.json())
    print(r.status_code)


if __name__ == '__main__':
    login()