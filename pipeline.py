import tokenize
from io import BytesIO
import ast
import os
import dis

line = "______________________________________________________________________________"

print(line,"\nYOUR CODE\n"+line)

code = b"""
message = "Jay Ganesh."
print(message)
"""

print("\n\n"+"1 message='Jay Ganesh'\n2 print(message)")
print("\n\n\n\n\n")

print(line,"\nYOUR CODE - TOKENIZED\n"+line,"\n\n")

tokens = tokenize.tokenize(BytesIO(code).readline)

for token in tokens:
    print(token)

print("\n\n\n\n\n")
print(line,"\nYOUR CODE - AST PARSING\n"+line,"\n\n")

tree = ast.parse(code)
print(ast.dump(tree, indent=4))

print("\n\n\n\n\n")

print(line,"\nYOUR CODE - AST EVAL\n"+line,"\n\n")
compiled_code = compile(code, "<string>", "exec")
print(dis.dis(code))

print(line,"\nYOUR CODE - BYTECODE .PYC\n"+line,"\n\n")
os.system("python3 -m compileall demo.py")