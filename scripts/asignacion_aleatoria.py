# asignacion_aleatoria.py: 
# asignación aleatoria del experimento (sección 5)

import numpy as np
import pandas as pd

# Las 10 tiendas del experimento y las 4 semanas de medición
# (10 tiendas x 4 semanas = 40 unidades tienda-semana)
tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro",
           "Guayaquil Norte", "Cuenca Centro", "Cuenca Sur",
           "Ambato Centro", "Manta", "Loja", "Machala"]
semanas = [1, 2, 3, 4]

# Generador de números aleatorios con semilla fija
rng = np.random.default_rng(1234597)

# SORTEO: para cada tienda se elige al azar con qué ubicación empieza
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))

# Construcción del diseño: una fila por tienda y semana
filas = []
for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    for s in semanas:
        # Impar: ubicación sorteada y la par: la contraria (2 semanas de cada una)
        filas.append({
            "tienda": tienda,
            "semana": s,
            "ubicacion": cond if s % 2 == 1 else otra,
        })

# Se convierte la lista en una tabla para verla y contarla
diseno = pd.DataFrame(filas)
print(diseno)

print(diseno["ubicacion"].value_counts())