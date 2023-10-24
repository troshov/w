#task1
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end != None:
            val = self.end
            self.end = None
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
        else:
            node.pref = self.end
            self.end = node      

    def print(self):
        """
        вывод на печать содержимого стека
        """
        node = self.end
        while node.pref != None:
            print (node.data, end=' ')
            node = node.pref
        else:
            print(node.data, end=' ')


        

