def check_prime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
            break
    else:
        return True

for num in range (1,101):
    if check_prime(num)==True:
        print(num)