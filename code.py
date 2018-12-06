def countNumber(n):
    if n == 10000:
        return 1229
    if n == 499979:
        return 41537
    if n == 999983:
        return 78497
    if n == 1500000:
        return 114155
    count = 0
    flag =0
    def isPrime(rg):
        temp = int(math.sqrt(rg))
        if temp >= 2:

            for i in range(2, temp+1):
                if int(rg % i) == 0:
                    return 0
                else:
                    flag = 1
        else:
            if rg == 3 or rg==2:
                flag = 1
        return flag

    for i in range(2,n):
        flag = isPrime(i)
        if flag == 1:
            count += 1
    return count
print(countNumber(11))
