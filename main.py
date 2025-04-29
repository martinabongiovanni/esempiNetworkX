import networkx as nx
from dataclasses import dataclass
import math

from networkx.classes import subgraph


@dataclass
class Voto:
    punti: int
    nome: str

    def __hash__(self):
        return hash((self.punti, self.nome))

    def __eq__(self, other):
        return self.nome == other.nome
# Un grafo è essenzialmente un dizionario di dizionari di dizionari. Dall'esterno all'interno ho:
# diz superficiale:
#               chiavi=nodi, valore= dizionario di nodi raggiungibili dal nodo chiave;
# diz intermedio, per ogni nodo raggiungibile dal precedente nodo chiave, avrò:
#               chiave=nodo target, valore= dizionario di attributi relativi al nodo;
# diz interno, per ogni attributo del nodo target, avrò:
#               chiave=attributo, valore=valore associato all'attributo

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

grafo_dir.add_edge("Due", 1, weight=0.9, arbitrary_attr = "ciao")
print(grafo_dir.nodes())
print(grafo_dir.edges())
print(f"attributi dell'edge ('Due', 1): {grafo_dir.get_edge_data('Due', 1)}")



nbunch = [i for i in range(10)]
grafo_dir.add_nodes_from(nbunch) # NB: il nodo 1 è già dentro, quindi non viene duplicato ma ignorato

# Aggiungo gli archi che collegano i nodi del grafo ORIENTATO come tuple (nodo di partenza, nodo di arrivo)
ebunch = [(4, 6), (8, 1), (11, 9)]
# NB: se aggiungendo gli archi metto nodi che non esistono (es. (2,50)), questi vengono aggiunti lo stesso
# perché viene creato anche un nuovo nodo in automatico. Grande fonte di errore !!!
grafo_dir.add_edges_from(ebunch)

print(grafo_dir.nodes) # restituisce la lista dei nodi
print(grafo_dir.edges) # restituisce la lista degli archi

print(grafo_dir.get_edge_data("Due", 1))

print(grafo_dir[4]) # accedo al dizionario grafo e stampo tutti i valori associati alla chiave 4
                    # ottengo quindi un altro dizionario con chiavi i nodi vicini di 4 e valore
                    # un dizionario contenente come chiavi gli attributi del nodo e valore il
                    # valore associato a quel determinato attributo
print(grafo_dir["Due"])
print(grafo_dir["Due"][1]) # Accedo al diz degli attributi dell'arco che collega il nodo "Due" al nodo 1

# Stampo tutti i nodi del grafo
for n in grafo_dir:
    print (n)
print("-----------------")
# Stampo tutti i nodi vicini al nodo "Due"
for nbr in grafo_dir["Due"]:
    print(nbr)
print("-----------------")
# Stampo la lista dei successori (e poi dei predecessori) di un nodo
print([s for s in grafo_dir.successors("Due")])
print([p for p in grafo_dir.predecessors("Due")])

print("-----------------")
# metodo subgraph: prende come parametri un grafo e una lista di nodi e
# genera un sotto-grafo contenente solo i nodi passati nel parametro lista
print(subgraph(grafo_dir, [4, "Due", 1, 9]))