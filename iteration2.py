x = int(input('請輸入一個正整數：'))
i = 1
factor = []
while i <= x:
    if x % i == 0:
        factor.append(i)
    i += 1
print(x ,'的因數為',factor)
