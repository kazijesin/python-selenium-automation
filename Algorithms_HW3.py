#Reverse a Statement

My_list = ['everything', 'is', 'hard', 'before', 'it', 'is', 'easy']

My_list.reverse()

print(My_list)

#Permutations

import itertools

if __name__ == '__main__':
    nums = list("ABC")
    permutations = list(itertools.permutations(nums))
    print([''.join(permutation) for permutation in permutations])

#Count Characters

my_string = ("Life is beautiful")
count_v = 0
count_c = 0

for i in my_string:
    if (i == 'a', i =='e', i =='i', i == 'o',i=='u'
    or i == 'A', i =='E', i =='I', i =='O', i =='U'):
        count_v = count_v+1

else:
 count_c = count_c+ 1

print("The number of consonents in the string is:", count_c)
print("The number of vowel in the string is:", count_v)




