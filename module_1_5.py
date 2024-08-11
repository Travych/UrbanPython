immutable_var = tuple = (1, True, 3, "python")
print(immutable_var)
#immutable_var[0] = 100
#print(immutable_var)
# в кортежах нельзя изменить данные, кортеж не изменяем
mutable_list = [1, 3, "F", "Python"]
print(mutable_list)
mutable_list[0] = 100
mutable_list[2] = "A"
mutable_list.reverse()
print(mutable_list)