
def decorating_fun(func_1):
    def wrap_function():
        print("func1 come on")
        func_1()
        print("func1 get out")
    return wrap_function
@decorating_fun
def decorated_fun():
    print("this is function between func come on and func get out")

decorated_fun()