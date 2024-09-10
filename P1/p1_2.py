'''
LOGIC:
First we should sort the array
left = 0 and right = 4 as per this scenario
closest sum and pair will be initialized as infinity and empty
left = 0, right = 4
Elements: arr[left] = -45, arr[right] = 30
Sum: -45 + 30 = -15

    if absolute is less than closest sum , we will update closest_sum and closest_pairs

absolute = |-15| = 15 is less than closest_sum (i..e, inf)
update closest_sum and closest_pairs

    since the sum is less than 0, increase left pointer, else decrease right pointer
    (left = 1, right = 4)

according to the second iteration, the absolute value is 10 which is less than 15. hence the closest sum and pairs will update

    but the sum is greater than 0, decrease right pointer
    (left = 1, right = 3)

'''

def closest_zero(arr):
    arr.sort()
    
    left = 0
    right = len(arr) - 1
    closest_sum = float('inf')
    closest_pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            closest_pairs = [(arr[left], arr[right])]
        elif abs(current_sum) == abs(closest_sum):
            closest_pairs.append((arr[left], arr[right]))

        if current_sum < 0:
            left += 1  # Increase from left to right
        else:
            right -= 1  # Decrease from right to left

    return closest_pairs

# Provided Input
input = [15, 5, -20, 30, -45]
output = closest_zero(input)
print("Output:", output)