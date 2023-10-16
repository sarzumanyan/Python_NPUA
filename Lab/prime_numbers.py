def prime_numbers(num):
    if num>=2:
        print(2)
    if num>=3:
        print(3)
    for n in range(4,num+1):
        if is_prime(n):
            print(n)


def is_prime(num):
    i=2
    divisors=[i]
    while i<=num**0.5:
        if num%i==0:
            return False
        i+=1
        divisors.append(i)
    #print(divisors)
    return True

prime_numbers(35)