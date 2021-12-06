import numpy as np
WIDTH_TOTAL = 750
COLOR_EMPTY = "gray"
FACTEUR_VIDE = 10  # nb case / facteur blanc cases blanches
# COLOR = ["blue", "red", "green", "yellow",  'pink']

COLOR = [list(np.random.choice(range(255),size=3)) for _ in range(10)]
COLOR = [f'#{e[0]:02x}{e[1]:02x}{e[2]:02x}' for e in COLOR]