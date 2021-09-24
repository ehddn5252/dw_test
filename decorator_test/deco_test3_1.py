def a_new_decorator(a_func):
    def wrapTheFunction():
        print("a_function_requiring_decoration()가 실행되기 전에 좀 지루한 일을 먼저 해야합니다")

        a_func()

        print("a_function_requiring_decoration()가 실행된 후에 좀 지루한 일을 해야합니다")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("저는 고약한 냄새를 없애기 위해 뭔가 추가된 함수입니다")

a_function_requiring_decoration()
#outputs: "저는 고약한 냄새를 없애기위해 뭔가 추가된 함수입니다"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#이제 wrapTheFunction()에 a_function_requiring_decoration이 들어갔습니다.

a_function_requiring_decoration()
#outputs: "a_function_requiring_decoration()가 실행되기 전에 좀 지루한 일을 먼저 해야합니다"
#       "저는 고약한 냄새를 없애기위해 뭔가 추가된 함수입니다"
#       "a_function_requiring_decoration()가 실행된 후에 좀 지루한 일을 해야합니다"