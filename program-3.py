a=int(input("Enter the number:"))

if a % 2==0:
    a -= 1

odd_num = [2*i + 1 for i in range(a)]


print(" , ".join(map(str,odd_num)))