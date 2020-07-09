''' QUESTION:
    Just Starting Info : This problem was recently asked by Google.
    Given Difficulty : EASY
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Challenge : Can you do this in one pass?


SOLUTION'''
# Solution 1
def twoNumberSum(arr,k):#Don't worry this is my personal naming way, nothing to get scared. It's called camelCasing btw.
    hash = []
    hash.append(arr[0])
    for i in range(1,len(arr)):
        if abs(k-arr[i]) in hash:
            return True
        hash.append(arr[i])   # hash+=k-arr[i] also works
        #print(hash)
    else:
        return False
arr = [10, 15, 3 ,7]
k = 17
print(twoNumberSum(arr,k))
# The above solution uses single iteration as per challenge but uses o(n) space too
# Here is another which doesn't make use of any extra space
# Solution 2
# And below is also my preferred solution

def twoNumberSum(arr, k):
    for i in arr:
        if k-i in arr:
            return True
    else:
        return False

arr = [10, 15, 3, 7]
k = 22
print(twoNumberSum(arr, k))
# The above can be modified little to even print those numbers which add upto k. But I am not going there as it
# is not my question. how about You give it a try.
