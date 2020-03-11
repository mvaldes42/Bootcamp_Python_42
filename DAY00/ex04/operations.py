import sys
import string
error_str_a = "Usage: python operations.py <number1> <number2>\n"
error_str_b = "Example:\n\tpython operations.py 10 3\n"
error_str = error_str_a + error_str_b
if len(sys.argv) < 2:
    exit(error_str)
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    print("InputError: only numbers\n")
    exit(error_str)
if len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    exit(error_str)
results = {
    'Sum:': a + b,
    'Difference:': a - b,
    'Product:': a * b,
    'Quotient:': a / b if b > 0 else 'ERROR (div by zero)',
    'Remainder:': a % b if b > 0 else 'ERROR (modulo by zero)\n'
}
for opr, res in results.items():
    print(f'{opr:15}   {res:<15}')
