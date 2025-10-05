from truth_table_parser import TruthTableParser
from itertools import product

class TruthTableVerifier:
    def __init__(self):
        self.parser = TruthTableParser()
    
    def verify_tautology(self, expression):
        """Verifica si una expresión es una tautología"""
        table = self.parser.generate_truth_table(expression)
        results = [row[-1] for row in table[1:]]
        return all(results)
    
    def verify_contradiction(self, expression):
        """Verifica si una expresión es una contradicción"""
        table = self.parser.generate_truth_table(expression)
        results = [row[-1] for row in table[1:]]
        return not any(results)
    
    def verify_contingency(self, expression):
        """Verifica si una expresión es una contingencia"""
        table = self.parser.generate_truth_table(expression)
        results = [row[-1] for row in table[1:]]
        return any(results) and not all(results)
    
    def verify_equivalence(self, expr1, expr2):
        """Verifica si dos expresiones son lógicamente equivalentes"""
        vars1 = set(self.parser.get_variables(expr1))
        vars2 = set(self.parser.get_variables(expr2))
        all_vars = sorted(list(vars1.union(vars2)))
        
        equivalent = True
        
        for combination in product([False, True], repeat=len(all_vars)):
            values = dict(zip(all_vars, combination))
            
            tokens1 = self.parser.tokenize(expr1)
            postfix1 = self.parser.shunting_yard(tokens1)
            result1 = self.parser.evaluate_postfix(postfix1, values)
            
            tokens2 = self.parser.tokenize(expr2)
            postfix2 = self.parser.shunting_yard(tokens2)
            result2 = self.parser.evaluate_postfix(postfix2, values)
            
            if result1 != result2:
                equivalent = False
                break
        
        return equivalent
    
    def verify_implication(self, premise, conclusion):
        """Verifica si la premisa implica la conclusión"""
        vars_premise = set(self.parser.get_variables(premise))
        vars_conclusion = set(self.parser.get_variables(conclusion))
        all_vars = sorted(list(vars_premise.union(vars_conclusion)))
        
        implies = True
        
        for combination in product([False, True], repeat=len(all_vars)):
            values = dict(zip(all_vars, combination))
            
            tokens_p = self.parser.tokenize(premise)
            postfix_p = self.parser.shunting_yard(tokens_p)
            result_p = self.parser.evaluate_postfix(postfix_p, values)
            
            tokens_c = self.parser.tokenize(conclusion)
            postfix_c = self.parser.shunting_yard(tokens_c)
            result_c = self.parser.evaluate_postfix(postfix_c, values)
            
            if result_p and not result_c:
                implies = False
                break
        
        return implies
    
    def analyze_expression(self, expression):
        """Análisis completo de una expresión"""
        print(f"Análisis de: {expression}")
        print("=" * 50)
        
        if self.verify_tautology(expression):
            print("✓ Es una TAUTOLOGÍA (siempre verdadera)")
        elif self.verify_contradiction(expression):
            print("✗ Es una CONTRADICCIÓN (siempre falsa)")
        else:
            print("○ Es una CONTINGENCIA (depende de los valores)")
        
        self.parser.print_truth_table(expression)
        print()

if __name__ == "__main__":
    # Ejemplos de uso del verificador solo
    verifier = TruthTableVerifier()
    
    print("VERIFICACIÓN DE EXPRESIONES LÓGICAS")
    print("=" * 50)
    
    verifier.analyze_expression("p ∨ ¬p")
    verifier.analyze_expression("p ∧ ¬p")
    verifier.analyze_expression("p ∧ q")