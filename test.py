from robot.api.deco import keyword
import requests 
import logging
import unittest
from robot.utils.asserts import assert_equal
    
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

    
    