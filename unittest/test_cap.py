import unittest
import cap

class TestaCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text= "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()

##### FAILURE #####
# F.
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# FAIL: test_multiple_words(__main__.TestaCap)
# ----------------------------------------------------------------------
# Traceback(most recent call last):
#   File "test_cap.py", line 14, in test_multiple_words
#   self.assertEqual(result, 'Monty Python')
# AssertionError: 'Monty python' != 'Monty Python'
# - Monty python
# ? ^
# + Monty Python
# ? ^


##### SUCCESSFUL #####
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
