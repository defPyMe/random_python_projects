#getting a wrapper workin 

def decorate(funct_to_decorate):
    def wrapper(*args, **kwargs):
        print("function decorated")
        return funct_to_decorate(*args, **kwargs)
    return wrapper
    
@decorate
def funct(word):
    print("ok" + word)
funct("not ok")
