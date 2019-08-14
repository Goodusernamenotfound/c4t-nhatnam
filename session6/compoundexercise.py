favourites = ["Ace Combat", "Sabaton", "music"]
print(*favourites, sep=" | ")
delet=str(input("pick item to delet: "))
favourites.remove(delet)
print(*favourites, sep=" | ")