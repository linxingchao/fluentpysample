registry = []

def register(func):
    print(f'running registry({func})')
    registry.append(func)
    return func

@register
def f1():
    print('runing f1')
    
@register
def f2():
    print('running f2')
    
def f3():
    print('running f3')