try:
    with open("class-06-files/files/films.txt", "r", encoding="utf8") as films, \
          open("class-06-files/files/upper_films.txt", "w", encoding="utf8") as upper_films:
        
        for film in films:
            upper_films.write(film.upper())

except FileNotFoundError:
    print("arquivo não encontrado")