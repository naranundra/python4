# n too hvtelh bvh anhnii too oloh
n = int(input())
for number in range(1, n+1):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count+=1
    if count == 2:
        print(number)