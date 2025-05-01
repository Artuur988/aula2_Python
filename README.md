# Python Programming Basics: A Learning Repository for Python Fundamentals

This repository contains educational Python scripts designed to help beginners learn fundamental Python programming concepts. It provides practical examples covering basic syntax, variables, indentation, and commenting practices in Python.

The repository serves as a structured learning resource that progressively introduces core Python concepts through hands-on examples. Each script focuses on a specific programming concept, making it easier for newcomers to understand and practice Python programming fundamentals. The examples are deliberately kept simple and well-documented to facilitate learning.

## Repository Structure
```
.
├── aula02-exemplos/           # Directory containing basic Python concept examples
│   ├── comentarios.py        # Demonstrates proper Python commenting practices
│   ├── indentacao.py        # Shows Python's indentation rules and importance
│   └── variaveis.py         # Examples of variable declaration and data types
└── aula1.py                 # Introduction to Python with Hello World program
```

## Usage Instructions
### Prerequisites
- Python 3.x installed on your system
- A text editor or IDE (e.g., VSCode, PyCharm, or IDLE)
- Basic understanding of command line interface

### Installation
1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Ensure Python is installed:
```bash
# Check Python version
python --version
# or
python3 --version
```

### Quick Start
1. Run the Hello World program:
```bash
python aula1.py
```

2. Explore the example scripts:
```bash
# To run variables example
python aula02-exemplos/variaveis.py

# To run indentation example
python aula02-exemplos/indentacao.py

# To run comments example
python aula02-exemplos/comentarios.py
```

### More Detailed Examples
#### Hello World Program
```python
# aula1.py
print("Hello World!")
```
Output:
```
Hello World!
```

### Troubleshooting
Common issues and solutions:

1. Python Command Not Found
```bash
# Error message:
command not found: python

# Solution:
# On Windows, ensure Python is added to PATH
# On macOS/Linux, try:
python3 [filename].py
```

2. Indentation Errors
- Problem: Inconsistent indentation in Python code
- Solution: Ensure all code blocks use consistent indentation (typically 4 spaces)
- Example error message: "IndentationError: unexpected indent"

Debug Tips:
- Use print statements to debug variable values
- Check file permissions if unable to execute scripts
- Verify correct Python version is being used

## Data Flow
The repository follows a progressive learning path, starting with basic concepts and building up to more complex examples.

```ascii
[Hello World] -> [Variables] -> [Indentation] -> [Comments]
     |              |               |               |
     v              v               v               v
Basic Output    Data Types    Code Structure   Documentation
```

Key Learning Points:
1. Basic Python syntax and program structure
2. Variable declaration and data types
3. Proper code indentation practices
4. Documentation and commenting conventions
5. Print statement usage for output