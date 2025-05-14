def subsequence(ind, arr, k):
    if k == 0:
        return True
    if k < 0 or ind == len(arr):
        return False
    # Include current element
    path1 = subsequence(ind + 1, arr, k - arr[ind])
    if path1:
        return True
    # Exclude current element
    path2 = subsequence(ind + 1, arr, k)
    return path2

def subsequentsum():
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter target sum (k): "))
    ind = 0
    result = subsequence(ind, arr, k)
    print("Subsequence with given sum exists:" if result else "No such subsequence exists.")

# Example call
print(subsequentsum())
