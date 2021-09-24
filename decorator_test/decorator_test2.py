def hi(name="yasoob"):

    return "hi yasoob"

def doSomethingBeforeHi(func):
    print("hi가 실행되기 전에 좀 지루한 일을 먼저 해야 합니다.")
    print(func())

doSomethingBeforeHi(hi)