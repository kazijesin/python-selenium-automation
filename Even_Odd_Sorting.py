#Your input is an array of integers, and you have to reorder its entries
# so that the even entries appear first. You are required to solve it without allocating
# additional storage (operate with the input array).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def even_odd(arr):
    even = 0
    odd = len(arr) - 1

    while even < odd:
        if arr[even] % 2 == 0:
            even += 1
        else:
            if arr[odd] % 2 == 0:
                arr[odd], arr[even] = arr[even], arr[odd]
                even += 1
                odd -= 1
            else:
                odd -= 1

    return arr


print(even_odd([1, 5, 2, 0, 3, 4, 5, 7, 8, 1, 10, 6]))


#Write a program that takes as input an array of digits encoding a nonnegative decimal integer D
# and updates the array to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def incrementinteger(a):
    n = len(a)

    a[n - 1] += 1
    carry = a[n - 1] / 10
    a[n - 1] = a[n - 1] % 10


    for i in range(n - 2, -1, -1):
        if (carry == 1):
            a[i] += 1
            carry = a[i] / 10
            a[i] = a[i] % 10

    if (carry == 1):
        a.insert(0, 1)


integer= [7, 8, 9, 9]

incrementinteger(integer)

for i in range(0, len(integer)):
    print(integer[i], end=" ")