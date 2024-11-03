immutable_var_ = 1, 2, 3, 'String'
# immutable_var[0] = 100 кортеж неизменяемый тип данных, выдаст ошибку!
immutable_var_2 = ([1, 2], 'string', 3,)

mutable_list = [1, 2, 3, 'String']
mutable_list2 = [1, 2, 3, 'String']
mutable_list2[0] = 200

print(immutable_var_)
print((immutable_var_2))
print(mutable_list)
print(mutable_list2)
