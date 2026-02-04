import base64
import datetime

class Card:
    def __init__(self,name:str,id:int,y:int,m:int,d:int):
        self.name=name
        self.y=y
        self.m=m
        self.d=d
        self.id=id
    def calc(self):
        a=int(self.id) * 2 // 5
        if int(self.id)*2%5!=0: # 计算校验码
            a*=2
            if a >=10000:
                a=a//5
            else:
                a=a+10
        else:
            a=a//2*10
        self.verifyid=a
        self.cida=a*2
    def encode(self):
        self.calc()
        n = f"{self.name},{self.id},{self.verifyid},{self.cida},{self.y},{self.m},{self.d}"
        n = n.encode('utf-8')
        try:
            card = base64.b64encode(n)
        except base64.binascii.Error as e:
            raise ValueError("编码错误，{}".format(e))
        card=str(card, 'utf-8')
        return card
    def decode(self,code:str):
        n = code.encode('utf-8')
        try:
            n = base64.b64decode(n)
        except base64.binascii.Error as e:
            raise ValueError("解码错误，{}".format(e))
        n=str(n, 'utf-8')
        n=n.split(',')
        self.name=n[0]
        self.id=int(n[1])
        self.verifyid=int(n[2])
        self.cida=int(n[3])
        self.y=int(n[4])
        self.m=int(n[5])
        self.d=int(n[6])
    def __str__(self):
        return self.encode()
    def info(self):
        return f"姓名:{self.name}\n卡号:{self.id}\n校验码:{self.verifyid}\nCIDA:{self.cida}\n有效期至:{self.y}年{self.m}月{self.d}日"
    def verify(self):
        a = int(self.id) * 2 // 5
        if int(self.id)*2%5!=0: # 计算校验码
            a*=2
            if a >=10000:
                a=a//5
            else:
                a=a+10
        else:
            a=a//2*10
        if self.cida // 2 == self.verifyid and self.verifyid == a:
            return True
        else:
            return False
    def date_verify(self):
        today = datetime.date.today()
        expire_date = datetime.date(self.y, self.m, self.d)
        return today >= expire_date
