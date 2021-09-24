# 데코레이터

## 데코레이터란?
사용자가 객체의 구조를 수정하지 않고, 기존 객체에 새로운 함수 기능을 추가할 수 있도록 하는 Python의 디자인 패턴이다.\
데코레이터는 함수 내에서 함수를 사용하는 형식입니다. \
이는 함수내 함수의 중복 사용을 줄일 수 있으며 주 목적은 **유지보수**입니다.

```python
def decorating_fun(func):
    def wrapping_function():
        # 추가된 기능인 print문
        print("this is wrapping function and get func start")
        func()
        # 추가된 기능인 print문
        print("func end")
    return wrapping_function
```

위와 같이 간단한 decorator function 을 만든다.\
decorator function 을 보면 다른 함수를 매개변수로 사용하고 그 함수가 안에 있는 wrapping_function 을 선언한다.\
그리고 wrapping_function 안에 매개 변수로 들어온 함수를 사용하고 wrapping_function 의 주소 값을 리턴한다.

```python
@decorating_fun
def decorated_func():
    print("i`m decorated")

decorated_func()

>>> this is wrapping function and get func start
>>> i`m decorated
>>> func end
```

2021.09.25에는 데코레이터로 흔히 사용하는 property 와 setter 를 구현해보자.

```python
class sample:
    def property(func):
        def property_wrapper():
        

```



decorator 관련 실습 자료(https://www.geeksforgeeks.org/decorators-in-python/)
