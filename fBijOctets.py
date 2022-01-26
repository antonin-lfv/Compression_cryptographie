from fBijOctetsCA import *
from Binaire603 import *
from arithmetiquedansZnZ import *


class fBijParDecallage(fBijOctetsCA):

    def __init__(self, decalage):
        super().__init__()
        self.decalage = decalage

    def __repr__(self):
        return f'fBijParDecallage({self.decalage})'

    def __call__(self, octet):
        """Renvoie l’image de octet par la bijection"""
        return (octet + self.decalage) % 256

    def valInv(self, octetC):
        "Renvoie l’antécédent de octetC"
        return (octet - self.decalage) % 256

    def plot_diffusion(self, monBin: Binaire603):
        lx = monBin
        ly_code = list(map(lambda x: fBijParDecallage(self.decalage).__call__(x), monBin))
        ly_origine = monBin
        lY_difference = [i - j for i, j in zip(ly_code, ly_origine)]
        fig = go.Figure()
        fig.add_scatter(x=lx, y=ly_code, mode='markers+lines', marker=dict(color='red'), line=dict(width=1),
                        name='octets codés')
        fig.add_scatter(x=lx, y=ly_origine, mode='markers+lines', marker=dict(color='blue'), line=dict(width=1),
                        name='octets d\'origine')
        fig.add_scatter(x=lx, y=lY_difference, mode='lines', line=dict(width=1, color='green', dash='dash'),
                        name='différence entre codé et origine')
        fig.update_layout(title=f"Chiffrement par décalage de {self.decalage}")
        plot(fig)


class fBijParAffine(fBijOctetsCA):

    def __init__(self, a, b):
        super().__init__()
        self.a = ElmtZnZ(a, 256).element
        assert ElmtZnZ(a, 256).estInversible()
        self.b = ElmtZnZ(b, 256).element

    def __repr__(self):
        return f'Chiffrement_affine({self.a},{self.b})'

    def __call__(self, octet):
        """Renvoie l’image de octet par la bijection"""
        return ElmtZnZ(element=self.a * octet + self.b, n=256).element

    def valInv(self, octetC):
        "Renvoie l’antécédent de octetC"
        return int(((octet - self.b) * ElmtZnZ(element=self.a, n=256).inverse()).element)

    def plot_diffusion(self, monBin: Binaire603):
        lx = monBin
        ly_code = list(map(lambda x: fBijParAffine(self.a, self.b).__call__(x), monBin))
        ly_origine = monBin
        lY_difference = [i-j for i, j in zip(ly_code, ly_origine)]
        fig = go.Figure()
        fig.add_scatter(x=lx, y=ly_code, mode='markers+lines', marker=dict(color='red'), line=dict(width=1),
                        name='octets codés')
        fig.add_scatter(x=lx, y=ly_origine, mode='markers+lines', marker=dict(color='blue'), line=dict(width=1),
                        name='octets d\'origine')
        fig.add_scatter(x=lx, y=lY_difference, mode='lines', line=dict(width=1, color='green', dash='dash'),
                        name='différence entre codé et origine')
        fig.update_layout(title=f"Chiffrement affine avec {self.a}x + {self.b}")
        plot(fig)


if __name__ == '__main__':
    monBin = Binaire603([11, 18, 1, 19, 12, 7, 21])

    # Décalage
    # fBijParDecallage(decalage=2).plot_diffusion(monBin)

    # Affine
    fBijParAffine(a=3, b=4).plot_diffusion(monBin)