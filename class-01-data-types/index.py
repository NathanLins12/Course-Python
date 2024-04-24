# Primitive types

milk = "leite"
volume = 2.5

print(type(milk))
print(type(volume))

print(milk)

preparation = milk
preparation2 = milk + str(1)

print(preparation)
print(preparation2)

life_cat = str(volume + 5)

print("O gato bebe " + milk)
print("E tem " + life_cat + " vidas")

print(f"O gato bebe {milk} e tem {life_cat} vidas") 

name = "Nathan"
age = 18
is_admin = False # boolean True or False

print(is_admin)
print(type(is_admin))

# Structural types (collections)

animes = ["Dragon Ball", "Jojo", "Death Note"]
        # =>     0        1         2
        # =>    -1       -2        -3

print(animes)
print(type(animes))
print(animes[0])
print(animes[1])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[-1])
print(list[-1][-1])

list[2] = False
list[3][0] = "D"
print(list)
print(len(list)) # length = tamanho

#  Tuple
tuple = ("A", 123, True)

print(type(tuple))
print(tuple[1])

#tuple[1] = 34532 # Error: tuple is immutable

print(tuple)

# Dict

dict = {
    "name": "Nathan",
    "age": 18
}

print(dict[])
print(type(dict))