'''10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
program:
# Input: Read the list elements as a single line of space-separated integers
elements = list(map(int, input().split()))

# Sort the list
elements.sort()

# Output: Print the sorted list
print(" ".join(map(str, elements)))

'''

