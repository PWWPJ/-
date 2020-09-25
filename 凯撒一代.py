print("加密请输入en,解密请输入de")
ch = input()
if ch == 'en':
    mw  = input("请输入明文:")
    my1 = input("请输入位移量:")
    for a in mw:
        print(chr(ord(a)%127+int(my1)),end="")
elif ch == 'de':
    miw = input("请输入密文:")
    my2 = input("请输入位移量:")
    for b in miw:
        print(chr(ord(b)-int(my2)%127),end="")
else:
    print("请正确输入en/de")
