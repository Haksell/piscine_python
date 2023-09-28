ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


class OrderedSet(set):
    def __str__(self):
        return "{" + str(sorted(self))[1:-1] + "}"


ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.discard("tutu!")
ft_set.add("Paris")
ft_set = OrderedSet(ft_set)
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
