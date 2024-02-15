# Задание 1. На языке Pythonнаписать алгоритм (функцию) определения четности целого числа.


def isEven(value):
    """С помощью операции побитового "И" проверяем младший бит входящего числа"""
    return value & 1 == 0


# Задание 2. На языке Python или С++ написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.


class QueueList:
    """Реализация с помощью списка python"""
    def __init__(self):
        self.queue = []

    def add_node(self, item):
        self.queue.append(item)

    def remove_node(self):
        if self.queue:
            return self.queue.pop(0)
        return "Очередь пуста"

    def get_first(self):
        return self.queue[0] if self.queue else 'Очередь пуста'


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Реализация с помощью односвязанного списка"""
    def __init__(self):
        self.first = self.next_in_line = None

    def add_node(self, node):
        if not self.first:
            self.first = self.next_in_line = node
        self.next_in_line.next = node
        self.next_in_line = node

    def remove_node(self):
        if not self.first:
            print("Очередь пуста")
            return
        if self.next_in_line == self.first:
            self.first = self.next_in_line = None
        else:
            self.first = self.first.next

    def get_first(self):
        """Возвращает элемент из начала очереди без удаления."""
        if not self.first:
            return "Очередь пуста"
        return self.first.data


#Задание 3. Ответ в README