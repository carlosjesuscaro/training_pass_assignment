def foo(x):
    x[0] = 99
    print(f'First element of the list: {id(x[0])}')

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

print(id(foo))
print(id(my_list))
print(f'First element of the list OUT of the function: {id(my_list[0])}')

print(f'IDs from an integer')
a = 94
print(id(a))
a = 82
print(id(a))

print(f'Another list IDs:')
another_list = [23, 54, 49]
print(id(another_list))
print(id(another_list[0]))
another_list = [3, 54, 29]
print(id(another_list))
print(id(another_list[0]))
qq = [23, 54, 49]
print(id(qq))
qq.append(50)
print(id(qq))
qq[0] = 101
print(id(qq))
qq[0] = 'a'
qq[1] = 'b'
qq[2] = 'c'
print(id(qq))

