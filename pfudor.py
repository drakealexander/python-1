



import colors as c
from util import ask

intro = c.magenta + '''Welcome to the Pink Fluffy Unicorns Quiz!''' + c.reset



def q1():
    print(c.reset)
    answer = ask("What color are the unicorns?")
    if answer == 'pink':
        print(c.base3 + ":)")
        return True
    print(c.base3 + ":(")
    return False
def q2():
    print(c.reset)
    answer = ask("Where are they dancing?")
    if answer.startswith("rainbow"):
        print(c.base3 + ":)")
        return True
    print(c.base3  + ":(")
    return  False    
def q3():
    print(c.reset)
    answer = ask("Please use one word to describe the texture of their magical fur:")
    if answer.startswith("smile"):
        print(c.base3 + ":)")
        return True
    print(c.base3 + ":(")
    return False
        
questions = [q1,q2,q3]




