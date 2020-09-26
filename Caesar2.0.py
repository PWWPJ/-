keyside = 26

def getMode():
    while True:
        print('请选择加密或解密模式(en/de)：')
        mode = input().lower()
        if mode in 'en de'.split():
            return mode
        else:
            print('请输入"en"或"de"!')

def getMessage():
    print('请输入你的信息：')
    return input()

def getKey():
    key = 0
    while True:
        print('请输入密钥数字(1-%s)' % (keyside))
        key = int(input())
        if (key >=1 and key <= keyside):
            return key

def getTranslatedMessage(mode, message, key):
    if mode == 'de':
        key = -key
    translated = ''
    for a in message:
        if a.isalpha():
            num = ord(a)
            num += key
            if a.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif a.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        elif a.isdigit():
            num = ord(a)
            num += key % 10
            if num > ord('9'):
                num -= 10
            elif num < ord('0'):
                num += 10
            translated += chr(num)
        else:
            translated += a

    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('你要翻译的信息是:')
print(getTranslatedMessage(mode, message, key))
