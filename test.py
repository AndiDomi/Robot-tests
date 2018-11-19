from robot.api.deco import keyword
import requests 
    

    
@keyword('Print name ${name}')
def print_name(name):
    print("atata")
    new_list = name.split(",")
    print (new_list)
    return new_list


    
@keyword('Make request to ${url} ${id}')
def make_request(url,id):
    r = requests.get(url)
    print (r.text)
    