arr = [0, 3, 2, -1]

# O(n)
min = 0
for n in arr:
    if n < min:
        min = n
print(min)


min = 0
min2 = 0
for n in arr:
    if n < min:
        min = n
    elif n < min2:
        min2 = n
print(min2)


# sort the array O(nlogn)
for i, n in enumerate(arr):
    print(i, n)
    while i > 0 and arr[i] < arr[i-1]:
        tmp = arr[i]
        print('tmp', tmp)
        arr[i] = arr[i-1]
        arr[i-1] = tmp
        print(i, arr[i-1], arr[i], arr)
        i -= 1


'''
nth min -- divide and conquer O(n+n)
          l
arr = [0, 3, 2, -1]
             r
'''









# end
