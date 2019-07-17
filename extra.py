class Grafo:
    vertices = []
    def __addVertices__(self, vertices):
        self.vertices = self.vertices + vertices

class Vertice:
    adjacentes = []
    estoque = 0
    def __init__(self, estoque):
        self.estoque = estoque
    def __addAdjacentes__(self, adjacentes):
        self.adjacentes = self.adjacentes + adjacentes

# Método que utilizei na prova.
def enviaDijkstra(grafo, origem, destino, quantidade):
    # Estabeleci que só é possível enviar sacas por uma adjacência, logo não é possível enviar 10 por uma aresta e 5 por outra saíndo do mesmo vértice.
    abertos = grafo.vertices
    # Enquanto existir vértice aberto
    while abertos != []:
        u = None
        # Escolho o vértice aberto u que tem o maior estoque
        for vertice in abertos:
            if u == None:
                u = vertice
            elif vertice.estoque > u.estoque:
                u = vertice
        # Fecho u
        abertos.remove(u)
        # Para todo vértice aberto v na adjacência de u
        for v in u.adjacentes:
            if v[0] in abertos:
                sacas = 0
                if u.estoque < v[1]:
                    sacas = u.estoque
                else:
                    sacas = v[1]
                # Se a quantidade de sacas que posso passar no caminho for maior que o estoque de v, atualizo o estoque de v
                if sacas > v[0].estoque:
                    v[0].estoque = sacas
    # Analiso se a demanda foi atendida, se não foi digo quantas sacas foi possível enviar
    if origem.estoque < quantidade and destino.estoque > origem.estoque:
        return "Só é possível enviar " + str(origem.estoque) + " sacas."
    elif destino.estoque < quantidade:
        return "Só é possível enviar " + str(destino.estoque) + " sacas."
    else:
        return "Demanda atendida."

# Método que o professor pedia na prova
def envia(origem, destino, quantidade):
    sacasrestantes = quantidade
    estoqueoriginal = origem.estoque
    for u in origem.adjacentes:
        if sacasrestantes > 0 and origem.estoque > 0:
            visita(u[0], u[1], destino)
            sacasrestantes -= u[1]
            origem.estoque -= u[1]
    if estoqueoriginal < quantidade and destino.estoque > estoqueoriginal:
        return "O estoque da origem não comporta a demanda, porém é possível enviar " + str(estoqueoriginal) + " sacas."
    elif destino.estoque < quantidade:
        return "A demanda não pode ser atendida, só é possível enviar " + str(destino.estoque) + " sacas."
    else:
        return "Demanda atendida."

def visita(u, quantidade, destino):
    u.estoque += quantidade
    if u != destino:
        for v in u.adjacentes:
            if u.estoque < v[1]:
                visita(v[0], u.estoque, destino)
                u.estoque = 0
            else:
                visita(v[0], v[1], destino)
                u.estoque -= v[1]




grafo = Grafo()
A = Vertice(30)
B = Vertice(0)
C = Vertice(0)
D = Vertice(0)
E = Vertice(0)
F = Vertice(0)
G = Vertice(0)
H = Vertice(0)
I = Vertice(0)
J = Vertice(0)
K = Vertice(0)
L = Vertice(0)
M = Vertice(0)
N = Vertice(0)
O = Vertice(0)
P = Vertice(0)
Q = Vertice(0)
R = Vertice(0)
S = Vertice(0)
T = Vertice(0)
A.__addAdjacentes__([(B, 10), (H, 5)])
B.__addAdjacentes__([(C, 10), (G, 15)])
C.__addAdjacentes__([(D, 10), (F, 25)])
D.__addAdjacentes__([(E, 20)])
E.__addAdjacentes__([(F, 15)])
F.__addAdjacentes__([(G, 20), (J, 10)])
G.__addAdjacentes__([(K, 15)])
H.__addAdjacentes__([(G, 10)])
I.__addAdjacentes__([(J, 20), (M, 10)])
J.__addAdjacentes__([(N, 10)])
K.__addAdjacentes__([(J, 10), (O, 20)])
L.__addAdjacentes__([(K, 10), (P, 20)])
M.__addAdjacentes__([(N, 10), (Q, 5)])
N.__addAdjacentes__([(R, 5)])
O.__addAdjacentes__([(S, 25)])
P.__addAdjacentes__([(O, 10), (S, 25)])
Q.__addAdjacentes__([(D, 20)])
R.__addAdjacentes__([(S, 10)])
S.__addAdjacentes__([])
T.__addAdjacentes__([(S, 10)])
grafo.__addVertices__([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T])

print(envia(A, S, 25))