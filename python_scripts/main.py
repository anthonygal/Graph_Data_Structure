# #### Create the graph

from Graph_Data_Structures import Graph
from Graph_Data_Structures import Node
from Graph_Data_Structures import Edge



node_ids = [
    'Business Management',
    'Human Sciences',
    'Mathematics 1',
    'Mathematics 2',
    'Physics 1',
    'Physics 2',
    'Mechanics 1',
    'Mechanics 2',
    'Software 1',
    'Software 2'
]

edges = [
    ('Mathematics 1','Mathematics 2'),
    ('Physics 1','Physics 2'),
    ('Mechanics 1','Mechanics 2'),
    ('Software 1', 'Software 2'),
    ('Mathematics 1','Software 1'),
    ('Mathematics 1','Mechanics 1'),
    ('Physics 1','Mechanics 1'),
]

g = Graph(node_ids, edges, oriented=True)
print(g)


# #### Topological sorting algorithm based on DFS (Depth First Search)

# The following algorithm will return a topological sort of the courses. By following the obtained order, the student will be able to complete all his courses respecting the prerequisites constraints.


def topologicalSort(graph, node, top_sort_list):
    """
    Recursive function based on depth first search returning a topoligical ordering for a given starting node.

    Args:
        graph: a graph object
        node: node object of the graph corresponding to the starting node of the DFS
        top_sort_list: topologically sorted list of node IDs

    Returns:
        A list of node IDs
    """
    if node.mark!=False:
        return
    for adj_node in graph.adjacentNodes(node.ID):
        topologicalSort(graph, adj_node, top_sort_list)
    node.mark = True
    top_sort_list.append(node.ID)
    

#Get all source nodes
source_nodes = []
for node in g.nodes:
    if g.degree(node.ID, reception=True) == 0:
        source_nodes.append(node)
        
#Execute topologicalSort() function over each source node       
g.clearMarks()
top_sort_list = []
for source_node in source_nodes:
    topologicalSort(g, source_node, top_sort_list)
top_sort_list.reverse()
g.clearMarks()

print("\n")
print("-------Topologically sorted list of courses-------")
print(top_sort_list)
print("--------------------------------------------------")