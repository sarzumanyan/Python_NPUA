

def sum_of_elements(numbers, exclude_negative=False):
    sum=0
    for item in numbers:
        item=int(item)
        if item<0 and exclude_negative:
            continue
        else:
            sum+=item
    return "Sum of elements is " + str(sum)


nums=input("Input space-seperated numbers: ")
numbers=nums.split()
answer=input("Do you want to exclude negative numbers?\n")
if answer.lower()=="yes":
    print(sum_of_elements(numbers,exclude_negative=True))
else:
    print(sum_of_elements(numbers))
