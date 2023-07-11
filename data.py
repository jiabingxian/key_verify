import random
import base64
import datetime
c=0

def add(name,y=9999,m=12,m1=31):
    b = random.randint(100000, 999999)
    text = [name,b]
    a=int(text[1]) * 2 // 5
    tmp=int(text[1])*2%5!=0
    if tmp: # 计算校验码
        a=a*2
        if a >=10000:
            a=a//5
        else:
            a=a+10
    else:
        a=a//2*10
    text.append(a)
    text.append(a * 2)
    text.append(y)
    text.append(m)
    text.append(m1)
    n = str(text[0]) + ',' + str(text[1]) + ',' + str(text[2]) + ',' + str(text[3]) + ',' + str(text[4]) + ',' + str(text[5]) + ',' + str(text[6])
    n = n.encode('utf-8')
    n = base64.b64encode(n)
    n=str(n, 'utf-8')
    return n

def if_key(value,all=False,turpe=False):
    global c
    value = base64.b64decode(value).decode("utf-8")
    text = value.split(',')
    if len(text) < 7:  # 标准卡号被Base64解码后应为8条
        return '格式错误'
    data={'name':text[0],'card':text[1],'checksum':text[2],'cida':text[3],'date':str(text[4:7]),'info':''}
    if all:
        print(data[0]+'\n'+data[1]+'\n'+data[2]+'\n'+data[3]+'\n'+data[4])
    time = datetime.date(int(text[4]), int(text[5]), int(text[6]))
    tdate = datetime.date.today()  # 今天的日期
    a = int(text[1]) * 2 // 5
    tmp = int(text[1]) * 2 % 5 != 0
    if tmp:  # 计算校验码
        a = a * 2
        if a >= 10000:
            a = a // 5
        else:
            a = a + 10
    else:
        a = a // 2 * 10
    if not turpe:  # 判断
        if int(text[3]) // 2 == int(text[2]) and int(text[2]) == a:
            if time >= tdate:
                c += 1
                return "验证通过，你是第" + str(c) + '个来的'
            else:
                return "验证失败，卡已过期"
        else:
            return "验证失败，卡格式错误"
    else:
        if int(text[3]) // 2 == int(text[2]) and int(text[2]) == a:
            if time >= tdate:
                c += 1
                data['info']="验证通过，你是第" + str(c) + '个来的'
            else:
                data['info']="验证失败，卡已过期"
        else:
            data['info']="验证失败，卡格式错误"
    return data
    
def tui():
    a=input('请输入请求(add/if)：')
    if a=='add':
        name = str(input('姓名：'))
        y = int(input('年：'))
        m = int(input('月：'))
        m1 = int(input('日：'))
        n = add(name, y, m, m1)
        print(n)
    elif a=='if':
        value = input('请输入二维码：')
        a = if_key(value, True)
        print(a)
    else:
        return None

if __name__=='__main__':
    tui()