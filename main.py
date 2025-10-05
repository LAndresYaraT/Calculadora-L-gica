from truth_table_parser import TruthTableParser
from truth_table_verifier import TruthTableVerifier

def main():
    parser = TruthTableParser()
    verifier = TruthTableVerifier()
    
    while True:
        print("\n=== CALCULADORA DE TABLAS DE VERDAD ===")
        print("1. Generar tabla de verdad")
        print("2. Verificar tipo de expresión")
        print("3. Verificar equivalencia")
        print("4. Verificar implicación")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            expresion = input("Ingresa la expresión lógica: ")
            print(f"\nTabla de verdad para: {expresion}")
            parser.print_truth_table(expresion)
            
        elif opcion == "2":
            expresion = input("Ingresa la expresión lógica: ")
            verifier.analyze_expression(expresion)
            
        elif opcion == "3":
            expr1 = input("Ingresa la primera expresión: ")
            expr2 = input("Ingresa la segunda expresión: ")
            equivalente = verifier.verify_equivalence(expr1, expr2)
            print(f"¿'{expr1}' es equivalente a '{expr2}'? {equivalente}")
            
        elif opcion == "4":
            premisa = input("Ingresa la premisa: ")
            conclusion = input("Ingresa la conclusión: ")
            implica = verifier.verify_implication(premisa, conclusion)
            print(f"¿'{premisa}' implica '{conclusion}'? {implica}")
            
        elif opcion == "5":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()