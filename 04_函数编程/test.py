def wrapper(func_fn):
    def inner(*args, **kwargs):
        print("装饰器1")
        return func_fn(*args, **kwargs)

    return inner


# @func : 1. fn() -> func(fn)()  -> 2. fn() = inner()


@wrapper
def fn(name):
    print("装饰器2：", name)


fn("python")
