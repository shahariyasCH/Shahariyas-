numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))

Dict={i:0 for i in range(1,10)}

for num in numbers:
    for i in range(1,10):
        if num%i==0:
            Dict[i]+=1

print(Dict)
