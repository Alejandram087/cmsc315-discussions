"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node is not in the graph, return an empty list.
    # This safely handles a missing starting node or an empty graph.
    if start not in graph:
        return []

    # The queue follows first-in, first-out order, which allows BFS
    # to explore all nearby nodes before moving to the next level.
    queue = deque([start])

    # The visited set prevents the same node from being processed
    # multiple times when there are several paths to it.
    visited = {start}

    # This list records the order in which BFS visits the nodes.
    traversal_order = []

    while queue:
        # Remove the node that has been waiting in the queue the longest.
        current = queue.popleft()
        traversal_order.append(current)

        # Add unvisited neighbors to the queue so they will be
        # explored level by level.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Unlike DFS, which follows one path deeply before backtracking,
    # BFS explores the closest connected nodes first.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph represents a streaming recommendation system.
    # Each node is a movie or show, and each edge connects
    # content that has similar genres or viewing preferences.
    graph = {
        "Movie A": ["Movie B", "Movie C"],
        "Movie B": ["Movie A", "Movie D", "Movie E"],
        "Movie C": ["Movie A", "Movie F"],
        "Movie D": ["Movie B"],
        "Movie E": ["Movie B", "Movie F"],
        "Movie F": ["Movie C", "Movie E"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Display each node and its connections.
    for node, neighbors in graph.items():
        print(node, "->", neighbors)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # Start at Movie A. BFS first visits Movie A, then its direct
    # neighbors, and continues outward level by level.
    start_node = "Movie A"
    traversal = bfs(graph, start_node)

    print("Starting node:", start_node)
    print("BFS traversal order:", traversal)

    # Add a new movie and connect it to Movie C.
    # Because the graph is undirected, both nodes list each other.
    graph["Movie G"] = ["Movie C"]
    graph["Movie C"].append("Movie G")

    print("\nAdded Movie G connected to Movie C.")
    updated_traversal = bfs(graph, start_node)
    print("Updated BFS traversal:", updated_traversal)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Try to start from a node that does not exist.
    # The bfs function safely returns an empty list.
    missing_node_result = bfs(graph, "Movie Z")
    print("Missing start node:", missing_node_result)

    # Edge Case 2: Test a graph containing only one node.
    # BFS visits the single node and then stops because it has
    # no neighbors to add to the queue.
    single_node_graph = {
        "Movie X": []
    }

    single_node_result = bfs(single_node_graph, "Movie X")
    print("Single-node graph:", single_node_result)


if __name__ == "__main__":
    main()
