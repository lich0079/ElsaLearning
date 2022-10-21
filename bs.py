import random

num1st = 0
num2nd = 1000

num = random.randint(num1st, num2nd)

end = False

count = 0

while end != True :
    print(f"请输入你猜的数字， 数字在  {num1st} 到 {num2nd} 之间")
    inStr=input()
    count = count + 1
    inNum = int(inStr, 10)
    if inNum > num :
        print("你猜大了")
        num2nd = inNum
    elif inNum < num :
        print("你猜小了")
        num1st = inNum
    else :
        print(f"你猜对了 数字是 {inNum}， 你猜了 {count} 次")
        end = True

