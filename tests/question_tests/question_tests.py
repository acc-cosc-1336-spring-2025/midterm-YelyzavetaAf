#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from question_a.question_a import test_config, reverse_string
from question_b.question_b import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")



class Test_QuestionB(unittest.TestCase):
    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid number")
