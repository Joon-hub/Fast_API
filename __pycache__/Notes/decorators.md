A decorator in Python is a design pattern that allows you to modify or extend the behavior of a function or method without permanently modifying its code. Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

### How Decorators Work

A decorator is itself a function that takes another function as an argument and returns a new function that usually extends or alters the behavior of the original function. 

Here is a simple example to illustrate how decorators work:

#### Basic Decorator Example

1. **Defining a Decorator**:
    ```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper
    ```

2. **Using the Decorator**:
    ```python
    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
    ```

### Explanation

- **Step 1: Defining a Decorator**

  ```python
  def my_decorator(func):
      def wrapper():
          print("Something is happening before the function is called.")
          func()
          print("Something is happening after the function is called.")
      return wrapper
  ```

  - `my_decorator` is a function that takes a function `func` as an argument.
  - Inside `my_decorator`, there is an inner function `wrapper` which adds some behavior before and after calling `func()`.
  - The `wrapper` function is then returned from `my_decorator`.

- **Step 2: Using the Decorator**

  ```python
  @my_decorator
  def say_hello():
      print("Hello!")
  ```

  - The `@my_decorator` syntax is a shorthand for applying the decorator to `say_hello`. It's equivalent to `say_hello = my_decorator(say_hello)`.
  - When `say_hello` is called, the `wrapper` function inside `my_decorator` is executed, adding behavior before and after the call to `say_hello`.

### Applying Decorators to Functions with Arguments

Decorators can also be used on functions that accept arguments:

1. **Defining a Decorator for Functions with Arguments**:
    ```python
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result
        return wrapper
    ```

2. **Using the Decorator**:
    ```python
    @my_decorator
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")
    ```

### Explanation

- The `wrapper` function uses `*args` and `**kwargs` to pass any number of positional and keyword arguments to the original function `func`.
- The decorator still adds behavior before and after the call to `func`.

### Real-World Example: FastAPI Decorators

In the code snippet you provided, FastAPI uses decorators to define routes for handling HTTP requests:

```python
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

- `@app.get("/")`: This decorator registers the `read_root` function to handle GET requests to the root URL (`/`).
- `@app.get("/items/{item_id}")`: This decorator registers the `read_item` function to handle GET requests to URLs like `/items/5`, extracting the `item_id` from the URL and handling the query parameter `q`.

### Summary

- **Decorator**: A function that takes another function and extends or alters its behavior.
- **Syntax**: Use the `@decorator_name` syntax above the function you want to decorate.
- **Use Case**: Decorators are used for logging, enforcing access control and authentication, instrumentation, caching, and more.

Understanding decorators is crucial for working with frameworks like FastAPI, as they rely heavily on decorators to define routes and middleware.