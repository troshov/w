class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None  # Начальный узел списка
        self.end = None  # Конечный узел списка
        self.current = None  # Текущий узел для итерации

    def __iter__(self):
        self.current = self.start  # Устанавливаем текущий узел на начальный узел
        return self
    
    def __next__(self):
        if self.current is not None:  # Если текущий узел существует
            result = self.current.data  # Получаем данные текущего узла
            self.current = self.current.next  # Переходим к следующему узлу
            return result
        else:
            raise StopIteration  # Генерируем исключение, чтобы завершить итерацию

    def push(self, val):
        val = Node(val)
        if self.start:  # Если список не пуст
            self.end.next = val  # Назначаем указатель на следующий узел в текущем последнем узле
            self.end = val  # Обновляем конечный узел на новый узел          
        else:  # Если список пуст
            self.start = val  # Начальный и конечный узлы становятся новым узлом
            self.end = val
            self.current = self.start  # Устанавливаем текущий узел на начальный узел

    def get(self, index):
        number = 0
        node = self.start
        while index != number:  # Перебираем элементы списка до тех пор, пока не достигнем заданного индекса
            node = node.next
            number += 1
        return node.data  # Возвращаем данные найденного узла

    def print(self):
        node = self.start
        while node is not None:  # Перебираем элементы списка пока не достигнем конца списка (None)
            print(node.data, end=" ")  # Выводим данные узла на экран
            node = node.next

    def remove(self, index):
        if index == 0:
            self.start = self.start.next
        else:
            num = 0
            node_l = self.start
            while index - 1 != num and node_l.next != None:  # Перебираем элементы списка до удаляемого узла
                node_l = node_l.next
                num += 1
                
            if not (index - 1 != num and node_l.next != None):
                raise ValueError('Индекс выходит за пределы диапазона')  # Вывод ошибки при выходе за пределы диапазона
            elif node_l.next.next != None:
                node_l.next = node_l.next.next
            else:
                node_l.next = None  # Удаляем узел путем перевязывания указателя
                self.end = node_l

    def insert(self, index, val):
        num = 0
        node = Node(val)
        node_l = self.start
        while index - 1 != num:  # Перебираем элементы списка до передаваемого индекса
            node_l = node_l.next
            num += 1
        node_r = node_l.next  # Сохраняем ссылку на следующий узел
        node_l.next = node  # Вставляем новый узел между текущим и следующим узлами
        node.next = node_r

