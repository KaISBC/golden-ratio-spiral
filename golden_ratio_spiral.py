import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc  # Corretto import da patches

def draw_golden_spiral(n_rectangles=10):
    """Disegna una spirale basata sulla proporzione aurea."""
    phi = (1 + np.sqrt(5)) / 2  # Proporzione aurea
    width, height = 1, 1 / phi

    # Inizializza figure
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis('off')

    # Coordinate iniziali
    x, y = 0, 0

    for i in range(n_rectangles):
        # Disegna il rettangolo
        rect = plt.Rectangle((x, y), width, height, edgecolor="black", facecolor="none")
        ax.add_patch(rect)

        # Disegna un arco per la spirale
        theta1 = i * 90
        theta2 = theta1 + 90
        arc = Arc((x + width, y), width * 2, height * 2, theta1=theta1, theta2=theta2, color="blue")
        ax.add_patch(arc)

        # Aggiorna le dimensioni per il prossimo rettangolo
        if i % 2 == 0:
            x += width
            width, height = height, width / phi
        else:
            y += height
            width, height = height / phi, width

    # Limiti del grafico
    ax.set_xlim(-1, 1 + n_rectangles)
    ax.set_ylim(-1, 1 + n_rectangles)

    plt.title(f"Spirale basata sulla proporzione aurea con {n_rectangles} rettangoli", fontsize=16)
    plt.show()

if __name__ == "__main__":
    draw_golden_spiral(12)
