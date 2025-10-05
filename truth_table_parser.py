import re
from itertools import product

class TruthTableParser:
    def __init__(self):
        self.operators = {
            '∧': 'and', '&': 'and', 'and': 'and',
            '∨': 'or', '|': 'or', 'or': 'or',
            '¬': 'not', '~': 'not', 'not': 'not',
            '→': 'implies', '->': 'implies',
            '↔': 'iff', '<->': 'iff',
            '⊕': 'xor', 'xor': 'xor'
        }
    
    def tokenize(self, expression):
        """Divide la expresión en tokens"""
        pattern = r'([a-zA-Z][a-zA-Z0-9]*|∧|∨|¬|→|↔|⊕|&|\||~|->|<->|xor|and|or|not|\(|\))'
        tokens = re.findall(pattern, expression)
        return [token.strip() for token in tokens if token.strip()]
    
    def shunting_yard(self, tokens):
        """Algoritmo Shunting Yard para convertir a notación postfija"""
        output = []
        stack = []
        precedence = {
            'not': 4, '¬': 4, '~': 4,
            'and': 3, '∧': 3, '&': 3,
            'or': 2, '∨': 2, '|': 2,
            'xor': 2, '⊕': 2,
            'implies': 1, '→': 1, '->': 1,
            'iff': 0, '↔': 0, '<->': 0
        }
        
        for token in tokens:
            if token.isalnum() and len(token) == 1:
                output.append(token)
            elif token in self.operators:
                op = self.operators[token]
                while (stack and stack[-1] in precedence and 
                       precedence[op] <= precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(op)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
        
        while stack:
            output.append(stack.pop())
        
        return output
    
    def evaluate_postfix(self, postfix, values):
        """Evalúa la expresión en notación postfija"""
        stack = []
        
        for token in postfix:
            if token in values:
                stack.append(values[token])
            elif token == 'not':
                a = stack.pop()
                stack.append(not a)
            elif token == 'and':
                b, a = stack.pop(), stack.pop()
                stack.append(a and b)
            elif token == 'or':
                b, a = stack.pop(), stack.pop()
                stack.append(a or b)
            elif token == 'xor':
                b, a = stack.pop(), stack.pop()
                stack.append(a != b)
            elif token == 'implies':
                b, a = stack.pop(), stack.pop()
                stack.append(not a or b)
            elif token == 'iff':
                b, a = stack.pop(), stack.pop()
                stack.append(a == b)
        
        return stack[0]
    
    def get_variables(self, expression):
        """Extrae las variables de la expresión"""
        tokens = self.tokenize(expression)
        variables = set()
        for token in tokens:
            if token.isalnum() and len(token) == 1 and token not in self.operators:
                variables.add(token)
        return sorted(list(variables))
    
    def generate_truth_table(self, expression):
        """Genera la tabla de verdad completa"""
        variables = self.get_variables(expression)
        tokens = self.tokenize(expression)
        postfix = self.shunting_yard(tokens)
        
        header = variables + [expression]
        table = [header]
        
        for combination in product([False, True], repeat=len(variables)):
            values = dict(zip(variables, combination))
            result = self.evaluate_postfix(postfix, values)
            row = list(combination) + [result]
            table.append(row)
        
        return table
    
    def print_truth_table(self, expression):
        """Imprime la tabla de verdad de forma legible"""
        table = self.generate_truth_table(expression)
        
        header = table[0]
        print(" | ".join(f"{str(col):^6}" for col in header))
        print("-" * (len(header) * 8))
        
        for row in table[1:]:
            formatted_row = [str(int(val)) if isinstance(val, bool) else str(val) for val in row]
            print(" | ".join(f"{col:^6}" for col in formatted_row))

if __name__ == "__main__":
    # Ejemplos de uso del parser solo
    parser = TruthTableParser()
    test_expressions = ["p ∧ q", "p ∨ q", "¬p"]
    
    for expr in test_expressions:
        print(f"\nTabla de verdad para: {expr}")
        parser.print_truth_table(expr)