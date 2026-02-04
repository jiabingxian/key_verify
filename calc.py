from main import Card

card=Card(input("姓名:"),int(input("卡号:")),int(input("有效期-年:")),int(input("有效期-月:")),int(input("有效期-日:")))
card.calc()
print("编码后的卡信息:{}".format(card.encode()))