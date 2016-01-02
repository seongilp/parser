import http.cookiejar #Cookie를 관리하기 위해 사용합니다.
import urllib
import ssl #ssl을 적용합니다.

cj = http.cookiejar.CookieJar() #Cookie 적용
https_sslv23_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)) 
opener = urllib.request.build_opener(https_sslv23_handler,urllib.request.HTTPCookieProcessor(cj))
opener.addheaders=[('User-agent','Mozilla/5.0'),('Accept-Language', 'ko-KR')] 
urllib.request.install_opener(opener)
login_url = "https://etorrent.co.kr" 
url = "http://etorrent.co.kr"
login_info = {
    'mb_id' : "zihado",
    'mb_password' : "aqswde"
}
login_request = urllib.parse.urlencode(login_info)
req = urllib.request.Request(login_url+'/bbs/login_check2.php',login_request.encode('UTF-8'))
res = urllib.request.urlopen(req)
write_info = {}
write_info[0] = {
    'bo_table':'eboard',
    'wr_subject':"TEST",
    'wr_content':"TEST",
    'wr_ccl_nc':"nc",
    'wr_ccl_nd':"nd"
}
write_request = urllib.parse.urlencode(write_info[0])
req = urllib.request.Request(url+"/bbs/write_update.php",write_request.encode('UTF-8'))
res = urllib.request.urlopen(req)
