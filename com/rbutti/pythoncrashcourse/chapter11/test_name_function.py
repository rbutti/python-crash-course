import unittest
import name_function


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        name = name_function.get_formatted_name("ravi", "kiran")
        self.assertEqual(name, "Ravi Kiran")

    def test_frist_middle_last_name(self):
        name = name_function.get_formatted_name("ravi", "kiran", "R")
        self.assertEqual(name, "Ravi R Kiran")

if __name__ == '__main__':
    unittest.main()
