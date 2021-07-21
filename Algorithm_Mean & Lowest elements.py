#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_ar_mean(arr):
    ar_mean = sum(arr) / len(arr)

    print('arithmetical mean:', str(ar_mean))

    my_list = []

    for i in arr:
        if i < ar_mean:
         my_list.append(i)
        return my_list

    test_array = [1, 3, 4, 5, 7, 9, 2]
    print(test_array)
    print(below_ar_mean(test_array))



#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3



my_list1 = [5, 8, 10, 20, 4, 45, 99]

my_list1.sort()

print("two lowest elements are :", *my_list1[:2])



