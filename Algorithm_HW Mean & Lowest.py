import statistics

# list of positive integer numbers
my_list = [1, 3, 4, 5, 7, 9, 2]

x = statistics.mean(my_list)

# Printing the mean
print("Mean is :", x)


def cal_mean(num):
    sum_num = 0
    for x in num:
        sum_num = sum_num + x

    avg = sum_num / len(num)
    return avg

print("The mean is", cal_mean([5,18,25,3,41,15]))

#find smallest

my_list1 = [5, 8, 10, 20, 4, 45, 99]

my_list1.sort()

print("Smallest element is:", *my_list1[:1])

#find smallest

a=[18, 52, 23, 41, 32]

smallest = a[0] if a else None

for i in a:
    if i<smallest:
	    smallest=i

print("Smallest element is: ", smallest)