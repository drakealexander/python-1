"""my quiz"""

import colors as c
import utils as ask

def q1():
    print(c.reset)
    answer = ask('How old is Drake Griffith?')
    if answer == '12':
        return True
    return False

def q2():
    print(c.reset)
    answer = ask("What is Drake's Favorite Subject in School?")
    if answer == 'math':
        return True
    return False

def q3():
    print(c.reset)
    answer = ask("What is Drake's favorite number?")
    if answer == '1738' or answer == '819':
        return True
    return False

def q4()
    print(c.reset)
    answer = ask("What is my favorite TV show?")
    if answer == 'spongebob' or answer == 'family guy':
        return True
    return False

def q5()
    print(c.reset)
    answer = ask("What are some of Drake's best friends")
    if answer == 'josh' or answer == 'evan' or answer == 'michael' or answer == 'jake':
        return True
    return False


questions = [q1,q2,q3,q4,q5]
