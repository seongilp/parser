import http.cookiejar #Cookie를 관리하기 위해 사용합니다.
import urllib
import ssl #ssl을 적용합니다.

cj = http.cookiejar.CookieJar() #Cookie 적용
https_sslv23_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)) #python의 ssl protocol_SSLv23을 적용하기 위한 handler

opener = urllib.request.build_opener(https_sslv23_handler,urllib.request.HTTPCookieProcessor(cj))#SSL과 Cookie를 사용하는 opner를 만듭니다.

opener.addheaders=[('User-agent','Mozilla/5.0'),('Accept-Language', 'ko-KR')] #Header에 필요한 것들을 추가 시켜줍니다.

urllib.request.install_opener(opener)#urllib에 생성해둔 opner를 만들어둡니다. 

login_url = "https://etorrent.co.kr" #login시 ssl을 이용하기에 https를 사용하는 주소를 적어두었습니다.
#login_url = "https://clien.net" #login시 ssl을 이용하기에 https를 사용하는 주소를 적어두었습니다.
url = "http://etorrent.co.kr" #login을 제외한 데이터는 http를 이용하여 사용합니다.
login_info = {
    'mb_id' : "zihado",#clien id를 적습니다.
    'mb_password' : "aqswde"#password를 적습니다.
}
login_request = urllib.parse.urlencode(login_info)
req = urllib.request.Request(login_url+'/bbs/login_check2.php',login_request.encode('UTF-8'))
res = urllib.request.urlopen(req)

print(res)

write_info = {}
write_info[0] = {
    'bo_table':'eboard',
    'wr_subject':"python으로 test입니다.",
    'wr_content':"테스트 후 정리하여 팁과 강좌에 글올리겠습니다.",
    'wr_ccl_nc':"nc",
    'wr_ccl_nd':"nd"
}

write_request = urllib.parse.urlencode(write_info[0])
req = urllib.request.Request(url+"/bbs/write_update.php",write_request.encode('UTF-8'))
res = urllib.request.urlopen(req)
