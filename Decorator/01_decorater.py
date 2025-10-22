from functools import wraps

def decorator_fun(func):
    @wraps(func)
    def wrapper():
        print("just before main function")
        func()
        print("just after main function")
    return wrapper

@decorator_fun
def chai_rating():
    print("chai is so good")

print(chai_rating())

chai_rating()
print(chai_rating.__name__)