def is_safe(graph, node, color, coloring):
    for neighbor in graph[node]:
        if coloring[neighbor] == color:
            return False
    return True


def color_map_util(graph, num_colors, coloring, node, num_nodes):
    if node == num_nodes:
        return True

    for color in range(1, num_colors + 1):
        if is_safe(graph, node, color, coloring):
            coloring[node] = color
            if color_map_util(graph, num_colors, coloring, node + 1, num_nodes):
                return True
            coloring[node] = 0  # Backtrack if the current color doesn't lead to a solution

    return False


def four_color_map(graph):
    num_nodes = len(graph)
    num_colors = 4
    coloring = [0] * num_nodes

    if not color_map_util(graph, num_colors, coloring, 0, num_nodes):
        print("Solution does not exist.")
    else:
        print("Coloring of the map:")
        for i in range(num_nodes):
            print(f"Region {i + 1}: Color {coloring[i]}")


if __name__ == "__main__":
    # Define the adjacency list representation of the map
    # Example: {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        # Add more nodes and their connections as needed
    }

    four_color_map(graph)
