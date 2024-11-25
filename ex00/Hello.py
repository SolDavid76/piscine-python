ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)   # ['Hello', 'World!']
print(ft_tuple)  # ('Hello', 'France!')
print(ft_set)    # {'Hello', 'Paris!'}
print(ft_dict)   # {'Hello': '42Paris!'}
