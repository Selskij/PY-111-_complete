"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""


# node = {
#     "key": ...,
#     "value":...,
#     "left" # Левое поддерево
#     "right" # Правое поддерево
# }
# # Определение левого и правого поддеревьев
# root = {
#     "key": 8,
#     "left": {
#         "key":3,
#         "left": None, # пока что нет, а так есть
#         "right": None
#     },
#     "right":{
#         "key":10,
#         "left": None, # пока что нет, а так есть
#         "right": None
#     }
#
# }

from typing import Any, Optional, Tuple
# import networkx as nx


class BinarySearchTree:

    @staticmethod
    def _create_node(key, value: Any, left: Optional[dict]=None, right: Optional[dict]=None) -> dict:
        """
            Фабрика узлов
            :param key:
            :param value:
            :param left:
            :param right:
            :return: Словари
            """
        return {
            "key": key,
            "value": value,
            "left": left,
            "right": right
        }

    def __init__(self):
        self.root: Optional[dict] = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        Алгоритм вставки элемента в дерево

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = self._create_node(key,value)
        else:
            current_node = self.root # Беру узел в котором сейчас нахожусь { Изначально он равен корню}
            while True:
                current_key = current_node["key"] # достаю ключ корня
                if key > current_key: # если ключ который мы хотим добавить больше то иду в правое полудерево
                    right_node = current_node["right"]
                    if right_node is None: # если дошли до листа вставляем элемент
                        current_node["right"] = self._create_node(key, value)
                        break
                    current_node = current_node["right"]
                else: # в противном случае, если ключ который мы хотим добавить меньше, то иду в левое полудерево
                    left_node = current_node["left"]
                    if left_node is None: # если дошли до листа вставляем элемент
                        current_node["left"] = self._create_node(key, value)
                        break
                    else:
                        current_node = current_node["left"]




                # Такая запись нарушает принцип DRY более элегантный вариант:

                # root_key = self.root["key"]
                # current_root = self.root["right"] if key > root_key else current_root # если ключ который мы хотим добавить больше
                # # ключа корня где я сейчас нахожусь то иду в правое поддерево, в противном случае иду в правое поддерево
                # # root переназначается на левый или правый
                # if current_root is None: # если дошли до листа вставляем элемент
                #     ...

        print(key, value)
        return None

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        def _find(current_node: Optional[dict]):
            if current_node is None: # базовый случай
                raise KeyError

            current_key = current_node["key"]
            if current_key == key:
                return current_node["value"]

            next_node = current_node["left"] if key < current_key else current_node["right"]
            # Если искомый ключ меньше current key то мы идём в левое поддерево в противном случае идём в правое поддерево
            return  _find(next_node)
        return _find(self.root)

    def generator(self): # Есть генератор
        current = self.root # Который от текущего узла
        if current is None: # Купируем проблему пустого дерева, ведь тогда нет ни левого ни правого
            return
        left = current.left # Возвращает по два элемента
        right = current.right
        while left or right: # Забираем либо левое либо правое поддерево до тех пор пока существует либо левое либо правое
            left = current.left
            right = current.right
            yield(left,right)

    def __iter__(self):
        return self.generator()

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None