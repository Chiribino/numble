NUMBLE

Un juego clásico implementado en Python donde debes adivinar un número secreto basándote en pistas de aciertos y coincidencias.
📋 Descripción
Este es un juego de lógica donde el programa genera un número secreto y tú debes adivinarlo. Después de cada intento, recibirás información sobre:

Aciertos: Dígitos correctos en la posición correcta
Coincidencias: Dígitos correctos pero en posición incorrecta

🎮 Características

Configurable: Elige cuántos dígitos tendrá el número secreto (de 1 a 10)
Modo flexible: Decide si los dígitos pueden repetirse o no
Contador de intentos: Sabrás en cuántos intentos lograste adivinar
Sistema de pistas: Retroalimentación clara después de cada intento

🚀 Cómo Jugar

Ejecuta el programa:

bashpython numble.py
```

2. Sigue las instrucciones en pantalla:
   - Elige la cantidad de dígitos del número secreto
   - Decide si quieres permitir dígitos repetidos (Y/N)
   - Comienza a adivinar ingresando números

3. El juego termina cuando:
   - Adivinas el número correctamente ✅
   - Ingresas algo que no sea un número (pierdes) ❌

## 📝 Ejemplo de Juego
```
Bienvenido a NUMBLE! Tienes que adivinar un número secreto.
Elige la cantidad de cifras que quieres que tenga el número: 4
Quieres que los dígitos se puedan repetir o no? (Y/N) n

Ingresa un número: 1234
Tienes 1 aciertos y 2 coincidencias

Ingresa un número: 5678
Tienes 2 aciertos y 0 coincidencias

Ingresa un número: 5639
Ganaste! el número era 5639! Lo has adivinado en 3 intentos
🛠️ Requisitos

Python 3.x
Módulo random (incluido en la biblioteca estándar)

📦 Instalación
bashgit clone https://github.com/chiribino/numble.git
cd numble
python numble.py
🎯 Estrategia
Para ganar más rápido:

Empieza con números que te den información sobre múltiples dígitos
Usa la información de aciertos y coincidencias para eliminar posibilidades
Lleva un registro mental o escrito de tus intentos anteriores
