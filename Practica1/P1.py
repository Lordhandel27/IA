import matplotlib.pyplot as plt
from collections import Counter
import re

#Cargar texto desde archico
with open('doc2.txt', 'r', encoding='utf-8') as file:
    texto = file.read().lower()

    # Tokenización simple separando por palabras (remover símbolos)
palabras = re.findall(r'\b\w+\b', texto)

#Contar palabras
total_palabras = len(palabras)
print(f'Total de palabras: {total_palabras}')

#Calcular frecuencia de las palabras
frecuencias = Counter(palabras)

#Mostrar 10 palabras más comunes
mas_comunes = frecuencias.most_common(10)
print('Palabras más comunes:')
for palabra, freq in mas_comunes:
    print(f'{palabra}: {freq}')


#Visualizar con gráfico de barras
#Esto me lo ofreció la IA y me pareció interesante para practicar
palabras, counts = zip(*mas_comunes)
plt.bar(palabras, counts)
plt.title('Palabras más comunes')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.show()