my_dict = {"Evgeniy": 1981, "Anna": 1990, "Potap": 2000, "Alla": 1965}
print(my_dict)
print(my_dict["Evgeniy"])
print(my_dict.get("Andrey", "Такого ключа нет"))
my_dict.update({"Andrey": 1971, "Sveta": 1954})
a = my_dict.pop("Potap")
print(a)
print(my_dict)
#Множества
my_set = {1, 1, 1, 2, 2, True, "Python", 3, 3, 5, 5, 7, 7, }
print(my_set)
my_set.update({"C++", 44, (65, 32,89)})
print(my_set)
my_set.discard(7)
print(my_set)
