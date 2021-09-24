def hi(name="yasoob"):
    print("여러분은 hi() 함수 안에 있습니다")

    def greet():
        return "여러분은 greet() 함수 안에 있죠"

    def welcome():
        return "여러분은 welcome() 함수 안에 있습니다."

    if name =="yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)