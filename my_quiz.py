"""my quiz"""

import colors as c
from util import ask
intro = c.base3 + """Welcome To Drake's Quiz...""" + c.reset 

def q1():
    print(c.reset)
    answer = ask(c.red + 'How old is Drake Griffith?')
    if answer == '12':
        print(c.base3 + ':)')
        return True
    print(c.base3 + ':(')
    return False

def q2():
    print(c.reset)
    answer = ask(c.blue + "What is Drake's Favorite Subject in School?")
    if answer == 'math':
        print(c.base3 + ':)')
        return True
    print(c.base3 + ':(')
    return False

def q3():
    print(c.reset)
    answer = ask(c.base3 + "What is Drake's favorite number?")
    if answer == '1738' or answer == '819':
        print(c.base3 + ':)')
        return True
    print(c.base3 + ':(')
    return False

def q4():
    print(c.reset)
    answer = ask(c.red + "What is my favorite TV show?")
    if answer == 'spongebob' or answer == 'family guy' or answer == 'south park':
        print(c.base3 + ':)')
        return True
    print(c.base3 +':(')
    return False

def q5():
    print(c.reset)
    answer = ask(c.blue + "What are some of Drake's best friends")
    if answer == 'josh' or answer == 'evan' or answer == 'michael' or answer == 'jake':
        print(c.base3 + ':)')
        return True
    print(c.base3 + ':(')
    return False


questions = [q1,q2,q3,q4,q5]
