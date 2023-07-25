from sql_command_processor import SQLCommandProcessor
from virtual_machine import VirtualMachine

class Interface:
    def __init__(self):
        self.sql_command_processor = SQLCommandProcessor()
        self.compiler = Compiler()
        self.virtual_machine = VirtualMachine()

    def execute(self, sql_command):
        # 1. Process the SQL command
        processed_command = self.sql_command_processor.process(sql_command)

        # 2. Compile the processed command into bytecode
        bytecode = self.compiler.compile(processed_command)

        # 3. Execute the bytecode on the virtual machine
        result = self.virtual_machine.run(bytecode)

        return result
