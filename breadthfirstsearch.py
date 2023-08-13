import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
# deque (short for "double-ended queue") is a data structure that provides efficient insertion and deletion operations from both ends. It is available in Python through the collections module. The main advantage of using a deque is its O(1) time complexity for adding and removing elements from both ends.

def bfs(graph, start_node):
    visited = set()                     #nodes that have been visited by the algo
    queue = deque([start_node])         #initialising a deque
    bfs_order = []

    while queue:
        node = queue.popleft()          
        if node not in visited:
            bfs_order.append(node)
            visited.add(node)
            queue.extend(graph[node] - visited)

    return bfs_order

# Example usage
if __name__ == "__main__":
    # This graph represents a simple undirected graph where the edges have no specific direction. The connections between nodes form a network where each node is connected to its neighboring nodes. The adjacency dictionary provides an efficient way to store and retrieve information about the relationships between node
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},           
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    start_node = 'A'
    
    # Create a NetworkX graph
    G = nx.Graph(graph)
    
    # Perform BFS traversal
    bfs_traversal = bfs(graph, start_node)
    print("BFS Traversal:", bfs_traversal)
    
    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000)
    
    # Highlight BFS traversal path
    edges = [(bfs_traversal[i], bfs_traversal[i+1]) for i in range(len(bfs_traversal)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
    
    plt.show()
