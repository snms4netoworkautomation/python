x = 10
expression = 'x * 5'
print(expression)
print(type(expression))
print(eval(expression))
print(int(expression))


'''
Using `print(int(expression))` works if `expression` is already evaluated as a numerical result. However, `int(expression)` will not work if `expression` is a string that contains a mathematical expression, such as `"x * 5"`—it would raise a `ValueError` because `int()` expects a string that represents a plain integer (e.g., `"50"`), not an expression like `"x * 5"`.

### When to Use `int(expression)` vs. `eval(expression)`

- **`eval(expression)`**: This is used when `expression` is a string representing a Python expression (e.g., `"x * 5"`). `eval()` interprets the string as code and evaluates it, which can include arithmetic or other operations.
  
  ```python
  x = 10
  expression = "x * 5"  # a string with a mathematical expression
  print(eval(expression))  # Output: 50
  ```

- **`int(expression)`**: This is used to convert a numeric string (like `"50"`) or a floating-point number into an integer. It won’t evaluate expressions and will only work with strings that can be directly converted to an integer.

  ```python
  expression = "50"
  print(int(expression))  # Output: 50

  expression = 50.0
  print(int(expression))  # Output: 50
  ```

### Why `int(expression)` Won't Work in Your Original Example

If `expression` is set to `"x * 5"` (a string with a math expression), `int()` will not understand the operation and will raise a `ValueError`. For example:

```python
x = 10
expression = "x * 5"
print(int(expression))  # Raises ValueError: invalid literal for int() with base 10: 'x * 5'
```

In summary:

- Use `eval(expression)` when you need to evaluate a string that represents a Python expression.
- Use `int(expression)` when you simply want to convert a string or float to an integer.
'''