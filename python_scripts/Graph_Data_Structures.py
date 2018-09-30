
# coding: utf-8

# # Implementation of a graph structure


from random import randint


# ## Class defintions

class Node:
    """
    A node object is identified by an ID attribute which should be a string.
    A node can be marked.
    """ 
    def __init__(self, ID, mark = False):
        self.ID = ID
        self.mark = mark
    
    def __str__(self):
        return self.ID

        
class Edge: 
    """
    An edge object is composed of two nodes.
    An edge can be marked.
    """ 
    def __init__(self, node1, node2, mark = False):
        self.node1 = node1
        self.node2 = node2
        self.mark = mark
    
    def __getitem__(self, key):
        if (key == 0):
            return self.node1
        elif (key == 1):
            return self.node2
        
    def __str__(self):
        return "(" + str(self.node1) + "," + str(self.node2) + ")"
    
    def index(self, node):
        if (node == self[0]):
            return 0
        elif (node == self[1]):
            return 1
        

class Graph:
    """
    A graph object is composed of a non-empty list of nodes and a list of edges.
    The graph is represented with an incidence matrix.
    The graph may be oriented or not.

    """ 
    def __init__(self, node_list, edge_list = [], oriented = False):
        """
        Graph constructor. 
        From a list of node IDs and a list of tuples of node IDs, 
        the node objects and edge objects composing the graph will be created 
        and attributed to the newly created graph object.
        An incidence matrix based on these nodes and edges is created 
        and attributed to the graph object.

        Args:
            node_list: a list of node IDs. The node IDs shoudl be string elements.
            edge_list: a list of edges. The edges should be tuples of the node IDs.
            oriented: A boolean value: 
                        If true the graph will be a directed graph. 
                        If false it will be an undirected graph.

        Returns:
            The graph object.

        """
        #Create node objects
        node_objects = []
        for node in node_list:
            node_objects.append(Node(node))
            
        #Create edge objects
        edge_objects = []
        for edge in edge_list:
            for node in node_objects:
                if(edge[0] == node.ID):
                    node1 = node
                if(edge[1] == node.ID):
                    node2 = node
            edge_objects.append( Edge(node1, node2) )
        
        # Initialise attributes
        self.nodes = node_objects
        self.edges = edge_objects
        self.oriented = oriented
        self.incidence_matrix = self.build_incidence_matrix(node_objects, edge_objects, oriented)
        
    def __str__(self):
        string = "--------------------Graph-------------------------"
        string += "\n"
        string += "Oriented: " + str(self.oriented)
        string += "\n"
        string += "Nodes: "
        for node in self.nodes:
            string +="\n    " + str(node)
        string += "\n"
        string += "Edges: "
        for edge in self.edges:
            string += "\n    " + str(edge)
        string += "\n"
        string += "Incidence Matrix: \n"
        for edge in self.incidence_matrix:
            string +="       " + str(edge) + "\n"
        string +="--------------------------------------------------"
        
        return string
        
    def build_incidence_matrix(self, nodes, edges = [], oriented = False):
        """
        Builds a 2D array representing the graph in the form of an incidence matrix.

        Args:
            nodes: the list of node objects composing the graph.
            edges: the list of edge objects composing that same graph.
            oriented: boolean attribute defining whether the graph is directe or undirected.
        Returns:
            The incidence matrix as a 2D array.

        """
        incidence_matrix = [ [0] * len(nodes) for n in range(len(edges))]

        for edge in edges:
            if (nodes.index(edge[0]) == nodes.index(edge[1])):
                incidence_matrix[ edges.index(edge) ] [ nodes.index(edge[0])] = 2

            else:
                if oriented:
                    incidence_matrix[ edges.index(edge) ] [ nodes.index(edge[0])] = -1
                    incidence_matrix[ edges.index(edge) ] [ nodes.index(edge[1])] = 1
                else:
                    incidence_matrix[ edges.index(edge) ] [ nodes.index(edge[0])] = 1
                    incidence_matrix[ edges.index(edge) ] [ nodes.index(edge[1])] = 1
                    
        return incidence_matrix
    
    def getNode(self, ID):
        """
        Returns the node object corresponding to the given node ID or None if it is not found.
        Args:
            ID: the string element identifying a node
        Returns:
            The node object or None

        """
        for node in self.nodes:
            if node.ID == ID:
                return node
    
    def getEdge(self, ID1, ID2):
        """
        Returns the edge object corresponding to the given node IDs or None if it is not found.
        Args:
            ID1: the string element identifying node 1 of the edge
            ID2: the string element identifying node 2 of the edge
        Returns:
            The edge object or None

        """
        for edge in self.edges:
            if ( (edge[0].ID == ID1 ) & (edge[1].ID == ID2)):
                return edge
    
    def addNode(self, new_node):
        """
        Updates the graph object creating and adding a new node to the graph from a given node ID.

        Args:
            new_node:  a string element corresponding to a new node ID

        Returns:
            nothing

        """
        if self.getNode(new_node) in self.nodes:
            print("This node already exists")
        else:
            new_node = Node(new_node)
            self.nodes.append(new_node)
            for edge in self.incidence_matrix:
                edge.append(0)
        
    
    def removeNode(self, node):
        """
        Updates the graph object removing a node from the graph from a given node ID.

        Args:
            node: a string element corresponding to an existing node ID

        Returns:
            nothing
        """
        node = self.getNode(node)
        if node in self.nodes:
            valid_edges = []
            for edge in self.edges:
                if ((node != edge[0]) & (node != edge[1])):
                    valid_edges.append(edge)
            self.nodes.remove(node)
            self.edges = valid_edges
            self.incidence_matrix = self.build_incidence_matrix(self.nodes, self.edges, self.oriented)
        else:
            print("This node does not exist")
        
    def connect(self, v1, v2):
        """
        Updates the graph object creating a new edge connecting the nodes whose node IDs are v1 and v2. 
        If the graph is oriented, v1 is the origin and v2 is the destination of the edge.

        Args:
            v1: string element corresponding to the ID of an existing node
            v2: string element corresponding to the ID of an existing node

        Returns:
            nothing

        """
        if (self.getNode(v1)!=None) & (self.getNode(v2)!=None):
            new_edge = Edge(self.getNode(v1), self.getNode(v2))
            self.edges.append(new_edge)

            edge = [0] * len(self.nodes)
            if (self.nodes.index(self.getNode(new_edge[0].ID)) == self.nodes.index(self.getNode(new_edge[1].ID))):
                edge[ self.nodes.index(self.getNode(new_edge[0].ID))] = 2

            else:
                if self.oriented:
                    edge[ self.nodes.index(self.getNode(new_edge[0].ID))] = -1
                    edge[ self.nodes.index(self.getNode(new_edge[1].ID))] = 1
                else:
                    edge[ self.nodes.index(self.getNode(new_edge[0].ID))] = 1
                    edge[ self.nodes.index(self.getNode(new_edge[1].ID))] = 1

                self.incidence_matrix.append(edge)
        else:
            print("One of the nodes does not exist")
    
    def disconnect(self, v1, v2):
        """
        Updates the graph object removing the edge connecting the nodes whose node IDs are v1 and v2. 
        If the graph is oriented, v1 is the origin and v2 is the destination of the edge.

        Args:
            v1: string element corresponding to the ID of an existing node
            v2: string element corresponding to the ID of an existing node

        Returns:
            nothing
        """
        edge = self.getEdge(v1, v2)
        if edge in self.edges:
            e = [0] * len(self.nodes)
            if (self.nodes.index(self.getNode(edge[0].ID)) == self.nodes.index(self.getNode(edge[1].ID))):
                e[ self.nodes.index(self.getNode(edge[0].ID))] = 2

            else:
                if self.oriented:
                    e[ self.nodes.index(self.getNode(edge[0].ID))] = -1
                    e[ self.nodes.index(self.getNode(edge[1].ID))] = 1
                else:
                    e[ self.nodes.index(self.getNode(edge[0].ID))] = 1
                    e[ self.nodes.index(self.getNode(edge[1].ID))] = 1
                    
            self.incidence_matrix.remove(e)
            self.edges.remove(edge)
        else:
            print("This edge does not exist")
            
    def order(self):
        """
        Returns the order of the graph object. 
        """
        return len(self.nodes)
    
    def randomNode(self):
        """
        Returns a randomly selected node object from the graph.
        """
        return self.nodes[randint(0,self.order()-1)]
    
    def adjacentNodes(self, node, predecessors = False):
        """
        Finds the nodes adjacent to a given node in the graph.
        If the graph is oriented, by default, it will return the successors of the given node unless the "predecessor" argument is True.
        Args:
            node: a string element corresponding the ID of an existing node.
            predecessors: boolean value that is only significant if the graph is oriented.
                If true, the predecessors of the given node will be returned.
                If false, the successors of the given node will be returned.
        Returns:
            a list containing the node objects adjacent to the node of given ID

        """
        node = self.getNode(node)
        if node in self.nodes:
            adjacent_nodes = []
            for edge in self.edges:
                if ((node == edge[0]) | (node == edge[1])):
                    if self.oriented:
                        if predecessors:
                            if (node == edge[1]):
                                adjacent_nodes.append(edge[0])
                        else:
                            if (node == edge[0]):
                                adjacent_nodes.append(edge[1])
                    else:
                        adjacent_nodes.append(edge[abs(edge.index(node)-1)])
                        
            return adjacent_nodes
        else:
            print("This node does not exist")
            
    def degree(self, node, reception = False):
        """
        Returns the degree of a given node.
        If the graph is directed, by default, it will return the degree of emission of the given node unless the reception argument is true, in which case it will return the degree of reception.
            node: a string element corresponding the ID of an existing node.
            reception: boolean value that is only significant if the graph is oriented.
                If true, the degree reception of the given node will be returned.
                If false, the degree of emission of the given node will be returned.

        
        """
        node = self.getNode(node)
        if node in self.nodes:
            if self.oriented:
                return len(self.adjacentNodes(node.ID, reception))
            return len(self.adjacentNodes(node.ID))
        else:
            print("This node does not exist")
    
    def isRegular(self):
        """
        Returns a boolean. 
        If true the graph is regular. 
        If false, it is not regular.
        """
        degree = self.degree(self.randomNode().ID)
        for node in self.nodes:
            if degree != self.degree(node.ID):
                return False
        return True
    
    def isComplete(self):
        """
        Returns a boolean. 
        If true the graph is complete. 
        If false, it is not complete.
        """
        for node in self.nodes:
            if len(set(self.adjacentNodes(node.ID))) != (len(self.nodes)-1):
                return False
        return True
    
    def __searchTransitiveClosure(self, node, already_visited):
        """
        Protected recursive method called by graph.transitiveClosure().
        """
        already_visited.append(node.ID)
        for adjacent_node in self.adjacentNodes(node.ID):
            if not (adjacent_node.ID in already_visited):
                self.__searchTransitiveClosure(adjacent_node, already_visited)
        return already_visited
        
        
    def transitiveClosure(self, node_id):
        """
        Finds the transitive closure of a given node of the graph.

        Args:
            node_id: string element corresponding to the id of an existing node

        Returns:
            A list of node IDs
        """
        already_visited = []
        node = self.getNode(node_id)
        if node != None:
            return self.__searchTransitiveClosure(node, already_visited)
        else:
            print("This node does not exist")
    
    def isConnected(self):
        """
        Returns a boolean.
        If true the graph is connected.
        If false the graph has a least two disconnected components.
        """
        transitive_closure = set(self.transitiveClosure(self.randomNode().ID))
        nodes = []
        for node in self.nodes:
            nodes.append(node.ID)
        return set(nodes) == transitive_closure
        
    def __hasCycleWith(self, node, previous_node, already_visited):
        """
        protected recursive method called by graph.isTree()
        """
        if node.ID in already_visited:
            return True
        already_visited.append(node.ID)
        for adjacent_node in self.adjacentNodes(node.ID):
            if adjacent_node!= previous_node:
                if self.__hasCycleWith(adjacent_node, node, already_visited):
                    return True
        already_visited.remove(node.ID)
        return False
    
    def isTree(self):
        """
        Returns a boolean. 
        If true the graph is a tree. 
        If false, it is not tree.
        """
        node = self.randomNode()
        return (self.isConnected()) & (not (self.__hasCycleWith(node,node,[])))
    
    def DFS(self, node_id):
        node = self.getNode(node_id)
        if node != None:
            node.mark = True
            for adj_node in self.adjacentNodes(node.ID):
                if not adj_node.mark:
                    self.DFS(adj_node.ID)
        else:
            print("This node does not exist")
            
    def clearMarks(self):
        for node in self.nodes:
            node.mark = False
    
    def markedNodes(self):
        marked_nodes = []
        for node in self.nodes:
            if node.mark !=False:
                marked_nodes.append(node)
        return marked_nodes