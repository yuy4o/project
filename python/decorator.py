# 装饰器decorator 不用改动原函数代码 就能修改或扩展函数或方法的行为
# 常用于 日志记录、性能测试、事务处理等场景

# 装饰器1：记录时间
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# 装饰器2：处理异常
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Function {func.__name__} raised an exception: {e}")
            raise
    return wrapper

# 装饰器3：参数验证
def validate_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("All arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

# 装饰器4：打印信息
def my_decorator(func): #装饰器是一个接受函数并返回一个新函数的函数
    def wrapper(*args, **kwargs): # args 任意数量的位置参数存成元组，kwargs 任意数量的关键字参数存成字典- C++中int main(int argc, char* argv[])
        print(f"Calling function {func.__name__} with args: {args} and kwargs: {kwargs} ...")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

@my_decorator
def add(a, b):
    return a + b

# Test the decorated functions
say_hello("Alice")
result = add(5, 3)
print(f"Result of add: {result}")
