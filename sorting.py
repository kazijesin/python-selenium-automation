#Selection Sort
#Implement the selection sort algorithm that is sorting in descending order.

def sortList(array):
	n = len(array)

	for j in range(n):
		minimum = j

		for i in range(j + 1, n):
			if array[i] > array[minimum]:
				minimum = i

		array[j], array[minimum] = array[minimum], array[j]


random_list_of_nums= [13, 9, 12, 8, 3, 20, 11]
sortList(random_list_of_nums)
print(random_list_of_nums)

#Bubble Sort
#Implement the bubble sort algorithm that is sorting in descending order.


def bubbleSort(arr):
	n = len(arr)


	for i in range(n):


		for j in range(0, n - i - 1):


			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print(arr)

#Insertion Sort
#Implement the insertion sort algorithm that is sorting in descending order.

def insertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i]


		j = i - 1
		while j <= 0 and key > arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

