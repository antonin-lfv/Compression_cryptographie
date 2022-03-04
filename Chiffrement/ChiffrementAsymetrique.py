import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np
import sympy as sp
from math import isqrt
from tqdm import tqdm  # progress bar

def est_premier(n) -> bool:
    """Test de primalité de n"""
    if n < 2:
        return False
    else:
        for i in [2] + [j for j in range(3, isqrt(n), 2)]:
            if n % i == 0:
                return False
    return True

def nombre_premier_entre_a_et_b(b, a=0):
    # return sum([sp.isprime(i) for i in range(a, b)])
    return sum([est_premier(i) for i in range(a, b)])


if __name__ == '__main__':
    fig = go.Figure()
    x = [i for i in range(2, 500)]
    y = [1 / np.log(i) for i in x]
    y_prime = [nombre_premier_entre_a_et_b(b=i, a=0) / i for i in tqdm(x)]
    fig.add_scatter(y=y, x=x, mode='lines', name="1/log(x)")
    fig.add_scatter(y=y_prime, x=x, mode='lines', name="pi(x)/x")
    fig.update_yaxes(range=[0, 0.6])
    plot(fig)