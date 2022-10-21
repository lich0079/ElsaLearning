print("请输入明文")
message=input()



print("生成的密文")
for c in message:
    number = ord(c)
    number = number + 2
    char = chr(number)
    print(char, end="")