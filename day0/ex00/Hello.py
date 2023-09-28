ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.discard("tutu!")
ft_set.add("Paris")
# sets in Python are not ordered, so we need to sort it before printing
ft_set = "{" + str(sorted(ft_set))[1:-1] + "}"
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
