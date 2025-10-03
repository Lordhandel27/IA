import random
from collections import defaultdict

def tokenizar_texto(texto):
    # Separa el texto en tokens usando espacios como delimitador
    tokens = texto.split()
    return tokens

def construir_diccionario(tokens):
    diccionario = defaultdict(list)  # clave: palabra, valor: lista de palabras siguientes
    for i in range(len(tokens) - 1):
        key = tokens[i]
        siguiente = tokens[i + 1]
        diccionario[key].append(siguiente)
    diccionario[tokens[-1]] = []  # controlar la última palabra 
    return diccionario

def generar_texto(diccionario, palabra_inicial, longitud=20):
    texto_generado = [palabra_inicial]
    palabra_actual = palabra_inicial

    for _ in range(longitud - 1):
        siguientes = diccionario.get(palabra_actual, [])
        if not siguientes:
            break
        palabra_actual = random.choice(siguientes)
        texto_generado.append(palabra_actual)

    return ' '.join(texto_generado)

# Texto de ejemplo
texto = ("Las montañas se alzaban majestuosas bajo el cielo grisáceo, cubiertas por un manto de nubes pesadas "
         "que amenazaban con descargar una tormenta inminente. El viento susurraba entre los pinos, como si "
         "contara secretos antiguos de épocas olvidadas. En la pequeña cabaña al pie de la colina, la luz titilaba "
         "débil, reflejando la lucha entre la oscuridad que se imponía y el calor que aún se resistía a abandonarla. "
         "Marta miró hacia la ventana, sintiendo un escalofrío que no provenía únicamente del frío, sino de la incertidumbre "
         "que le envolvía el alma en aquellos días.")

tokens = tokenizar_texto(texto)
diccionario = construir_diccionario(tokens)

# Pedir palabra inicial al usuario
palabra_inicial = input("Introduce la palabra inicial para generar texto: ")

# Generar y mostrar texto
texto_generado = generar_texto(diccionario, palabra_inicial, 2)
print("\nTexto generado:\n", texto_generado)