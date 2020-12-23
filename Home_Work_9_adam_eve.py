class Human():
    attr = 'Homosapiens'
        
class Man(Human):
    sex = 'man'
    
class Woman(Human):
    sex = 'woman'

def God():
    Adam = Man()
    Eve = Woman()
    
    return Adam, Eve