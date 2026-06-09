nums = list(map(int, input("Enter list elements: ").split()))

biggest = nums[0]

for i in range(1, len(nums)):
    if nums[i] > biggest:
        biggest = nums[i]

print("Largest Number =", biggest)
