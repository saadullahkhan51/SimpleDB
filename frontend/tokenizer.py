"""
SELECT (keyword)
name (identifier)
, (symbol)
age (identifier)
FROM (keyword)
users (identifier)
WHERE (keyword)
age (identifier)
> (operator)
30 (literal)
; (symbol)
"""

class Tokenizer:
    def __init__(self) -> None:
        self.keywords = set(["select", "from", "where", "insert", "update", "delete"])
        self.operators = set(['=', '>', '<'])
        self.symbols = set([';', ',', '(', ')'])
        self.tokens = []

    def tokenize(self, sql_command: str):
        # Implement the logic to tokenize the SQL command
        words = sql_command.split()
        self.tokens = []
        for word in words:
            if word:  # Check if the word is not empty
                if word.lower() in self.keywords:
                    self.tokens.append(('KEYWORD', word.upper()))
                elif word in self.operators:
                    self.tokens.append(('OPERATOR', word))
                elif word.isdigit():
                    self.tokens.append(('INTEGER_LITERAL', int(word)))
                elif word.startswith("'") and word.endswith("'"):
                    self.tokens.append(('STRING_LITERAL', word[1:-1]))
                elif word in self.symbols:
                    self.tokens.append(('SYMBOL', word))
                else:
                    self.tokens.append(('IDENTIFIER', word))


tokenizer = Tokenizer()
tokenizer.tokenize("SELECT name FROM users WHERE age > 30;")
print(tokenizer.tokens)