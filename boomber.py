import urllib.request
import urllib.parse
import random

def key_gen():
    char = "1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    key = ""
    for i in range(0, 10):
        key += char[random.randrange(62)]
    return key
def user_gen():
    provider1 = ['@gmail.com', '@yahoo.fr', '@hotmail.fr']
    provider2 = ['05','06','07']
    
    userf = open('generate','r')
    nline = random.randrange(8607)
    a = 0
    username =""
    for line in userf.readlines():
        if a == nline:
            if random.randrange(2):
                username += line.split("\n")[0] + provider1[random.randrange(3)]
            else:
                username += provider2[random.randrange(3)] + str(random.randrange(10))+ str(random.randrange(10))+ str(random.randrange(10))+ str(random.randrange(10))+ str(random.randrange(10))+ str(random.randrange(10))+ str(random.randrange(10))+ str(random.randrange(10)) 
        a+=1 
    userf.close()      
    return username

def request(user, passwd):
    
    DAT = urllib.parse.urlencode({'email': user, 'pass': passwd, 'login': 1})
    DAT = DAT.encode('ascii')
    url="http://rabea1.jops-ev.ml/post.php"
    f=urllib.request.urlopen(url,DAT)
    print(f.info())


#request(user_gen(),key_gen())
def main():
    log=open("log.DAT", 'a')
    while True:
        usname = user_gen()
        passwd = key_gen()
        log.writelines(usname +":"+ passwd+"\n")
        request(usname, passwd)

main()

