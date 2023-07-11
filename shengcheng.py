from MyQR import myqr
from data import add

name = str(input('姓名：'))
y = int(input('年：'))
m = int(input('月：'))
m1 = int(input('日：'))
n=add(name, y, m, m1)
print(n)
_ = input('(Y/N)')
if _ == 'Y' or _ == 'y':
    myqr.run(words=n, save_name='barcode_png\\' + str(name) + '.jpg')
