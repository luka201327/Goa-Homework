numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even:", even)
print("Odd:", odd)
