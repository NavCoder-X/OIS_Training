from graphviz import Digraph,Graph

DELIMITER = "-"

def maze_to_graph(filename):
    with open(filename, 'r') as file:
        # converto in una matrice
        n, m = map(int, file.readline().split())
        maze = [line.strip() for line in file]
        maze = [list(row.split(" ")) for row in maze]
        for i in range(n):
            for j in range(m):
                print(maze[i][j], end=' ')
            print()

        # scorro tutte le celle per qulle che sono 1 == empty creo un nodo di id i_j e lo collego a quelli adiacenti che sono 1 , grafo non orientato
        graph = Digraph('G', filename='maze_graph.gv')

        valids = "13"
        for i in range(n):
            for j in range(m):
                if maze[i][j] in valids:
                    node_id = f"{i}{DELIMITER}{j}"
                    graph.node(node_id)
                    # collego a destra
                    if j + 1 < m and maze[i][j + 1] in valids:
                        graph.edge(node_id, f"{i}{DELIMITER}{j + 1}")
                        graph.edge(f"{i}{DELIMITER}{j + 1}", node_id)
                    # collego in basso
                    if i + 1 < n and maze[i + 1][j] in valids:
                        graph.edge(node_id, f"{i + 1}{DELIMITER}{j}")
                        graph.edge(f"{i + 1}{DELIMITER}{j}", node_id)

        graph.view()


def maze_to_ldj(filename, output_filename = "output.txt", weighted=False):
    with open(filename, 'r') as file:
        with open(output_filename, 'w') as output_file:
            n, m = map(int, file.readline().split())
            maze = [line.strip() for line in file]
            maze = [list(row.split(" ")) for row in maze]

            valids = "13"
            for i in range(n):
                for j in range(m):
                    if maze[i][j] in valids:
                        node_id = f"{i}{DELIMITER}{j}"
                        # collego a destra
                        if j + 1 < m and maze[i][j + 1] in valids:
                            output_file.write(f"{node_id} {i}{DELIMITER}{j + 1} 1\n")
                            if weighted:
                                output_file.write(f"{i}{DELIMITER}{j + 1} {node_id} 1\n")
                        # collego in basso
                        if i + 1 < n and maze[i + 1][j] in valids:
                            output_file.write(f"{node_id} {i + 1}{DELIMITER}{j} 1\n")
                            if weighted:
                                output_file.write(f"{i + 1}{DELIMITER}{j} {node_id} 1\n")


def ldj_to_graph(filename, directed=False, weighted=False):
    with open(filename, "r") as file:
        # grafo non orientato con peso, formato del file: a b peso
        graph = Graph('G', filename='ldj_graph.gv') if not directed else Digraph('G', filename='ldj_graph.gv')
        for line in file:
            a, b, peso = line.split()
            if not weighted:
                peso = None
            graph.edge(a, b, label=peso)
        graph.view()

if __name__ == "__main__":
    #maze_to_graph("DivideEtImpera/input1.txt")
    ldj_to_graph("output.txt")
    # maze_to_ldj("DivideEtImpera/input1.txt", "grafi/output.txt")
    