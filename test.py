from robot.api.deco import keyword
import requests 
import logging
import unittest
import random
    
@keyword('Print reminder ${name}')
def print_reminder(name):
    print("atata")
    new_list = name.split(",")
    logging.info(new_list)


    
@keyword('Make request to ${url} ${id}')
def make_request(url,id):
    r = requests.get(url+id)
    logging.info(r.status_code)
    return r.status_code


def function_to_be_tested(first, second, third, fourth, fift, sixt):
     logging.info(first)
     logging.info(second)
     logging.info(third)
     logging.info(fourth)
     logging.info(fift)
     logging.info(sixt)
     return first+second+third+fourth+fift+sixt
    
@keyword('Randomize parameters')
def randomize_parameters():
    first = random.randint(1,2)
    second = random.randint(1,2)
    third = random.randint(1,2)
    fourth = random.randint(1,2)
    fift = random.randint(1,2)
    sixt = random.randint(1,2)
    sum = function_to_be_tested(first, second, third, fourth, fift, sixt)
    if sum < 9:
        logging.info('4 params are = to 1')
    




