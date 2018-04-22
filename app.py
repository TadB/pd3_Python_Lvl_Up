#!/usr/bin/python
import json


def add_tag(tag):
    #real decorator
    def wrap(function):
        def wraper(*args, **kwargs):
            #wykonuje to co robi dekorator teraz
            return f"<{tag}>{function(*args, **kwargs)}</{tag}>"
        return wraper
    #return real decorator
    return wrap

def validate_json(*arguments):
    def wrap(function):
        def wraper(*args):
            #ustalam akcje dekoratora
            nonlocal arguments
            #convert args tuple to dictionary
            data = json.loads(args[0])
            if set(arguments)==set(data.keys()):
                return function(*args)
            else:
                return "Value error"
        return wraper
    return wrap


@validate_json('first_name', 'last_name')
def process_json(data):
    return len(data)


@add_tag('h1')
def testPrint():
    return f'test input'


