from task4 import *
import unittest


class TestReverseString(unittest.TestCase):

    def test_reverse_area(self):
        self.assertEqual(create_new_string("Помимо C# вы будете изучать Java, C++ и другие языки программирования."),
                         "омимоП C# ыв етедуб ьтачузи avaJ, C++ и еигурд икызя яинавориммаргорп.")

        self.assertEqual(create_new_string("Те.сти3,р0ван?ие"), "еТ.3итс,нав0р?еи")

        self.assertEqual(create_new_string("Я обучаюсь следующим языкам программирования: С++, Java, Python, 33, 44."),
                         "Я ьсюачубо мищюуделс макызя яинавориммаргорп: С++, avaJ, nohtyP, 33, 44.")
