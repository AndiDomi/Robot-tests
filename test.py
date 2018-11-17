from robot.api.deco import keyword

    

    
@keyword('Print name ${name}')
def print_name(name):
    print("atata")
    new_list = name.split(",")
    print (new_list)
    return new_list
    