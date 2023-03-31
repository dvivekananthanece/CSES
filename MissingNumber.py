total_number = int(input())
all_numbers = list(map(int, input().split()))
all_numbers.sort()
try:
    for i in range(1,total_number+1):
        if all_numbers[i-1] != i:
            print(i)
            break
except:
    print(total_number)

