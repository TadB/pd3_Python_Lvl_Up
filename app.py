#!/usr/bin/python

def add_tag(tag):
    #real decorator
    def wrap(function):
        def wraper(*args, **kwargs):
            #wykonuje to co robi dekorator teraz
            return f"<{tag}>{function(*args, **kwargs)}</{tag}>"
        return wraper
    #return real decorator
    return wrap

@add_tag('h1')
def testPrint():
    return f'test input'

