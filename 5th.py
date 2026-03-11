count = 1
while count <= 5 :
    print("hello")
    count += 1


 print(count)

# # print number from 1 to 100#

i = 100
while i >= 1:
    print(i)
    i -= 1

# table #
n = int(input("enter number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1
# loops#
nums = [1,4,9,25,36,49,64,81,100]
print(nums[0])
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

 # Break & continue #
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        Break
    i += 1
print("end of loop")

# # For loops#
nums = [1,2,3,4,6,7]
for val in nums:
    print(val)

nums = (1,4,9,25,36,49,64,81,100)
x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1

#Range#


for i in range(2, 10):
    print(i)
