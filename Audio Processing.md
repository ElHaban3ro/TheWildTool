# The Wild Tool


## Main Ideas.
Técnicas para el procesamiento de audio:
- Segmentación. (La idea que tengo desde el inicio y posiblemente la más viable)
- Clasificar. (idk)
- Extracción de características. (Patrones?)



## Utilziaciones del analisis de audio.
- Speaker Verification (la que nosotros necesitamos)
- Segmentación de voces. Para separar la voz de otros sonidos o voces.
- Speaker detection (se encuentra a una persona especifica hablando y se detecta si es una persona X persona propuesta)
- Analisis de sentimiento (para extender)
- Speech Synthesis (texto a audio)



## Técnicas de muestreo.
-  Muetreo periodico.


## Teorema de muestreo.
- En este teorema plantea transformar el audio al doble de su frecuencia original, para que el trabajo sea más facil durante el entrenamiento. (y luego normalizar entre -1 y 1)

---
---


## Preparación de datos.
1.  Para comenzar a trabajar con los datos es importante tengamos los audios mismos.

2. Obtener el espectograma del audio. (Con la transformada de Fourier o con la (idealmente) Transformada rápida de Fourirer.)

3. Coeficientes de Mel: Con esto, es posible extraer caracteristicas por medio del espectrograma. Este método hace un fuerte enfasis en las frecuencias que suelen tener las voces.