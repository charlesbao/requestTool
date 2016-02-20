
def search(patten,contents,useTry = False,n = 1):
    from re import search,S
    if useTry:
        try:
            replacement = search(patten,contents,S).group(n)
        except:
            print 'SEARCH ERROR:%s' % str(patten)
            return [False,'']
        else:
            return [True,replacement]
    else:
        return search(patten,contents,S).group(n)


def findall(patten,contents,useTry = False):
    from re import findall,S
    if useTry:
        replacement = findall(patten,contents,S)
        if len(replacement) == 0:
            print 'FIND ERROR:%s' % str(patten)
            return [False,[]]
        else:
            return [True,replacement]
    else:
        return findall(patten,contents,S)

def mapFindall(list,n = 0):
    arr = []
    for each in list:
        arr.append(each[n])
    return arr

def writeJson(fileName,dict):
    from json import dumps
    jsonStr = dumps(dict, sort_keys=True, indent=2)
    fp = open(fileName+'.json','w')
    fp.write(jsonStr)
    fp.close()
    return 'JSON COMPLETE'

def usePool(function,list,n = 5):
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(n)
    pool.map(function,list)
    pool.close()
    pool.join()

def get(url,header = None,timeout = 5):
    from urllib2 import Request,urlopen
    if header == None:
        header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    req = Request(url,headers=header)
    try:
        content  = urlopen(req,timeout = timeout).read()
    except:
        print 'GET ERROR:%s' % url
        return [False,'',url]
    else:
        return [True,content]

def post(url,data = '',header = None,timeout = 5):
    from urllib2 import Request,urlopen
    from urllib import urlencode
    if header == None:
        header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    req = Request(url,urlencode(data),headers=header)
    try:
        content  = urlopen(req,timeout = timeout).read()
    except:
        print 'POST ERROR:%s' % url
        return [False,'',url]
    else:
        return [True,content]

def sleep(waitTimeOrTimeList):
    from time import sleep
    if type(waitTimeOrTimeList) == list:
        if type(waitTimeOrTimeList[0] == float):
            from random import uniform
            waitTime = uniform(waitTimeOrTimeList[0],waitTimeOrTimeList[1])
            sleep(waitTime)
            return waitTime
        else:
            from random import randint
            waitTime = randint(waitTimeOrTimeList[0],waitTimeOrTimeList[1])
            sleep(waitTime)
            return waitTime
    else:
        sleep(waitTimeOrTimeList)
        return waitTimeOrTimeList

def useThread(list):
    import threading
    threads = []
    for each in list:
        t = threading.Thread(target=each[0],args=each[1])
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
    return 'THREAD OVER'

def listenServer(functionList = [],function = None,port = 8870,ip = '127.0.0.1'):
    import BaseHTTPServer
    from SocketServer import ThreadingMixIn
    import threading
    class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            if function == None:
                self.wfile.write('HELLO')
            else:
                self.wfile.write(function)
    class ThreadingHttpServer( ThreadingMixIn, BaseHTTPServer.HTTPServer ):
        pass
    server = ThreadingHttpServer((ip,port), WebRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print "SERVER LOOP RUNNING IN:", "http://%s:%d" % (ip,port)
    useThread(functionList)
    while True:
        pass

def sendMail(HostAndPortTuple,userNameAndPassTuple,toAddressMail,title = 'SUBJECT',content = 'HELLO WORLD'):
    import smtplib
    import email.mime.text
    mail_username= userNameAndPassTuple[0]
    mail_password= userNameAndPassTuple[1]
    from_addr = mail_username
    to_addrs= toAddressMail
    HOST = HostAndPortTuple[0]
    PORT = HostAndPortTuple[1]
    smtp = smtplib.SMTP()
    try:
        smtp.connect(HOST,PORT)
    except:
        print 'CONNECT ERROR'
        return False
    smtp.starttls()
    try:
        smtp.login(mail_username,mail_password)
    except:
        print 'LOGIN ERROR'
        return False
    msg = email.mime.text.MIMEText(content)
    msg['From'] = from_addr
    msg['To'] = to_addrs
    msg['Subject']= title
    smtp.sendmail(from_addr,to_addrs,msg.as_string())
    smtp.quit()
    print 'SEND SUCCESS'
    return True

def exit(n = 0):
    from os import _exit
    _exit(n)

