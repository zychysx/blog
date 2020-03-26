import requests as req

ip_api = 'http://ip-api.com/json/'
lan = '?lang=zh-CN'


def ip_information(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get('HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
    req_ip = ip_api + user_ip + lan

    information = req.get(req_ip)




"""
{
    "status":"success",
    "country":"中国",
    "countryCode":"CN",
    "region":"SX",
    "regionName":"山西",
    "city":"太原",
    "zip":"",
    "lat":37.8706,
    "lon":112.549,
    "timezone":"Asia/Shanghai",
    "isp":"CNC Group CHINA169 Shanxi Province Network",
    "org":"",
    "as":"AS4837 CHINA UNICOM China169 Backbone",
    "query":"118.73.225.149"
 }
"""