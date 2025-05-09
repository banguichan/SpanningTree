def generate_all_spanning_trees(graph):
    def is_tree(candidate_tree_edges):
        # Vérifie si les arêtes forment un arbre en visitant tous les nœuds
        visited = set()
        for edge in candidate_tree_edges:
            visited.add(edge[0])
            visited.add(edge[1])
        return len(visited) == len(graph)

    def generate_trees_helper(current_edges, remaining_nodes):
        if not remaining_nodes:
            if is_tree(current_edges):
                all_spanning_trees.add(tuple(sorted(current_edges)))
            return
        for node in remaining_nodes:
            for neighbor in graph[node]:
                if (node, neighbor) not in current_edges and (neighbor, node) not in current_edges:
                    new_current_edges = current_edges.copy()
                    new_current_edges.add((node, neighbor))
                    new_remaining_nodes = remaining_nodes.copy()
                    new_remaining_nodes.remove(node)
                    generate_trees_helper(new_current_edges, new_remaining_nodes)

    all_spanning_trees = set()
    nodes = list(graph.keys())
    generate_trees_helper(set(), nodes)
    return all_spanning_trees

# Exemple d'utilisation
# Remplacez cette liste d'adjacence par la représentation de votre graphe
graph = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}

all_spanning_trees = generate_all_spanning_trees(graph)

# Afficher les résultats
for i, tree in enumerate(all_spanning_trees):
    print(f"Arbre {i + 1}: {tree}")
