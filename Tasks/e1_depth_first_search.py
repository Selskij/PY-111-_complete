from typing import Hashable, List
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()

# Прямой путь решения
# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an depth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node of search
#     :return: list of nodes in the visited order
#     """
#     draw_graph(g)
#     path_node = []
#     visited_nodes = {node: False for node in g.nodes}
#
#     wait_nodes = [] # питоновский список  вершина справа {СТЭК}
#     wait_nodes.append(start_node)
#     visited_nodes[start_node] = True
#
#     while wait_nodes:
#         current_node = wait_nodes.pop()
#         path_node.append(current_node)
#
#         neighbours = g[current_node]
#         for neighbour in neighbours:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)
#                 visited_nodes[neighbour] = True
#
#     return path_node



# Рекурсивный способ решения
def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    draw_graph(g)
    visited_nodes = {node: False for node in g.nodes}
    node_path = [] # путь рекурсии

    def recursion_dfs(current_node): # рекурсивная функция
        #               ^----откуда запускаем рекурсию
        if visited_nodes[current_node]:
            return None # не нужно рекурсивно запускать обход если мы уже были в этом узле
        # если в узле не был, то:
        visited_nodes[current_node] = True # говорю что я посетил этот узел
        node_path.append(current_node) # добавляю переменную в путь обхода

# опять нужно перебрать соседей текущего узла
        neighbours = g[current_node]
        for neighbour in neighbours: # и от каждого из этих соседей
            if not visited_nodes[neighbour]:# если я его не посещал [ Можно убрать т.к есть эта проверка на 56 строке]
                recursion_dfs(neighbour) # мы рекурсивно запускаем обход в глубину

        return node_path

#     return recursion_dfs(start_node)
