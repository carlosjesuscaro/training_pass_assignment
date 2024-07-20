def foo(var=[]):
    var.append(1)
    return var
print(foo())
print(foo())
print(foo())

def abc(var = None):
    if var is None:
        var = []
    var.append(2)
    return var
print(abc())
print(abc())
print(abc())
