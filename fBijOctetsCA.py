import plotly.graph_objects as go
from plotly.offline import plot
# pip install plotly

class fBijOctetsCA(object):
    "Une classe abstraite de bijection de [0..255]"

    def __init__(self):
        pass

    def __repr__(self):
        raise NotImplementedError

    def __call__(self, octet):
        """Renvoie l’image de octet par la bijection"""
        raise NotImplementedError

    def valInv(self, octetC):
        "Renvoie l’antécédent de octetC"
        raise NotImplementedError

    def plot_diffusion(self, monBin):
        raise NotImplementedError