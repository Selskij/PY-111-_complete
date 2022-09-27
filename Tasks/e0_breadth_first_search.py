from typing import Hashable, List
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt
# функция отрисовывающая граф из лекции


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


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    draw_graph(g) # отрисовка гафа [Добавляется после написания основного кода]
    path_node = []
    visited_nodes = {node:  False for node in g.nodes} # словарь из непосещённых узлов(изначальо они все непосещены)
    wait_nodes = deque()  # очередь из узлов которые ожидают обхода

    wait_nodes.append(start_node) # с помощью append-a помещаю стартовый узел откуда буду посещать остальные
#   ^---- подожгли первый узел
    #  Конец очредеи справа, начало слева. Новые подошедшие узлы улетают в конец очереди

    while wait_nodes: # будет выполняться пока есть хоть один элемент
        # есть запас из очереди горящих узлов, мы достаём оттуда горящий узел и он поджигает рядом с собой тех кто не был зажжен
        # дважды не поджигаем один и тот же узел
        current_node = wait_nodes.popleft() # забрали первый стоящий в очереди слева
        path_node.append(current_node) # узел добавлен в список посещённых узлов
        visited_nodes[current_node] = True # узел сгорел

        # поджигаем соседей только что посещённого узла
        for neighbour in g[current_node]:
            #_______________#2----------
          if not visited_nodes[neighbour]: # только если сосед не был посещён мы его добавляем в очредь
              #______________#2_________

              #1  # они являются подоженными когда попадают в очередь
                wait_nodes.append(neighbour) # подожгли соседа
                visited_nodes[neighbour] = True
              #1  #
    return path_node




    # g.nodes # все узлы графа
    # g[start_node] # соседи узла
    # print(g, start_node)
    # return list(g.nodes)
