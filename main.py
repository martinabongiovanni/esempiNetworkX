import networkx as nx
from dataclasses import dataclass
import math

@dataclass
class Voto:
    punti: int
    nome: str

    def __hash__(self):
        return hash((self.punti, self.nome))

    def __eq__(self, other):
        return self.nome == other.nome


grafo = nx.Graph()         # grafo semplice
grafo_dir = nx.DiGraph()   # grafo diretto

# aggiungo nodi: solitamente i nodi sono omogenei (i nodi sono tutti dello stesso tipo)
grafo.add_node(1) # aggiungo un intero
grafo.add_node("Due") # aggiungo una stringa
grafo.add_node(Voto(25, "TDP")) # aggiungo un oggetto di tipo custom
grafo.add_node(math.cos) # aggiungo una funzione

print(grafo.nodes)
print(grafo.edges)
print()

grafo_dir.add_node(1) # aggiungo un intero
grafo_dir.add_node("Due") # aggiungo una stringa
grafo_dir.add_node(Voto(25, "TDP")) # aggiungo un oggetto di tipo custom
grafo_dir.add_node(math.cos) # aggiungo una funzione

grafo_dir.add_edge("Due", 1, weight=0.9, arbitrary_attr = "ciao") # arco pesato
print(grafo_dir.nodes())
print(grafo_dir.edges())
print(f"attributi dell'edge ('Due', 1): {grafo_dir.get_edge_data('Due', 1)}") # il peso è un dizionario

nbunch = [i for i in range(10)]
grafo_dir.add_nodes_from(nbunch) # NB: il nodo 1 è già dentro, quindi non viene duplicato ma ignorato

ebunch = [(4,6), (8,1), (2,9)] # NB: se aggiungendo gli archi metto nodi che non esistono (es. (2,50)), questi vengono aggiunti lo stesso. Grande fonte di errore !!!
grafo_dir.add_edges_from(ebunch)

print(grafo_dir.nodes)
print(grafo_dir.edges)
