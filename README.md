## Задание №1

На языке Python или C++ написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

```
def isEven(value):
      return value % 2 == 0
```
Данная функция определяет четность числа сравнивая остаток при делении на 2,
если остаток равен 0, число четное.

#### Плюсы:
* Простота реализации, код понятен на интуитивном уровне.
```
def isEven(value):
    return value & 1 == 0
```
В данной реализации мы используем побитовую операцию "&" между __value__ и __1__, чтобы проверить младший бит числа. Если младший бит равен 0, то число четное.

#### Плюсы:
* Производительность, данная операция более эфективна на уровне аппаратуры, чем операция нахождения остатка от деления.

#### Минусы:
* Для не опытных программистов подход может быть не очевидным.

## Задание №2

На языке Python или С++ написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

#### С помощью списка Python

Достоинства:
* Простота реализации кода за счет использования встроенной структуры данных, методы которой можно использовать для управления очередью.
* Доступ к элементам списка за время О(1).

Недостатки:
* Низкая производительность при удалении из начала списка, время выполнения О(n), что не эффективно для больших очередей.

#### С помощью связанного списка
Достоинства:
* Эффективность удаления элемента из начала списка за время О(1), т.к. нет необходимости перемещать все элементы как в предыдущей реализации.

Недостатки:
* Занимает больше памяти чем простой список
* Сложность доступа к элементу О(n), для доступа к элементу необходимо пройти по всем предшествующим элементам.

#### Сравнение двух реализаций:
* Использование связанного списка обеспечивает эффективность добавления и удаления элементов в очередь, в особенности при работе с большим объемом данных
* Использование простого списка более эффективно в случаях, требующих быстрого доступа к элементу по индексу.

* ## Задание №3

На языке Python или С++ предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.

* По скольку при разработке я использую ЯП Python более эффективно будет использовать встроенный метод сортировки списка __sort()__, т.к. он реализован на с++, что делает его более быстрым и эффективным, чем реалиция одной из быстрых сортировок на Python.
