import random

class GrapheAleatoire:
    def __init__(self, nombre_de_noeuds, probabilite):
        self.nombre_de_noeuds = nombre_de_noeuds
        self.probabilite = probabilite
        self.graphe = self.generer_graphe()
        self.aretes = self.generer_aretes()
        self.nombres_aleatoires = self.generer_nombres_aleatoires()

    def generer_graphe(self):
        graphe = {}
        visited = set()
        stack = []

        # Start with a random node
        start_node = random.randint(0, self.nombre_de_noeuds - 1)
        stack.append(start_node)

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                if node not in graphe:
                    graphe[node] = []

                # Connect with other nodes based on the probability
                for j in range(self.nombre_de_noeuds):
                    if j != node and (random.random() < self.probabilite or j not in graphe):
                        stack.append(j)
                        graphe[node].append(j)
                        graphe[j] = [node]

        return graphe

    def afficher_graphe(self):
        for noeud, voisins in self.graphe.items():
            print(f"Noeud {noeud}: {voisins}")

       
    def generer_aretes(self):
        aretes = []

        for noeud, voisins in self.graphe.items():
            for voisin in voisins:
                edge = tuple(sorted((noeud, voisin)))
                aretes.append(edge)

    # Remove duplicate edges by converting the list to a set and back to a list
        aretes = list(set(aretes))

        return aretes
       
    def afficher_aretes(self):
        print("Liste de toutes les arêtes:")
        print(self.aretes)

                 
    def generer_nombres_aleatoires(self):
        return [random.randint(1, 100) for _ in range(len(self.aretes))]
       
    def afficher_nombres_aleatoires(self):
        print("Liste d'entiers aléatoires :")
        print(self.nombres_aleatoires)

    def parcour_en_profondeur(self, start_noeud):
        visited = set()
        traversal_path = []

        def dfs(noeud):
            if noeud not in visited:
                traversal_path.append(noeud)
                visited.add(noeud)
                for neighbor in self.graphe.get(noeud, []):
                    dfs(neighbor)

        dfs(start_noeud)
        return traversal_path
                 
#graphe_aleatoire = GrapheAleatoire(nombre_de_noeuds=5, probabilite=0.3)
#graphe_aleatoire.afficher_graphe()
#graphe_aleatoire.afficher_aretes()
#graphe_aleatoire.afficher_nombres_aleatoires()
#traversal_result = graphe_aleatoire.parcour_en_profondeur(0)
#print("parcour en profondeur:", traversal_result)



