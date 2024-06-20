# defining a decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the func is called.")
    return wrapper


# Using the decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

