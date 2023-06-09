class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node
