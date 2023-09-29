nums = input("Input the numbers of list: ")
nums_list = nums.split(" ")


def classify_numbers(nums_list):
    even_nums = []
    odd_nums = []
    for item in nums_list:
        item = int(item)
        if item % 2 == 0:
            even_nums.append(item)
        else:
            odd_nums.append(item)
    return "Even numbers: {0}\nOdd numbers: {1}".format(even_nums, odd_nums)


print(classify_numbers(nums_list))
