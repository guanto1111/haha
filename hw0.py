money_a = int(input())
money_s = int(input())
adult = int(input())
student = int(input())
fee = int(input())
print(str(fee) + ',' +
    str(money_a*adult + money_s*student) + ',' +
    str(fee - money_a*adult - money_s*student))
