import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

# https://www.miximum.fr/blog/cryptographie-courbes-elliptiques-ecdsa/

if __name__ == '__main__':

    # plotly

    fig = go.Figure()
    x = np.linspace(-2, 6, 1000)

    for x_val in x:
        fig.add_scatter(x=[x_val], y=[abs((x_val**3+7)**(1/2))], marker=dict(color='blue', size=2))
        fig.add_scatter(x=[x_val], y=[-1*abs((x_val**3+7)**(1/2))], marker=dict(color='blue', size=2))
    fig.update_layout(showlegend=False)
    plot(fig)



    # matplotlib

    import matplotlib.pyplot as plt

    x = np.linspace(-1.999, 6, 50)
    y1 = np.sqrt(x ** 3 + 7)
    y2 = -np.sqrt(x ** 3 + 7)

    plt.plot(x, y1, x, y2)
    plt.show()