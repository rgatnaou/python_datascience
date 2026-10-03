ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.append("World!")

#we cannot append to a tuple because it is immutable
ft_tuple = ft_tuple[:1] + ("Morocco!",)

ft_set.remove("tutu!")

ft_set.add("Khouribgha!")

ft_dict["Hello"] = "Morrocco!"

print(__name__)
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)