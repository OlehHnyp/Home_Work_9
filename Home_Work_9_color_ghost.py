import random as r

class Ghost(object):
    
    def __init__(self):
        print('init')
        self.color = r.choice(['white', 'yellow', 'red', 'purple'])