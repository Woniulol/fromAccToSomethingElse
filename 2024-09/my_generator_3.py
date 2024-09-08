"""
Sub-generator
Sub-generator allows a generator to delegate work to a sub-generator.

The `for` loop is the client code, `gen` is the delegating generator, and `sub_gen` is the `subgenerator`.
Note that `yield from` pauses `gen`, and `sub_gen` takes over until it is exhausted. The values yielded by
`sub_gen` pass through `gen` directly to the client `for` loop. Meanwhile, `gen` is suspended and cannot see the values passing through it.

Only when `sub_gen` is done, `gen` resumes.

When the subgenerator contains a `return` statement with a vlaue, that value can be captured in the delegating generator by using `yield from`
as part of an expression.

"""

def sub_gen():
    yield 1.1
    yield 1.2
    return "Done!"

def gen():
    yield 1
    result = yield from sub_gen()
    print(result)
    yield 2

for x in gen():
    print(x)


def tree(cls, level):
    yield cls.__name__, level
    for sub_cls in cls.__subclasses__():
        yield from tree(sub_cls, level+1)

def display(cls):
    for cls_name, level in tree(cls, 0):
        indent = ' ' * level * 4
        print(f'{indent}{cls_name}')

display(BaseException)