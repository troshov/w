#task2
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start != None:
            val = self.start
            self.start = val.nref
            return val.data
        else:
            return None

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        node = Node(val)
        if self.end == None:
            self.end = node
            self.start = node
        else:
            self.end.nref = node
            node.pref = self.end
            self.end = node  

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        num = 0
        node = Node(val)
        node_r = self.start
        while n >= 0 and num != n:
            node_r = node_r.nref
            num += 1
        node_l = node_r.pref
        node_l.nref, node.pref = node, node_l
        node_l.pref, node.nref = node, node_r

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        node = self.start
        while node.nref != None:
            print (node.data, end=' ')
            node = node.nref
        else:
            print(node.data, end=' ')


