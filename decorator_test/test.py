def decorating_fun(func):
    def wrapping_function():
        print("this is wrapping function and get func start")
        func()
        print("func end")
    return wrapping_function


@decorating_fun
def decorated_func():
    print("i`m decoraed")


decorated_func()