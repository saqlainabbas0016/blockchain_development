# n = (input('Enter the number:'))
# i = 2
# prime = True
# while i <= n :
#     if n % i == 0 : 
#         prime = False
#         break
#     i += 1
# if prime : 
#     print(n, 'is prime')
# else : 
#     prime(n, 'is not prime number')



n = int(input('Enter the number: '))
i = 2
prime = True

# Handle special cases
if n <= 1:
    prime = False
else:
    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

if prime:
    print(n, 'is prime')
else:
    print(n, 'is not a prime number')

