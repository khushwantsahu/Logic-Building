#1. Sum of the series of n terms Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.
def sum_of_series(num):
    sum = 0
    for i in range(1,num+1):
        sum += (1/i)

    return sum

answer = sum_of_series(4)
print(f'{answer:.6f}')

#2.  Finding the Most Frequent Element in an Array
def most_frequent():
    arr = [1,2,2,3,3,3]
    max_count = 0
    element = arr[0]
    freq = {}
    for i_element in arr:
        if i_element in freq:
            freq[i_element] += 1
        else:
            freq[i_element] = 1
    
        if freq[i_element] > max_count:
            max_count = freq[i_element]
            element = i_element

    print(f"\nMost frequent element is {element} come {max_count} times\n")

most_frequent()


#3.  Print the Array in Sorted Order (Ascending and Descending):
def sort_array():
    arr = [2,3,5,4,1]
    print(f"Array in ascending order :{sorted(arr)}")
    print(f"Array in descending order :{sorted(arr, reverse=True)}")

sort_array()