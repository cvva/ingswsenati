# importar librerias
import matplotlib.pyplot as plt
import numpy as np

# crear los datos
x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

# generar grafico
plt.plot(x, y, 'm--')
plt.show()
