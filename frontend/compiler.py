class Compiler:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.parser = Parser()
        self.code_generator = CodeGenerator()

    def compile(self, sql_command):
        tokens = self.tokenizer.tokenize(sql_command)
        ast = self.parser.parse(tokens)
        bytecode = self.code_generator.generate(ast)
        return bytecode
