from frontend.tokenizer import Tokenizer
import unittest

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_empty_string(self):
        self.tokenizer.tokenize("")
        self.assertEqual(self.tokenizer.tokens, [])

    def test_keywords(self):
        self.tokenizer.tokenize("SELECT FROM WHERE")
        expected_tokens = [
            ('KEYWORD', 'SELECT'),
            ('KEYWORD', 'FROM'),
            ('KEYWORD', 'WHERE'),
        ]
        self.assertEqual(self.tokenizer.tokens, expected_tokens)

    def test_operators(self):
        self.tokenizer.tokenize("= > <")
        expected_tokens = [
            ('OPERATOR', '='),
            ('OPERATOR', '>'),
            ('OPERATOR', '<'),
        ]
        self.assertEqual(self.tokenizer.tokens, expected_tokens)

    def test_identifiers(self):
        self.tokenizer.tokenize("column1 tablename")
        expected_tokens = [
            ('IDENTIFIER', 'column1'),
            ('IDENTIFIER', 'tablename'),
        ]
        self.assertEqual(self.tokenizer.tokens, expected_tokens)

    def test_symbols(self):
        self.tokenizer.tokenize(";,()")
        expected_tokens = [
            ('SYMBOL', ';'),
            ('SYMBOL', ','),
            ('SYMBOL', '('),
            ('SYMBOL', ')'),
        ]
        self.assertEqual(self.tokenizer.tokens, expected_tokens)

    def test_complex_input(self):
        self.tokenizer.tokenize("SELECT * FROM table1 WHERE column1 > 100;")
        expected_tokens = [
            ('KEYWORD', 'SELECT'),
            ('IDENTIFIER', '*'),
            ('KEYWORD', 'FROM'),
            ('IDENTIFIER', 'table1'),
            ('KEYWORD', 'WHERE'),
            ('IDENTIFIER', 'column1'),
            ('OPERATOR', '>'),
            ('INTEGER_LITERAL', 100),
            ('SYMBOL', ';'),
        ]
        self.assertEqual(self.tokenizer.tokens, expected_tokens)

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
