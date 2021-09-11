import requests


url = "http://localhost:8080/wrapgoods/get"

params = {"cacheEnable":"false","companyId":"12","shopId":"12","goodsId":"10001590","templateId":"0","withTemplateName":"true"}


res = requests.get(url=url,params=params)

print(res.text)