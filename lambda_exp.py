x = lambda a,b : a * b
print(x(5 , 6))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#title method is used to convert every word of first letter into uppercase

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('salman raj', 'veeranki'))

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))