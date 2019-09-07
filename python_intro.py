print('Hello, Django girls!')
if 3>2:
    print('It works!')
if 5>2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey sonja!')
else:
    print('Hey anonymous!')
def hi():
    print('Hi there!')
    print('How are you?')
hi()

def hi(name):
    if name == 'Ola':
        print('Hi ola!')
    elif name == 'sonja':
        print('Hi sonja!')
    else:
        print('Hi anonymous!')
hi("Ola")
hi("sonja")

def hi(name):
    print('Hi' + name + '!')
hi("Rachel")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'YOu']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    print(i)