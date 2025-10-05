# Calculadora-L-gica
Calculadora de Tablas de Verdad
Una herramienta completa para generar y analizar tablas de verdad de expresiones lógicas, escrita en Python.

Características
✅ Generación de tablas de verdad para expresiones lógicas complejas

✅ Análisis de expresiones: identifica tautologías, contradicciones y contingencias

✅ Verificación de equivalencia entre expresiones lógicas

✅ Verificación de implicación lógica

✅ Soporte múltiple de operadores: ∧, ∨, ¬, →, ↔, ⊕, y sus equivalentes en texto

✅ Interfaz interactiva fácil de usar

Operadores Soportados
Operador	Símbolos	Descripción
AND	∧, &, and	Conjunción
OR	∨, |, or	Disyunción
NOT	¬, ~, not	Negación
IMPLICA	→, ->	Implicación
SI Y SOLO SI	↔, <->	Bicondicional
XOR	⊕, xor	OR exclusivo
Instalación
Clona o descarga los archivos del proyecto

Asegúrate de tener Python 3.6+ instalado

No se requieren dependencias externas

Estructura del Proyecto
text
truth_table_calculator/
│
├── truth_table_parser.py    # Parser para generar tablas de verdad
├── truth_table_verifier.py  # Verificador de propiedades lógicas
├── main.py                  # Programa principal interactivo
└── README.md               # Este archivo
Uso
Opción 1: Interfaz Interactiva (Recomendado)
Ejecuta el programa principal:

bash
python main.py
Selecciona una opción del menú:

text
=== CALCULADORA DE TABLAS DE VERDAD ===
1. Generar tabla de verdad
2. Verificar tipo de expresión
3. Verificar equivalencia
4. Verificar implicación
5. Salir
Opción 2: Uso Directo desde Código
python
from truth_table_parser import TruthTableParser
from truth_table_verifier import TruthTableVerifier

# Crear instancias
parser = TruthTableParser()
verifier = TruthTableVerifier()

# Ejemplo 1: Generar tabla de verdad
print("Tabla de verdad para: p ∧ q")
parser.print_truth_table("p ∧ q")

# Ejemplo 2: Verificar si es tautología
expresion = "p ∨ ¬p"
if verifier.verify_tautology(expresion):
    print(f"'{expresion}' es una tautología")

# Ejemplo 3: Verificar equivalencia
equivalente = verifier.verify_equivalence("¬(p ∧ q)", "¬p ∨ ¬q")
print(f"Las expresiones son equivalentes: {equivalente}")

# Ejemplo 4: Análisis completo
verifier.analyze_expression("(p → q) ∧ p → q")
Ejemplos de Expresiones
Expresiones básicas:
p ∧ q (p AND q)

p ∨ q (p OR q)

¬p (NOT p)

p → q (p IMPLICA q)

p ↔ q (p SI Y SOLO SI q)

Expresiones compuestas:
(p ∧ q) ∨ r

p → (q ∨ r)

¬(p ∧ q) ↔ (¬p ∨ ¬q) (Ley de De Morgan)

(p → q) ∧ (q → p)

Tautologías conocidas:
p ∨ ¬p (Ley del tercero excluido)

p → p (Ley de identidad)

(p → q) ↔ (¬q → ¬p) (Contrarrecíproco)

Ejemplos de Salida
Generar tabla de verdad:
text
Tabla de verdad para: p ∧ q
========================
  p   |  q   | p ∧ q 
------------------------
  0   |  0   |   0   
  0   |  1   |   0   
  1   |  0   |   0   
  1   |  1   |   1   
Análisis de expresión:
text
Análisis de: p ∨ ¬p
==================================================
✓ Es una TAUTOLOGÍA (siempre verdadera)
  p   | p ∨ ¬p 
----------------
  0   |   1   
  1   |   1   
Funciones Principales
Parser (truth_table_parser.py)
generate_truth_table(expression): Genera la tabla de verdad completa

print_truth_table(expression): Imprime la tabla de forma legible

get_variables(expression): Extrae las variables de la expresión

Verificador (truth_table_verifier.py)
verify_tautology(expression): Verifica si es tautología

verify_contradiction(expression): Verifica si es contradicción

verify_contingency(expression): Verifica si es contingencia

verify_equivalence(expr1, expr2): Verifica equivalencia entre expresiones

verify_implication(premise, conclusion): Verifica implicación lógica

analyze_expression(expression): Análisis completo con tabla de verdad

Reglas de Sintaxis
Variables: Letras individuales (p, q, r, a, b, etc.)

Paréntesis: Usa () para agrupar expresiones

Operadores: Puedes mezclar símbolos y texto (p ∧ q o p and q)

Espacios: Los espacios son opcionales pero recomendados

Casos de Uso Típicos
Para estudiantes de lógica:
Verificar leyes lógicas (De Morgan, distributivas, etc.)

Practicar con ejercicios de tablas de verdad

Comprobar equivalencias entre expresiones

Para desarrolladores:
Verificar condiciones lógicas en código

Analizar circuitos lógicos

Validar expresiones booleanas complejas

Limitaciones
Las variables deben ser de un solo carácter

No soporta expresiones con más de 6 variables (por rendimiento)

No incluye operadores de cuantificación (∀, ∃)

Contribuir
Si encuentras algún error o quieres agregar funcionalidades:

Haz fork del proyecto

Crea una rama para tu feature

Realiza tus cambios

Envía un pull request