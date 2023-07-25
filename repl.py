import argparse
import sys
import pickle5

# constants
ID_SIZE = 4
UNAME_SIZE = 32
ID_OFFSET = 0
UNAME_OFFSET = ID_OFFSET + ID_SIZE
ROW_SIZE = ID_SIZE + UNAME_SIZE
PAGE_SIZE = 4096

def attr_size(obj, attribute):
    return sys. getsizeof(obj.attribute)

def serialize_row(row):
    return pickle5.dumps(row)

def deserialize_row(serialized_row):
    return pickle5.loads(serialized_row)

class Statement:
    def __init__(self, type, row) -> None:
        self.type = type
        self.row = Row(row.id, row.uname)
class Table:
    def __init__(self, num_rows) -> None:
        self.num_rows = num_rows
        self.pages = None
class Pager:
    def __init__(self) -> None:
        pass
    
class Row:
    def __init__(self, id, uname) -> None:
        self.id = id
        self.uname = uname


def prep_statement(input, statementType):
    pass


def execute_statement(statement):
    if statement == "insert":
        print("Do insert op")
    elif statement == "select":
        print("Do select op")
    elif statement == "update":
        print("Do update op")
    elif statement == "delete":
        print("Do delete op")


def main():
    while True:
        user_input = input("db >> ").split
        if user_input and user_input[0] == ".q":
            break

        prep_statement(user_input[0], )
