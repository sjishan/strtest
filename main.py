import unittest

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

class Test(unittest.TestCase):
    def test_should_handle_simple_tests(self):
        self.assertEqual(first_non_repeating_letter("a"), "a")
        self.assertEqual(first_non_repeating_letter("stress"), "t")
        self.assertEqual(first_non_repeating_letter("moonmen"), "e")


if __name__ == '__main__':
    unittest.main()
