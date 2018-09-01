__author__ = 'GaoLiaoLiao'
def sum(a, b, c, d):
    return a + b + c + d

values1 = (1, 2)
values2 = { 'c': 10, 'd': 15 }
s = sum(*values1, **values2)
# will execute as:
# s = sum(1, 2, c=10, d=15)
print(s)

first, *rest = [1,2,3,4]
print(first)
print(rest)

first, *l, last = [1,2,3,4]
print(first)
print(l)
print(last)

# Also Python 3 adds new semantic (refer PEP 3102: reference: https://www.python.org/dev/peps/pep-3102/):
# def func(arg1, arg2, arg3, *, kwarg1, kwarg2):
#     pass
# Such function accepts only 3 positional arguments, and everything after * can only be passed as keyword arguments.
#


def phuck(fn):
    print("phuck %s!" % fn.__name__[::-1].upper())

@phuck
def wfg():
    pass

def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()

#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>


#example 3:
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do {0}, {1} and {2} like platypus? {3}".format(a, b, c, platypus))


function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
# 参数只打印了一次
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!


# decorated_function = a_decorator_passing_arbitrary_arguments(function_with_named_arguments)
# decorated_function("Bill", "Linus", "Steve", platypus="Indeed!")
# 参数打印了两次
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# ('Bill', 'Linus', 'Steve')
# {'platypus': 'Indeed!'}
# Do Bill, Linus and Steve like platypus? Indeed!

def make_html_tag(tag, *args, **kwargs):
    def real_decorator(fn):
        if "css_class" in kwargs:
            css_class = " class='{0}'".format(kwargs["css_class"])
        else:
            css_class = ""
        def wrapped(content):
            return "<"+tag+css_class+">" + fn(content) + "</"+tag+">"
        return wrapped
    return real_decorator

@make_html_tag(tag="b", css_class="bold_css")
@make_html_tag(tag="i", css_class="italic_css")
def hello(content):
    return content
print(hello("content you want to wrap"))
