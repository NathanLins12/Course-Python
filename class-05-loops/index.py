# loops

print("start")

count = 0 
while count < 10:
    count += 1
    print(count)

print("end")


musics = ["bateu 20H", "Time", "Clocks", "Menina Veneno"]

index_music = 0
while index_music < len(musics):
    print(musics[index_music])
    index_music += 1

for i in range(0, 11, 2):
    print(i)

for music in musics:
    print(music)

letters = [
    ["a", "b", "c"],
["a", "b", "c"]
]

for array in letters:
    for letter in array:
        print(letter)