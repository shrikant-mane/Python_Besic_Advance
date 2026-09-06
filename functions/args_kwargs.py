# *args collects positional arguments into a tuple.
def data(*args):
    print(args)     # --> tuple

data([1,2,3,4])

def add(*args):
    print(args)
    print(sum(args))

add(1,2,3,4)
add(1,2,3,4,5)


# **kwargs collects keyword arguments into a dictionary.
def info(**kwargs):
    print(kwargs)       # --> dict
    print(kwargs['name'])
    print(kwargs['age'])
    # print(kwargs['emp_id'])   --> KeyError: 'emp_id'
info(name='Nitish', age=25)


# Using both together
def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_kwargs(1, 2, name='Sameer', cto_location='USA')

