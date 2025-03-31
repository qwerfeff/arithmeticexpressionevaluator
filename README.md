# Arithmetic Expression Evaluator

A basic implementation of different algorithms that evaluate an arithmetic expression.

## Syntax

The basic syntax for inputting an arithmetic expression is as follows:

### Binary Operators:
- **Exponentiation** operand is given by the symbol `^`
- **Division** operand is given by the symbol `/`
- **Multiplication** operand is given by the symbol `*`
- **Addition** operand is given by the symbol `+`
- **Subtraction** operand is given by the symbol `-`

### Unary Operators:
- The unary minus sign is given by `-`

### Precedence Operators:
- Open and close brace operands are given by `(` and `)` respectively

### Numbers:
- Numbers are represented as usual

## Restrictions

The arithmetic expression evaluators will not process the input under the following circumstances:
- Complex numbers are involved, e.g., `(-1)^(1/2)`
- Division by zero, e.g., `(1)/(0)`
- Incorrect syntax for an arithmetic expression, e.g., `1+/*78))((`, `oneplusone`
