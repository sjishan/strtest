Problem
---
Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").

Code
---
```python
def first_non_repeating_letter(str):

    #stores the frequency of the letter
    frequency_table = {}

    #lower case representation of the word
    lc_word = str.lower()

    word_length = len(lc_word)

    #if the letter is found for the first time then
    #initialize the key-value in the dictionary
    #else increase the frequency
    for i in range(0, word_length):
        if lc_word[i] in frequency_table:
            frequency_table[lc_word[i]] += 1
        else:
            frequency_table[lc_word[i]] = 1

    #return the letter in the correct case if it is non-repeated
    for i in range(0, word_length):
        if frequency_table[lc_word[i]] == 1:
            return str[i]
```

Tests
---
```python
import unittest
# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_handle_simple_tests(self):
    self.assertEqual(first_non_repeating_letter("a"), "a")
    self.assertEqual(first_non_repeating_letter("stress"), "t")
    self.assertEqual(first_non_repeating_letter("moonmen"), "e")
```