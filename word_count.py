def count_distinct_characters(text):
    # Usamos un conjunto para contar caracteres únicos
    return len(set(text))

def count_distinct_words(text):
    # Dividimos el texto en palabras usando split
    words = text.split()
    # Usamos un conjunto para contar palabras únicas
    return len(set(words))

if __name__ == "__main__":
    # Leer el archivo de texto
    with open("lorem_ipsum.txt", "r", encoding="utf-8") as file:
        texto = file.read()

    # Contar caracteres distintos
    num_distinct_characters = count_distinct_characters(texto)

    # Contar palabras distintas
    num_distinct_words = count_distinct_words(texto)

    # Mostrar los resultados
    print(f"Número de caracteres distintos: {num_distinct_characters}")
    print(f"Número de palabras distintas: {num_distinct_words}")
