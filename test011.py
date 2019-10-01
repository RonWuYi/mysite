from functools import wraps

class Test:
    # Decorator
    def decorate1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator called')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorate2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator called 2')
            return func(*args, **kwargs)
        return wrapper
    
if __name__ == '__main__':
    a = Test()
    @a.decorate2
    def spam():
        pass
    
    spam()