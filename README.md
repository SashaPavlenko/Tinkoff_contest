# Tinkoff_contest
Репозиторий для задания Тинькофф по программированию

#### Задача
Написать утилиту, анализирующую 2 файла с кодом на питоне на плагиат.

Весь функционал представлен в файле **compare.py**

Для работы необходимо вызвать в консоли следующий код:
`compare.py <имя входного файла> <имя выходного файла для записи>`

Пример входного файла формата **.txt**:

files/main.py plagiat1/main.py
files/loss.py plagiat2/loss.py
files/loss.py files/loss.py

Пример выходного файла формата **.txt**:

0.63
0.84
0.153

##### Примечание
- Утилита принимает на вход файл, в котором содержится строки пар файлов, которые необходимо проеврить на антиплагиат.
- На выход утилита создает файл, где в каждой строчке соответственно пишет результат сравнения от 0 до 1, где 0 -- файлы индентичны, а 1 -- файлы полностью различаются
