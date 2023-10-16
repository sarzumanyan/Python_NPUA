num = input("Enter positive number: ")


def reversed_sum_of_digits(number):
    add = 0
    for i in number:
        add += int(i)
    result = str(add)
    return result[::-1]


print(reversed_sum_of_digits(num))
