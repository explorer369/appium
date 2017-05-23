#conding:GBK
import sys, urllib, urllib2, json, base64,codecs,time,re

def picture_text(screen_path=r"D:\\screen\\image.png"):
    url = 'http://apis.baidu.com/apistore/idlocr/ocr'
    data = {}
    data['fromdevice'] = "pc"
    data['clientip'] = "10.10.10.0"
    data['detecttype'] = "LocateRecognize"
    data['languagetype'] = "CHN_ENG"
    data['imagetype'] = "1"
    data['image'] = "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDABMNDxEPDBMREBEWFRMXHTAfHRsbHTsqLSMwRj5KSUU+RENNV29eTVJpU0NEYYRiaXN3fX59S12Jkoh5kW96fXj/2wBDARUWFh0ZHTkfHzl4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHj/wAARCAAfACEDAREAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAQDBQb/xAAjEAACAgICAgEFAAAAAAAAAAABAgADBBESIRMxBSIyQXGB/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APawEBAQEBAgy8i8ZTVV3UY6V1eU2XoWDDZB19S646Gz39w9fkKsW1r8Wm2yo1PYis1be0JG9H9QNYCAgc35Cl3yuVuJZl0cB41rZQa32dt2y6OuOiOxo61vsLcVblxaVyXD3hFFjL6La7I/sDWAgICAgICB/9k="


    f = open(screen_path,'rb')
    data['image'] = base64.b64encode(f.read())
    f.close()

    decoded_data = urllib.urlencode(data)
    req = urllib2.Request(url, data = decoded_data)

    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "1eac708088669a6006ff1af307bd1dcb")

    resp = urllib2.urlopen(req)
    content = resp.read()

    if(content):
        content = content.decode("unicode-escape").encode("GBK")
        NW = re.findall(r'word\"\:\"(.*?)\"\,\"charset',content)
        ee ='\n'.join(NW)
        return ee.decode('GBK')
