#### ☑️task1 (№23)
Реализовать функцию:
которая создаст новый список элементов из **четных элементов** первого списка, которых нет во втором списке, и **нечетных элементов** второго списка, которых нет в первом списке. Элементы в возвращаемом списке должны быть представлены в порядке **возрастания** значений.
>Для данных задач также необходимо реализовать **ввод данных** с файла и **запись результата** в файл.
#### ☑️task2 (№23)
Для двух переданных **прямоугольных массивов** целых чисел определить, можно ли второй массив **наложить** на первый таким образом, чтобы значения в ячейках **совпадали**.
Функция должна вернуть **координаты ячейки первого массива**, на который требуется поместить верхний левый угол второго массива.

#### ☑️task3 (№23)
Задан **набор отрезков**, которые могут накладываться друг на друга. 
>Отрезок на прямой линии задается координатой **начала A** и координатой **окончания B** (точки начала и окончания отрезка **принадлежат** отрезку).
>
Входные данные соответствуют предыдущей задаче, только теперь вам необходимо среди заданного набора отрезков найти **три непересекающихся отрезка**, сумма длин которых будет **максимальной**.

**📋UnitTest task3:**
```python
    def test_reverse_area(self):
        test1 = [(6,7),(4,5),(2,3)]
        test2 = [(2, 6), (10, 14), (5, 9), (7, 12), (1, 3), (13, 20)]
        test3 = [(1, 100), (200, 300)]
        test4 = [(2, 99)]
        test5 = [(12, 16), (1, 2), (30, 40), (11, 18), (5, 6), (14, 17)]
        sum1, segments1 = max_sum_of_segments(test1)
        sum2, segments2 = max_sum_of_segments(test2)
        sum3, segments3 = max_sum_of_segments(test3)
        sum4, segments4 = max_sum_of_segments(test4)
        sum5, segments5 = max_sum_of_segments(test5)

        self.assertEqual(sum1, 3)
        self.assertEqual(sum2, 16)
        self.assertEqual(sum3, 199)
        self.assertEqual(sum4, 97)
        self.assertEqual(sum5, 18)
```

#### ☑️task4 (№23)
Закодировать текст следующим образом: в каждом слове переставить буквы в **обратном** порядке.
>Словом считается **непрерывная** последовательность символов (строчных и прописных) А-Я, A-Z и цифр. 

**Например**, "Помимо C# вы будете изучать Java, C++ и другие языки программирования." после кодирования превратится в "омимоП C# ыв етедуб ьтачузи avaJ, C++ и еигурд икызя яинавориммаргорп."

**📋UnitTest task4:**
```python
    def test_reverse_area(self):
        self.assertEqual(create_new_string("Помимо C# вы будете изучать Java, C++ и другие языки программирования."),
                         "омимоП C# ыв етедуб ьтачузи avaJ, C++ и еигурд икызя яинавориммаргорп.")

        self.assertEqual(create_new_string("Те.сти3,р0ван?ие"), "еТ.3итс,нав0р?еи")

        self.assertEqual(create_new_string("Я обучаюсь следующим языкам программирования: С++, Java, Python, 33, 44."),
                         "Я ьсюачубо мищюуделс макызя яинавориммаргорп: С++, avaJ, nohtyP, 33, 44.")
```


