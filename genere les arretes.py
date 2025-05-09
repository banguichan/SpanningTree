#graph = [(9,8),(3,7),(7,9),(1,8),(4,6),(6,8),(3,9)]
#ponderation=[(21),(69),(33),(10),(55),(16),(3)]
k=500
import random
from graphe import *
graphe_aleatoire = GrapheAleatoire(nombre_de_noeuds=5, probabilite=0.3)
graph = graphe_aleatoire.aretes
ponderation = graphe_aleatoire.nombres_aleatoires
print(graph)
print(ponderation)

"""
    FONCTIONS ANNEXES
                        """

def update_perso(destination_set, source_set):
    for element in source_set:
        destination_set.add(element)

#renvoie le nombre de points                      
def nombre_points(graph):
    sommets = set()#verifie qu il n y a pas de doublons
   
    for arrete in graph:
        update_perso(sommets, set(arrete))#on ajoute les sommets dans les arrete qu on a pas deja vu
   
    return len(sommets)

#renvoie la liste des points
def liste_points(graph):
     sommets = set()
     
     for arrete in graph:
         update_perso(sommets, set(arrete))
     
     return sommets
     
def min_longeur(len1, len2):
    return len1 if len1 < len2 else len2

def zip_perso(iterable1, iterable2):
    min_len = min_longeur(len(iterable1), len(iterable2))
    return [(iterable1[i], iterable2[i]) for i in range(min_len)]

def sum_perso(iterable):
    result = 0
    for element in iterable:
        result += element
    return result

def enumerate_perso(iterable, start=0):
    result = []
    for i in range(len(iterable)):
        result.append((i + start, iterable[i]))
    return result




"""
    FONCTIONS PRINCIPALES
                          """
def genere_ensemble_arrete(graph):
    all_edges = set(graph)
    num_edges = len(all_edges)

    stocks = []
    for i in range(2 ** num_edges):
        stock = set()
        for j in range(num_edges): 
            if (i // (2 ** j)) % 2 == 1:
                stock.add(tuple(list(all_edges)[j]))
        stocks.append(stock)
    return stocks


def nombre_arrete(stocks, num_edges):
    return [stock for stock in stocks if len(stock) == nombre_de_points - 1]

def calculer_poids(arbre, ponderation, edge_weights):
    poids_total = sum_perso(edge_weights[edge] for edge in arbre)
    return poids_total
   
def arbre_couvrant(nombre_arrete, liste_point, ponderation): 
    edge_weights = {edge: weight for edge, weight in zip_perso(graph, ponderation)}
    arbres_filtrés = []

    for arbre in nombre_arrete:
        sommets_arbre = set(point for arrete in arbre for point in arrete)

        # Vérifie si l'arbre couvrant contient tous les sommets
        if liste_point == sommets_arbre:
            poids_arbre = calculer_poids(arbre, ponderation, edge_weights)
            arbres_filtrés.append((arbre, poids_arbre))

    return arbres_filtrés
                         

def couvrant_moin_k(arbres_couvrant, k):
    for _, poids in arbres_couvrant:
        if poids < k:
            return True
    return False







"""
    SIMPLIFICATION POUR PRINT
                              """
nombre_de_points = nombre_points(graph)

stocks = genere_ensemble_arrete(graph)

nbr_arrete = nombre_arrete(stocks, len(set(graph)))

liste_point= liste_points(graph)

arbres_couvrant = arbre_couvrant(nbr_arrete, liste_point, ponderation)






"""
    LES AFFICHAGES
                    """

print(f"Le graphe a {nombre_de_points} points différents.")

for i, stock in enumerate_perso(stocks, start=1):
    print(f"Sous-ensemble d'arêtes {i}: {stock}")

for i, stock in enumerate_perso(nbr_arrete, start=1):
    print(f"Sous-ensemble d'arêtes {i}: {stock}")

for i, (arbre, poids) in enumerate_perso(arbres_couvrant, start=1):
    print(f"Arbre couvrant {i}: {arbre}, Poids: {poids}")

if arbres_couvrant !=[]:
    print("Il existe un arbre couvrant")
else:
    print("il n existe pas d arbre couvrant")
   
if couvrant_moin_k(arbres_couvrant, k):
    print(f"Au moins un arbre couvrant a un poids inférieur à {k}.")
else:
    print(f"Aucun arbre couvrant n'a un poids inférieur à {k}.")
